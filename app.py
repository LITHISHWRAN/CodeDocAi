import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import system_prompt
from config import generation_config   # import config here

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use config from config.py
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config=generation_config
)

def ask_ai(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== CodeDoc AI – Personal Debugging Mentor ===")
    print("Paste your buggy code below (multi-line supported).")
    print("👉 When done, press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows):\n")

    # Read user code
    try:
        user_code = ""
        while True:
            line = input()
            user_code += line + "\n"
    except EOFError:
        pass

    final_prompt = f"{system_prompt}\n\nHere is the code to debug:\n{user_code}"

    print("\n=== Debugging Result ===")
    print(ask_ai(final_prompt))
