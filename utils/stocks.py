import yfinance as yf
import pandas as pd
import json
from yahooquery import Ticker
from pprint import pprint
from yahoofinancials import YahooFinancials
from nsepython import *
from scrapers.StockData import STOCKMARKET
from scrapers.MutualFunds import MUTUALFUND
from scrapers.ETF import ETF

stock=STOCKMARKET()
mutualFunds=MUTUALFUND()
etfs=ETF()

# Stock List
def handle_stock_list(exchange: str, offset: int, limit: int):
    if (exchange == "NSE"):
        with open("./data/NSE_Stocks.json", "r") as file:
            objArr = json.load(file)
        refinedData = []
        for el in objArr[offset:limit]:
            data=stock.get_company_data(el['Symbol'])
            refinedData.append(data)
        return refinedData
    else:
        with open("./data/BSE_Stocks.json", "r") as file:
            objArr = json.load(file)
        refinedData = []
        for el in objArr[offset:limit]:
            data=stock.get_company_data(el['Symbol'].replace(".BO", ""))
            refinedData.append(data)
        return refinedData

# Stock Financial Ratios
def handle_stock_financial_ratios(symbol: str):
    financial = stock.get_financial_ratios(symbol)
    return financial

# Stock Revenue Statement Graph
def handle_stock_revenue_statement_graph(symbol: str, duration: str):
    stock = Ticker(symbol)
    incomeStmt = json.loads(stock.income_statement(duration).to_json(orient="records"))
    revenue_statement = []

    for istmt in incomeStmt:
        revenue_statement.append({
            'period_type': istmt.get('periodType', 'N/A'),
            'as_of_date': pd.to_datetime(istmt.get('asOfDate', 0), unit='ms'),
            'Total_revenue': istmt.get('TotalRevenue', 0),
            'Net_income': istmt.get('NetIncome', 0),
            'Operating_income': istmt.get('OperatingIncome', 0)
        })
    return revenue_statement

# Stock Cash Flow Graph
def handle_stock_cash_flow_graph(symbol: str, duration: str):
    stock = Ticker(symbol)
    cashflowStmt = json.loads(stock.cash_flow(duration).to_json(orient="records"))

    cashflow_statement = []

    for cstmt in cashflowStmt:
        if (cstmt['OperatingCashFlow'] != None and cstmt['InvestingCashFlow'] != None and cstmt['FinancingCashFlow'] != None):
            cashflow_statement.append({
                'operating_cash_flow': cstmt.get('OperatingCashFlow', 0),
                'investing_cash_flow': cstmt.get('InvestingCashFlow', 0),
                'financing_cash_flow': cstmt.get('FinancingCashFlow', 0),
                'period_type': cstmt.get('periodType', 0),
                'as_of_date': pd.to_datetime(cstmt.get('asOfDate', 0), unit='ms'),
            })

    return cashflow_statement

# Stock Balance Sheet Graph
def handle_stock_balance_sheet_graph(symbol: str, duration: str):
    stock = Ticker(symbol)
    balanceSheet = json.loads(stock.balance_sheet(duration).to_json(orient="records"))

    balance_sheet = []

    for bSheet in balanceSheet:
        balance_sheet.append({
            'total_assets': bSheet.get('TotalAssets', 0),
            'total_debt': bSheet.get('TotalDebt', 0),
            'period_type': bSheet.get('periodType', 0),
            'as_of_date': pd.to_datetime(bSheet.get('asOfDate', 0), unit='ms'),
        })

    return balance_sheet

# Stock Historical Data
def handle_stock_historical_data(symbol: str, period: str, interval: str):
    historical_data = json.loads(yf.Ticker(symbol+".NS").history(period, interval).to_json(orient="table"))['data']
    return historical_data

# Stock Info Profile
def handle_stock_info_profile(symbol: str):
    stock = yf.Ticker(symbol)
    return {
        'info': stock.info
    }

# Stock Balance Sheet
def handle_stock_balance_sheet(symbol: str, duration: str):
    stock = Ticker(symbol)
    balancesheet = json.loads(stock.balance_sheet(duration).to_json(orient="records"))
    return balancesheet

# Stock Cash Flow
def handle_stock_cash_flow(symbol: str, duration: str):
    stock = Ticker(symbol)
    cashflow = json.loads(stock.cash_flow(duration).to_json(orient="records"))
    return cashflow

# Stock Income Statement
def handle_stock_income_statement(symbol: str, duration: str):
    stock = Ticker(symbol)
    incomestatement = json.loads(stock.income_statement(duration).to_json(orient="records"))
    return incomestatement

def handle_stock_price(symbol: str):
    stock = yf.Ticker(symbol).info
    current_gap_percentage = ((stock['currentPrice'] - stock['regularMarketPreviousClose']) / stock['currentPrice']) * 100
    curr_gap = round(stock['currentPrice'] - stock['regularMarketPreviousClose'], 2)

    return {
        'curr_price': stock['currentPrice'],
        'curr_gap' : curr_gap,
        'curr_gap_percentage': current_gap_percentage
    }
    
def handle_index():
    nse = YahooFinancials('^NSE')
    bse = YahooFinancials("^BSESN")

    return {
        "nse": {
            "name": "NIFTY50",
            "symbol": "^NSEI",
            "current_price": nse.get_current_price(),
            "curr_per": nse.get_current_percent_change(),
            "curr_gap": nse.get_current_change()
        },
        "bse": {
            "name": "SENSEX",
            "symbol": "^BSESN",
            "current_price": bse.get_current_price(),
            "curr_per": bse.get_current_percent_change(),
            "curr_gap": bse.get_current_change()
        }
    }
    
def handle_top_stock():
    top_gainers = json.loads(nse_get_top_gainers().to_json(orient="records"))
    top_losers = json.loads(nse_get_top_losers().to_json(orient="records"))

    return {
        "gainers": top_gainers,
        "losers": top_losers
    }
