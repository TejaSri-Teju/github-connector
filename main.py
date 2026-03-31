from fastapi import FastAPI, HTTPException
from app.models import RepoRequest, IssueRequest, ListIssuesRequest
from app.github_service import (
    get_repositories,
    create_issue,
    list_issues
)

app = FastAPI(title="GitHub Cloud Connector API")


@app.get("/")
def home():
    return {"message": "GitHub Connector Running 🚀"}


# 🔹 Fetch Repositories
@app.post("/repos")
def fetch_repos(request: RepoRequest):
    try:
        repos = get_repositories(request.username)
        return repos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 🔹 Create Issue
@app.post("/create-issue")
def create_issue_api(request: IssueRequest):
    try:
        issue = create_issue(
            request.owner,
            request.repo,
            request.title,
            request.body
        )
        return {"status": "success", "data": issue}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 🔹 List Issues
@app.post("/list-issues")
def list_issues_api(request: ListIssuesRequest):
    try:
        issues = list_issues(request.owner, request.repo)
        return {"no_of_issues":len(issues), "data": issues}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))