from curses.ascii import US
import logging
from reader import FundsScrapper
import Levenshtein as lv
from settings import FUNDS_FILE, TICKERS_NAMES_FILE, MAX_CATCH, MIN_CATCH, BROKER, DNI, USER, PASSWORD
import datetime
from pyhomebroker import HomeBroker

# Logging config
logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

hb = HomeBroker(int(BROKER))
hb.auth.login(dni=DNI, user=USER, password=PASSWORD, raise_exception=True)
# --------------------------------

def load_parameters() -> list:
    try:
        with open(FUNDS_FILE) as f:
            lis: list = []
            for line in f:
                lis.append(line.strip().split(","))
            print("[OK] Load Parameters")
            logging.info("[OK] Load Parameters")
            return lis[1:]

    except Exception as e:
        print("[ERROR] Load parameters")
        logging.error("[ERROR] Load parameters: " + str(e))
        return []

def lv_ratio_matcher(name: str, all_tickers: list) -> str:
    best_match: int = 0
    best_result: str = ""
    for ticker in all_tickers:
        ratio: float = lv.ratio(name.upper(), ticker[0].upper())
        if ratio >= MAX_CATCH:
            return ticker[1]
        elif ratio >= MIN_CATCH and ratio >= best_match:
            best_match = ratio
            best_result = ticker[1]
    
    return best_result


def symbols_update(funds_data: dict) -> None:
    
    with open(TICKERS_NAMES_FILE, encoding="utf8") as f:
            all_tickers: list = []
            for line in f:
                all_tickers.append(line.strip().strip("Clase").split(","))
    for fund in funds_data.keys():
        tickers_not_found: list = []
        qty_ars_not_found: list = []
        for i in range(len(funds_data[fund]["tickers"]["names"])):
            match: str = lv_ratio_matcher(funds_data[fund]["tickers"]["names"][i],all_tickers)
            if match != "" and match not in funds_data[fund]["tickers"]["names"]:
                logging.info("Replace tickers: " + str(funds_data[fund]["tickers"]["names"][i]) + " - " + match)
                funds_data[fund]["tickers"]["names"][i] = match
            else:
                tickers_not_found.append(funds_data[fund]["tickers"]["names"][i])
                qty_ars_not_found.append(funds_data[fund]["tickers"]["qty_ars"][i])
        
        for t in tickers_not_found:
            funds_data[fund]["tickers"]["names"].remove(t)
        for q in qty_ars_not_found:
            funds_data[fund]["tickers"]["qty_ars"].remove(q)
    
        logging.warning("Tickers not found: "+str(tickers_not_found))
            

def price_qty_update(funds_data: dict) -> None:

    for fund in funds_data.values():
        fund["tickers"]["prices"] = [1] * len(fund["tickers"]["names"])

def send_to_server() -> None:
    pass

def main() -> None:
    funds_list: list = load_parameters()
    funds_scrapper = FundsScrapper(funds_list, 6)
    funds_data:dict = funds_scrapper.run()
    for i in funds_data["error"]:
        logging.error(i)
    funds_data = funds_data["data"]
    symbols_update(funds_data)
    price_qty_update(funds_data)
    print(funds_data)


main()

# print(lv.ratio("TRANSP GAS DEL NORTE C","TRANSPORTADORA GAS DEL NORTE"))