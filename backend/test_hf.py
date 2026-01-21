"""
Quick test script to verify HuggingFace API token and model access
"""
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('HUGGINGFACE_API_TOKEN')
model = os.getenv('LLM_MODEL', 'google/flan-t5-large')

print(f"Testing HuggingFace API...")
print(f"Token: {token[:20]}... (truncated)")
print(f"Model: {model}")
print()

# Test 1: Check if token is loaded
if not token:
    print("❌ ERROR: Token not loaded from .env file!")
    exit(1)
else:
    print(f"✓ Token loaded successfully")

# Test 2: Try to connect to HuggingFace
try:
    client = InferenceClient(token=token)
    print(f"✓ InferenceClient created")
except Exception as e:
    print(f"❌ Failed to create client: {e}")
    exit(1)

# Test 3: Try a simple text generation
try:
    print(f"\nTesting text generation with prompt: 'Hello, how are you?'")
    response = client.text_generation(
        "Answer this question: What is 2+2?",
        model=model,
        max_new_tokens=50,
        temperature=0.7
    )
    print(f"✓ SUCCESS! Response: {response}")
except Exception as e:
    print(f"❌ Text generation failed!")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    
    # Additional debugging info
    import traceback
    print("\nFull traceback:")
    traceback.print_exc()
