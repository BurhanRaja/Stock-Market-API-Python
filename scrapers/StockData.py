import requests
from bs4 import BeautifulSoup
import pprint
import re

class STOCKMARKET:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
    
    # def get_nifty_50(self):
    #     data = self.session.get("https://www.nseindia.com", headers=self.headers)
    #     html = BeautifulSoup(data.text, 'html.parser')
    #     data = html.find_all(class_ = "tab_box")[0]
    #     name=data.find(class_="tb_name").getText()
    #     curr_price=data.find(class_="tb_val").getText().split()[0]
    #     change=data.find(class_="tb_per").getText().split()
    #     curr_change=float(change[0])
    #     curr_per_change=float(change[1][1:-2])

    #     return {
    #         "name": name,
    #         "curr_price": curr_price,
    #         "curr_change": curr_change,
    #         "curr_per_change": curr_per_change
    #     }
    # Get Index Data
    def get_index_data(self, urlStr="nse/nifty"):
        data=self.session.get("https://ticker.finology.in/market/index/"+urlStr, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        # Get Name
        name=html.find("h1").getText()
        
        # Get Data
        data=html.find(id="mainContent_clsprice")
        curr_price=float(data.find(class_="currprice").find(class_="Number").getText())
        
        check=data.find(id="mainContent_pnlPriceChange").find(class_="text-success")
        
        curr_change=""
        curr_per_change=""
        
        if (check != None):
            curr_change=float(data.find(id="mainContent_pnlPriceChange").find(class_="text-success").find(class_="Number").getText())
            curr_per_change=float("0"+data.find(id="mainContent_pnlPriceChange").find_all(class_="text-success")[1].find(class_="Number").getText())
        else:
            curr_change=float("-"+data.find(id="mainContent_pnlPriceChange").find(class_="text-danger").find(class_="Number").getText())
            curr_per_change=float("-0"+data.find(id="mainContent_pnlPriceChange").find_all(class_="text-danger")[1].find(class_="Number").getText())
        
        return {
            "name": name,
            "curr_price": curr_price,
            "curr_change": curr_change,
            "curr_per_change": curr_per_change
        }
        
    # Get Index Gainers and losers
    def get_market_gainers(self, skip: int, limit: int):
        data=self.session.get("https://ticker.finology.in/market/top-gainers", headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        gainersTable=html.find(id="mainContent_pnlhighlow").find("tbody").find_all("tr")
        gainersData=[]
        
        for gainers in gainersTable[skip:limit]:
            g=gainers.find_all("td")[1:]
            gainersData.append({
                "symbol": g[0].find("a").attrs["href"].split("/")[2],
                "company": g[0].find("a").getText(),
                "price": float(g[1].getText()),
                "change": float(g[2].find('span').getText().replace("%", "").replace("+", "")),
            })
        
        return gainersData
    
    def get_market_losers(self, skip: int, limit: int):
        data=self.session.get("https://ticker.finology.in/market/top-losers", headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        losersTable=html.find(id="mainContent_pnlhighlow").find("tbody").find_all("tr")
        losersData=[]
        
        for losers in losersTable[skip:limit]:
            l=losers.find_all("td")[1:]
            losersData.append({
                "symbol": l[0].find("a").attrs["href"].split("/")[2],
                "company": l[0].find("a").getText(),
                "price": float(l[1].getText()),
                "change": float(l[2].find('span').getText().replace("%", "").replace("+", "")),
            })
        
        return losersData
        
    
    # Get Company Data
    def get_company_data(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        full_name=html.find(id="mainContent_ltrlCompName").getText()
        
        priceData=html.find(id="mainContent_clsprice")
        curr_price=float(priceData.find(class_="currprice").find(class_="Number").getText())
        
        changeData=priceData.find(id="mainContent_pnlPriceChange").getText()
        
        curr_change=float(changeData.split()[0].replace("+", ""))
        curr_per_change=float(changeData.split()[1].replace("(", "").replace(")", "").replace("%", ""))
        
        return {
            "name": full_name,
            "symbol": symbol,
            "curr_price": curr_price,
            "curr_change": curr_change,
            "curr_per_change": curr_per_change
        }
    
    # Get Company Price Summary
    def get_company_price_summary(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        priceData=html.find(id="mainContent_clsprice")
        curr_price=float(priceData.find(class_="currprice").find(class_="Number").getText())
        
        todaysHigh=float(html.find(id="mainContent_ltrlTodayHigh").getText())
        yearHigh=float(html.find(id="mainContent_ltrl52WH").getText())
        todaysLow=float(html.find(id="mainContent_ltrlTodayLow").getText())
        yearLow=float(html.find(id="mainContent_ltrl52WL").getText())
        
        return {
            "curr_price": curr_price,
            "today_high": todaysHigh,
            "today_low": todaysLow,
            "year_high": yearHigh,
            "year_low": yearLow
        }
    
    def get_company_essentials(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        companyData=html.find(id="mainContent_updAddRatios").find_all(class_="compess")[:-1]
        companyEssentials=[]
        # d=companyData.find("small").getText()
        for data in companyData:
            companyEssentials.append({
                "name": re.sub(" +", " ", data.find("small").getText().replace("\n", "").replace("\r", "")),
                "value": re.sub(" +", " ", data.find("p").getText().replace("\n", "").replace("\r", "")).replace("\xa0", "")
            })
        return companyEssentials
    
    # Get Quaterly Results
    def get_quaterly_results(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        quaterlyTable=html.find(id="mainContent_quarterly").find("table")
        
        tableBody=quaterlyTable.find("tbody").find_all("tr")
        
        quaterlyTableData=[]
        
        for allRow in tableBody:
            head=allRow.find("th").getText()
            allCol=allRow.find_all("td")
            
            quaterlyTableData.append({
                "particular": head,
                "March 2022": re.sub(" +", " ", allCol[0].find("span").getText().replace("\n", "").replace("\r", "")),
                "Jun 2022": re.sub(" +", " ", allCol[1].find("span").getText().replace("\n", "").replace("\r", "")),
                "Sep 2022": re.sub(" +", " ", allCol[2].find("span").getText().replace("\n", "").replace("\r", "")),
                "Dec 2022": re.sub(" +", " ", allCol[3].find("span").getText().replace("\n", "").replace("\r", "")),
                "March 2022": re.sub(" +", " ", allCol[4].find("span").getText().replace("\n", "").replace("\r", ""))
            })
        
        return quaterlyTableData

    # Get yearly Results 
    def get_yearly_results(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        yearlyTable=html.find(id="profit").find("table")
        
        tableBody=yearlyTable.find("tbody").find_all("tr")
        
        yearlyTableData=[]
        
        for allRow in tableBody:
            head=allRow.find("th").getText()
            allCol=allRow.find_all("td")
            
            yearlyTableData.append({
                "particular": head,
                "March 2019": re.sub(" +", " ", allCol[0].find("span").getText().replace("\n", "").replace("\r", "")),
                "March 2020": re.sub(" +", " ", allCol[1].find("span").getText().replace("\n", "").replace("\r", "")),
                "March 2021": re.sub(" +", " ", allCol[2].find("span").getText().replace("\n", "").replace("\r", "")),
                "March 2022": re.sub(" +", " ", allCol[3].find("span").getText().replace("\n", "").replace("\r", "")),
                "March 2023": re.sub(" +", " ", allCol[4].find("span").getText().replace("\n", "").replace("\r", ""))
            })
        
        return yearlyTableData
    
    # Get Yearly Balance Sheet
    def get_yearly_balance_sheet(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        balanceSheetTable=html.find(id="balance").find("table")
        
        tableBody=balanceSheetTable.find("tbody").find_all("tr")
        
        equityLiabilities=[]
        assets=[]
        
        for index, allRow in enumerate(tableBody):
            if (index > 0 and index < 7):
                head=allRow.find("th").getText()
                allCol=allRow.find_all("td")
                
                equityLiabilities.append({
                    "particular": head,
                    "March 2019": re.sub(" +", " ", allCol[0].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2020": re.sub(" +", " ", allCol[1].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2021": re.sub(" +", " ", allCol[2].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2022": re.sub(" +", " ", allCol[3].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2023": re.sub(" +", " ", allCol[4].find("span").getText().replace("\n", "").replace("\r", ""))
                })
            
            if (index > 7):
                head=allRow.find("th").getText()
                allCol=allRow.find_all("td")
                
                assets.append({
                    "particular": head,
                    "March 2019": re.sub(" +", " ", allCol[0].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2020": re.sub(" +", " ", allCol[1].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2021": re.sub(" +", " ", allCol[2].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2022": re.sub(" +", " ", allCol[3].find("span").getText().replace("\n", "").replace("\r", "")),
                    "March 2023": re.sub(" +", " ", allCol[4].find("span").getText().replace("\n", "").replace("\r", ""))
                })
        
        balanceSheetTableData= {
            "equityLiabilities": equityLiabilities,
            "assets" : assets
        }
        
        return balanceSheetTableData

    # Get Yearly Cash Flow
    def get_yearly_cash_flow(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        yearlyTable=html.find(id="mainContent_cashflows").find("table")
        
        tableBody=yearlyTable.find("tbody").find_all("tr")
        
        yearlyTableData=[]
        
        for allRow in tableBody:
            head=allRow.find("th").getText()
            allCol=allRow.find_all("td")[:-3]
            
            yearlyTableData.append({
                "particular": head,
                "March 2019": re.sub(" +", " ", allCol[0].getText().replace("\n", "").replace("\r", "")),
                "March 2020": re.sub(" +", " ", allCol[1].getText().replace("\n", "").replace("\r", "")),
                "March 2021": re.sub(" +", " ", allCol[2].getText().replace("\n", "").replace("\r", "")),
                "March 2022": re.sub(" +", " ", allCol[3].getText().replace("\n", "").replace("\r", "")),
                "March 2023": re.sub(" +", " ", allCol[4].getText().replace("\n", "").replace("\r", ""))
            })
        
        return yearlyTableData
    
    # Get All Ratios
    def get_ratios(self, symbol: str):
        data=self.session.get("https://ticker.finology.in/company/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        ratiosData=html.find(id="ratios").find_all(class_="col-12")
        allRatios=[]
        
        for ratios in ratiosData:
            name=re.sub(" +", " ", ratios.find(class_="card").find("h4").getText().replace("\n", "").replace("\r", ""))
            
            ratiosYears = ratios.find_all(class_="ratiosingle")
            data=""
            if (len(ratiosYears) > 0):
                data={
                    "1 year": re.sub(" +", " ", ratiosYears[0].find(class_="durationvalue").getText().replace("\n", "").replace("\r", "")),
                    "3 year": re.sub(" +", " ", ratiosYears[1].find(class_="durationvalue").getText().replace("\n", "").replace("\r", "")),
                    "5 year": re.sub(" +", " ", ratiosYears[2].find(class_="durationvalue").getText().replace("\n", "").replace("\r", ""))
                }
            else:
                data=re.sub(" +", " ", ratios.find(class_="h2").getText().replace("\n", "").replace("\r", ""))
            
            allRatios.append({
                "name": name,
                "data": data
            })
            
        return allRatios
        
        