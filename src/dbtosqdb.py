import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np

# Load cleaned CSV
df = pd.read_csv("data_cleaned.csv")

# Replace NaN with empty string (MySQL does not accept NaN)
df = df.replace(np.nan, "", regex=True)

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS sales_data")
cursor.execute("USE sales_data")

# Create table with all columns as TEXT
columns = ", ".join([f"`{col}` TEXT" for col in df.columns])

create_table = f"""
CREATE TABLE IF NOT EXISTS sales_table (
{columns}
);
"""

cursor.execute(create_table)

# Insert rows safely
insert_query = "INSERT INTO sales_table VALUES (" + ",".join(["%s"] * len(df.columns)) + ")"

batch = []
count = 0

for _, row in df.iterrows():
    batch.append(tuple(row))
    count += 1
    
    if count % 500 == 0:  # insert every 500 rows
        cursor.executemany(insert_query, batch)
        connection.commit()
        batch = []

# Insert remaining rows
if batch:
    cursor.executemany(insert_query, batch)
    connection.commit()

print("✔ Data successfully inserted into MySQL!")

cursor.close()
connection.close()
