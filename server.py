from hashlib import sha256

from mcp.server.fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "24f3001946@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Exam MCP Server")


@mcp.tool()
async def solve_challenge() -> str:
    headers = get_http_headers()

    challenge = headers.get("x-exam-challenge", "")

    return sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]


app = mcp.streamable_http_app()