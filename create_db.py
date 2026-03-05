import sqlite3

# create database
conn = sqlite3.connect("company.db")

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE employees(
id INTEGER,
name TEXT,
department TEXT,
salary INTEGER
)
""")

# insert data
cursor.execute("INSERT INTO employees VALUES (1,'John','IT',50000)")
cursor.execute("INSERT INTO employees VALUES (2,'Alice','HR',45000)")
cursor.execute("INSERT INTO employees VALUES (3,'Bob','Sales',55000)")
cursor.execute("INSERT INTO employees VALUES (4,'Carol','IT',60000)")

conn.commit()
conn.close()

print("Database created successfully")