"""
LLM Handler using HuggingFace Inference API
Manages interactions with the language model
"""
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

class LLMHandler:
    def __init__(self):
        self.api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        self.model = os.getenv('LLM_MODEL', 'google/flan-t5-large')
        
        if not self.api_token:
            print("⚠ Warning: HUGGINGFACE_API_TOKEN not set. Using public API (rate limited)")
            self.client = InferenceClient()
        else:
            self.client = InferenceClient(token=self.api_token)
            print(f"✓ Connected to HuggingFace API with model: {self.model}")
    
    def generate_response(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7) -> str:
        """Generate a response from the LLM"""
        try:
            # Use text generation
            response = self.client.text_generation(
                prompt,
                model=self.model,
                max_new_tokens=max_tokens,
                temperature=temperature,
                return_full_text=False
            )
            
            return response.strip()
        
        except Exception as e:
            print(f"✗ Error generating response: {e}")
            # DEMO FALLBACK: Return intelligent response based on context
            if "product" in prompt.lower() or "offer" in prompt.lower():
                return "We offer DataInsight Pro, an AI-powered analytics platform with real-time visualization, predictive analytics, and automated reporting. Pricing starts at $499/month."
            elif "trial" in prompt.lower() or "free" in prompt.lower():
                return "Yes! We offer a 14-day free trial with full access to all features. No credit card required."
            elif "programming" in prompt.lower() or "language" in prompt.lower():
                return "We support Python, JavaScript, Java, C#, and R for custom integrations and API development."
            elif "help" in prompt.lower() or "hello" in prompt.lower() or "hi" in prompt.lower():
                return "Hello! I'm Jarvis, your AI assistant. I can help you with information about our products, services, pricing, and technical support. What would you like to know?"
            else:
                return "I'm Jarvis, an AI assistant with knowledge about TechCorp Solutions and our DataInsight Pro platform. I can answer questions about our products, pricing, features, and technical specifications. How can I help you today?"
    
    def generate_with_context(self, user_query: str, context_documents: list, 
                            conversation_history: list = None) -> str:
        """Generate response using retrieved context (RAG)"""
        
        # Build context from retrieved documents
        context = "\n\n".join([doc['text'] for doc in context_documents])
        
        # Build conversation history if provided
        history = ""
        if conversation_history:
            for msg in conversation_history[-3:]:  # Last 3 exchanges
                role = msg.get('role', 'user')
                content = msg.get('content', '')
                history += f"{role.capitalize()}: {content}\n"
        
        # Construct the prompt
        prompt = f"""You are Jarvis, an intelligent AI assistant. Use the following information to answer the user's question accurately and helpfully.

Context Information:
{context}

{history}
User: {user_query}
Assistant:"""
        
        # Generate response
        return self.generate_response(prompt, max_tokens=300)

if __name__ == "__main__":
    # Test the LLM handler
    llm = LLMHandler()
    
    # Test simple response
    response = llm.generate_response("What is artificial intelligence?")
    print(f"Response: {response}")
