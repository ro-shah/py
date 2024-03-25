from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
import requests
from bs4 import BeautifulSoup
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import os
from openai import OpenAI

google_api_key = "AIzaSyCxady4-MPUmP2mGS8OTtlQ0VzyxVR-Qcw"
google_cse_id = "662fb373bc5b6471c"
openai_key = "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"

os.environ["GOOGLE_CSE_ID"] = google_cse_id
os.environ["GOOGLE_API_KEY"] = google_api_key

search = GoogleSearchAPIWrapper()

tool = Tool(
    name = "Google Search",
    description = "Search Google for recent results.",
    func = search.run,
)

client = OpenAI(
    api_key = openai_key
)

tag = input("Stock: ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
url = "https://finance.yahoo.com/quote/" + tag

r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, "html.parser")

price_tag = soup.find('fin-streamer', {"class": "Fw(b) Fz(36px) Mb(-4px) D(ib)"})
change_tag = soup.find('fin-streamer', {"class": "Fw(500) Pstart(8px) Fz(24px)"})
change_in_percent_tag = soup.find('fin-streamer', {"class": "Fw(500) Pstart(8px) Fz(24px)"})

price = float(price_tag["value"])
change = float(change_tag["value"])
change_in_percent = float(change_in_percent_tag["value"]) * 100

summarize_text = str(tool.run("recent news on " + tag))
response = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": summarize_text + "summarize text"},
  ]
)

print("The value of " + tag + " is " + str(round(price, ndigits = 1)) +     ", with a change in " + str(round(change, ndigits = 2)) + " from yesterday.")
# print(summarize_text)
print("\n\n" + "According to Google, " + response.choices[0].message.content)