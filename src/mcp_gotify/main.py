from fastmcp import FastMCP
from mcp_gotify.config import GOTIFY_URL, GOTIFY_TOKEN
from httpx import AsyncClient

mcp: FastMCP = FastMCP(
    name="mcp-gotify",
)

@mcp.tool(
    name="send_notification"
)
async def send_notification(title:str, message: str) -> str:
    """Send a notification to Gotify"""

    if not GOTIFY_TOKEN:
        return "GOTIFY_TOKEN not set"

    route = f"{GOTIFY_URL}/message?token={GOTIFY_TOKEN}"

    data = {
        "title": title,
        "message": message,
        "priority": 5,
    }

    async with AsyncClient() as client:
        resp = await client.post(route, json=data)

    try:
        resp.raise_for_status()
    except Exception as e:
        return f"Error: {e}"

    return "Notification sent: " + resp.text