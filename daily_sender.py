import json
from datetime import date
from email_sender import send_email

with open("challenges.json", "r", encoding="utf-8") as f:
    data = json.load(f)

day_number = date.today().timetuple().tm_yday

keys = list(data.keys())
day_key = keys[(day_number - 1) % len(keys)]

challenge = data[day_key]

content = challenge["content"]
difficulty = challenge["difficulty"]

email_body = f"""
<html>
<body style="font-family: Arial, sans-serif;">
<h2>Daily Analytics Challenge</h2>
<p><b>Day:</b> {day_key}<br>
<b>Difficulty:</b> {difficulty}</p>
<pre>{content}</pre>
</body>
</html>
"""

send_email(
    subject=f"Daily Analytics Challenge - Day {day_key}",
    body=email_body,
    to_email="ali.hass927@gmail.com"
)

print("Email sent.")