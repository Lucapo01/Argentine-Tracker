from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re

class FundsScrapper:

    def __init__(self, fondos: list, speed: int):

        self.driver = webdriver.Firefox()
        sleep(3)

        self.speed = speed
        self.fondos = fondos
        self.ticker_percentage_regex = """<!-- ngIf: row\.tipo == 'data' --><td class="ng-binding ng-scope" ng-if="row\.tipo == 'data'">(.*)<\/td><!-- end ngIf: row\.tipo == 'data' -->'"""

    def run(self):
        self.get_data(self.fondos[0][0], self.fondos[0][1])

    def get_data(self, name: str, url: str):
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
            
            except:
                error: bool = True
                print("[WARNING] HTML element not found, trying again...")
                sleep(2)
    
            
        print("[OK] HTML element found: ", name)
        with open('data_raw.txt', 'w') as f:
            f.write(data_raw)
        data = re.findall(self.ticker_percentage_regex, data_raw)
        print(data)