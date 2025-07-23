import httpx
import os
API_KEY = "AIzaSyBy9rxI02eVTQ2JV70-49a_2WyECcZT9Ho" #Environmental variable os.getenv()

def question_to_sql(user_question):
    prompt = f"""
You are helping generate SQL queries for an SQLite database that contains the following tables and columns:

1. AdSalesMetrics(
    date TEXT,
    item_id INTEGER,
    ad_sales REAL,
    impressions INTEGER,
    ad_spend REAL,
    clicks INTEGER,
    units_sold INTEGER
)

2. TotalSalesMetrics(
    date TEXT,
    item_id INTEGER,
    total_sales REAL,
    total_units_ordered INTEGER
)

3. Eligibility(
    eligibility_datetime_utc TEXT,
    item_id INTEGER,
    eligibility INTEGER,
    message TEXT
)

Convert the following natural language question into a valid SQLite SQL query using the column names and table names above. 
Only return the SQL query — do not include markdown, backticks, or any other formatting.

Question: {user_question}
"""

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = httpx.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        headers=headers,
        json=body
    )

    try:
        text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip()
    except Exception as e:
        return f"Error extracting SQL: {str(e)}"
