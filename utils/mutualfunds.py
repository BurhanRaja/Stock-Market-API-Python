from mftool import Mftool
import json
import yahooquery as yq
from yahoofinancials import YahooFinancials

mf = Mftool()

refinedArray=[]

def traverse_mutual_fund_all(data, skip: int=None, limit: int=None):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                traverse_mutual_fund_all(value)
            elif isinstance(value, str):
                performace = yq.Ticker(key+".BO").fund_performance[key+".BO"]
                refinedArray.append({
                    "symbol": key,
                    "fund": value,
                    "return_one_year": float(performace['trailingReturns']['oneYear']) * 100, 
                    "return_five_year": float(performace['trailingReturns']['fiveYear']) * 100, 
                })
    elif isinstance(data, list):
        for item in data[skip:limit]:
            traverse_mutual_fund_all(item)
    return refinedArray

# Get All Mutual Fund
def all_mutual_fund(skip: int, limit: int):
    with open('./data/code.json') as file:
        json_data = json.load(file)
    
    arr = traverse_mutual_fund_all(json_data, skip, limit)
    
    return arr

# Get UTI Mutual Fund
def uti_mutual_fund(skip: int, limit: int):
    with open('./data/UTI.json') as file:
        json_data = json.load(file)
    
    return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": limit / 10
    }

# Get Union Mutual Fund
def union_mutual_fund(skip: int, limit: int):
    with open('./data/Union.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Tata Mutual Fund
def tata_mutual_fund(skip: int, limit: int):
    with open('./data/Tata.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get SBI Mutual Fund
def sbi_mutual_fund(skip: int, limit: int):
    with open('./data/SBI.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Reliance Mutual Fund
def reliance_mutual_fund(skip: int, limit: int):
    with open('./data/Reliance.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Nippon Mutual Fund
def nippon_mutual_fund(skip: int, limit: int):
    with open('./data/Nippon.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Navi Mutual Fund
def navi_mutual_fund(skip: int, limit: int):
    with open('./data/Navi.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Motilal Mutual Fund
def moitilal_mutual_fund(skip: int, limit: int):
    with open('./data/Motilal_Oswal.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Mahindra Manulife Mutual Fund
def mahindra_manulife_mutual_fund(skip: int, limit: int):
    with open('./data/Mahindra_Manulife.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get LIC Mutual Fund
def lic_mutual_fund(skip: int, limit: int):
    with open('./data/LIC.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Kotak Mahindra Mutual Fund
def kotak_mutual_fund(skip: int, limit: int):
    with open('./data/Kotak_Mahindra.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get IDFC Mutual Fund
def idfc_mutual_fund(skip: int, limit: int):
    with open('./data/IDFC.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get IDBI Mutual Fund
def idbi_mutual_fund(skip: int, limit: int):
    with open('./data/IDBI.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get ICICI Mutual Fund
def icici_mutual_fund(skip: int, limit: int):
    with open('./data/ICICI.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get HSBC Mutual Fund
def hsbc_mutual_fund(skip: int, limit: int):
    with open('./data/HSBC.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get HDFC Mutual Fund
def hdfc_mutual_fund(skip: int, limit: int):
    with open('./data/HDFC.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Franklin Mutual Fund
def franklin_mutual_fund(skip: int, limit: int):
    with open('./data/Franklin.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Axis Mutual Fund
def axis_mutual_fund(skip: int, limit: int):
    with open('./data/Axis.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Aditya Birla Mutual Fund
def aditya_birla_mutual_fund(skip: int, limit: int):
    with open('./data/Aditya_Birla_Sun_Life.json') as file:
        json_data = json.load(file)
    
    
    return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Best Debt Fund
def best_debt_mutual_fund(skip: int, limit: int):
    with open('./data/Best_Debt_Funds.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Best Equity Fund
def best_equity_mutual_fund(skip: int, limit: int):
    with open('./data/Best_Equity_Funds.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Best Long Duration Fund
def best_long_duration_mutual_fund(skip: int, limit: int):
    with open('./data/Best_Long_Duration_Funds.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Best Returns Fund
def best_returns_mutual_fund(skip: int, limit: int):
    with open('./data/Best_Returns_Funds.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }

# Get Best Tax Saver Fund
def best_tax_saver_mutual_fund(skip: int, limit: int):
    with open('./data/Best_Tax_Saver_Funds.json') as file:
        json_data = json.load(file)
    
        return {
        "data": json_data[skip:limit],
        "total_pages": int(len(json_data) / 10),
        "page_num": int(limit / 10)
    }
        
# Mutual Fund History 
def mutualfund_history(mf_id: str, duration: str):
    history_data = mf.history(mf_id,start=None,end=None,period=duration,as_dataframe=True)
    
    return json.loads(history_data.to_json(orient="table"))['data']

# Mutual Fund Details
def mutualfund_info(mf_id: str):
    info_data = json.loads(mf.get_scheme_info(mf_id))
    performance = yq.Ticker(mf_id+".BO").fund_performance
    ownership = json.loads(yq.Ticker(mf_id+".BO").fund_ownership.to_json(orient="records"))
    bondHoldings = yq.Ticker(mf_id+".BO").fund_bond_holdings
    equityHoldings = yq.Ticker(mf_id+".BO").fund_equity_holdings
    holdingInfo = yq.Ticker(mf_id+".BO").fund_holding_info
    return {
        "info": info_data,
        "ownership": ownership,
        "performance": performance[mf_id+".BO"],
        "holding_info": holdingInfo[mf_id+".BO"],
        "bond_holdings": bondHoldings[mf_id+".BO"],
        "equity_holdings": equityHoldings,
    }

def mutualFundCurrentPrice(symbol: str):
    return {
        "curr_price" : YahooFinancials(symbol + ".BO").get_current_price(),
        "curr_per_change": YahooFinancials(symbol + ".BO").get_current_percent_change(),
        "curr_change": YahooFinancials(symbol + ".BO").get_current_change(),
    }
