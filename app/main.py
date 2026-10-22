from fastapi import FastAPI

from app.models.job import JobSearchRequest
from app.agents.research_agent import research_agent

app = FastAPI(title="ApplyAI")


@app.get("/")
def root():
    return {"message": "ApplyAI is running"}


@app.post("/jobs/search")
def search_jobs(request: JobSearchRequest):
    result = research_agent(
        role=request.role,
        location=request.location
    )

    return result