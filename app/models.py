from pydantic import BaseModel

class RepoRequest(BaseModel):
    username: str


class IssueRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str


class ListIssuesRequest(BaseModel):
    owner: str
    repo: str