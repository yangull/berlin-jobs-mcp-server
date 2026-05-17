from sqlalchemy import or_
from db.connection import get_db_session
from db.models import Job

def search_jobs(query: str) -> str:
    """
    Search Berlin tech jobs by keyword.
    Use when the user wants to find, search, or browse job listings.
    Matches against job role and company name.
    """
    session = get_db_session()
    query = query.strip()  # removes newlines and trailing spaces from inspector input
    try:
        results = session.query(Job).filter(
            or_(
                Job.role.ilike(f"%{query}%"),    # %query% means "contains" — not exact match
                Job.company.ilike(f"%{query}%")  # or_ means either column can match
            )
        ).all()

        if not results:
            return f"No jobs found matching '{query}'."

        lines = [f"Found {len(results)} job(s) matching '{query}':\n"]
        for job in results:
            salary_str = f"€{job.salary:,}" if job.salary else "Not specified"
            lines.append(
                f"- [{job.id}] {job.role} at {job.company} | {job.location} | {salary_str}"
            )
        return "\n".join(lines)

    finally:
        session.close()  # always runs even if the query crashes — prevents connection leaks