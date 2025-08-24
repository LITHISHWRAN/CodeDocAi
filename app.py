import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import system_prompt

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_ai(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== CodeDoc AI - Personal Debugging Mentor ===")
    print("Paste your buggy Python code below. End input with a blank line:")
    
    # Take multi-line user input
    user_code_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":  # stop if empty line
                break
            user_code_lines.append(line)
        except EOFError:
            break

    user_code = "\n".join(user_code_lines)

    final_prompt = f"{system_prompt}\n\nHere is the code to debug:\n{user_code}"
    
    print("\n=== Debugging Result ===")
    print(ask_ai(final_prompt))
