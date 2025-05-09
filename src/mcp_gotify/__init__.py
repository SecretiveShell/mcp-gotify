import asyncio

from mcp_gotify.main import mcp

def main() -> None:
    asyncio.run(mcp.run_async())

def main_sse() -> None:
    asyncio.run(mcp.run_sse_async())

def main_streaming_http() -> None:
    asyncio.run(mcp.run_streamable_http_async())

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "sse":
        main_sse()
    elif len(sys.argv) > 1 and sys.argv[1] == "streaming_http":
        main_streaming_http()
    else:
        main()