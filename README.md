# DailyDevLog

DailyDevLog is an AI-powered tool that automatically generates a human-readable daily summary of your GitHub commits. It fetches commits from your repository for the current day, sends commit messages to OpenAI’s GPT-4 model, and produces a clear, concise work summary.

## Features

- Automatically fetches daily commits from your GitHub repository  
- Generates natural language summaries using OpenAI GPT-4  
- Saves the summary in a well-formatted Markdown file in the `reports` directory  
- Simple to configure and run locally or via automation  
- Output is clear, professional, and human-readable  

## Getting Started

### Prerequisites

- Python 3.8+  
- GitHub Fine-Grained Personal Access Token with repository-specific access  
- OpenAI API Key  

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ProgrammerNomad/DailyDevLog.git
   cd DailyDevLog
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file by copying `.env.example`:

   ```bash
   cp .env.example .env
   ```

4. Fill in your credentials in the `.env` file:

   ```properties
   GITHUB_TOKEN=ghp_yourgithubtoken
   OPENAI_API_KEY=sk_youropenaiapikey
   REPO=yourusername/yourrepository
   AUTHOR=yourgithubusername
   ```

### How to Get Your Credentials

#### GitHub Fine-Grained Personal Access Token (`GITHUB_TOKEN`)

1. Log in to your GitHub account.
2. Navigate to [Settings](https://github.com/settings) > [Developer settings](https://github.com/settings/apps) > [Personal access tokens](https://github.com/settings/tokens).
3. Click **Generate new token** and select **Fine-grained token**.
4. Specify the repository you want to grant access to (e.g., `MobrilzPvtLtd/RESO-HEATH-WebApp-API-and-Backend`).
5. Select the required permissions:
   - **Metadata** (Mandatory)
   - **Commit statuses**
   - **Contents**
6. Generate the token and copy it. Add it to the `.env` file as `GITHUB_TOKEN`.

#### OpenAI API Key (`OPENAI_API_KEY`)

1. Log in to your OpenAI account at [https://platform.openai.com](https://platform.openai.com).
2. Navigate to **API Keys** in the dashboard.
3. Click **Create new secret key**.
4. Copy the generated key and add it to the `.env` file as `OPENAI_API_KEY`.

### Usage

1. Run the script to generate the daily summary:

   ```bash
   python devlog.py
   ```

2. The summary will be saved in the `reports` directory as a Markdown file named `DailyDevLog_<date>.md`.

3. Open the generated file to view the summary.

### Example Output

#### Markdown File:
```markdown
# DailyDevLog Summary for 2025-06-06

- Fixed bug in user authentication.
- Updated README with installation instructions.
- Refactored database connection logic.
```

### Troubleshooting

- **Missing Dependencies**: Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **Invalid Credentials**: Verify your `.env` file contains the correct `GITHUB_TOKEN` and `OPENAI_API_KEY`.
- **No Commits Found**: Ensure there are commits in the specified repository for the current day.

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Repository

Find the source code on GitHub: [DailyDevLog](https://github.com/ProgrammerNomad/DailyDevLog)