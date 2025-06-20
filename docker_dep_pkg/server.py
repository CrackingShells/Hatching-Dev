from mcp_utils.hatch_mcp import HatchMCP

hatch_mcp = HatchMCP("docker_dep_pkg",
                origin_citation="Docker dependency package for testing",
                mcp_citation="Docker dependency package MCP implementation")

@hatch_mcp.server.tool()
def docker_check() -> str:
    """Dummy tool that requires a docker image (e.g., nginx)."""
    return "Docker dependency tool executed. (Pretend this needs 'nginx' docker image)"

if __name__ == "__main__":
    hatch_mcp.server.run()
