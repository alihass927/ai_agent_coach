import os
from openai import OpenAI

# (1) Read API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set envionment variable before running")

# (2) Client to talk to OpenAI
client = OpenAI(api_key=api_key)

# (3) Defining system prompt (rules for AI)
SYSTEM_PROMPT = """
You are an analytics training AI coach.
You generate daily Excel and SQL challenges.
Each challenge must include 1 to 3 solutions:
- Solution 1: Beginner approach
- Solution 2: Intermediate approach
- Solution 3: Professional approach
"""

# (4) Defining user prompt (daily request)
def daily_prompt(day_number, difficulty):
    return f"""
Day: {day_number}
Difficulty: {difficulty}

Generate:
1) One Excel challenge
2) One SQL challenge

For each challenge, include:
- Scenario
- Task
- Solution 1 (Beginner approach)
- Solution 2 (Intermediate approac)
- Solution 3 (Professional approac)

Format clearly with headings.
"""

# (5) Creating connection to OpenAI
def generate_daily_challenges(day_number, difficulty):
    user_prompt = daily_prompt(day_number, difficulty)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("\n--- ERROR CALLING OPENAI ---")
        print("This is the full error message:\n")
        print(e)
        print("\n---------------------------\n")
        raise



# (6) Run the script for today
if __name__ == "__main__":
    day_number = 1
    difficulty = "Beginner"

    result = generate_daily_challenges(day_number, difficulty)
    print(result)
