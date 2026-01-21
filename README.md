# Jarvis - Personal AI Assistant

A personal AI assistant built with **self-hosted LLM**, **vector database**, and **conversational UI** for enterprise use.

## Overview

This project implements a complete RAG (Retrieval Augmented Generation) pipeline with:
- **LLM**: HuggingFace Inference API (Flan-T5)
- **Vector Database**: ChromaDB (local, no account required)
- **Frontend**: Modern chatbot interface with real-time messaging
- **Knowledge Base**: Semantic search through indexed documents

## Quick Start

### Prerequisites
- Python 3.9+
- HuggingFace account (free) - [Sign up here](https://huggingface.co/join)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/khambampatibhavyasri/diligent-exam.git
   cd jarvis-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure environment**
   - Get HuggingFace API token from https://huggingface.co/settings/tokens
   - Open `.env` file and add your token:
     ```
     HUGGINGFACE_API_TOKEN=your_token_here
     ```

5. **Start the backend server**
   ```bash
   python backend/app.py
   ```

6. **Open the frontend**
   - Open `frontend/index.html` in your browser

## Usage

Once the server is running and frontend is open:
1. Check that status shows "Online • 10 docs loaded"
2. Type your questions in the chat interface
3. Try asking:
   - "What products do you offer?"
   - "Do you offer a free trial?"
   - "What programming languages do you support?"

## Project Structure

```
jarvis-assistant/
├── backend/
│   ├── app.py              # Flask API server
│   ├── llm_handler.py      # LLM integration
│   ├── vector_db.py        # ChromaDB handler
│   └── rag_pipeline.py     # RAG pipeline
├── frontend/
│   ├── index.html          # Chatbot interface
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── data/
│   └── knowledge_base.txt  # Sample knowledge
└── README.md
```

## Technology Stack

**Backend:**
- Python, Flask
- ChromaDB (vector database)
- HuggingFace Inference API
- Sentence Transformers (embeddings)
- LangChain (RAG orchestration)

**Frontend:**
- HTML/CSS/JavaScript
- Modern UI with animations
- Real-time API communication

## Features

- ✅ Semantic search through knowledge base
- ✅ Context-aware responses using RAG
- ✅ Conversation history management
- ✅ Modern, responsive UI with animations
- ✅ Real-time typing indicators
- ✅ Local vector database (no cloud dependency)

## API Endpoints

- `GET /api/health` - Check server status
- `POST /api/chat` - Send message and get response
- `POST /api/add-knowledge` - Add knowledge to database
- `POST /api/clear-history` - Clear conversation history
- `GET /api/stats` - Get system statistics

## Assignment Details

**Exercise:** Build Your Own Jarvis  
**Tool:** Visual Studio, Co-pilot  
**Duration:** 40 minutes  
**Objective:** Design an AI-powered feature for a SaaS product

## License

Educational project for programming assignment.

---

**Built with** Python, AI, and modern web technologies
