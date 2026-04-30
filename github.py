import requests
import os

def get_headers():
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    return {"Accept": "application/vnd.github.v3+json"}

def fetch_from_github(url):
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": True, "message": str(e)}

def get_issues(repo):
    url = f"https://api.github.com/repos/{repo}/issues"
    return fetch_from_github(url)

def get_prs(repo):
    url = f"https://api.github.com/repos/{repo}/pulls"
    return fetch_from_github(url)