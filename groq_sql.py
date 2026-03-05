from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(query):

    prompt = f"""
Convert the following natural language query to MySQL SQL.

Table: employees
Columns:
id
name
department
salary

User Query: {query}

Return only SQL query.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()
    
    # Remove markdown code blocks if present
    if sql.startswith("```"):
        # Remove ```sql or ``` at the start
        sql = sql.split("\n", 1)[1] if "\n" in sql else sql[3:]
        # Remove ``` at the end
        if sql.endswith("```"):
            sql = sql[:-3]
    
    return sql.strip()