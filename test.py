import httpx
import asyncio

async def testFunc():
    symbol="0P0001EI9O"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
    url="https://finance.yahoo.com/quote/" + symbol + "/holdings?p=" + symbol
    
    async with httpx.AsyncClient() as httpx_client:
        res = await httpx_client.get(url, headers)
    
    print(res.text)

testFunc()