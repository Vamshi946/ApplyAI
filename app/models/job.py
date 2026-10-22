from pydantic import BaseModel


class JobSearchRequest(BaseModel):
    role: str
    location: str