import yfinance as yf
import pandas as pd
import json
from yahooquery import Ticker
from pprint import pprint

# Stock List
def handle_stock_list(exchange: str, offset: int, limit: int):
    if (exchange == "NSE"):
        tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50', match="Company Name")
        data = tickers[0].to_json(orient="records")
        objArr = json.loads(data)

        refinedData = []

        for el in objArr[offset:limit]:
            stock = yf.Ticker(el['Symbol'] + ".NS").info
            current_gap_percentage = round(((stock['currentPrice'] - stock['regularMarketPreviousClose']) / stock['currentPrice']) * 100, 2)
            curr_gap = round(stock['currentPrice'] - stock['regularMarketPreviousClose'], 2)
            
            refinedData.append({
                'company_name': el['Company Name'],
                'symbol': el['Symbol'] + ".NS",
                'sector': el['Sector[18]'],
                "price": stock['currentPrice'],
                'curr_per': current_gap_percentage,
                'curr_gap': curr_gap
            })

        return refinedData
    else:
        tickers = pd.read_html('https://en.wikipedia.org/wiki/BSE_SENSEX', match="ticker Number")
        data = tickers[0].to_json(orient="records")
        objArr = json.loads(data)
        
        refinedData = []

        for el in objArr[offset:limit]:
            stock = yf.Ticker(el['Symbol']).info
            current_gap_percentage = round(((stock['currentPrice'] - stock['regularMarketPreviousClose']) / stock['currentPrice']) * 100, 2)
            curr_gap = round(stock['currentPrice'] - stock['regularMarketPreviousClose'], 2)
            
            refinedData.append({
                'company_name': el['Companies'],
                'symbol': el['Symbol'],
                'sector': el['Sector'],
                'price': stock['currentPrice'],
                'curr_per': current_gap_percentage,
                'curr_gap': curr_gap
            })
        return refinedData

# Stock Financial Ratios
def handle_stock_financial_ratios(symbol: str):
    financial = yf.Ticker(symbol).info
    debtEquity = 'N/A'
    if 'debtToEquity' in financial:
        debtEquity = financial['debtToEquity']

    financial_ratios = {
        'profitability': {
            'operating_margins': financial['operatingMargins'] * 100,
            'profit_margins': financial['profitMargins'] * 100,
            'return_on_assets': financial['returnOnAssets'] * 100,
            'return_on_equity': financial['returnOnEquity'] * 100,
        },
        'operational': {
            'current_ratio': financial['currentRatio'],
            'quick_ratio': financial['quickRatio'],
            'debt_to_equity': debtEquity
        },
        'valuation': {
            'pe_ratio': financial['trailingPE'],
            'pb_ratio': financial['currentPrice'] / financial['bookValue'],
            'ev_ebitda': (financial['currentPrice'] * financial['sharesOutstanding']) + financial['totalDebt'] - financial['totalCash'],
            'dividend_yield': financial['trailingAnnualDividendYield']
        }
    }
    return financial_ratios

# Stock Revenue Statement Graph
def handle_stock_revenue_statement_graph(symbol: str, duration: str):
    stock = Ticker(symbol)
    incomeStmt = json.loads(stock.income_statement(duration).to_json(orient="records"))
    revenue_statement = []

    for istmt in incomeStmt:
        revenue_statement.append({
            'period_type': istmt['periodType'],
            'as_of_date': pd.to_datetime(istmt['asOfDate'], unit='ms'),
            'Total_revenue': istmt['TotalRevenue'],
            'Net_income': istmt['NetIncome'],
            'Operating_income': istmt['OperatingIncome']
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
                'operating_cash_flow': cstmt['OperatingCashFlow'],
                'investing_cash_flow': cstmt['InvestingCashFlow'],
                'financing_cash_flow': cstmt['FinancingCashFlow'],
                'period_type': cstmt['periodType'],
                'as_of_date': pd.to_datetime(cstmt['asOfDate'], unit='ms'),
            })

    return cashflow_statement

# Stock Balance Sheet Graph
def handle_stock_balance_sheet_graph(symbol: str, duration: str):
    stock = Ticker(symbol)
    balanceSheet = json.loads(stock.balance_sheet(duration).to_json(orient="records"))

    balance_sheet = []

    for bSheet in balanceSheet:
        balance_sheet.append({
            'total_assets': bSheet['TotalAssets'],
            'total_debt': bSheet['TotalDebt'],
            'period_type': bSheet['periodType'],
            'as_of_date': pd.to_datetime(bSheet['asOfDate'], unit='ms'),
        })

    return balance_sheet

# Stock Historical Data
def handle_stock_historical_data(symbol: str):
    historical_data = json.loads(Ticker(symbol).history("5y", "1d").to_json(orient="records"))
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