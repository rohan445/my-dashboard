import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('events.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pestle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    insight TEXT,
    url TEXT,
    title TEXT,
    added TEXT,
    published TEXT,
    start_year INTEGER,
    end_year INTEGER,
    intensity INTEGER,
    relevance INTEGER,
    impact INTEGER,
    likelihood INTEGER,
    sector_id INTEGER,
    topic_id INTEGER,
    country_id INTEGER,
    region_id INTEGER,
    source_id INTEGER,
    pestle_id INTEGER,
    FOREIGN KEY(sector_id) REFERENCES Sectors(id),
    FOREIGN KEY(topic_id) REFERENCES Topics(id),
    FOREIGN KEY(country_id) REFERENCES Countries(id),
    FOREIGN KEY(region_id) REFERENCES Regions(id),
    FOREIGN KEY(source_id) REFERENCES Sources(id),
    FOREIGN KEY(pestle_id) REFERENCES Pestle(id)
);
''')

print("Database and tables created successfully.")
conn.commit()
conn.close()
