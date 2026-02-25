from celery_worker import celery_app
from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

from database import SessionLocal
from models import AnalysisResult

@celery_app.task
def analyze_document_task(file_path: str, query: str, filename: str):
    # Run CrewAI analysis
    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    # Save result to database
    db = SessionLocal()
    db_result = AnalysisResult(
        filename=filename,
        query=query,
        result=str(result)
    )
    db.add(db_result)
    db.commit()
    db.close()

    return {"status": "completed", "filename": filename}