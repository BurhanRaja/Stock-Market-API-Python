import requests
from bs4 import BeautifulSoup

class MUTUALFUND:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
    
    def get_curr_data(self, symbol: str):
        data=self.session.get("https://finance.yahoo.com/quote/"+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        price=float(html.find(class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").getText())
        price_change=float(html.find(class_="Fw(500) Pstart(8px) Fz(24px)").find("span").getText().replace("+", ""))
        per_change=float(html.find_all(class_="Fw(500) Pstart(8px) Fz(24px)")[1].find("span").getText().replace("(", "").replace(")", "").replace("+", "").replace("%", ""))
        
        return {
            "curr_price": price,
            "price_change": price_change,
            "per_change": per_change
        }
        
    def get_performace(self, symbol: str):
        data=self.session.get("https://finance.yahoo.com/quote/"+symbol+"/performance?p="+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")
        
        returnsTable=html.find(class_="Pb(20px) smartphone_Px(20px) smartphone_Pt(20px)").find_all(class_="Mb(25px)")[1]
        all_returns=returnsTable.find_all(class_="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)")
        
        ytd=all_returns[0].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        one_month=all_returns[1].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        three_month=all_returns[2].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        one_year=all_returns[3].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        three_year=all_returns[4].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        five_year=all_returns[5].find(class_="W(20%) D(b) Fl(start) Ta(e)").getText().replace("%", "")
        
        return {
            "ytd": float(ytd),
            "one_month": float(one_month),
            "three_month": float(three_month),
            "one_year": float(one_year),
            "three_year": float(three_year),
            "five_year": float(five_year)
        }
        
    def get_holdings_data(self, symbol: str):
        data=self.session.get("https://finance.yahoo.com/quote/"+symbol+"/holdings?p="+symbol, headers=self.headers)
        html=BeautifulSoup(data.text, "html.parser")

        alltable=html.find(id="Main").find("section").find_all(class_="Mb(25px)")
        
        positionComposition=alltable[0].find_all(class_="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)")
        positionCompositionData=[]
        
        for pc in positionComposition:
            name=pc.find(class_="Mend(5px) Whs(nw)").getText()
            value=pc.find(class_="Fl(end)").getText()
            positionCompositionData.append({
                "name": name,
                "value": float(value.replace("%",""))
            })
        
        sectorWeighting=alltable[1].find_all(class_="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)")
        sectorWeightingData=[]
        
        for sw in sectorWeighting:
            name=sw.find(class_="Mend(5px) Whs(nw)").getText()
            value=sw.find(class_="W(20%) D(b) Fl(start) Ta(e)").getText()
            sectorWeightingData.append({
                "name": name,
                "value": float(value.replace("%",""))
            })
        
        equityHoldings=alltable[2].find_all(class_="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)")
        equityHoldingsData=[]
        
        for eh in equityHoldings:
            name=eh.find(class_="Mend(5px) Whs(nw)").getText()
            value=eh.find(class_="W(20%) D(b) Fl(start) Ta(e)").getText()
            equityHoldingsData.append({
                "name": name,
                "value": value
            })
        
        return {
            "portfolioComposition": positionCompositionData,
            "sectorWeighting": sectorWeightingData,
            "equityHoldings": equityHoldingsData
        }
        