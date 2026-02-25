from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    query = Column(String)
    result = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)