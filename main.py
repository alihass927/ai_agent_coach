# Allow main.py to call Gmail sender
# -----------------------------
from email_sender import send_email

# Allow main.py to call local AI generator
# -----------------------------
from ollama_generator import generate_daily_challenges

# Difficulty logic
# -----------------------------
def get_difficulty_level(day_number):
    if day_number <= 20:
        return "Beginner"
    elif day_number <= 50:
        return "Intermediate"
    else:
        return "Professional"


# Daily configuration
# -----------------------------
day_number = 1
difficulty_level = get_difficulty_level(day_number)


def run_coach_ai():
    print("Daily Analytics Challenge")
    print("-" * 60)
    print(f"Day: {day_number}")
    print(f"Difficulty: {difficulty_level}\n")

    ai_output = generate_daily_challenges(day_number, difficulty_level)

    before_sql, separator, after_sql = ai_output.partition("=== SQL CHALLENGE ===")

    if not separator:
        raise ValueError("AI output missing SQL section header")

    excel_section = before_sql.replace("=== EXCEL CHALLENGE ===", "").strip()
    sql_section = after_sql.strip()

    email_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height:1.6;">
        <h2>Daily Analytics Challenge</h2>

        <p><b>Day:</b> {day_number}<br>
        <b>Difficulty:</b> {difficulty_level}</p>

        <hr>

        <h3>Excel Challenge</h3>
        <pre>{excel_section}</pre>

        <hr>

        <h3>SQL Challenge</h3>
        <pre>{sql_section}</pre>
    </body>
    </html>
    """

    send_email(
        subject=f"Daily Analytics Challenge - Day {day_number}",
        body=email_body,
        to_email="ali.hass927@gmail.com"
    )

    print("Email sent successfully.")

run_coach_ai()
