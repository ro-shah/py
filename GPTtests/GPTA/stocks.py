import requests

api_key = "SLO488PC9T4HDR2T"
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}"

response = requests.request("GET", url)

print(response.text)