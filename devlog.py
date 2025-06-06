import requests, openai, os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO = os.getenv("REPO")
AUTHOR = os.getenv("AUTHOR")

def fetch_commits(repo, author, since, until, token):
    url = f"https://api.github.com/repos/{repo}/commits"
    params = {"since": since, "until": until, "author": author}
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def generate_summary(commit_messages, openai_api_key):
    openai.api_key = openai_api_key
    prompt = (
        "You are a project manager summarizing developer work.\n"
        "Summarize the following commit messages in a clear, concise, human-readable format:\n"
        f"{commit_messages}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You summarize developer commits clearly."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    now = datetime.utcnow()
    since = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"
    until = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"

    commits = fetch_commits(REPO, AUTHOR, since, until, GITHUB_TOKEN)
    if not commits:
        print("No commits found today.")
        return

    commit_messages = "\n".join(f"- {c['commit']['message'].strip()}" for c in commits)
    summary = generate_summary(commit_messages, OPENAI_API_KEY)

    print(f"🧠 DailyDevLog Summary for {now.date()}:\n")
    print(summary)

if __name__ == "__main__":
    main()
