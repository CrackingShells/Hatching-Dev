"""repo_prefix_dep_pkg: Dummy Hatch package for testing repo prefix dependencies."""
from mcp_utils.hatch_mcp import HatchMCP

# Initialize MCP server with metadata
hatch_mcp = HatchMCP("repo_prefix_dep_pkg",
                origin_citation="Repo prefix dependency package for testing",
                mcp_citation="Repo prefix dependency package MCP implementation")

@hatch_mcp.server.tool()
def repo_prefix_function(param: str) -> str:
    """Function from repo prefix dependency package.

    Args:
        param (str): Input parameter.
    
    Returns:
        str: Processed result.
    """
    hatch_mcp.logger.info(f"Repo prefix function called with param: {param}")
    return f"Repo prefix dependency package processed: {param}"

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting MCP server")
    hatch_mcp.server.run()
