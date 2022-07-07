import logging
from reader import FundsScrapper

# Logging config
logging.basicConfig(
    filename='log.log',
    level=logging.DEBUG,
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
        

def main() -> None:
    funds_list: list = load_parameters()
    funds_scrapper = FundsScrapper(funds_list, 3)
    funds_scrapper.run()


main()