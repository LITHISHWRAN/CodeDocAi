# System Prompt (RTFC)
system_prompt = """
You are CodeDoc AI, a personal debugging mentor. 
Role: Identify bugs, explain why they happen, and suggest optimized fixes.
Task: Analyze given code, diagnose issues, fix them, and explain clearly.
Format: 
1. Bug Diagnostics
2. Fix Suggestions
3. Explanation
Constraints: Keep answers simple and educational.
"""

# User Prompt (example code to debug)
user_prompt = """
Here is my Python function. Please debug and explain:

def divide(a, b):
    return a/b
"""

# Zero-shot
zero_shot_prompt = """
Debug this code and explain the bug:

def add_numbers(a, b)
    return a+b
"""

# One-shot
one_shot_prompt = """
Example:
Buggy Code:
def multiply(a, b)
    return a*b

Diagnosis: Missing colon
Fix: Add ":" at end of function declaration

Now debug this code:
def divide(a, b)
    return a/b
"""

# Multi-shot
multi_shot_prompt = """
Example 1:
Buggy Code:
def subtract(a, b)
    return a-b
Diagnosis: Missing colon
Fix: Add ":"

Example 2:
Buggy Code:
for i in range(5)
    print(i)
Diagnosis: Missing colon
Fix: Add ":"

Now debug this code:
def square(x)
    return x*x
"""


# Dynamic Prompt
def dynamic_prompt(user_code):
    return f"""
You are CodeDoc AI. Debug the following user code:

{user_code}

Explain bugs, suggest fixes, and provide an optimized version.
"""

# Chain-of-Thought
cot_prompt = """
Debug the following code step by step. 
First, identify possible errors → then analyze cause → then give fix → finally show corrected code.

Code:
def divide(a, b):
    return a/b
print(divide(10,0))
"""
