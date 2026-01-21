# 🚀 Quick Start Guide - Jarvis AI Assistant

## ⚡ Fast Setup (5 Minutes)

### Step 1: Get HuggingFace Token (1 min)
1. Go to https://huggingface.co/settings/tokens
2. Sign up for free if needed
3. Click "New token" → Create
4. Copy the token

### Step 2: Configure Environment (30 sec)
1. Open `.env` file in the project root
2. Paste your token:
   ```
   HUGGINGFACE_API_TOKEN=hf_your_token_here
   ```
3. Save the file

### Step 3: Start Backend (1 min)
```bash
cd backend
python app.py
```

Wait for:
```
✓ Created new ChromaDB collection
✓ Loaded embedding model  
✓ Loaded knowledge from knowledge_base.txt
Running on: http://localhost:5000
```

### Step 4: Open Frontend (30 sec)
Double-click: `frontend/index.html`

### Step 5: Start Chatting! 🎉
Try asking:
- "What products do you offer?"
- "What is DataInsight Pro?"
- "Do you offer a free trial?"
- "What programming languages do you support?"

---

## 📝 Test Checklist

- [ ] Backend server starts without errors
- [ ] Frontend shows "Online" status  
- [ ] Can send messages
- [ ] Receives contextual responses
- [ ] Typing indicator appears
- [ ] Conversation history works
- [ ] Clear history works

---

## 🐛 Common Issues

**"Module not found"**  
→ Run: `pip install -r backend/requirements.txt`

**"HUGGINGFACE_API_TOKEN not set"**  
→ Add your token to `.env` file

**Backend won't start**  
→ Make sure port 5000 is free

**"Failed to get response"**  
→ Ensure backend is running at http://localhost:5000

---

## 📚 Knowledge Sources

The AI uses `data/knowledge_base.txt` for context.  
To add more knowledge:
1. Edit the file
2. Restart backend
3. Test with related questions

---

**Need help?** Check `README.md` for full documentation
