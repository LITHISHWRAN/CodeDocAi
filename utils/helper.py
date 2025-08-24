import google.generativeai as genai

def ask_gemini(model, prompt):
    response = model.generate_content(prompt)
    return response.text
