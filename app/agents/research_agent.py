from app.tools.job_tools import search_jobs_tool


def research_agent(role: str, location: str):
    jobs = search_jobs_tool(role=role, location=location)

    return {
        "agent": "research_agent",
        "jobs": jobs
    }