import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Test
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Hello Gemini!")
print(response.text)
