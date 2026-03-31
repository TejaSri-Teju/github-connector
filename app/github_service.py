import requests
from app.config import HEADERS

BASE_URL = "https://api.github.com"


def handle_github_response(response):
    """Centralized error handling"""

    if response.status_code == 401:
        raise Exception("Unauthorized: Invalid or expired GitHub token")

    elif response.status_code == 403:
        raise Exception("Forbidden: Rate limit exceeded or insufficient permissions")

    elif response.status_code == 404:
        raise Exception("Not Found: Repository or user does not exist")

    elif response.status_code >= 500:
        raise Exception("GitHub Server Error")

    elif response.status_code not in [200, 201]:
        raise Exception(f"GitHub Error: {response.json()}")

    return response.json()


def get_repositories(username: str):
    if not username:
        raise ValueError("Username cannot be empty")

    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)

    repos = handle_github_response(response)

    # ✅ Filter response
    return [
        {
            "id": repo.get("id"),
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "html_url": repo.get("html_url"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "private": repo.get("private")
        }
        for repo in repos
    ]


def create_issue(owner: str, repo: str, title: str, body: str):
    if not owner or not repo or not title:
        raise ValueError("Owner, repo, and title are required")

    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    return handle_github_response(response)


def list_issues(owner: str, repo: str):
    if not owner or not repo:
        raise ValueError("Owner and repo are required")

    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    response = requests.get(url, headers=HEADERS)

    return handle_github_response(response)