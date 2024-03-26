from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import os
from openai import OpenAI

google_api_key = ""
google_cse_id = ""
openai_key = ""

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

input_text = input("Search: ")
summarize_text = str(tool.run(input_text))

response = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": summarize_text + ", summarize this text in a cohesive way"},
  ]
)

if ".com" not in str(response.choices[0].message.content):
    print(response.choices[0].message.content)
else:
    word_response = response.choices[0].message.content.split()
    loader = AsyncChromiumLoader(["https://www." + str(word_response[-1]) + ".com"])
    html = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])
    
    response_website = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": docs_transformed + "summarize this text in a cohesive way"}
        ]
    )
    
    print(response_website.choices[0].message.content)