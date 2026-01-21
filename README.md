# 🤖 Jarvis - Personal AI Assistant

Build your own intelligent AI assistant powered by **self-hosted LLM**, **vector database**, and **conversational UI**!

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)

## 📋 Overview

Jarvis is a personal AI assistant that uses:
- **🧠 LLM**: HuggingFace Inference API (Google Flan-T5 or LLaMA models)
- **📚 Vector Database**: ChromaDB (local, no account required)
- **🔍 RAG**: Retrieval Augmented Generation for contextual responses
- **💬 Modern UI**: Beautiful, responsive chatbot interface

## ✨ Features

- ✅ Semantic search through knowledge base
- ✅ Context-aware responses using RAG
- ✅ Conversation history management
- ✅ Add custom knowledge dynamically
- ✅ Beautiful, animated UI
- ✅ Real-time typing indicators
- ✅ No external accounts required (except HuggingFace token)

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- HuggingFace account (free) - [Sign up here](https://huggingface.co/join)

### Installation

1. **Navigate to the project directory**
   ```bash
   cd jarvis-assistant
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

5. **Get your HuggingFace API token**
   - Go to https://huggingface.co/settings/tokens
   - Click "New token"
   - Copy the token

6. **Configure environment variables**
   - Open `.env` file in the project root
   - Add your HuggingFace token:
     ```
     HUGGINGFACE_API_TOKEN=your_token_here
     ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   python app.py
   ```
   
   You should see:
   ```
   ==================================================
    Jarvis AI Assistant API Server
   ==================================================
    Running on: http://localhost:5000
   ==================================================
   ```

2. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Or use a simple HTTP server:
     ```bash
     cd frontend
     python -m http.server 8000
     ```
   - Then navigate to `http://localhost:8000`

3. **Start chatting!**
   - Type your questions in the chat interface
   - Jarvis will use the knowledge base to provide contextual answers

## 📁 Project Structure

```
jarvis-assistant/
├── backend/
│   ├── app.py              # Flask API server
│   ├── llm_handler.py      # LLM integration
│   ├── vector_db.py        # ChromaDB handler
│   ├── rag_pipeline.py     # RAG pipeline
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Chat interface
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── data/
│   └── knowledge_base.txt  # Sample knowledge
├── .env                    # Configuration
└── README.md              # This file
```

## 🎯 Usage

### Adding Custom Knowledge

**Option 1: Edit the knowledge file**
- Edit `data/knowledge_base.txt`
- Restart the backend server

**Option 2: Use the API**
```bash
curl -X POST http://localhost:5000/api/add-knowledge \
  -H "Content-Type: application/json" \
  -d '{"text": "Your custom knowledge here"}'
```

### API Endpoints

- `GET /api/health` - Check server status
- `POST /api/chat` - Send a message
  ```json
  {
    "message": "What products do you offer?"
  }
  ```
- `POST /api/add-knowledge` - Add knowledge
  ```json
  {
    "text": "New knowledge",
    "metadata": {"source": "custom"}
  }
  ```
- `POST /api/clear-history` - Clear conversation history
- `GET /api/stats` - Get system statistics

## 🎨 Customization

### Change the LLM Model

Edit `.env`:
```
LLM_MODEL=meta-llama/Llama-2-7b-chat-hf
```

Available models:
- `google/flan-t5-large` (default, fast)
- `google/flan-t5-xl` (better quality, slower)
- `meta-llama/Llama-2-7b-chat-hf` (requires approval)

### Modify the UI

- **Colors**: Edit `frontend/style.css` gradient values
- **Fonts**: Change Google Fonts import in `frontend/index.html`
- **Layout**: Modify HTML structure in `frontend/index.html`

## 🔧 Troubleshooting

**Issue**: `HUGGINGFACE_API_TOKEN not set`
- **Solution**: Make sure you've added your token to the `.env` file

**Issue**: `ModuleNotFoundError`
- **Solution**: Activate virtual environment and run `pip install -r backend/requirements.txt`

**Issue**: Backend server won't start
- **Solution**: Check if port 5000 is already in use. Change port in `.env`:
  ```
  FLASK_PORT=5001
  ```

**Issue**: "Failed to get response" in UI
- **Solution**: Make sure the backend server is running on `http://localhost:5000`

**Issue**: Slow responses
- **Solution**: Try a smaller/faster model like `google/flan-t5-base`

## 📝 Technical Details

### RAG Pipeline

1. **User Query** → Embedding Generation
2. **Vector Search** → Retrieve top 3 relevant documents from ChromaDB
3. **Context Augmentation** → Combine query + context + history
4. **LLM Generation** → Generate contextual response
5. **Response** → Display to user

### Technologies

- **Backend**: Flask, LangChain, ChromaDB
- **LLM**: HuggingFace Inference API
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Storage**: Local ChromaDB (persistent)

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [HuggingFace Hub](https://huggingface.co/docs/hub/)
- [RAG Explained](https://www.pinecone.io/learn/retrieval-augmented-generation/)

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built as part of programming assignment
- Uses open-source models and libraries
- Inspired by enterprise AI assistants

---

**Made with ❤️ using Python, AI, and modern web technologies**
