# MCP Server implementation using streamable http to handle loan-related queries
''' 
List of functionalities:
1. Fetch interest rates based on loan type
'''

from mcp.server.fastmcp import FastMCP
import loan_db_ops as ops
from .schemas import InterestRates

# Instantiate the FastMCP server
mcp = FastMCP("XYZ Loan Services")

@mcp.tool()
def fetch_interest_rates(loan_type: str) -> list[InterestRates]:
    """Return interest rates when queried by loan type"""
    result = ops.get_interest_rates_by_loan_type(loan_type)
    if result is None:
        return "Interest rates not found"
    else:
        return result