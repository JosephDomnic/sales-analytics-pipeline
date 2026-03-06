import sqlite3
import pandas as pd
import requests

# ============================================================
# CONFIGURATION - Add your API key here
# Get a free Gemini key from: https://aistudio.google.com
# Get an Anthropic key from: https://console.anthropic.com
# ============================================================

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY_HERE"

# Set this to "gemini" or "anthropic"
AI_PROVIDER = "gemini"

# ============================================================

conn = sqlite3.connect('data/sales.db')

def get_schema():
    return """
    Table: sales
    Columns: order_date, region, category, sub_category,
             sales, profit, quantity, discount
    """

def run_query(sql):
    try:
        sql = sql.replace("```sql", "").replace("```", "").strip()
        result = pd.read_sql(sql, conn)
        return result.to_string()
    except Exception as e:
        return f"Query error: {e}"

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={GEMINI_API_KEY}"
    response = requests.post(url, json={
        "contents": [{"parts": [{"text": prompt}]}]
    })
    data = response.json()
    if "candidates" not in data:
        return f"Gemini error: {data.get('error', {}).get('message', 'Unknown error')}"
    return data["candidates"][0]["content"]["parts"][0]["text"]

def ask_anthropic(prompt):
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    if "content" not in data:
        return f"Anthropic error: {data.get('error', {}).get('message', 'Unknown error')}"
    return data["content"][0]["text"]

def ask_ai(prompt):
    if AI_PROVIDER == "gemini":
        return ask_gemini(prompt)
    else:
        return ask_anthropic(prompt)

def ask_agent(question):
    # Step 1: Generate SQL
    sql = ask_ai(f"""You are a data analyst. You have access to this database:
{get_schema()}

The user asks: {question}

Write ONE SQL query to answer this. Reply with ONLY the SQL query, nothing else.""")

    print(f"\nGenerated SQL:\n{sql}")

    # Step 2: Run the query
    data = run_query(sql)

    # Step 3: Get business insight
    answer = ask_ai(f"""The user asked: {question}
SQL run: {sql}
Results: {data}

Give a clear, concise business insight answer in 2-3 sentences.""")

    print(f"\nAgent: {answer}\n")

# ============================================================
print("Sales Analytics Agent")
print(f"Using: {AI_PROVIDER.upper()} API")
print("Type 'quit' to exit\n")

while True:
    question = input("You: ")
    if question.lower() == 'quit':
        break
    ask_agent(question)