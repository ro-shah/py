import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from datasets import load_dataset

key = "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"
os.environ[key] = key

chat = ChatOpenAI(
    openai_api_key = key,
    model = 'gpt-3.5-turbo'
)

input_text = input("input: ")
messages = [
    SystemMessage(content = "You are a helpful assistant."),
    HumanMessage(content = "Hi AI, how are you today?"),
    AIMessage(content = "I'm great, thank you, How can I help you?"),
    HumanMessage(content = input_text)
    ]

res = chat(messages)
print(res.content)

messages.append(res)

llama2_info = "Llama 2 is a family of generative text models that are optimized for assistant-like chat use cases or can be adapted for a variety of natural language generation tasks. Code Llama models are fine-tuned for programming tasks."

source_knwowlege = "\n".join(llama2_info)

query = "Can you tell me abt llama2?"
augemented_prompt = f"""Using the conext below, answer the query

Contexts:
{source_knwowlege}

Query: {query}"""

prompt2 = HumanMessage(content = augemented_prompt)
messages.append(prompt2)
res = chat(messages)
print(res.content)