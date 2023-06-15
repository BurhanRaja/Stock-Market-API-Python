from pandas_datareader import data as pdr
from pprint import pprint
import json
import pandas as pd

import yfinance as yf

# yf.pdr_override()

# tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50', match="Company Name")
# data = tickers[0].to_json(orient="records")

# obj = json.loads(data);

# refinedData = []

# for el in obj:
#     refinedData.append({
#         'company_name': el['Company Name'],
#         'symbol': el['Symbol'] + ".NS",
#         'sector': el['Sector[18]']
#     })

# print(refinedData)


# tickers = pd.read_html('https://en.wikipedia.org/wiki/BSE_SENSEX', match="ticker Number")
# data = tickers[0].to_json(orient="records")

# print(data)

# obj = json.loads(data)

# refinedData = []

# for el in obj:
#     refinedData.append({
#         'company_name': el['Companies'],
#         'symbol': el['Symbol'],
#         'sector': el['Sector']
#     })

# print(refinedData)
