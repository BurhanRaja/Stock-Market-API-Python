
# MUTUAL FUNDS
# Add all the schemes with scheme codes in json
# code.json from mftool github
# (oldest price - latest price) / oldest price
# show listing only 10 per page
# Filter using the Rapid api
# https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV

# Stocks

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



