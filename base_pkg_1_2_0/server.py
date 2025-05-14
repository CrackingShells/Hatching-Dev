import requests
from mcp_utils.hatch_mcp import HatchMCP

# Initialize MCP server with metadata
hatch_mcp = HatchMCP("base_pkg_1",
                origin_citation="Base package 1 for testing with enhanced functionality",
                mcp_citation="Base package 1 MCP implementation v1.2.0")

@hatch_mcp.server.tool()
def base_function(param: str) -> str:
    """Basic function for testing.
    
    Args:
        param: Input parameter
        
    Returns:
        str: Processed result
    """
    hatch_mcp.logger.info(f"Base function called with param: {param}")
    return f"Base package 1 (v1.2.0) processed: {param}"

@hatch_mcp.server.tool()
def enhanced_function(param: str, option: str = "default") -> dict:
    """Enhanced function added in version 1.2.0.

    Args:
        param: Input parameter
        option: Optional processing option
        
    Returns:
        dict: Processed result with metadata
    """
    hatch_mcp.logger.info(f"Enhanced function called with param: {param}, option: {option}")
    
    # Using the requests library (added as dependency in v1.2.0)
    try:
        # This is just for demonstration - not making an actual HTTP request
        # in a test package. In a real package, this could be a real API call.
        mock_response = {
            "status": "success",
            "input": param,
            "option": option,
            "processed_by": "base_pkg_1 v1.2.0",
            "timestamp": requests.utils.formatdate()
        }
        return mock_response
    except Exception as e:
        hatch_mcp.logger.error(f"Error in enhanced_function: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting MCP server for base_pkg_1 v1.2.0")
    hatch_mcp.server.run()