# DailyDevLog

DailyDevLog is an AI-powered tool that automatically generates a human-readable daily summary of your GitHub commits. It fetches commits from your repository for the current day, sends commit messages to OpenAI’s GPT-4 model, and produces a clear, concise work summary.

## Features

- Automatically fetches daily commits from your GitHub repo  
- Generates natural language summaries using OpenAI GPT-4  
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
   git clone https://github.com/yourusername/DailyDevLog.git
   cd DailyDevLog