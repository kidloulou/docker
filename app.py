import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)


DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'clienthub_db')

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/clients')
def get_clients():
    try:
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, email FROM clients")
                result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
