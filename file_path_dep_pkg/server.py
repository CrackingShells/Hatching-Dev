"""file_path_dep_pkg: Dummy Hatch package for testing file path dependencies."""
from mcp_utils.hatch_mcp import HatchMCP

# Initialize MCP server with metadata
hatch_mcp = HatchMCP("file_path_dep_pkg",
                origin_citation="File path dependency package for testing",
                mcp_citation="File path dependency package MCP implementation")

@hatch_mcp.server.tool()
def file_path_function(param: str) -> str:
    """Function from file path dependency package.

    Args:
        param (str): Input parameter.
    
    Returns:
        str: Processed result.
    """
    hatch_mcp.logger.info(f"File path function called with param: {param}")
    return f"File path dependency package processed: {param}"

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting MCP server")
    hatch_mcp.server.run()
