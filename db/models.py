from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from db.connection import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=True)
    tech_stack = Column(String, nullable=True)
    seniority = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
