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
# Build and start the container
docker-compose up --build -d

# Access the interactive agent
docker exec -it aura-intelligent-agent python main.py
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
- Groq API (llama-3.3-70b-versatile)
- Python 3.12