import logging
from reader import FundsScrapper

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
    price_qty_update(funds_data)
    return funds_data


print(main())