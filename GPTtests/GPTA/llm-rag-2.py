import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import pinecone
from datasets import load_dataset
import time
from langchain.embeddings.openai import OpenAIEmbeddings
from tqdm.auto import tqdm  # for progress bar
from langchain.vectorstores import Pinecone

openai_key = "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"
pinecone_key = "c0ded864-610a-4e06-9ec4-c19622dad458"

embed_model = OpenAIEmbeddings(
    openai_api_key = openai_key, 
    model = "text-embedding-ada-002"
    )

dataset = load_dataset(
    "jamescalam/llama-2-arxiv-papers-chunked",
    split = "train"
)

pinecone.init(
    api_key = pinecone_key,
    environment = "gcp-starter"
)

chat = ChatOpenAI(
    openai_api_key = openai_key,
    model = 'gpt-3.5-turbo'
)

messages = [
    SystemMessage(content = "You are a helpful assistant."),
    HumanMessage(content = "Hi AI, how are you today?"),
    AIMessage(content = "I'm great, thank you, How can I help you?")
    ]

res = chat(messages)
print(res.content)

index_name = "llama-2-rag"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        index_name,
        dimension = 1536,
        metric = "cosine"
    )
    while not pinecone.describe_index(index_name).status["ready"]:
        time.sleep(1)

    print("finished creating index")

index = pinecone.Index(index_name)

texts = [
    "first chunk of text",
    "second chunk of text"
]

res = embed_model.embed_documents(texts)

data = dataset.to_pandas()  # this makes it easier to iterate over the dataset

batch_size = 100

for i in tqdm(range(0, len(data), batch_size)):
    i_end = min(len(data), i+batch_size)
    # get batch of data
    batch = data.iloc[i:i_end]
    # generate unique ids for each chunk
    ids = [f"{x['doi']}-{x['chunk-id']}" for i, x in batch.iterrows()]
    # get text to embed
    texts = [x['chunk'] for _, x in batch.iterrows()]
    # embed text
    embeds = embed_model.embed_documents(texts)
    # get metadata to store in Pinecone
    metadata = [
        {'text': x['chunk'],
         'source': x['source'],
         'title': x['title']} for i, x in batch.iterrows()
    ]
    # add to Pinecone
    index.upsert(vectors=zip(ids, embeds, metadata))

text_field = "text"

vectorstore = Pinecone(
    index, embed_model.embed_query, text_field
    )

query = input("Ask a question about llama 2: ")

def augmentPrompt(query: str):
    results = vectorstore.similarity_search(query, k = 3)
    source_knowledge = "\n".join([x.page_content for x in results])
    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augmented_prompt

# create a new user prompt
prompt = HumanMessage(
    content = augmentPrompt(query)
)
# add to messages
messages.append(prompt)

res = chat(messages)

print(res.content)