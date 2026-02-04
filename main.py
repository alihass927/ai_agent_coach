
# Allow main.py to call Gmail sender
from email_sender import send_email
# Allow main.py to call local AI generator
from ollama_generator import generate_daily_challenges

# Difficulty level Automation

def get_difficulty_level(day_number):
    if day_number <= 20:
        return "Beginner"
    elif day_number <=50:
        return "Intermediate"
    else:
        return "Professional"
    
# Daily Challenge Configuration

day_number = 1
difficulty_level = get_difficulty_level(day_number)

# Excel Challenge

excel_challenge = (
    "EXCEL CHALLENGE\n"
    "Scenario:\n"
    "You are given a sales dataset with columns:\n"
    "Date, Product, Region, Revenue\n\n"
    "Task:\n"
    "Calculate total revenue by product using Excel.\n"
)

excel_solutions = {
    "Beginner Solution": (
        "Use SUMIF or SUMIFS to sum revenue by product.\n"
        "Steps:\n"
        "1. Select the Revenue column.\n"
        "2. Use SUMIF with Product as the criteria.\n"
    ),
    "Intermediate Solution": (
        "Create a Pivot Table.\n"
        "Place Product in Rows and Revenue in Values.\n"
        "This reduces formula complexity and improves readability.\n"
    ),
    "Professional Solution": (
        "Use Power Query to aggregate revenue by product.\n"
        "This approach is scalable, refreshable, and production-ready.\n"
    )
}

# SQL Challenge

sql_challenge = (
    "SQL CHALLENGE\n"
    "Scenario:\n"
    "You have a table called sales_data with columns:\n"
    "date, product, region, revenue\n\n"
    "Task:\n"
    "Write a SQL query to calculate total revenue by product.\n"
)

sql_solutions = {
    "Beginner Solution": (
        "SELECT product, SUM(revenue)\n"
        "FROM sales_data\n"
        "GROUP BY product;\n"
    ),
    "Intermediate Solution": (
        "Use GROUP BY with proper aliasing.\n"
        "SELECT product, SUM(revenue) AS total_revenue\n"
        "FROM sales_data\n"
        "GROUP BY product;\n"
    ),
    "Professional Solution": (
        "Add ordering and filtering for analysis.\n"
        "SELECT product, SUM(revenue) AS total_revenue\n"
        "FROM sales_data\n"
        "GROUP BY product\n"
        "ORDER BY total_revenue DESC;\n"
    )
}

# Output Formatting

def run_coach_ai():
    print("Daily Analytics Challenge")
    print("-" * 60)
    print(f"Day: {day_number}")
    print(f"Difficulty: {difficulty_level}\n")

    ai_output = generate_daily_challenges(day_number, difficulty_level)

    # Split AI output into sections for readability
    excel_section, sql_section = ai_output.split("=== SQL CHALLENGE ===")

    excel_section = excel_section.replace("=== EXCEL CHALLENGE ===", "").strip()
    sql_section = sql_section.strip()

    email_body = f"""
        <html>
        <body style="font-family: Arial, san-serif; line-height:2;">
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