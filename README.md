# RepoPilot 🚀

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-green.svg)

**RepoPilot** is an AI-powered CLI tool designed for open-source maintainers. It automates the tedious parts of maintaining a repository, such as reading long issue threads and summarizing pull requests.

## ✨ Features
- **AI Issue Summaries**: Instantly grasp the core problem of any issue using GPT-4o-mini.
- **Pull Request Summaries**: Get the gist of code changes without reading a wall of text.
- **Fast & Robust**: Avoids GitHub API limits and handles errors gracefully.

## 📦 Installation

\\\ash
# Clone the repository
git clone https://github.com/joyaltecher/repopilot.git
cd repopilot

# Install dependencies
pip install -r requirements.txt
\\\

## ⚙️ Configuration

Copy the example environment file and add your tokens:
\\\ash
cp .env.example .env
\\\
Edit .env and add:
- \OPENAI_API_KEY\: (Required) Your OpenAI API key.
- \GITHUB_TOKEN\: (Optional but recommended) A GitHub Personal Access Token to avoid rate limits (5,000 requests/hr vs 60 requests/hr).

## 🚀 Usage

RepoPilot provides a clean, user-friendly CLI:

\\\ash
# See all available options
python main.py --help

# Summarize the latest 5 issues
python main.py issues owner/repo

# Summarize the latest 5 Pull Requests
python main.py prs owner/repo
\\\

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a Pull Request.