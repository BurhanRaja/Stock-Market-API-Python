import yfinance as yf
import pandas as pd
import json
from pprint import pprint
from yahooquery import Ticker

def handle_stock_list(exchange: str, limit: int, offset: int):
    if (exchange == "NSE"):
        tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50', match="Company Name")
        data = tickers[0].to_json(orient="records")
        objArr = json.loads(data)

        refinedData = []

        for el in objArr[limit:offset]:
            stock = yf.Ticker(el['Symbol'] + ".NS").info
            current_gap_percentage = round(((stock['currentPrice'] - stock['regularMarketOpen']) / stock['currentPrice']) * 100, 2)
            curr_gap = round(stock['currentPrice'] - stock['regularMarketOpen'], 2)
            
            refinedData.append({
                'company_name': el['Company Name'],
                'symbol': el['Symbol'] + ".NS",
                'sector': el['Sector[18]'],
                'curr_per': current_gap_percentage,
                'curr_gap': curr_gap
            })
        return refinedData
    else:
        tickers = pd.read_html('https://en.wikipedia.org/wiki/BSE_SENSEX', match="ticker Number")
        data = tickers[0].to_json(orient="records")
        objArr = json.loads(data)
        
        refinedData = []
        
        print(len(objArr))

        for el in objArr[limit:offset]:
            stock = yf.Ticker(el['Symbol']).info
            current_gap_percentage = round(((stock['currentPrice'] - stock['regularMarketOpen']) / stock['currentPrice']) * 100, 2)
            curr_gap = round(stock['currentPrice'] - stock['regularMarketOpen'], 2)
            
            refinedData.append({
                'company_name': el['Companies'],
                'symbol': el['Symbol'],
                'sector': el['Sector'],
                'curr_per': current_gap_percentage,
                'curr_gap': curr_gap
            })
        return refinedData

def handle_stock_details(symbol):
    stock1 = yf.Ticker(symbol).info
    stock2 = Ticker(symbol)
    
    
    
    return

data1 = Ticker('ASIANPAINT.NS')
data2 = yf.Ticker("ASIANPAINT.NS")
# pprint(json.loads(data1.balance_sheet().to_json(orient="records")))
pprint(json.loads(data1.income_statement('a').to_json(orient="records")))
# # pprint(Ticker('0P0000XVT7.BO').fund_performance)

'''
financial_ratios: 
(yahoofinance)
    Profitability
        operatingMargins:
        profitMargins(net profit margin):
        returnOnAssets:
        returnOnEquity:
    Operational
        currentRatio:
        quickRatio:
        debtToEquity:
    Valuatuion
        P/E: forwardPE
        P/B: currentPrice / bookValue
        EV / EBITDA: (currentPrice * sharesOutstanding) + totalDebt - totalCash
        Dividend_Yield: trailingAnnualDividendYield
'''

'''
Revenue Statement
    TotalRevenue:
    OperatingRevenue:
    NetIncome:
    OperatingIncome:
'''

'''
Cash Flow for graph (Yearly/ Quaterly)
    OperatingCashFlow:
    InvestingCashFlow:
    FinancingCashFlow:
'''

'''
Balance_Sheet for graph (Yearly / Quaterly)
    TotalAssets:
    TotalDebt:
'''
