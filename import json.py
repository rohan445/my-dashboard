import json
import psycopg2

# Load JSON file
with open('jsondata.json') as file:
    data = json.load(file)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id SERIAL PRIMARY KEY,
        intensity FLOAT,
        likelihood FLOAT,
        relevance FLOAT,
        year INT,
        country TEXT,
        topics TEXT,
        region TEXT,
        city TEXT,
        end_year INT,
        sector TEXT,
        pest TEXT,
        source TEXT,
        swot TEXT
    )
""")
conn.commit()

# Insert data
for record in data:
    cursor.execute("""
        INSERT INTO data (intensity, likelihood, relevance, year, country, topics, region, city, end_year, sector, pest, source, swot)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        record.get('intensity'),
        record.get('likelihood'),
        record.get('relevance'),
        record.get('year'),
        record.get('country'),
        record.get('topics'),
        record.get('region'),
        record.get('city'),
        record.get('end_year'),
        record.get('sector'),
        record.get('pest'),
        record.get('source'),
        record.get('swot')
    ))
conn.commit()

cursor.close()
conn.close()
