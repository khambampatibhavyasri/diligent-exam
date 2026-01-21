"""
RAG (Retrieval Augmented Generation) Pipeline
Combines vector search with LLM generation
"""
from vector_db import VectorDBHandler
from llm_handler import LLMHandler

class RAGPipeline:
    def __init__(self):
        self.vector_db = VectorDBHandler()
        self.llm = LLMHandler()
        self.conversation_history = []
        print("✓ RAG Pipeline initialized")
    
    def query(self, user_message: str, top_k: int = 3) -> dict:
        """Process a user query through the RAG pipeline"""
        
        # Step 1: Retrieve relevant documents from vector database
        relevant_docs = self.vector_db.search(user_message, top_k=top_k)
        
        # Step 2: Generate response using LLM with context
        if relevant_docs:
            response = self.llm.generate_with_context(
                user_message,
                relevant_docs,
                self.conversation_history
            )
        else:
            # No relevant context found, generate without context
            response = self.llm.generate_response(
                f"You are Jarvis, a helpful AI assistant. Answer this question: {user_message}"
            )
        
        # Step 3: Update conversation history
        self.conversation_history.append({
            'role': 'user',
            'content': user_message
        })
        self.conversation_history.append({
            'role': 'assistant',
            'content': response
        })
        
        # Keep only last 10 messages (5 exchanges)
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
        
        return {
            'response': response,
            'sources': relevant_docs,
            'context_used': len(relevant_docs) > 0
        }
    
    def add_knowledge(self, text: str, metadata: dict = None):
        """Add new knowledge to the vector database"""
        self.vector_db.add_documents([text], [metadata] if metadata else None)
    
    def load_knowledge_file(self, filepath: str):
        """Load knowledge from a file"""
        self.vector_db.load_knowledge_from_file(filepath)
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("✓ Conversation history cleared")
    
    def get_stats(self):
        """Get pipeline statistics"""
        return {
            **self.vector_db.get_collection_stats(),
            'conversation_length': len(self.conversation_history)
        }

if __name__ == "__main__":
    # Test the RAG pipeline
    rag = RAGPipeline()
    
    # Load knowledge
    rag.load_knowledge_file('../data/knowledge_base.txt')
    
    # Test query
    result = rag.query("What products do you offer?")
    print(f"\nResponse: {result['response']}")
    print(f"\nSources used: {len(result['sources'])}")
