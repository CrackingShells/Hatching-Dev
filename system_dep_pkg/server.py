from mcp_utils.hatch_mcp import HatchMCP

hatch_mcp = HatchMCP("system_dep_pkg",
                origin_citation="System dependency package for testing",
                mcp_citation="System dependency package MCP implementation")

@hatch_mcp.server.tool()
def system_check() -> str:
    """Dummy tool that requires a system package (e.g., curl)."""
    return "System dependency tool executed. (Pretend this needs 'curl')"

if __name__ == "__main__":
    hatch_mcp.server.run()
