# GitHub User Activity CLI

A simple Command Line Interface (CLI) that fetches and displays the recent activity of a GitHub user using the GitHub API.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features
- Fetch recent public activity from GitHub API
- Beautiful colored terminal output with timestamps
- Proper error handling (user not found, rate limit, network issues)
- Clean and readable activity display
- No external heavy frameworks — only `requests` and `colorama`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/amirhossein-rajabi/github-activity-cli.git
   cd github-activity-cli
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
   # source venv/bin/activate   # For Linux / Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py <username>
```

**Examples:**
```bash
python main.py torvalds
python main.py kamranahmedse
python main.py amirhossein-rajabi
```

## Example Output
```
Fetching recent activity for user: torvalds...

Recent activity for user (showing up to 10 events):

• Pushed to torvalds/linux (2026-06-13 00:54)
• Pushed to torvalds/GitPedal (2026-06-12 21:14)
• Starred some-repo (2026-06-12 18:30)
```

## Project Structure
```
github-activity-cli/
├── main.py                 # CLI entry point
├── github_activity.py      # Core logic + API handling
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_github_activity.py
```

## Technologies Used
- **Python 3.14**
- `requests` — for GitHub API calls
- `colorama` — for colored terminal output

## Error Handling
- Invalid username → Clear message
- Network / API failures
- Rate limiting by GitHub
- Empty activity

## Learning Outcomes
- Working with REST APIs
- JSON data parsing
- Building CLI applications
- Command-line argument parsing
- Error handling & Git workflow
