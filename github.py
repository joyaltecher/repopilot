import requests

def get_issues(repo):
    url = f"https://api.github.com/repos/{repo}/issues"
    return requests.get(url).json()

def get_prs(repo):
    url = f"https://api.github.com/repos/{repo}/pulls"
    return requests.get(url).json()