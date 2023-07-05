import json
from pprint import pprint
from yahooquery import Ticker
import yfinance as yf
from yahoofinancials import YahooFinancials
import requests

refinedArray = []

def all_etfs(skip: int = 1, limit: int = 6):

    with open('./data/all_ETFs.json', "r") as write_file:
        objArr = json.load(write_file)
    
    dataArr = []

    for ticker in objArr[skip:limit]:
        sybmol = ticker['1'] + ".NS"
        dataArr.append({
            "name": ticker['0'],
            "symbol": sybmol,
            "price": YahooFinancials(ticker['1'] + ".NS", concurrent=True).get_current_price()
        })
    
    return dataArr
    
def singleETFs(symbol: str):
    if '.NS' in symbol:
        data = yf.Ticker(symbol).info
        price = YahooFinancials(symbol, concurrent=True).get_current_price()
        curr_change = YahooFinancials(symbol, concurrent=True).get_current_change()
        per_change = YahooFinancials(symbol, concurrent=True).get_current_percent_change()
    if '.BO' in symbol:
        data = yf.Ticker(symbol).info
        price = YahooFinancials(symbol, concurrent=True).get_current_price()
        curr_change = YahooFinancials(symbol, concurrent=True).get_current_change()
        per_change = YahooFinancials(symbol, concurrent=True).get_current_percent_change()
    if '.NS' not in symbol:
        data = yf.Ticker(symbol + ".NS").info
        price = YahooFinancials(symbol + ".NS", concurrent=True).get_current_price()
        curr_change = YahooFinancials(symbol + ".NS", concurrent=True).get_current_change()
        per_change = YahooFinancials(symbol + ".NS", concurrent=True).get_current_percent_change()

    sData = {
        "price": price,
        "curr_change": curr_change,
        "per_change": per_change,
        "data": data
    }
    
    return sData

def best_bond_etf():
    with open("./data/Best_Bond_ETF.json") as file:
        bondData = json.load(file)
    data = []
    for bd in bondData:
        price = YahooFinancials(bd['symbol'], concurrent=True).get_current_price()
        per_change = YahooFinancials(bd['symbol'], concurrent=True).get_current_percent_change()
        curr_change = YahooFinancials(bd['symbol'], concurrent=True).get_current_change()
        name = bd['name']
        symbol = bd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price,
            "curr_change": curr_change,
            "per_change": per_change
        })
    return data

def best_gold_etf():
    with open("./data/Best_Gold_ETF.json") as file:
        goldData = json.load(file)
    data = []
    for gd in goldData:
        price = YahooFinancials(gd['symbol'], concurrent=True).get_current_price()
        per_change = YahooFinancials(gd['symbol'], concurrent=True).get_current_percent_change()
        curr_change = YahooFinancials(gd['symbol'], concurrent=True).get_current_change()
        name = gd['name']
        symbol = gd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price,
            "curr_change": curr_change,
            "per_change": per_change
        })
    return data

def best_index_etf():
    with open("./data/Best_Index_ETF.json") as file:
        indexData = json.load(file)
    data = []
    for indexd in indexData:
        price = YahooFinancials(indexd['symbol'], concurrent=True).get_current_price()
        per_change = YahooFinancials(indexd['symbol'], concurrent=True).get_current_percent_change()
        curr_change = YahooFinancials(indexd['symbol'], concurrent=True).get_current_change()
        name = indexd['name']
        symbol = indexd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price,
            "curr_change": curr_change,
            "per_change": per_change
        })
    return data

def best_sector_etf():
    with open("./data/Best_Sector_ETF.json") as file:
        sectorData = json.load(file)
    data = []
    for sd in sectorData:
        price = YahooFinancials(sd['symbol'], concurrent=True).get_current_price()
        per_change = YahooFinancials(sd['symbol'], concurrent=True).get_current_percent_change()
        curr_change = YahooFinancials(sd['symbol'], concurrent=True).get_current_change()
        name = sd['name']
        symbol = sd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": price,
            "curr_change": curr_change,
            "per_change": per_change
        })
    return data

def etfCurrentPrice(symbol: str):
    return {
        "curr_price" : YahooFinancials(symbol, concurrent=True).get_current_price(),
        "curr_per_change": YahooFinancials(symbol, concurrent=True).get_current_percent_change(),
        "curr_change": YahooFinancials(symbol, concurrent=True).get_current_change(),
    }

def etfDetails(symbol: str):
    info = yf.Ticker("UTIBANKETF.NS").info
    curr_price = YahooFinancials(symbol, concurrent=True).get_current_price()
    per_change = YahooFinancials(symbol, concurrent=True).get_current_percent_change()
    curr_change = YahooFinancials(symbol, concurrent=True).get_current_change()
    
    return {
        "info": info,
        "curr_price": curr_price,
        "curr_change": curr_change,
        "per_change": per_change
    }

def etfHistoricalData(symbol: str, period: str, interval: str):
    print(symbol)
    print(period)
    print(interval)
    historical_data = json.loads(Ticker(symbol).history(period, interval).to_json(orient="table"))['data']
    return historical_data