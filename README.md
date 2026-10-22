# ApplyAI

ApplyAI is an agentic AI platform designed to assist with job discovery, job matching, resume tailoring, and application preparation.

The goal of this project is to build a production-oriented multi-agent system while learning and applying:

- Python
- Agentic AI
- Multi-agent orchestration
- MCP tools and servers
- FastAPI
- PostgreSQL
- RAG and embeddings
- Async programming
- Testing
- Docker
- Git and GitHub
- CI/CD

## Planned Workflow

```text
User
  |
  v
Supervisor Agent
  |
  v
Task Planner
  |
  +--> Job Research Agent
  |
  +--> Job Matching Service
  |
  +--> Resume Agent
  |
  v
Application Agent
  |
  v
Human Approval
  |
  v
Application Preparation / Submission
```

## Project Status

Currently under development.

### Phase 1
- Project setup
- Git and GitHub setup
- Python environment
- FastAPI backend foundation

### Future Phases
- Job discovery
- Resume parsing
- Job-to-resume matching
- Resume tailoring
- MCP integrations
- Application tracking
- Agent reliability and retries
- Evaluation and observability
- Docker deployment
- CI/CD

## Important Principle

The system should never fabricate skills, experience, education, or achievements while tailoring a resume.

## Tech Stack

- Python 3.11
- FastAPI
- LangGraph
- MCP
- OpenAI / Gemini
- PostgreSQL
- pgvector
- Redis
- pytest
- Docker
- GitHub Actions

## Author

Vamshi Macharla

Robotics & AI Engineer  
Agentic AI | Physical AI | ROS2 | MCP