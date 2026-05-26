from db.connection import get_db_session
from db.models import Job

def get_job_details(job_id: int) -> str:
    """
    Get full details for a specific job by its ID.
    Use when the user asks for more info about a specific job listing.
    """
    session = get_db_session()
    try:
        job = session.query(Job).filter(Job.id == job_id).first()

        if not job:
            return f"No job found with ID {job_id}."

        return (
            f"Job ID: {job.id}\n"
            f"Title: {job.title}\n"
            f"Company: {job.company}\n"
            f"Seniority: {job.seniority or 'Unknown'}\n"
            f"Tech Stack: {job.tech_stack or 'Not specified'}\n"
            f"URL: {job.url or 'Not available'}\n"
            f"Description:\n{job.description or 'Not available'}"
        )
    finally:
        session.close()
