from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("Serving request for {a} * {b}")
    return a * b

if __name__ == "__main__":
    # To run as STDIO PIPE
    mcp.run(transport="stdio")