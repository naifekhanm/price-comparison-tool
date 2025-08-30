from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend JS

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE name LIKE ?", ('%' + query + '%',)
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in products])

if __name__ == '__main__':
    app.run(debug=True)
