from mcp.server.fastmcp import FastMCP
from app.mcp.weather_tool import get_weather
import os

mcp = FastMCP("local-tools")


@mcp.tool()
def weather(city: str) -> str:
    """Get weather of a city"""
    return get_weather(city)


@mcp.tool()
def list_files() -> str:
    """List project files"""
    return str(os.listdir("."))


if __name__ == "__main__":
    mcp.run()