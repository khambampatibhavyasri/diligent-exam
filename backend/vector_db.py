"""
Vector Database Handler using ChromaDB
Handles document storage and semantic search
"""
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class VectorDBHandler:
    def __init__(self):
        # Initialize ChromaDB with persistent storage
        persist_dir = os.getenv('CHROMA_PERSIST_DIR', './chroma_db')
        self.client = chromadb.Client(Settings(
            persist_directory=persist_dir,
            anonymized_telemetry=False
        ))
        
        # Create or get collection
        try:
            self.collection = self.client.create_collection(
                name="knowledge_base",
                metadata={"description": "Jarvis AI knowledge storage"}
            )
            print("✓ Created new ChromaDB collection")
        except:
            self.collection = self.client.get_collection("knowledge_base")
            print("✓ Connected to existing ChromaDB collection")
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✓ Loaded embedding model")
    
    def add_documents(self, texts: List[str], metadata: List[Dict] = None):
        """Add documents to the vector database"""
        if not texts:
            return
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(texts).tolist()
        
        # Prepare IDs
        existing_count = self.collection.count()
        ids = [f"doc_{existing_count + i}" for i in range(len(texts))]
        
        # Prepare metadata
        if metadata is None:
            metadata = [{"source": "user_input"} for _ in texts]
        
        # Add to collection
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadata,
            ids=ids
        )
        print(f"✓ Added {len(texts)} documents to vector database")
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search for relevant documents using semantic similarity"""
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        # Search in ChromaDB
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        # Format results
        documents = []
        if results['documents'] and len(results['documents'][0]) > 0:
            for i, doc in enumerate(results['documents'][0]):
                documents.append({
                    'text': doc,
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'distance': results['distances'][0][i] if results['distances'] else 0
                })
        
        return documents
    
    def load_knowledge_from_file(self, filepath: str):
        """Load knowledge from a text file and add to vector database"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split into chunks (by paragraphs)
            chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]
            
            # Add to database
            metadata = [{"source": filepath} for _ in chunks]
            self.add_documents(chunks, metadata)
            
            print(f"✓ Loaded {len(chunks)} chunks from {filepath}")
        except Exception as e:
            print(f"✗ Error loading knowledge file: {e}")
    
    def get_collection_stats(self):
        """Get statistics about the collection"""
        count = self.collection.count()
        return {
            "total_documents": count,
            "collection_name": self.collection.name
        }

if __name__ == "__main__":
    # Test the vector DB handler
    db = VectorDBHandler()
    
    # Load sample knowledge
    db.load_knowledge_from_file('../data/knowledge_base.txt')
    
    # Test search
    results = db.search("What products do you offer?")
    print("\nSearch Results:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['text'][:100]}...")
    
    # Show stats
    print(f"\n{db.get_collection_stats()}")
