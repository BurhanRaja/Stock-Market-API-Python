from mftool import Mftool
from pprint import pprint
import json
import numpy as np
from array import array
from yahooquery import Ticker
from financedatabase import Funds, Equities, ETFs

mf = Mftool()

# print(mf.get_scheme_codes())

data = json.loads(Funds().search(country="India", currency="INR", category_group="Value Fund").to_json(orient="table"))



# data = Ticker('HDFCNEXT50.NS').fund_holding_info
pprint(data)