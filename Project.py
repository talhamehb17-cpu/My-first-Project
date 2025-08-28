import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Test model
model = genai.GenerativeModel("gemini-1.5-flash")

print("🤖 Welcome to Talha's AI! (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye 👋")
        break
    
    # Send user input to model
    response = model.generate_content(user_input)
    
    # Print AI response
    print("AI:", response.text)
