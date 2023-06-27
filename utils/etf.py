import json
from pprint import pprint
from yahooquery import Ticker
import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials

refinedArray = []

def all_etfs(skip: int = 1, limit: int = 10):
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_Indian_exchange-traded_funds', match="Name")
    data = tickers[0].to_json(orient="records")
    objArr = json.loads(data)

    dataArr = []
    
    pprint(objArr)

    for ticker in objArr[skip:limit]:
        sybmol = ticker['1'] + ".NS"
        price = YahooFinancials(sybmol  ).get_current_price()
        dataArr.append({
            "name": ticker['0'],
            "symbol": ticker['1'],
            "price": price
        })
    
    return dataArr
    
def singleETFs(symbol: str):
    if '.NS' in symbol:
        data = yf.Ticker(symbol).info
        price = YahooFinancials(symbol + ".NS").get_current_price()
    if '.BO' in symbol:
        data = yf.Ticker(symbol).info
        price = YahooFinancials(symbol + ".NS").get_current_price()
    if '.NS' not in symbol:
        data = yf.Ticker(symbol + ".NS").info
        price = YahooFinancials(symbol + ".NS").get_current_price()
    
    sData = {
        "price": price,
        "data": data
    }
    
    return sData

def best_bond_etf():
    with open("./data/Best_Bond_ETF.json") as file:
        bondData = json.load(file)
    data = []
    for bd in bondData:
        price = YahooFinancials(bd['symbol']).get_current_price()
        name = bd['name']
        symbol = bd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price
        })
    return data

def best_gold_etf():
    with open("./data/Best_Gold_ETF.json") as file:
        goldData = json.load(file)
    data = []
    for gd in goldData:
        price = YahooFinancials(gd['symbol']).get_current_price()
        name = gd['name']
        symbol = gd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price
        })
    return data

def best_index_etf():
    with open("./data/Best_Index_ETF.json") as file:
        indexData = json.load(file)
    data = []
    for indexd in indexData:
        price = YahooFinancials(indexd['symbol']).get_current_price()
        name = indexd['name']
        symbol = indexd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price
        })
    return data

def best_sector_etf():
    with open("./data/Best_Sector_ETF.json") as file:
        sectorData = json.load(file)
    data = []
    for sd in sectorData:
        price = YahooFinancials(sd['symbol']).get_current_price()
        name = sd['name']
        symbol = sd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price
        })
    return data
