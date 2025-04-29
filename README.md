# MCP-gotify

MCP server for sending gotify push notifications.

## Installation

### stdio

claude json:

```json5
{
    "mcpServers": {
        "mcp-gotify": {
            "command": "uvx",
            "args": ["mcp-gotify"],
            "env": {
                "GOTIFY_SERVER": "http://localhost:2081", # Change this to your gotify server
                "GOTIFY_TOKEN": "YOUR TOKEN" # Get this from gotify
            }
        }
    }
}
```

### sse

```bash
git clone https://github.com/SecretiveShell/mcp-gotify
cd mcp-gotify
uv run mcp-gotify-sse
```

## License

MIT