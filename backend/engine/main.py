import logging
from reader import FundsScrapper
import Levenshtein as lv
from settings import FUNDS_FILE, TICKERS_NAMES_FILE, MAX_CATCH, MIN_CATCH, BROKER, DNI, USER, PASSWORD
import datetime
from pyhomebroker import HomeBroker
import requests
import json

ENGINE_PSWD = "g21jhv3223b1h"

# Logging config
logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

hb = HomeBroker(int(BROKER))
hb.auth.login(dni=DNI, user=USER, password=PASSWORD, raise_exception=True)
print("[OK] Load HomeBroker")
logging.info("[OK] Load HomeBroker")
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
        fund["tickers"]["prices"] = []
        tickers_not_found: list = []
        qty_ars_not_found: list = []
        for t in range(len(fund["tickers"]["names"])):
            price: list = list(dict(hb.history.get_daily_history(fund["tickers"]["names"][t], datetime.date.today()-datetime.timedelta(days=1), datetime.date.today()))["close"])
            if price != []:
                fund["tickers"]["prices"].append(price[-1])
            else:
                tickers_not_found.append(fund["tickers"]["names"][t])
                qty_ars_not_found.append(fund["tickers"]["qty_ars"][t])
        for t in tickers_not_found:
            fund["tickers"]["names"].remove(t)
        for q in qty_ars_not_found:
            fund["tickers"]["qty_ars"].remove(q)
        
        logging.warning("Ticker price not found: "+str(tickers_not_found))
        print("[OK] Price for found completed")
        logging.info("[OK] Price for found completed")

def send_to_server(funds_data: dict) -> None:
    final_json: dict = {}
    # change format
    for fund_key, fund in funds_data.items():
        for i in range(len(fund["tickers"]["names"])):
            if fund["tickers"]["names"][i] not in final_json.keys():
                final_json[fund["tickers"]["names"][i]] = {}
                final_json[fund["tickers"]["names"][i]]["total"] = {"qty": 0, "price": fund["tickers"]["prices"][i]}
            final_json[fund["tickers"]["names"][i]][fund_key] = {"qty": fund["tickers"]["qty_ars"][i], "price": fund["tickers"]["prices"][i]}
            final_json[fund["tickers"]["names"][i]]["total"]["qty"] = round(final_json[fund["tickers"]["names"][i]]["total"]["qty"] + fund["tickers"]["qty_ars"][i], 2)
    logging.info("Sending JSON: \n" + json.dumps(final_json))
    r = requests.post("http://localhost:8000/engineUpdate/"+ENGINE_PSWD, json=final_json)
    logging.info("Server responded with code: " + str(r.status_code))

def main() -> None:
    funds_list: list = load_parameters()
    funds_scrapper = FundsScrapper(funds_list, 6)
    funds_data:dict = funds_scrapper.run()
    for i in funds_data["error"]:
        logging.error(i)
    funds_data = funds_data["data"]
    symbols_update(funds_data)
    price_qty_update(funds_data)
    send_to_server(funds_data)
    logging.info("ENGINE FINISH")


main()

# print(lv.ratio("TRANSP GAS DEL NORTE C","TRANSPORTADORA GAS DEL NORTE"))