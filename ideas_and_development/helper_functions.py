## imports
import pandas as pd
import requests
import json
## global constants
url = "https://alpha-vantage.p.rapidapi.com/query"


## functions



querystring = {"outputsize":"compact","datatype":"json","function":"TIME_SERIES_DAILY","symbol":"MSFT"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "e42b45b6b2mshe2ffddfc6ce2893p18c10cjsn50c116e38e6a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(type(response))
print(dir(response))
stock_raw = response.text
stock_json = json.loads(stock_raw)
stock_df = pd.json_normalize(stock_json)
