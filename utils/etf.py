import json
from yahooquery import Ticker
import yfinance as yf
from scrapers.ETF import ETF
import asyncio
import aiohttp
import math

etfs = ETF()


async def all_etfs(skip: int = 1, limit: int = 10):
    with open("./data/all_ETFs.json", "r") as write_file:
        objArr = json.load(write_file)

    objArr = objArr[1:]
    async with aiohttp.ClientSession() as session:
        data=[etfs.get_curr_data(ticker["1"] + ".NS", session) for ticker in objArr[skip:limit]]
        refinedData=await asyncio.gather(*data)
        return {"data": refinedData, "total": math.floor((len(objArr) - limit)/10)}


def singleETFs(symbol: str):
    data = yf.Ticker(symbol).info
    priceData = etfs.get_curr_data(symbol)

    if ".NS" not in symbol:
        data = yf.Ticker(symbol + ".NS").info
        priceData = etfs.get_curr_data(symbol + ".NS")

    sData = {
        "price": priceData["curr_price"],
        "price_change": priceData["price_change"],
        "per_change": priceData["per_change"],
        "data": data,
    }

    return sData


def best_bond_etf():
    with open("./data/Best_Bond_ETF.json") as file:
        bondData = json.load(file)
    data = []
    for bd in bondData:
        priceData = etfs.get_curr_data(bd["symbol"])
        name = bd["name"]
        symbol = bd["symbol"]
        data.append(
            {
                "name": name,
                "symbol": symbol,
                "price": priceData["curr_price"],
                "price_change": priceData["price_change"],
                "per_change": priceData["per_change"],
            }
        )
    return {
        "data": data,
        "total_pages": int(len(bondData) / 10),
        "page_num": int(len(bondData) / 10),
    }


def best_gold_etf():
    with open("./data/Best_Gold_ETF.json") as file:
        goldData = json.load(file)
    data = []
    for gd in goldData:
        priceData = etfs.get_curr_data(gd["symbol"])
        name = gd["name"]
        symbol = gd["symbol"]
        data.append(
            {
                "name": name,
                "symbol": symbol,
                "price": priceData["curr_price"],
                "price_change": priceData["price_change"],
                "per_change": priceData["per_change"],
            }
        )
    return {
        "data": data,
        "total_pages": int(len(goldData) / 10),
        "page_num": int(len(goldData) / 10),
    }


def best_index_etf():
    with open("./data/Best_Index_ETF.json") as file:
        indexData = json.load(file)
    data = []
    for indexd in indexData:
        priceData = etfs.get_curr_data(indexd["symbol"])
        name = indexd["name"]
        symbol = indexd["symbol"]
        data.append(
            {
                "name": name,
                "symbol": symbol,
                "price": priceData["curr_price"],
                "price_change": priceData["price_change"],
                "per_change": priceData["per_change"],
            }
        )
    return {
        "data": data,
        "total_pages": int(len(indexData) / 10),
        "page_num": int(len(indexData) / 10),
    }


def best_sector_etf():
    with open("./data/Best_Sector_ETF.json") as file:
        sectorData = json.load(file)
    data = []
    for sd in sectorData:
        priceData = etfs.get_curr_data(sd["symbol"])
        name = sd["name"]
        symbol = sd["symbol"]
        data.append(
            {
                "name": name,
                "symbol": symbol,
                "price": priceData["curr_price"],
                "price_change": priceData["price_change"],
                "per_change": priceData["per_change"],
            }
        )
    return {
        "data": data,
        "total_pages": int(len(sectorData) / 10),
        "page_num": int(len(sectorData) / 10),
    }


def etfCurrentPrice(symbol: str):
    data = etfs.get_curr_data(symbol)
    return data


def etfDetails(symbol: str):
    info = yf.Ticker(symbol).info
    priceData = etfs.get_curr_data(symbol)

    return {
        "info": info,
        "priceData": priceData
    }


def etfHistoricalData(symbol: str, period: str, interval: str):
    historical_data = json.loads(yf.Ticker(symbol).history(period, interval).to_json(orient="table"))['data']
    return historical_data

def handle_search_etfs(search: str):
    with open("./data/all_ETFs.json", "r") as etfFile:
        data = json.load(etfFile)
    searchedETF = []  
    for etfD in data[1:]:
        if search in etfD['0'] or search in etfD['0'].lower():
            searchedETF.append({
                                "name": etfD['0'],
                                "symbol": etfD['1']
                                })
    return searchedETF