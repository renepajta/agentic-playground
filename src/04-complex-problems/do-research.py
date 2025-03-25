"""
Goal: Searches for job listings, evaluates relevance based on a CV, and applies 

@dev You need to add OPENAI_API_KEY to your environment variables.
Also you have to install PyPDF2 to read pdf files: pip install PyPDF2
"""

import csv
import os
import sys
from pathlib import Path
import logging
from typing import List, Optional
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use import ActionResult, Agent, Controller
from browser_use.browser.context import BrowserContext
from browser_use.browser.browser import Browser, BrowserConfig

# Validate required environment variables
load_dotenv()
# token = os.environ["GITHUB_TOKEN"]
# endpoint = "https://models.inference.ai.azure.com"
# model_name = "gpt-4o"

# model4o = ChatOpenAI(
#     model=model_name,
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     api_key=token,
#     base_url=endpoint
# )

model4o = AzureChatOpenAI(
    azure_deployment="gpt-4o",  # or your deployment
    api_version="2024-07-18",  # or your api version
    temperature=0,
    max_tokens=None,
    timeout=None,
    # other params...
)

logger = logging.getLogger(__name__)
# full screen mode
controller = Controller()

# NOTE: This is the path to your taxonomy file
TAX = Path.cwd() / 'battery_chem.xml'

if not TAX.exists():
	raise FileNotFoundError(f'You need to set the path to your cv file in the CV variable. CV file not found at {TAX}')


class Insights(BaseModel):
	title: str
	link: str
	description: str
	taxonomy_reference: str
	reasoning: str


@controller.action('Save insights to file - with a score how well it fits to my objective', param_model=Insights)
def save_insights(insights: list[Insights]):
	with open('insights.json', 'a', newline='') as f:
		writer = csv.writer(f)
		for job in insights:
			writer.writerow([job.title, job.link, job.description, job.taxonomy_reference, job.reasoning])

	return 'Saved insights to file'


@controller.action('Read insights from file')
def read_insights():
	with open('insights.json', 'r') as f:
		return f.read()


@controller.action('Read the taxonomy file')
def read_taxonomy():
	text = ''
	with open(TAX, 'r') as f:
		text = f.read()
		logger.info(f'Read taxonomy file with {len(text)} characters')	
	return ActionResult(extracted_content=text, include_in_memory=True)

browser = Browser(
	config=BrowserConfig(
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
		disable_security=True,
	)
)


async def main():
	ground_task = (
		'You are a chemist and need to prepare a briefing for chemist working group. '
		'1. Read the taxonomy file and extract the most important information from it using read_taxonomy. '
		'2. Take a look at the list of websites listed below. Extract the most relevant facts and structure it according to the taxonomy.'
		'3. Provide reasoning to every insight you generate and store it in the reasoning field.'
		'4. Save the insights to a file called insights.json using save_insights .'
		'5. The insights should be in the following format:'
		'{"title": "title", "link": "link", "description": "description", "taxonomy_reference": "taxonomy_reference", "reasoning": "reasoning"}'
		'take a look at this list of articles:'
	)
	tasks = [
		ground_task + '\n' + 'https://pubs.acs.org/doi/10.1021/acs.jchemed.8b00479',
	]

	agents = []
	for task in tasks:
		agent = Agent(task=task, llm=model4o, controller=controller, browser=browser)
		agents.append(agent)

	await asyncio.gather(*[agent.run() for agent in agents])


if __name__ == "__main__":
	asyncio.run(main())