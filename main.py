import os
import asyncio
from dotenv import load_dotenv

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Defining the MCP server
mcp_fetch_server = MCPServerStdio(
    command='python',
    args=['-m', 'mcp_server_fetch']
)

# Defining the agent
agent = Agent(
    model="groq:llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    mcp_server=[mcp_fetch_server],
)

# Defining the main function
async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("Extract the content and summarize it: https://www.turing.com/resources/finetuning-large-language-models")
        output = result.output
        return output

# Running the main function
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)
