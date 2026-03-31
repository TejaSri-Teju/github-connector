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


@app.post("/repos")
def fetch_repos(request: RepoRequest):
    try:
        return get_repositories(request.username)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create-issue")
def create_issue_api(request: IssueRequest):
    try:
        return create_issue(
            request.owner,
            request.repo,
            request.title,
            request.body
        )

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/list-issues")
def list_issues_api(request: ListIssuesRequest):
    try:
        issues = list_issues(request.owner, request.repo)
        return {
            "count": len(issues),
            "issues": issues
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))