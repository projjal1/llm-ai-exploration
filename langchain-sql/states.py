# Maintains state of the SQL database connection and operations
from typing_extensions import TypedDict, Annotated

# State management for SQL operations
class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

class QueryOutput(TypedDict):
    """Generated SQL query."""

    query: Annotated[str, ..., "Syntactically valid SQL query."]