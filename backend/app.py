"""
Flask API Server for Jarvis AI Assistant
Provides REST API endpoints for the chatbot interface
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_pipeline import RAGPipeline
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Initialize RAG pipeline
print("Initializing Jarvis AI Assistant...")
rag = RAGPipeline()

# Load initial knowledge base
knowledge_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base.txt')
knowledge_file = os.path.abspath(knowledge_file)
if os.path.exists(knowledge_file):
    rag.load_knowledge_file(knowledge_file)
    print(f"✓ Loaded knowledge from {knowledge_file}")
else:
    print(f"⚠ Warning: Knowledge file not found at {knowledge_file}")

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    stats = rag.get_stats()
    return jsonify({
        'status': 'healthy',
        'message': 'Jarvis AI Assistant is running',
        'stats': stats
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'error': 'Message cannot be empty'
            }), 400
        
        # Process through RAG pipeline
        result = rag.query(user_message)
        
        return jsonify({
            'response': result['response'],
            'context_used': result['context_used'],
            'num_sources': len(result['sources'])
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/add-knowledge', methods=['POST'])
def add_knowledge():
    """Add new knowledge to the vector database"""
    try:
        data = request.json
        text = data.get('text', '').strip()
        metadata = data.get('metadata', {})
        
        if not text:
            return jsonify({
                'error': 'Text cannot be empty'
            }), 400
        
        rag.add_knowledge(text, metadata)
        
        return jsonify({
            'message': 'Knowledge added successfully',
            'stats': rag.get_stats()
        })
    
    except Exception as e:
        print(f"Error in add-knowledge endpoint: {e}")
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    try:
        rag.clear_history()
        return jsonify({
            'message': 'Conversation history cleared'
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get system statistics"""
    try:
        return jsonify(rag.get_stats())
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"\n{'='*50}")
    print(f" Jarvis AI Assistant API Server")
    print(f"{'='*50}")
    print(f" Running on: http://localhost:{port}")
    print(f" Debug mode: {debug}")
    print(f"{'='*50}\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
