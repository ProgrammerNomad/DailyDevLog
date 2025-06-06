import requests, openai, os, logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

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
    params = {"since": since, "until": until, "author": author}
    headers = {"Authorization": f"token {token}"}
    try:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching commits: {e}")
        return []

def generate_summary(commit_messages, openai_api_key):
    """Generate summary using OpenAI GPT-4."""
    openai.api_key = openai_api_key
    prompt = (
        "You are a project manager summarizing developer work.\n"
        "Summarize the following commit messages in a clear, concise, human-readable format:\n"
        f"{commit_messages}"
    )
    try:
        response = openai.ChatCompletion.create(
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
    """Save the summary to a Markdown file."""
    report_filename = f"DailyDevLog_{date}.md"
    with open(report_filename, "w") as file:
        file.write(f"# DailyDevLog Summary for {date}\n\n")
        file.write(summary)
    logging.info(f"Report saved to {report_filename}")

def main():
    """Main function to fetch commits and generate the report."""
    now = datetime.utcnow()
    since = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"
    until = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"

    logging.info("Fetching commits...")
    commits = fetch_commits(REPO, AUTHOR, since, until, GITHUB_TOKEN)
    if not commits:
        print("No commits found today.")
        return

    commit_messages = "\n".join(f"- {c['commit']['message'].strip()}" for c in commits)
    logging.info("Generating summary...")
    summary = generate_summary(commit_messages, OPENAI_API_KEY)

    print(f"🧠 DailyDevLog Summary for {now.date()}:\n")
    print(summary)

    save_report(summary, now.date())

if __name__ == "__main__":
    main()
