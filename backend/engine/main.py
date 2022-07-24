import logging
from reader import FundsScrapper
import Levenshtein as lv

# Logging config
logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
# --------------------------------

# Configs
FUNDS_FILE = "funds.csv"
TICKERS_NAMES_FILE = "ticker_names"

MIN_CATCH = 0.62 # lv_ratio_matcher() will start catching names from MIN_CATCH
MAX_CATCH = 0.8  # lv_ratio_matcher() will take the name without continuing
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
    return name + " c"

def symbols_update(funds_data: dict) -> None:
    tickers_not_found = []
    tickers_not_found_index = []
    with open(FUNDS_FILE) as f:
            all_tickers: list = []
            for line in f:
                all_tickers.append(line.strip().split(","))

    for fund in funds_data.keys():
        for i in range(len(funds_data[fund]["tickers"]["names"])):
            match: str = lv_ratio_matcher(funds_data[fund]["tickers"]["names"][i],all_tickers)
            if match != "":
                funds_data[fund]["tickers"]["names"][i] = match
            else:
                tickers_not_found_index.append(i)
        
        for t in tickers_not_found_index:
            funds_data[fund]["tickers"]["qty_ars"].pop(t)
            tickers_not_found.append(funds_data[fund]["tickers"]["names"].pop(t))

    


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

#print(lv.ratio("GRUPO SUPERVIELLE CB","BANCO SUPERVIELLE"))