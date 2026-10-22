from app.services.job_search import find_jobs


def search_jobs_tool(role: str, location: str):
    return find_jobs(role=role, location=location)