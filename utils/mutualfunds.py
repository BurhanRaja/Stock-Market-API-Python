from mftool import Mftool
from pprint import pprint
import json
import yahooquery as yq
from yfinance import Ticker

mf = Mftool()

refinedArray=[]

def find_values_with_word(data, word):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                find_values_with_word(value, word)
            elif isinstance(value, str) and word in value:
                performace = yq.Ticker(key+".BO").fund_performance[key+".BO"]
                refinedArray.append({
                    "symbol": key,
                    "fund": value,
                    "return_one_year": performace['trailingReturns']['oneYear'] * 100, 
                    "return_five_year": performace['trailingReturns']['fiveYear'] * 100, 
                })
        with open("./data/Axis.json", "w") as write_file:
            json.dump(refinedArray, write_file)
    elif isinstance(data, list):
        for item in data:
            find_values_with_word(item, word)

# Load JSON data from a file
with open('./data/code.json') as file:
    json_data = json.load(file)

# Specify the word you're looking for
search_word = "Axis"

# Call the function to find values containing the word
find_values_with_word(json_data, search_word)

# Aditya Birla Sun Life Mutual Fund
# Axis Mutual Fund
# Bandhan Mutual Fund
# Baroda BNP Paribas Mutual Fund
# Canara Robeco Mutual Fund
# DSP Mutual Fund
# Edelweiss Mutual Fund
# Franklin Templeton Mutual Fund
# HDFC Mutual Fund
# HSBC Mutual Fund
# ICICI Prudential Mutual Fund
# Invesco Mutual Fund
# ITI Mutual Fund
# Kotak Mahindra Mutual Fund
# LIC Mutual Fund
# Mirae Asset Mutual Fund
# Nippon India Mutual Fund
# Reliance Mutual Fund
# DHFL Pramerica Mutual Fund
# PGIM India Mutual Fund
# SBI Mutual Fund
# Sundaram Mutual Fund
# Tata Mutual Fund
# Trust Mutual Fund
# UTI Mutual Fund
# Union Mutual Fund
# IDFC Mutual Fund
# Bank of India Mutual Fund
# IDBI Mutual Fund
# Groww Mutual Fund
# JM Financial Mutual Fund
# Mahindra Manulife Mutual Fund
# Quantum Mutual Fund
# quant Mutual Fund
# Baroda Pioneer Mutual Fund
# Motilal Oswal Mutual Fund
# Navi Mutual Fund
# PPFAS Mutual Fund
# Taurus Mutual Fund
# WhiteOak Capital Mutual Fund
# BOI AXA Mutual Fund
# Indiabulls Mutual Fund
# NJ Mutual Fund
# Samco Mutual Fund
# Shriram Mutual Fund

# pprint(json.loads(mf.get_scheme_info("0P00005UXL")))
# print(mf.get_available_schemes(search_word))
# pprint(yq.Ticker("0P00005UXL.BO").price["0P00005UXL.BO"]['regularMarketPrice'])
# pprint(yq.Ticker("0P00005UXL.BO").fund_performance["0P00005UXL.BO"])