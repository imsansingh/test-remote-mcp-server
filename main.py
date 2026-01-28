from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number. 

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# Tool: Generates a random number
mcp.tool()
def random_number(min_value: int = 1, max_value: int = 100) -> int:
    """Generate a random number within a specified range.

    Args:
        min_value (int): The minimum value of the range(default is 1).
        max_value (int): The maximum value of the range(default is 100).

    Returns:
        int: A random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)

# Resource : Server Infprmation
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A simple server that provides basic calculator functions and random number generation.",
        "tools": ["add", "random_number"],
        "authors": "Your Name"
    }
    return json.dumps(info, indent=2)

# Start the FastMCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

