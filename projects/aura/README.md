# AURA - Intelligent Agent

LangChain agent with LLM + tool Calculator.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Docker

```bash
docker-compose up
```

## Usage

```
You: Calculate 15 plus 25
You: What is artificial intelligence?
```

Exit: `exit`

## Stack

LangChain + Hugging Face (`google/flan-t5-small`) + PyTorch