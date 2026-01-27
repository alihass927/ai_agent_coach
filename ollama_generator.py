import requests
import json

# 1. Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# 2. System prompt (rules for the AI)
SYSTEM_PROMPT = """
You are an analytics training AI coach.
You generate daily Excel and SQL challenges.
Each challenge must include:
- A clear scenario
- A clear task
- Tiered solutions:
  - Beginner approach
  - Intermediate approach
  - Professional approach
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

# 5. Run the script directly
if __name__ == "__main__":
    day_number = 1
    difficulty = "Beginner"

    result = generate_daily_challenges(day_number, difficulty)
    print(result)
