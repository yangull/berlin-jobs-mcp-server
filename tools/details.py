from db.connection import get_db_session
from db.models import Job

def get_job_details(job_id: int) -> str:
    """
    Get full details for a specific job by its ID.
    Use when the user asks for more info about a specific job listing.
    """
    session = get_db_session()
    try:
        job = session.query(Job).filter(Job.id == job_id).first()  # .first() returns None if not found

        if not job:
            return f"No job found with ID {job_id}."

        salary_str = f"€{job.salary:,}" if job.salary else "Not specified"
        return (
            f"Job ID: {job.id}\n"
            f"Role: {job.role}\n"
            f"Company: {job.company}\n"
            f"Location: {job.location}\n"
            f"Salary: {salary_str}"
        )
    finally:
        session.close()