from unicodedata import name
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re

class FundsScrapper:

    def __init__(self, fondos: list, speed: int):

        self.driver = webdriver.Firefox()
        sleep(speed)

        self.speed = speed
        self.fondos = fondos
        self.ticker_percentage_regex = r"""<!-- ngIf: row\.tipo == 'data' --><td class="ng-binding ng-scope" ng-if="row\.tipo == 'data'">(.*?)<\/td><!-- end ngIf: row.tipo == 'data' -->"""
        self.name_tickers = r"""<!-- ngIf: row.tipo == 'data' --><td class="ng-binding ng-scope" ng-if="row.tipo == 'data'" style="text-align:left">(.*?)</td><!-- end ngIf: row.tipo == 'data' -->"""
        self.patrimony = r"""<!-- ngIf: row\.tipo == 'pie' --><td class="ng-scope" ng-if="row\.tipo == 'pie'"><strong class="ng-binding">(.*?)<\/strong><\/td><!-- end ngIf: row\.tipo == 'pie' -->"""

    def run(self) -> dict:
        # with open("raw_data.txt", "w") as f:
        #     f.write(self.get_raw_data(self.fondos[1][0], self.fondos[1][1]))
        # return {}
        fund_json = {}
        error_list = []
        for fund in self.fondos:
            raw_data: str = self.get_raw_data(fund[0], fund[1])
            fund_data: dict = self.convert_data(raw_data)
            if "error" not in fund_data.keys():
                fund_json[fund[0]] = fund_data
            else:
                error_list.append(fund_data["error"] + fund[0])
        return {"error":error_list, "data":fund_json}

    def get_raw_data(self, name: str, url: str) -> str:
        self.driver.get(url)
        sleep(self.speed)
        error: bool = False
        while not error:
            try:
                self.driver.find_element(By.CLASS_NAME,"html").click()
                sleep(self.speed)
                self.driver.switch_to.window(self.driver.window_handles[1])
                sleep(self.speed)

                html = self.driver.execute_script(
                    "return document.documentElement.outerHTML")
                sel_soup = BeautifulSoup(html, "html.parser")
                data_raw = sel_soup.findAll("tr")
                data_raw = str(data_raw)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                error = True
            
            except:
                error = False
                print("[WARNING] HTML element not found, trying again...")
                self.driver.refresh()
                sleep(2)
    
            
        print("[OK] HTML element found: ", name)
        return data_raw
        
    def convert_data(self, raw_data: str) -> dict:
        try:
            text_data_per_string = re.findall(self.ticker_percentage_regex, raw_data)
            text_data_tickers = re.findall(self.name_tickers, raw_data)
            text_data_per =  [float(i) for i in text_data_per_string]
            if len(text_data_tickers) != len(text_data_per):
                print("[ERROR] List does not match")
                raise ValueError('[ERROR] List does not match')
            patrimony_string: str = re.search(self.patrimony, raw_data).group(1)
            patrimony_float=float(re.sub(",","",patrimony_string))
            for i in range(len(text_data_per)): 
                text_data_per[i]= round(text_data_per[i]*patrimony_float /100, 2)
            
            
            result = {
            "tickers":text_data_tickers,
            "qty_ars": text_data_per,
            "patrimony": patrimony_float
            }
            return result
        except Exception as e:
            return {"error": "[ERROR]: "+str(e)}