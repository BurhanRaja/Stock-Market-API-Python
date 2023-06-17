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
                    "return_one_year": int(performace['trailingReturns']['oneYear']) * 100, 
                    "return_five_year": int(performace['trailingReturns']['fiveYear']) * 100, 
                })
        with open("./data/Nippon.json", "w") as write_file:
            json.dump(refinedArray, write_file)
    elif isinstance(data, list):
        for item in data:
            find_values_with_word(item, word)

# Load JSON data from a file
with open('./data/code.json') as file:
    json_data = json.load(file)

# Specify the word you're looking for
search_word = "Nippon"

# Call the function to find values containing the word
find_values_with_word(json_data, search_word)

# pprint(json.loads(mf.get_scheme_info("0P00005UXL")))
# print(mf.get_available_schemes(search_word))
# pprint(yq.Ticker("0P00005UXL.BO").price["0P00005UXL.BO"]['regularMarketPrice'])
# pprint(yq.Ticker("0P00005UXL.BO").fund_performance["0P00005UXL.BO"])