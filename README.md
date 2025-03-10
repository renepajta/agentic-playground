# AI Agent playground

This project does not require azure resources and support GitHub AI models.

## Preparation
1. Create a personal access token

To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings or set up an Azure production key. [GitHub Free AI Token](https://github.com/settings/tokens)

You can now access AI inference with your GitHub PAT. [Learn more about limits based on your plan](https://github.com/marketplace/models/azure-openai/gpt-4o-mini/playground#:~:text=Learn%20more%20about%20limits%20based%20on%20your%20plan.). You do not need to give any permissions to the token. 

To use the code snippets below, create an environment variable to set your token as the key for the client code.

If you're using bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```

2. Install dependencies

```
python -m pip -r requirements.txt
```

## Workshop contents

The scope of this workshop covers the following scenarios and technology stacks:

| Name | Description | Technology  |
| :-- | :--| :-- |
| [Hello World](./src/01-basic/hello-world.py) | Hello World model | OpenAI |
| [Visual comparision](./src/02-vision-models/compare-images.py) | Multimodel Prompting | OpenAI, Vision model |
| [Knowledge Graphs](./src/03-complex-data/knowledge-graphs.py) | Knowledge graph generation | OpenAI, Structured output |
| [Onthologies](./src/03-complex-data/create-onthologies.py) | Onthologies | OpenAI, OWL |
| [Existing DSL](./src/04-complex-problems/translate-gerkhin.py) | Gherkin | OpenAI, Tools |
| [Custom DSL](./src/04-complex-problems/trucking-plan.py) | Domain specific languages | OpenAI, Tools |
| [Single Agent](./src/05-search-agent/react-agent-lc.py) | ReAct Agent | OpenAI,LangChain, Llama Index, Tools |
| [Human in the loop](./src/06-human-in-the-loop/app.py) | Human in the loop agents | OpenAI, LangChain, LangGraph, Tools |
| [Society of agents](./src/07-society-of-agents/simple-group.py) | Magentic one | OpenAI, AutoGen |
