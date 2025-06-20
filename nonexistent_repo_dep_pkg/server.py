"""nonexistent_repo_dep_pkg: Dummy Hatch package for testing nonexistent repo dependencies."""
from mcp_utils.hatch_mcp import HatchMCP

# Initialize MCP server with metadata
hatch_mcp = HatchMCP("nonexistent_repo_dep_pkg",
                origin_citation="Nonexistent repo dependency package for testing",
                mcp_citation="Nonexistent repo dependency package MCP implementation")

@hatch_mcp.server.tool()
def nonexistent_repo_function(param: str) -> str:
    """Function from nonexistent repo dependency package.

    Args:
        param (str): Input parameter.
    
    Returns:
        str: Processed result.
    """
    hatch_mcp.logger.info(f"Nonexistent repo function called with param: {param}")
    return f"Nonexistent repo dependency package processed: {param}"

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting MCP server")
    hatch_mcp.server.run()
