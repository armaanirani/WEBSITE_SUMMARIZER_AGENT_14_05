import os
import asyncio
from dotenv import load_dotenv

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

# Load environment variables from .env file
load_dotenv()

# Defining the MCP server
mcp_fetch_server = MCPServerStdio(
    command='python',
    args=['-m', 'mcp_server_fetch']
)