from mftool import Mftool
from pprint import pprint
import json
import numpy as np
from array import array

mf = Mftool()

# scheme_codes = mf.get_scheme_codes(as_json=True)

# obj = json.loads(scheme_codes)
# scheme_code_list = np.array([x for x in obj])

# print(len(obj))
# print(len(scheme_code_list))

# fundHouses = []
# for scheme_code in scheme_code_list:
#     data = mf.get_scheme_details(scheme_code)
#     if data['fund_house'] not in fundHouses:
#         print(data['fund_house'])
#         fundHouses.append(data['fund_house'])
# print(fundHouses)

    
# data = mutual_fund_all(scheme_code_list)
# print(data['fundHouses'])
scheme_codes = mf.get_available_schemes('Nippon India')

# obj = json.loads(scheme_codes)
scheme_code_list = [x for x in scheme_codes]

# num1 = 1
# num2 = 5
# for x in scheme_code_list[num1:num2]:
#     data = mf.get_scheme_details(x)
#     print(data)

# mf.calculate_returns()

# print("Nippon India Mutual Fund".split(" Mutual Fund"))

# mf.calculate_returns()



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