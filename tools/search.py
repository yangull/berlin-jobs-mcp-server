from sqlalchemy import or_
from db.connection import get_db_session
from db.models import Job

def search_jobs(query: str) -> str:
    """
    Search Berlin tech jobs by keyword.
    Use when the user wants to find, search, or browse job listings.
    Matches against job title, company name, and tech stack.
    """
    session = get_db_session()
    query = query.strip()
    try:
        results = session.query(Job).filter(
            or_(
                Job.title.ilike(f"%{query}%"),
                Job.company.ilike(f"%{query}%"),
                Job.tech_stack.ilike(f"%{query}%")
            )
        ).all()

        if not results:
            return f"No jobs found matching '{query}'."

        lines = [f"Found {len(results)} job(s) matching '{query}':\n"]
        for job in results:
            lines.append(
                f"- [{job.id}] {job.title} at {job.company} | {job.seniority or 'Unknown'} | {job.tech_stack or 'Not specified'}"
            )
        return "\n".join(lines)

    finally:
        # always runs even if the query crashes — prevents connection leaks
        session.close()
