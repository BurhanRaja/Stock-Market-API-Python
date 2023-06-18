from fastapi import FastAPI
from utils.stocks import *
from utils.mutualfunds import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# ------------------------------------ STOCKS -------------------------------------------

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


# -------------------------------- MUTUAL FUND ----------------------------------

# Get All Mutual Fund
@app.get("/mutualfund/all")
def read_all_mf(skip: int, limit: int):
    data = all_mutual_fund(skip, limit)
    return data

# Get UTI Mutual Fund
@app.get("/mutualfund/uti")
def read_uti_mf(skip: int, limit: int):
    data = uti_mutual_fund(skip, limit)
    return data

# Get Union Mutual Fund
@app.get("/mutualfund/union")
def read_union_mf(skip: int, limit: int):
    data = union_mutual_fund(skip, limit)
    return data

# Get Tata Mutual Fund
@app.get("/mutualfund/tata")
def read_tata_mf(skip: int, limit: int):
    data = tata_mutual_fund(skip, limit)
    return data

# Get SBI Mutual Fund
@app.get("/mutualfund/sbi")
def read_sbi_mf(skip: int, limit: int):
    data = sbi_mutual_fund(skip, limit)
    return data

# Get Reliance Mutual Fund
@app.get("/mutualfund/reliance")
def read_reliance_mf(skip: int, limit: int):
    data = reliance_mutual_fund(skip, limit)
    return data

# Get Nippon Mutual Fund
@app.get("/mutualfund/nippon")
def read_nippon_mf(skip: int, limit: int):
    data = nippon_mutual_fund(skip, limit)
    return data

# Get Navi Mutual Fund
@app.get("/mutualfund/navi")
def read_navi_mf(skip: int, limit: int):
    data = navi_mutual_fund(skip, limit)
    return data

# Get Motilal Mutual Fund
@app.get("/mutualfund/moitilal")
def read_moitilal_mf(skip: int, limit: int):
    data = moitilal_mutual_fund(skip, limit)
    return data

# Get Mahindra-Manulife Mutual Fund
@app.get("/mutualfund/mahindra-manulife")
def read_mahindra_manulife_mf(skip: int, limit: int):
    data = mahindra_manulife_mutual_fund(skip, limit)
    return data

# Get LIC Mutual Fund
@app.get("/mutualfund/lic")
def read_lic_mf(skip: int, limit: int):
    data = lic_mutual_fund(skip, limit)
    return data

# Get Kotak Mutual Fund
@app.get("/mutualfund/kotak")
def read_kotak_mf(skip: int, limit: int):
    data = kotak_mutual_fund(skip, limit)
    return data

# Get IDFC Mutual Fund
@app.get("/mutualfund/idfc")
def read_idfc_mf(skip: int, limit: int):
    data = idfc_mutual_fund(skip, limit)
    return data

# Get IDBI Mutual Fund
@app.get("/mutualfund/idbi")
def read_idbi_mf(skip: int, limit: int):
    data = idbi_mutual_fund(skip, limit)
    return data

# Get ICICI Mutual Fund
@app.get("/mutualfund/icici")
def read_icici_mf(skip: int, limit: int):
    data = icici_mutual_fund(skip, limit)
    return data

# Get HSBC Mutual Fund
@app.get("/mutualfund/hsbc")
def read_hsbc_mf(skip: int, limit: int):
    data = hsbc_mutual_fund(skip, limit)
    return data

# Get HDFC Mutual Fund
@app.get("/mutualfund/hdfc")
def read_hdfc_mf(skip: int, limit: int):
    data = hdfc_mutual_fund(skip, limit)
    return data

# Get Franklin Mutual Fund
@app.get("/mutualfund/franklin")
def read_franklin_mf(skip: int, limit: int):
    data = franklin_mutual_fund(skip, limit)
    return data

# Get Axis Mutual Fund
@app.get("/mutualfund/axis")
def read_axis_mf(skip: int, limit: int):
    data = axis_mutual_fund(skip, limit)
    return data

# Get Aditya-Birla Mutual Fund
@app.get("/mutualfund/aditya-birla")
def read_aditya_birla_mf(skip: int, limit: int):
    data = aditya_birla_mutual_fund(skip, limit)
    return data

# Get Best Debt Mutual Fund
@app.get("/mutualfund/best-debt")
def read_best_debt_mf(skip: int, limit: int):
    data = best_debt_mutual_fund(skip, limit)
    return data

# Get Best Long Duration Mutual Fund
@app.get("/mutualfund/best-long-duration")
def read_best_long_duration_mf(skip: int, limit: int):
    data = best_long_duration_mutual_fund(skip, limit)
    return data

# Get Best Returns Mutual Fund
@app.get("/mutualfund/best-returns")
def read_best_returns_mf(skip: int, limit: int):
    data = best_returns_mutual_fund(skip, limit)
    return data

# Get Best Equity Mutual Fund
@app.get("/mutualfund/best-equity")
def read_best_equity_mf(skip: int, limit: int):
    data = best_equity_mutual_fund(skip, limit)
    return data

# Get Best Tax Saver Mutual Fund
@app.get("/mutualfund/best-tax-saver")
def read_best_tax_saver_mf(skip: int, limit: int):
    data = best_tax_saver_mutual_fund(skip, limit)
    return data

@app.get("/mutualfund/history/{mf}")
def read_mutual_fund_history(mf: str, duration: str):
    history_data = mutualfund_history(mf, duration)
    return history_data

@app.get("/mutualfund/details/{mf}")
def read_mutual_fund_history(mf: str):
    history_data = mutualfund_info(mf)
    return history_data