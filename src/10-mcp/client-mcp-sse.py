import os
import asyncio
import dotenv

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient

dotenv.load_dotenv()

llm: ChatOpenAI = None

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

llm = ChatOpenAI(
    model=model_name,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=token,
    base_url=endpoint
)

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent


from pprint import pprint

async def main():

    client = MultiServerMCPClient(
        {
            "datetimespace": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    )
    tools = await client.get_tools()

    print("tools: ", tools)

    # Create and run the agent
    agent = create_react_agent(llm, tools)
    agent_response = await agent.ainvoke({"messages": "what is the current time"})
    # pprint(agent_response)

    for message in agent_response["messages"]:
        pprint(message.content)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Cleaning up...")
    except Exception as e:
        print(f"An error occurred: {e}")