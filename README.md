# Create AI assistance chatbot using qwen2.5:7b 

# 🤖 Local Multi-Agent AI Assistant

A local-first multi-agent AI assistant built using FastAPI, Ollama, and a modular agent architecture.

This project demonstrates how to build a ChatGPT-style intelligent assistant locally with:

Conversational Memory

Retrieval Augmented Generation (RAG)

Tool Execution

Agent Routing

Planning & Execution system

All running fully offline on a laptop.

# 🚀 Features

✅ Local LLM using Ollama
✅ Multi-Agent Architecture
✅ Intelligent Router (LLM-based intent detection)
✅ RAG (Document Question Answering)
✅ Conversation Memory
✅ Tool Execution Agent
✅ Planner + Executor workflow
✅ Persistent Vector Database
✅ Modular & scalable structure

# Work flow
User
 │
 ▼
FastAPI API Layer
 │
 ▼
Router Agent (LLM Intent Detection)
 │
 ├── Chat Agent      → Conversation + Memory
 ├── RAG Agent       → Knowledge Retrieval
 ├── Tool Agent      → System Actions
 └── Planner Agent   → Goal Decomposition
          │
          ▼
     Executor Agent
          │
          ▼
 Local LLM (Ollama)

 # 📁 Project Structure

 ai_chatbot/
│
├── app/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── router_agent.py
│   │   ├── chat_agent.py
│   │   ├── rag_agent.py
│   │   ├── tool_agent.py
│   │   ├── planner_agent.py
│   │   └── executor_agent.py
│   │
│   ├── api/
│   │   └── chat_routes.py
│   │
│   ├── llm/
│   │   └── ollama_client.py
│   │
│   ├── memory/
│   │   └── memory.py
│   │
│   ├── rag/
│   │   └── rag.py
│   │
│   └── main.py
│
├── data/
│   └── vector_db/
│
├── add_doc.py
└── README.md

# ⚙️ Requirements

Python 3.11

Linux / macOS

16GB RAM recommended

# Ollama installed
ollama pull qwen2.5:7b
## verify ollama
ollama run qwen2.5:7b

# 🐍 Setup Environment
uv venv
source .venv/bin/activate
uv pip install fastapi uvicorn chromadb sentence-transformers requests

# ▶️ Run Application

Start API server:

uv run uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

