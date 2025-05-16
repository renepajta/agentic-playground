# Model context protocol

This playground is about leveraging the Model Context protocol for discovering tools and executing them using local or remote MCP servers

## Local MCP Server (Stdio)

```mermaid
graph LR
    User(User) <--> App (LangGraph)
    App (LangGraph) <--> MCP Client (Tools)
    MCP Client (Tools) <--> MCP Server
    MCP Server <--> Local code

    style User fill:#f9f9f9
    style App (LangGraph) fill:#0072C6,color:white
    style MCP Client (Tools) fill:#5cb85c,color:white
    style MCP Server fill:#d9534f,color:white
```

Start the local app, which will then launch the local MCP server
```
python client-mcp-stdio.py
```

This patterns is relevant if you want to leverage local user authentication or context for the execution of tools.

## Remote MCP Server (SSE)

```mermaid
graph LR
    User(User) <--> App (LangGraph)
    App (LangGraph) <--> MCP Client (Tools)
    MCP Client (Tools) <--> MCP Server (SSE)
    MCP Server (SSE) <--> Remote code

    style User fill:#f9f9f9
    style App (LangGraph) fill:#0072C6,color:white
    style MCP Client (Tools) fill:#5cb85c,color:white
    style MCP Server (SSE) fill:#d9534f,color:white
```


Start the remote MCP Server
```
python server-mcp-sse.py
```

Start the local app
```
python client-mcp-sse.py
```

This patterns is relevant if you want to leverage remote MCP servers that are running on the network.