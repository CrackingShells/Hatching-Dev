from mcp_utils.hatch_mcp import HatchMCP

# Initialize MCP server with metadata
hatch_mcp = HatchMCP("base_pkg_1",
                origin_citation="Base package 1 for testing with enhanced functionality",
                mcp_citation="Base package 1 MCP implementation v1.3.0")

@hatch_mcp.server.tool()
def base_function(param: str) -> str:
    """Basic function for testing.
    
    Args:
        param: Input parameter
        
    Returns:
        str: Processed result
    """
    hatch_mcp.logger.info(f"Base function called with param: {param}")
    return f"Base package 1 (v1.3.0) processed: {param}"

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting MCP server for base_pkg_1 v1.3.0")
    hatch_mcp.server.run()