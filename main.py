import argparse
import os
from github import get_issues, get_prs
from ai import summarize
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
console = Console()

def display_items(items, item_type):
    if isinstance(items, dict) and items.get("error"):
        console.print(f"[bold red]GitHub API Error:[/bold red] {items.get('message')}")
        return

    if not isinstance(items, list):
        console.print(f"[bold red]Unexpected response from GitHub API.[/bold red]")
        return

    if not items:
        console.print(f"[bold yellow]No {item_type} found in this repository.[/bold yellow]")
        return

    for item in items[:5]:
        title = item.get('title', 'No Title')
        body = item.get('body', '')
        
        console.print(f"\n[bold blue]{item_type.upper()}:[/bold blue] {title}")
        
        with console.status("[bold cyan]Generating AI summary...", spinner="dots"):
            summary = summarize(body)
            
        console.print(Panel(summary, title="AI Summary", border_style="green"))

def main():
    parser = argparse.ArgumentParser(description="RepoPilot - AI Assistant for Open Source Maintainers")
    parser.add_argument("command", choices=["issues", "prs"], help="What to summarize: 'issues' or 'prs'")
    parser.add_argument("repo", help="The repository to analyze, e.g., 'owner/repo'")
    
    args = parser.parse_args()
    
    if not os.getenv("GITHUB_TOKEN"):
        console.print("[yellow]Warning: GITHUB_TOKEN is not set. You may hit API rate limits quickly.[/yellow]")

    console.print(f"[bold magenta]Analyzing {args.command} for {args.repo}...[/bold magenta]")
    
    if args.command == "issues":
        display_items(get_issues(args.repo), "Issue")
    elif args.command == "prs":
        display_items(get_prs(args.repo), "Pull Request")

if __name__ == "__main__":
    main()