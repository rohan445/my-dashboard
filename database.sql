CREATE TABLE Sectors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Regions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Pestle (
    id SERIAL PRIMARY KEY,
    category VARCHAR(100) UNIQUE
);

CREATE TABLE Events (
    id SERIAL PRIMARY KEY,
    insight TEXT,
    url TEXT,
    title TEXT,
    added TIMESTAMP,
    published TIMESTAMP,
    start_year INT,
    end_year INT,
    intensity INT,
    relevance INT,
    impact INT,
    likelihood INT,
    sector_id INT REFERENCES Sectors(id),
    topic_id INT REFERENCES Topics(id),
    country_id INT REFERENCES Countries(id),
    region_id INT REFERENCES Regions(id),
    source_id INT REFERENCES Sources(id),
    pestle_id INT REFERENCES Pestle(id)
);
