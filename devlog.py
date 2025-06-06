import requests
from openai import OpenAI
import os
import logging
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO = os.getenv("REPO")
AUTHOR = os.getenv("AUTHOR")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_commits(repo, author, since, until, token):
    """Fetch commits from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/commits"
    # Remove author from params to get all commits
    params = {"since": since, "until": until}
    headers = {"Authorization": f"Bearer {token}"}
    try:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        commits = resp.json()
        
        # Log detailed commit information
        logging.info(f"Found {len(commits)} commits")
        for commit in commits:
            author_name = commit['commit']['author']['name']
            logging.info(
                f"Commit: {commit['sha'][:8]} | "
                f"Date: {commit['commit']['author']['date']} | "
                f"Author: {author_name} | "
                f"Message: {commit['commit']['message'].strip()}"
            )
        return commits
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching commits: {e}")
        return []

def generate_summary(commit_messages, openai_api_key):
    """Generate summary using OpenAI GPT-4."""
    client = OpenAI(api_key=openai_api_key)
    prompt = (
        "You are a project manager summarizing developer work.\n"
        "Summarize the following commit messages in a clear, concise, human-readable format:\n"
        f"{commit_messages}"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You summarize developer commits clearly."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return "Error generating summary."

def save_report(summary, date):
    """Save the summary to a Markdown file in the 'reports' directory."""
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)  # Create the directory if it doesn't exist
    report_filename = os.path.join(reports_dir, f"DailyDevLog_{date}.md")
    with open(report_filename, "w") as file:
        file.write(f"# DailyDevLog Summary for {date}\n\n")
        file.write(summary)
    logging.info(f"Report saved to {report_filename}")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate summary of GitHub commits')
    parser.add_argument(
        '--date', 
        choices=['today', 'yesterday'],
        default='today',
        help='Choose date range for commits (today/yesterday)'
    )
    return parser.parse_args()

def get_time_range(date_choice):
    """Get the time range based on user choice."""
    now = datetime.now(timezone.utc)
    
    if date_choice == 'yesterday':
        start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    else:  # today
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    return start_date.isoformat(), end_date.isoformat()

def main():
    """Main function to fetch commits and generate the report."""
    args = parse_args()
    since, until = get_time_range(args.date)

    logging.info(f"Fetching commits for {REPO}")
    logging.info(f"Time range: {since} to {until}")
    
    commits = fetch_commits(REPO, AUTHOR, since, until, GITHUB_TOKEN)
    if not commits:
        print(f"No commits found for {args.date}.")
        return

    # Format commit messages with SHA and author
    commit_messages = "\n".join(
        f"- [{c['sha'][:8]}] ({c['commit']['author']['name']}) {c['commit']['message'].strip()}" 
        for c in commits
    )
    
    logging.info("Generating summary...")
    summary = generate_summary(commit_messages, OPENAI_API_KEY)

    date_str = datetime.fromisoformat(since.replace('Z', '+00:00')).date()
    print(f"\n🧠 DailyDevLog Summary for {date_str}:\n")
    print(f"{summary}\n")

    # Save report with commit IDs and authors
    save_report(f"{summary}\n\n## Commit Details\n\n{commit_messages}", date_str)

if __name__ == "__main__":
    main()
