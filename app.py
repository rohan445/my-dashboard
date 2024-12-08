from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )

@app.route('/api/data', methods=['GET'])
def get_data():
    filters = request.args
    query = "SELECT * FROM data WHERE TRUE"

    # Apply filters dynamically
    if 'year' in filters:
        query += f" AND year = {filters['year']}"
    if 'country' in filters:
        query += f" AND country = '{filters['country']}'"
    # Add more filters as needed...

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    # Convert to JSON-friendly format
    keys = ['id', 'intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city', 'end_year', 'sector', 'pest', 'source', 'swot']
    data = [dict(zip(keys, row)) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
