from typing import Any
from fastmcp import FastMCP
from mcp_gotify.config import GOTIFY_URL, GOTIFY_TOKEN
from httpx import AsyncClient

mcp: FastMCP[Any] = FastMCP(
    name="mcp-gotify",
)


@mcp.tool(
    name="send_notification"
)
async def send_notification(title: str, message: str, priority: int = 5, content_type: str = "text/markdown") -> str:
    """Send a notification to Gotify"""

    if not GOTIFY_TOKEN:
        return "GOTIFY_TOKEN not set"

    route = f"{GOTIFY_URL}/message?token={GOTIFY_TOKEN}"

    data: dict[str, Any] = {
        "title": title,
        "message": message,
        "priority": priority,
        "extras": {
            "client::display": {
                "contentType": content_type
            }
        }
    }

    async with AsyncClient() as client:
        resp = await client.post(route, json=data)

    try:
        resp.raise_for_status()
    except Exception as e:
        return f"Error: {e}"

    return "Notification sent: " + resp.text
