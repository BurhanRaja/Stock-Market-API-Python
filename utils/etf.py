import json
from pprint import pprint
from yahooquery import Ticker
import yfinance as yf
import pandas as pd

def all_etfs(offset: int = 1, limit: int = 10):
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_Indian_exchange-traded_funds', match="Name")
    data = tickers[0].to_json(orient="records")
    objArr = json.loads(data)

    dataArr = []

    for ticker in objArr[offset:limit]:
        dataArr.append({
            "name": ticker['0'],
            "symbol": ticker['1']
        })
    return dataArr
    
def singleETFs(symbol: str):
    data = yf.Ticker(symbol + ".NS").info
    return data
