import os
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from browser_use import Agent
import asyncio

load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

model4o = ChatOpenAI(
    model=model_name,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=token,
    base_url=endpoint
)

# model4o = AzureChatOpenAI(
#     azure_deployment="gpt-4o",  # or your deployment
#     api_version="2024-08-06",  # or your api version
#     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     # other params...
# )

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=model4o,
    )
    await agent.run()

asyncio.run(main())