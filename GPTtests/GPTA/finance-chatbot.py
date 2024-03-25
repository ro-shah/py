import os
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

openai_key = ""
os.environ["OPENAI_API_KEY"] = openai_key

llm = ChatOpenAI(temperature=0.0)
tools = [YahooFinanceNewsTool()]
agent_chain = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True,
)

print(agent_chain.run(
    "how did he microsoft stock do today",
))