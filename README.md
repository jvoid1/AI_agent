# AI Agent for Invoice Generation

AI agent designed to automate the process of reading information from specified websites, locating the billing section, filling out the required forms, and generating invoices. The agent is built using Python 3.12. It is containerized with Docker and employs Playwright for web navigation and testing.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Execution](#execution)
- [Usage](#usage)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-agent-project
   ```

2. **Install Poetry:**
   Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

   If you are using Windows, ensure that the Poetry executable is located in the following directory:
   ```
   %APPDATA%\Python\Scripts
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Build the Docker image:**
   ```bash
   docker build -t ai-agent .
   ```

## Configuration

The configuration settings for the agent are stored in `src/config/settings.json`. You can modify this file to include the URLs of the websites to be processed and other relevant parameters.

Example `settings.json` structure:
```json
{
  "websites": [
    {
      "name": "Website 1",
      "url": "https://example1.com/billing"
    },
    {
      "name": "Website 2",
      "url": "https://example2.com/billing"
    },
    {
      "name": "Website 3",
      "url": "https://example3.com/billing"
    }
  ]
}
```

## Execution

To run the AI agent, use the following command:

```bash
poetry run python src/agent/main.py
```

Alternatively, if you want to run it inside the Docker container:

```bash
docker run --rm ai-agent
```

If you want to record the playwright interaction with the website run the container as:

```bash
docker run --rm -v "$(pwd)/videos:/app/videos" ai-agent
```

## Usage

The AI agent will automatically navigate to the specified websites, locate the billing sections, fill out the invoice forms, and submit them. Ensure that the necessary information is available in the configuration file.
