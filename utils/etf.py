import json
from yahooquery import Ticker
import yfinance as yf
from scrapers.ETF import ETF

etfs=ETF()

refinedArray = []

def all_etfs(skip: int = 1, limit: int = 6):

    with open('./data/all_ETFs.json', "r") as write_file:
        objArr = json.load(write_file)
    
    dataArr = []

    objArr=objArr[1:]

    for ticker in objArr[skip:limit]:
        symbol = ticker['1'] + ".NS"
        print(symbol)
        data=etfs.get_curr_data(ticker['1'] + ".NS")
        dataArr.append({
            "name": ticker['0'],
            "symbol": symbol,
            "curr_price": data['curr_price'],
            "curr_per_change": data['per_change'],
            "curr_price_change": data['price_change']
        })
    
    return {
        "data": dataArr,
        "total": len(dataArr)
    }
    
def singleETFs(symbol: str):
    data = yf.Ticker(symbol).info
    priceData=etfs.get_curr_data(symbol)
    
    if '.NS' not in symbol:
        data = yf.Ticker(symbol + ".NS").info
        priceData=etfs.get_curr_data(symbol + ".NS")

    sData = {
        "price": priceData['curr_price'],
        "price_change": priceData['price_change'],
        "per_change": priceData['per_change'],
        "data": data
    }
    
    return sData

def best_bond_etf():
    with open("./data/Best_Bond_ETF.json") as file:
        bondData = json.load(file)
    data = []
    for bd in bondData:
        priceData=etfs.get_curr_data(symbol)
        name = bd['name']
        symbol = bd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": priceData['curr_price'],
            "price_change": priceData['price_change'],
            "per_change": priceData['per_change']
        })
    return data

def best_gold_etf():
    with open("./data/Best_Gold_ETF.json") as file:
        goldData = json.load(file)
    data = []
    for gd in goldData:
        priceData=etfs.get_curr_data(symbol)
        name = gd['name']
        symbol = gd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": priceData['curr_price'],
            "price_change": priceData['price_change'],
            "per_change": priceData['per_change']
        })
    return data

def best_index_etf():
    with open("./data/Best_Index_ETF.json") as file:
        indexData = json.load(file)
    data = []
    for indexd in indexData:
        priceData=etfs.get_curr_data(symbol)
        name = indexd['name']
        symbol = indexd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": priceData['curr_price'],
            "price_change": priceData['price_change'],
            "per_change": priceData['per_change']
        })
    return data

def best_sector_etf():
    with open("./data/Best_Sector_ETF.json") as file:
        sectorData = json.load(file)
    data = []
    for sd in sectorData:
        priceData=etfs.get_curr_data(symbol)
        name = sd['name']
        symbol = sd['symbol']
        data.append({
            "name": name,
            "symbol": symbol,
            "price": priceData['curr_price'],
            "price_change": priceData['price_change'],
            "per_change": priceData['per_change']
        })
    return data

def etfCurrentPrice(symbol: str):
    data=etfs.get_curr_data(symbol)
    return data

def etfDetails(symbol: str):
    info = yf.Ticker(symbol).info
    priceData=etfs.get_curr_data(symbol)
    
    return {
        "info": info,
        "price": priceData['curr_price'],
        "price_change": priceData['price_change'],
        "per_change": priceData['per_change']
    }

def etfHistoricalData(symbol: str, start: str, end: str, interval: str):
    historical_data = etfs.get_historical_data(symbol, start, end, interval)
    return historical_data