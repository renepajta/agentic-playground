# AI Agent playground

This project demonstrates agentic concepts, orchestration patterns and functional scenarios using GitHub models and various open souce frameworks like Llama Index, Semantic Kernel, LangChain and AutoGen.

## What is an Agent?

> ***agent***: 	perceives its environment, makes decisions, takes actions autonomously in order to achieve goals, and may improve its performance with learning or acquiring knowledge 

![What is an agent](/img/agents.png)

A simple LLM-based chatbot primarily focuses on generating responses based on predefined patterns and language models, often requiring user input to continue the conversation. In contrast, autonomous agents are designed to perform tasks independently, making decisions and taking actions without constant user input, often leveraging advanced AI techniques to achieve their goals. 

![Spectrum of agentic behaviour](/img/spectrum.png)

## Preparation

This project does not require azure resources and support GitHub AI models.

1. Create a personal access token

To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings or set up an Azure production key. [GitHub Free AI Token](https://github.com/settings/tokens)

You can now access AI inference with your GitHub PAT. [Learn more about limits based on your plan](https://github.com/marketplace/models/azure-openai/gpt-4o-mini/playground#:~:text=Learn%20more%20about%20limits%20based%20on%20your%20plan.). You do not need to give any permissions to the token. 

To use the code snippets below, create an environment variable to set your token as the key for the client code.

If you're using bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```

or rename the file `.env_template` to `.env` and put the value inside the `.env` file. Each python script will load the value from that value automatically.

2. Install dependencies (should be already done when using a GitHub codespace)

```
python -m pip -r requirements.txt
```

## Workshop contents

The scope of this workshop covers the following scenarios and technology stacks:

| Name | Description | Technology  |
| :-- | :--| :-- |
| [Hello World](./src/01-basic/README.md) | Hello World model | OpenAI |
| [Multimodal models](./src/02-multimodal-models/README.md) | Multimodel Prompting | OpenAI, Vision model, Realtime model |
| [Knowledge Graphs](./src/03-complex-data/README.md) | Knowledge graph generation | OpenAI, Structured output |
| [Onthologies](./src/03-complex-data/README.md) | Onthologies | OpenAI, OWL |
| [Custom DSL](./src/04-complex-problems/README.md) | Domain specific languages | OpenAI, Tools |
| [Single Agent](./src/05-search-agent/README.md) | ReAct Agent | OpenAI,LangChain, Llama Index, Tools |
| [Human in the loop](./src/06-human-in-the-loop/README.md) | Human in the loop agents | OpenAI, LangChain, LangGraph, Semantic Kernel Tools |
| [Multi agent collaboration](./src/07-multi-agent-collaboration/README.mdy) | Multi turn agent collaboration| OpenAI, Semantic Kernel, LangGraph |
| [Society of agents](./src/08-society-of-agents/README.md) | Dynamic planning | OpenAI, AutoGen, MagenticOne |
| [Event Driven Agents](./src/09-eventdriven-agents/README.md) | Dynamic planning | OpenAI, Semantic Kernel |
