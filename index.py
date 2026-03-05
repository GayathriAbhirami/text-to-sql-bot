from flask import Flask, render_template, request
from groq_sql import generate_sql
import os
import sqlite3

app = Flask(__name__)

# Initialize in-memory database for Vercel serverless
def get_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE employees(
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
    )
    """)
    cursor.execute("INSERT INTO employees VALUES (1,'John','IT',50000)")
    cursor.execute("INSERT INTO employees VALUES (2,'Alice','HR',45000)")
    cursor.execute("INSERT INTO employees VALUES (3,'Bob','Sales',55000)")
    cursor.execute("INSERT INTO employees VALUES (4,'Carol','IT',60000)")
    conn.commit()
    return conn

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    sql_query = None

    if request.method == "POST":
        question = request.form["query"]
        sql_query = generate_sql(question)
        
        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            result = [columns] + list(rows)
        except Exception as e:
            result = [["Error"],[str(e)]]
        
        conn.close()

    return render_template("index.html", result=result, sql=sql_query)

# For local development
if __name__ == "__main__":
    app.run(debug=True)
