# Agentic Coding Fitness - Python Exercises

Hands-on Python exercises for each week of the curriculum.

## Prerequisites

- Python 3.10+
- [Anthropic API key](https://console.anthropic.com/)

## Setup

```bash
cd exercises
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Week Index

### Week 2 - API Basics
| File | Description |
|------|-------------|
| `claudeapicall.py` | Single API call to Claude |
| `claudemulti_turn.py` | Multi-turn conversation |
| `claudestreamingapi.py` | Streaming responses |

### Week 3 - Tool Use & Agentic Patterns
| File | Description |
|------|-------------|
| `toolsuse.py` | Basic tool use with calculate and weather tools |
| `buildsmartassistant3tools.py` | Smart assistant with web search, calculate, and file reader |
| `hwadd4thtool.py` | Homework: add a 4th tool |
| `hwadd5thtool.py` | Homework: add a 5th tool |

### Week 4+
Coming soon.

## Running

```bash
source venv/bin/activate
python week2/claudeapicall.py
```
