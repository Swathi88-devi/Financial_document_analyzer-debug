from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "financial_tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)