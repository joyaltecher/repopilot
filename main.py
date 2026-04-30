import sys
from github import get_issues, get_prs
from ai import summarize
from rich.console import Console

console = Console()

def summarize_issues(repo):
    issues = get_issues(repo)
    if isinstance(issues, dict) and "message" in issues:
        console.print(f"[red]Error:[/red] {issues['message']}")
        return
    for issue in issues[:5]:
        console.print(f"\n[bold blue]TITLE:[/bold blue] {issue['title']}")
        console.print("[bold green]SUMMARY:[/bold green]", summarize(issue.get("body", "")))

def summarize_prs(repo):
    prs = get_prs(repo)
    if isinstance(prs, dict) and "message" in prs:
        console.print(f"[red]Error:[/red] {prs['message']}")
        return
    for pr in prs[:5]:
        console.print(f"\n[bold blue]PR:[/bold blue] {pr['title']}")
        console.print("[bold green]SUMMARY:[/bold green]", summarize(pr.get("body", "")))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        console.print("Usage: python main.py [issues|prs] owner/repo")
        sys.exit(1)
        
    cmd = sys.argv[1]
    repo = sys.argv[2]
    
    if cmd == "issues":
        summarize_issues(repo)
    elif cmd == "prs":
        summarize_prs(repo)