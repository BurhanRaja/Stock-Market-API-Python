import json
from pprint import pprint
from yahooquery import Ticker
import pandas as pd

def all_etfs(skip: int = 10, offset: int = 1):
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_Indian_exchange-traded_funds', match="Name")
    data = tickers[0].to_json(orient="records")
    objArr = json.loads(data)

    dataArr = []

    for ticker in objArr[offset:skip]:
        dataArr.append({
            "name": ticker['0'],
            "symbol": ticker['1']
        })
    return dataArr
    
