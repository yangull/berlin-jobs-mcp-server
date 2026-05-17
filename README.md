# berlin-jobs-mcp-server

An MCP (Model Context Protocol) server that exposes a PostgreSQL jobs database to Claude.

## What it does

Connects Claude to a live PostgreSQL database of Berlin tech job listings. Claude can search jobs by keyword and fetch details by ID through natural language — no manual data copying required.

## Tools

- `search_jobs(query)` — searches job listings by role or company name
- `get_job_details(job_id)` — returns full details for a specific job by ID

## Stack

- Python, FastMCP, SQLAlchemy, PostgreSQL, psycopg2

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add a `.env` file: