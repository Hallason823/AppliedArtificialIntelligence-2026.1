# AURA - Intelligent Agent

LangChain ReAct agent with Groq API and Calculator tool.

## Prerequisites

Get a free API key from https://console.groq.com/keys

## Setup

1. Clone and configure environment:
```bash
cd projects/aura
cp .env.example .env
```

2. Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_actual_api_key_here
```

## Running with Docker (Recommended)

```bash
docker-compose up --build
```

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Usage Examples

```
You: Calculate 15 plus 25
You: What is 100 divided by 4?
You: What is artificial intelligence?
```

Exit: `exit` or `quit`

## Stack

- LangChain (ReAct agent framework)
- Groq API (llama3-groq-8b-8192-tool-use-preview)
- Python 3.12