from mcp.server.fastmcp import FastMCP
from tools.search import search_jobs as _search_jobs
from tools.details import get_job_details as _get_job_details
# we import with _ prefix to avoid name collision with the decorated functions below

mcp = FastMCP("berlin-jobs-mcp-server")  # creates the MCP server instance
                                          # this name appears in Claude Desktop

@mcp.tool()
def search_jobs(query: str) -> str:
    """
    Search Berlin tech jobs by keyword.
    Use when the user wants to find, search, or browse job listings.
    Matches against job role and company name.
    """
    return _search_jobs(query)  # delegates to tools/search.py

@mcp.tool()
def get_job_details(job_id: int) -> str:
    """
    Get full details for a specific job by its ID.
    Use when the user asks for more info about a specific job listing.
    """
    return _get_job_details(job_id)  # delegates to tools/details.py

if __name__ == "__main__":
    mcp.run()  # starts the server and listens for MCP client connections