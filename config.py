# config.py
# Centralized configuration for Gemini model

generation_config = {
    "top_p": 0.7,            # nucleus sampling (controls creativity)
    "temperature": 0.7,      # randomness in output
    "max_output_tokens": 512 # limit on response length
}
