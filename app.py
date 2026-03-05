from flask import Flask, render_template, request
from db import connect_db
from groq_sql import generate_sql
import os
import sqlite3

app = Flask(__name__)

# Initialize database if it doesn't exist
def init_db():
    if not os.path.exists("company.db"):
        conn = sqlite3.connect("company.db")
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
        conn.close()
        print("Database initialized successfully")

init_db()

@app.route("/", methods=["GET","POST"])

def index():

    result = None
    sql_query = None

    if request.method == "POST":

        question = request.form["query"]

        sql_query = generate_sql(question)

        conn = connect_db()
        cursor = conn.cursor()

        try:

            cursor.execute(sql_query)

            rows = cursor.fetchall()

            columns = [i[0] for i in cursor.description]

            result = [columns] + list(rows)

        except Exception as e:

            result = [["Error"],[str(e)]]

        conn.close()

    return render_template("index.html",result=result,sql=sql_query)


if __name__ == "__main__":
    app.run(debug=True)