from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

class Submission(BaseModel):
    submission_id: str
    number1: float
    number2: float

jobs = {}

@app.post("/submit/")
def submit_job(submission: Submission):
    job_id = str(uuid4())
    submission_id = submission.submission_id
    number1 = submission.number1
    number2 = submission.number2

    logging.info(f"Job {job_id} started with submission ID: {submission_id}")

    # Performing operations
    logging.info(f"Job {job_id} - Step 1/3: Adding {number1} and {number2}")
    addition_result = number1 + number2

    logging.info(f"Job {job_id} - Step 2/3: Subtracting {number2} from {number1}")
    subtraction_result = number1 - number2

    logging.info(f"Job {job_id} - Step 3/3: Multiplying {number1} and {number2}")
    multiplication_result = number1 * number2

    jobs[job_id] = {
        "submission_id": submission_id,
        "addition_result": addition_result,
        "subtraction_result": subtraction_result,
        "multiplication_result": multiplication_result,
        "status": "Completed"
    }

    logging.info(f"Job {job_id} completed")

    return {"job_id": job_id, "status": "Job completed successfully"}

@app.get("/status/{job_id}")
def get_job_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

# To run the app, save this file and run `uvicorn filename:app --reload` in your terminal.
