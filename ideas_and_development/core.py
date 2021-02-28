import requests
import json
import yaml_handler as y

av_key = 'DREASXN2231RALOE'
#api_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=DREASXN2231RALOE"
#api_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo"
api_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo"
response = requests.get(api_url_base)

print ('response.status_code is {0}'.format(response.status_code))
#dct =json.loads(response.decode())
response = response.json()

y.yaml_dump('stocks.yaml', response)
