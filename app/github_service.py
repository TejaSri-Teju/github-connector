import requests
from app.config import HEADERS

BASE_URL = "https://api.github.com"

def get_repositories(username: str):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub Error: {response.json()}")

    repos = response.json()

    # ✅ Filter required fields
    filtered_repos = []
    for repo in repos:
        filtered_repos.append({
            "id": repo.get("id"),
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "html_url": repo.get("html_url"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "private": repo.get("private")
        })

    return filtered_repos


def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code not in [200, 201]:
        raise Exception(f"GitHub Error: {response.json()}")

    return response.json()


def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub Error: {response.json()}")

    return response.json()