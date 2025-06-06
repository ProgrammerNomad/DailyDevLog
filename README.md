# DailyDevLog

DailyDevLog is an AI-powered tool that automatically generates a human-readable daily summary of your GitHub commits. It fetches commits from your repository for the current day, sends commit messages to OpenAI’s GPT-4 model, and produces a clear, concise work summary.

## Features

- Automatically fetches daily commits from your GitHub repository  
- Generates natural language summaries using OpenAI GPT-4  
- Saves the summary in a well-formatted Markdown file  
- Simple to configure and run locally or via automation  
- Output is clear, professional, and human-readable  

## Getting Started

### Prerequisites

- Python 3.8+  
- GitHub Personal Access Token with `repo` access  
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

### Usage

Run the script to generate the daily summary:

```bash
python devlog.py
```

The summary will be saved in a Markdown file named `DailyDevLog_<date>.md`.

### Example Output

#### Markdown File:
```markdown
# DailyDevLog Summary for 2025-06-06

- Fixed bug in user authentication.
- Updated README with installation instructions.
- Refactored database connection logic.
```

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Repository

Find the source code on GitHub: [DailyDevLog](https://github.com/ProgrammerNomad/DailyDevLog)