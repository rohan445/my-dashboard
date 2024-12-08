import json
import psycopg2
from psycopg2.extras import execute_values

# Load JSON file
with open('jsondata.json', 'r') as file:
    data = json.load(file)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password="mypass",
    host="localhost"
)
cur = conn.cursor()

# Function to insert unique values into a table and return the ID
def get_or_create(table, column, value):
    if not value:  # Skip if value is empty
        return None
    cur.execute(f"INSERT INTO {table} ({column}) VALUES (%s) ON CONFLICT ({column}) DO NOTHING RETURNING id;", (value,))
    result = cur.fetchone()
    if result:
        return result[0]
    cur.execute(f"SELECT id FROM {table} WHERE {column} = %s;", (value,))
    return cur.fetchone()[0]

# Iterate over JSON data
for entry in data:
    sector_id = get_or_create("Sectors", "name", entry.get("sector"))
    topic_id = get_or_create("Topics", "name", entry.get("topic"))
    country_id = get_or_create("Countries", "name", entry.get("country"))
    region_id = get_or_create("Regions", "name", entry.get("region"))
    source_id = get_or_create("Sources", "name", entry.get("source"))
    pestle_id = get_or_create("Pestle", "category", entry.get("pestle"))

    # Insert into Events table
    cur.execute("""
        INSERT INTO Events (
            insight, url, title, added, published, start_year, end_year,
            intensity, relevance, impact, likelihood, sector_id, topic_id,
            country_id, region_id, source_id, pestle_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        entry.get("insight"),
        entry.get("url"),
        entry.get("title"),
        entry.get("added"),
        entry.get("published"),
        entry.get("start_year"),
        entry.get("end_year"),
        entry.get("intensity"),
        entry.get("relevance"),
        entry.get("impact"),
        entry.get("likelihood"),
        sector_id,
        topic_id,
        country_id,
        region_id,
        source_id,
        pestle_id
    ))

# Commit changes
conn.commit()
cur.close()
conn.close()
print("Data successfully inserted!")
