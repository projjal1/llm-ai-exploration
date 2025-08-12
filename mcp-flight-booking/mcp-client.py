# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters, stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import asyncio

# Use Ollama's Llama 3 (8B)
model = ChatOllama(
    model="mistral:7b",   # Model name for Ollama
    temperature=0,       # Optional: set low temperature for deterministic output
)

abs_path = "/Users/projjalgop/Documents/Code-Artifacts/ai-codes/mcp-flight-booking/"

server_params = StdioServerParameters(
    command="python3",
    args=[abs_path + "mcp-server.py"],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            return agent_response['messages'][-1].content

# Run the async function
if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)