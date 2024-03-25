import requests

api_key = ""
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}"

response = requests.request("GET", url)

print(response.text)