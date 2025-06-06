# DailyDevLog

DailyDevLog is an AI-powered tool that automatically generates a human-readable daily summary of your GitHub commits. It fetches commits from your repository for the current day, sends commit messages to OpenAI's GPT-4 model, and produces a clear, concise work summary.

## Features

- Automatically fetches all commits from your GitHub repository (regardless of author)
- Generates natural language summaries using OpenAI GPT-4
- Saves detailed summaries with commit IDs and author information
- Supports both today's and yesterday's commit summaries
- Organizes reports in a dedicated `reports` directory
- Provides detailed logging for troubleshooting
- Simple to configure and run locally or via automation

## Getting Started

### Prerequisites

- Python 3.8+
- GitHub Fine-Grained Personal Access Token with repository-specific access
- OpenAI API Key
- Git installed on your machine

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
   REPO=organization/repository
   AUTHOR=yourgithubusername
   ```

### Configuration

#### GitHub Fine-Grained Personal Access Token (`GITHUB_TOKEN`)

1. Log in to your GitHub account
2. Navigate to [Settings](https://github.com/settings) > [Developer settings](https://github.com/settings/apps) > [Personal access tokens](https://github.com/settings/tokens)
3. Click **Generate new token** and select **Fine-grained token**
4. Configure the token:
   - Set the Repository access to "Only select repositories"
   - Select your target repository
   - Set the following permissions:
     - **Metadata** (Mandatory): Read-only
     - **Commit statuses**: Read-only
     - **Contents**: Read-only
5. Generate and copy the token
6. Add it to your `.env` file as `GITHUB_TOKEN`

#### OpenAI API Key (`OPENAI_API_KEY`)

1. Log in to [OpenAI Platform](https://platform.openai.com)
2. Navigate to **API Keys** in the dashboard
3. Click **Create new secret key**
4. Copy the generated key
5. Add it to your `.env` file as `OPENAI_API_KEY`

### Usage

The script provides several ways to generate commit summaries:

1. Generate today's summary (default):
   ```bash
   python devlog.py
   ```

2. Generate yesterday's summary:
   ```bash
   python devlog.py --date yesterday
   ```

### Output Format

The script generates two types of output:

1. Console output with logging information:
   ```
   2025-06-06 15:54:39 - INFO - Fetching commits for organization/repository
   2025-06-06 15:54:39 - INFO - Found 5 commits
   2025-06-06 15:54:39 - INFO - Commit: a1b2c3d4 | Author: John | Message: Update API
   ```

2. Markdown report in the `reports` directory:
   ```markdown
   # DailyDevLog Summary for 2025-06-06

   1. Developer John implemented new API features
   2. Developer Jane fixed authentication bugs

   ## Commit Details

   - [a1b2c3d4] (John) Update API endpoint for better performance
   - [e5f6g7h8] (Jane) Fix authentication token validation
   ```

### Directory Structure

```
DailyDevLog/
├── devlog.py           # Main script
├── .env                # Environment variables (create this)
├── .env.example        # Environment variables template
├── requirements.txt    # Python dependencies
├── README.md          # Documentation
└── reports/           # Generated reports directory
    └── DailyDevLog_2025-06-06.md
```

### Troubleshooting

#### Common Issues

1. **No Commits Found**
   - Verify the repository path in `.env`
   - Check if the date range contains commits
   - Ensure GitHub token has correct permissions

2. **Authentication Errors**
   - Verify `GITHUB_TOKEN` is valid
   - Check if token has required permissions
   - Ensure token is not expired

3. **OpenAI API Errors**
   - Verify `OPENAI_API_KEY` is valid
   - Check OpenAI API status
   - Ensure you have API credits available

#### Debug Logging

The script includes detailed logging. Check the console output for:
- Number of commits found
- Commit details (ID, author, message)
- API request status
- Error messages

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Repository

Find the source code on GitHub: [DailyDevLog](https://github.com/ProgrammerNomad/DailyDevLog)