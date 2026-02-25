import os
import uuid
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from tasks_queue import analyze_document_task

# Load environment variables
load_dotenv()

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

app = FastAPI(
    title="Financial Document Analyzer API",
    description="Analyze financial documents using CrewAI with background processing",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Financial Document Analyzer API is running"
    }

@app.post("/analyze")
async def analyze_financial_document_api(
    file: UploadFile = File("data/sample.pdf"),
    query: str = Form(default="Analyze this financial document")
):
    try:
        # Generate unique file name
        file_id = str(uuid.uuid4())
        file_path = f"data/{file_id}_{file.filename}"

        # Save uploaded file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Send task to Celery queue
        task = analyze_document_task.delay(
            file_path=file_path,
            query=query,
            filename=file.filename
        )

        return JSONResponse(
            status_code=202,
            content={
                "status": "queued",
                "task_id": task.id,
                "filename": file.filename,
                "message": "Document submitted for background processing"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )