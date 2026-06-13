# GitHub User Activity CLI

A simple Command Line Interface (CLI) application that fetches and displays the recent activity of a GitHub user using the GitHub API.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoint](#api-endpoint)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [Optional Enhancements](#optional-enhancements)
- [Learning Outcomes](#learning-outcomes)

## Overview

This project helps practice working with APIs, handling JSON data, building CLI applications, error handling, and parsing command-line arguments.

The application runs from the command line, accepts a GitHub username as an argument, fetches the user's recent activity, and displays it in a readable format.

## Features

- Fetch recent GitHub user events via public API
- Display activity in human-readable format (e.g., pushes, issues, stars)
- Graceful error handling for invalid users, network issues, etc.
- No external libraries for HTTP requests (use built-in capabilities)
- Pure command-line interface

## Requirements

- Any programming language of your choice (e.g., Python, Node.js, Go, etc.)
- Internet access for API calls
- Command-line environment

## Installation

1. Clone or download the project repository.
2. Ensure you have the required runtime for your chosen language (e.g., Python 3.x).
3. No additional dependencies needed for core functionality.

```bash
# Example for Python
git clone <repository-url>
cd github-activity-cli
# Run directly with python
```

## Usage

```bash
github-activity <username>
```

**Example:**

```bash
github-activity kamranahmedse
```

**Expected Output:**

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Forked kamranahmedse/developer-roadmap
```

## Project Structure

```
github-activity-cli/
├── README.md
├── src/          # Source code directory
│   └── main.<ext> # Main CLI script (e.g., main.py)
└── ...           # Other files as needed
```

## API Endpoint

Use the GitHub Events API:

```
GET https://api.github.com/users/{username}/events
```

**Reference:** [GitHub API Documentation](https://docs.github.com/en/rest)

## Error Handling

The application handles:

- Invalid GitHub usernames → "Error: User not found"
- Network or API failures
- Empty activity responses
- Rate limiting (consider adding delays or messages)

## Examples

See usage section above.

Additional example with error:

```bash
github-activity nonexistentuser12345
```

Output:
```
Error: User not found
```

## Optional Enhancements

- Filter activity by event type
- Colored terminal output
- Pagination support
- Caching responses
- Display timestamps
- Fetch additional repo/user info
- Interactive mode

## Learning Outcomes

- REST API integration
- JSON parsing
- CLI argument parsing
- HTTP requests with standard libraries
- Robust error handling
- Terminal output formatting
