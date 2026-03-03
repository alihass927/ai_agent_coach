import json
from ollama_generator import generate_daily_challenges

TOTAL_DAYS = 61

def get_difficulty(day):
    if day <= 20:
        return "Beginner"
    elif day <= 50:
        return "Intermediate"
    else:
        return "Professional"
    
all_challenges = {}

for day in range(1, TOTAL_DAYS + 1):
    difficulty = get_difficulty(day)

    print(f"Generating Day {day}...")

    content = generate_daily_challenges(day, difficulty)

    all_challenges[str(day)] = {
        "difficulty": difficulty,
        "content": content
    }


with open("challenges.json", "w", encoding="utf-8") as f:
    json.dump(all_challenges, f, indent=2)

print("Saved to challenges.json")