
# MUTUAL FUNDS
# Add all the schemes with scheme codes in json
# code.json from mftool github
# (oldest price - latest price) / oldest price
# show listing only 10 per page
# Filter using the Rapid api
# https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV

from fastapi import FastAPI
from utils.stocks import *
from financedatabase import Funds
from mftool import Mftool

mf = Mftool()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# ALl Stocks NSE or BSE
@app.get("/all/stocks/{exchange}")
def read_stocks(exchange: str, skip: int = 0, limit: int = 10):
    stocklist = handle_stock_list(exchange, skip, limit)
    return stocklist

# Stock Current Price
@app.get("/stock/currentprice/{stock}")
def read_current_price(stock: str):
    stock_price = handle_stock_price(stock)
    return stock_price

# Stock Financial ratios
@app.get("/stock/financial/ratios/{stock}")
def read_stock_financial_ratios(stock: str):
    stock_financial_ratios = handle_stock_financial_ratios(stock)
    return stock_financial_ratios

# Stock Revenue Statement
@app.get("/stock/revenue/statement/graph/{stock}")
def read_stock_revenue_statement_graph(stock: str, duration: str):
    if (duration == "yearly"):
        stock_revenue_statement = handle_stock_revenue_statement_graph(stock, 'a')
    else:
        stock_revenue_statement = handle_stock_revenue_statement_graph(stock, 'q')
    return stock_revenue_statement

# Stock Balance Sheet
@app.get("/stock/balance/sheet/graph/{stock}")
def read_stock_balance_sheet_graph(stock: str, duration: str):
    if (duration == "yearly"):
        stock_balance_sheet = handle_stock_balance_sheet_graph(stock, 'a')
    else:
        stock_balance_sheet = handle_stock_balance_sheet_graph(stock, 'q')
    return stock_balance_sheet

# Stock Cash Flow
@app.get("/stock/cash/flow/graph/{stock}")
def read_cash_flow_graph(stock: str, duration: str):
    if (duration == "yearly"):
        stock_cash_flow = handle_stock_cash_flow_graph(stock, 'a')
    else:
        stock_cash_flow = handle_stock_cash_flow_graph(stock, 'q')
    return stock_cash_flow

# Stock Historical Data
@app.get("/stock/historical/data/{stock}")
def read_historical_data(stock: str, period: str, interval: str):
    stock_historical_data = handle_stock_historical_data(stock, period, interval)
    return stock_historical_data

# Stock Information
@app.get("/stock/info/{stock}")
def read_stock_info(stock: str):
    stock_info = handle_stock_info_profile(stock)
    return stock_info

# Stock Cash Flow
@app.get("/stock/cash/flow/{stock}")
def read_stock_cash_flow(stock: str, duration: str):
    if (duration == "yearly"):
        stock_cashflow = handle_stock_cash_flow(stock, 'a')
    else:
        stock_cashflow = handle_stock_cash_flow(stock, 'q')
    return stock_cashflow

# Stock Balance Sheet
@app.get("/stock/balancesheet/{stock}")
def read_balancesheet(stock: str, duration: str):
    if (duration == "yearly"):
        stock_balancesheet = handle_stock_balance_sheet(stock, 'a')
    else:
        stock_balancesheet = handle_stock_balance_sheet(stock, 'q')
    return stock_balancesheet

# Stock Income Statement
@app.get("/stock/income/statement/{stock}")
def read_income_statement(stock: str, duration: str):
    if (duration == "yearly"):
        stock_incomestatement = handle_stock_income_statement(stock, 'a')
    else:
        stock_incomestatement = handle_stock_income_statement(stock, 'q')
    return stock_incomestatement
