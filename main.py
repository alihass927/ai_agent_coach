# Difficulty Automation

def get_difficulty_level(day_number):
    if day_number <= 20:
        return "Beginner"
    elif day_number <=50:
        return "Intermediate"
    else:
        return "Professional"
    
# Daily Challenge Configuration

day_number = 55
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

    print(excel_challenge)
    for level, solution in excel_solutions.items():
        print(f"{level}:\n{solution}")

    print("\n" + "-" * 40 + "\n")

    print(sql_challenge)
    for level, solution in sql_solutions.items():
        print(f"{level}:\n{solution}")
run_coach_ai()