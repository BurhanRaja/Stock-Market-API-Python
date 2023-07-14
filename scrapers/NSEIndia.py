import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint

class NSE:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
    
    def get_nifty_50(self):
        data = self.session.get("https://www.nseindia.com", headers=self.headers)
        html = BeautifulSoup(data.text, 'html.parser')
        data = html.find_all(class_ = "tab_box")[0]
        name=data.find(class_="tb_name").getText()
        curr_price=data.find(class_="tb_val").getText().split()[0]
        change=data.find(class_="tb_per").getText().split()
        curr_change=float(change[0])
        curr_per_change=float(change[1][1:-2])

        print({
            "name": name,
            "curr_price": curr_price,
            "curr_change": curr_change,
            "curr_per_change": curr_per_change
        })

    def nse_gainers(self):
        driver = webdriver.Chrome('path/to/chromedriver')
        driver.get("https://www.nseindia.com")
        data = driver.page_source
        html = BeautifulSoup(data.text, "html.parser")
        data = html.find_all('table', id="tab1Ganier")
        print(data)
    
    def nse_losers(self):
        driver = webdriver.Chrome('path/to/chromedriver')
        driver.get("https://www.nseindia.com")
        data = driver.page_source
        html = BeautifulSoup(data.text, "html.parser")
        data = html.find_all('table', id="tab1Loser")
        print(data)
    

    

NSE().nse_gainers()


