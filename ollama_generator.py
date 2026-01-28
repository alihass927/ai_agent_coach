import requests
import json

# 1. Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# 2. System prompt (rules for the AI)
SYSTEM_PROMPT = """
You are an analytics training AI coach.

You MUST format your response exactly using the following structure
and you MUST follow ALL rules below.

RULES (MANDATORY):
- Any table you include MUST contain realistic example data
- Tables MUST have at least 10 rows
- DO NOT return empty or placeholder tables
- Data must be sufficient to solve the task
- Do not say "example data omitted" or similar

FORMAT (DO NOT DEVIATE):

=== EXCEL CHALLENGE ===
Scenario:
Include a short business context.

Dataset:
Provide a table with at least 10 rows of realistic data.

Task:
Clearly state what must be calculated or analyzed.

Solution 1 (Beginner):
Explain step-by-step using basic Excel functions.

Solution 2 (Intermediate):
Use more efficient Excel techniques.

Solution 3 (Professional):
Use advanced or scalable approaches.

=== SQL CHALLENGE ===
Scenario:
Include a short business context.

Dataset:
Provide a table schema AND at least 10 rows of example data.

Task:
Clearly state the SQL problem.

Solution 1 (Beginner):
Simple, readable SQL.

Solution 2 (Intermediate):
Optimized SQL with advance queries.

Solution 3 (Professional):
Production-quality SQL with best practices.

DO NOT include any text outside these sections.
"""

# 3. Build the daily prompt dynamically
def build_daily_prompt(day_number, difficulty):
    return f"""
Day: {day_number}
Difficulty: {difficulty}

Generate:
1) One Excel challenge
2) One SQL challenge

For each challenge include:
- Scenario
- Task
- Solution 1 (Beginner)
- Solution 2 (Intermediate)
- Solution 3 (Professional)

Format clearly with headings.
"""

# 4. Call Ollama and return the response
def generate_daily_challenges(day_number, difficulty):
    full_prompt = SYSTEM_PROMPT + "\n" + build_daily_prompt(day_number, difficulty)

    payload = {
        "model": "llama3.1",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
