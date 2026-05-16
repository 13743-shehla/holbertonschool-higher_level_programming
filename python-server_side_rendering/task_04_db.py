#!/usr/bin/python3
"""
Flask application that handles data rendering from JSON, CSV, and SQLite 
data sources dynamically with comprehensive error handling.
"""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read data from products.json."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    """Read data from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products


def read_sql(product_id=None):
    """
    Read data from SQLite database.
    Returns a tuple: (list_of_products, error_message)
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Configure connection to return rows as dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            rows = cursor.fetchall()
            if not rows:
                return None, "Product not found"
        else:
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()

        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
        return products, None

    except sqlite3.Error as e:
        # Handle database-related errors gracefully
        return None, f"Database error: {str(e)}"


@app.route('/products')
def products():
    """Route to view products from multiple data sources."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Edge Case 1: Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Handle SQL source separately due to distinct database connection workflow
    if source == 'sql':
        target_id = None
        if product_id:
            try:
                target_id = int(product_id)
            except ValueError:
                return render_template('product_display.html', error="Product not found")

        data, db_error = read_sql(target_id)
        if db_error:
            return render_template('product_display.html', error=db_error)
        return render_template('product_display.html', products=data)

    # Handle file-based sources (JSON / CSV)
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # Filter file data if id is provided
    if product_id:
        try:
            target_id = int(product_id)
            data = [p for p in data if p['id'] == target_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
