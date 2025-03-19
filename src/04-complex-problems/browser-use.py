import os
from langchain_openai import ChatOpenAI

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

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=model4o,
    )
    await agent.run()

asyncio.run(main())