#!/usr/bin/python3
"""
Flask application that reads data from JSON or CSV files based on URL parameters
and applies filtering and error handling mechanisms.
"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read and return data from products.json."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    """Read and return data from products.csv as a list of dicts."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products


@app.route('/products')
def products():
    """
    Route that handles product data fetching, filtering by source and id,
    and processing application edge cases.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Edge Case 1: Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Fetch data based on source selection
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # Filter data if id parameter is provided
    if product_id:
        try:
            target_id = int(product_id)
            # Filter the list to find the matching id
            data = [p for p in data if p['id'] == target_id]
            
            # Edge Case 2: Product not found
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            # Handle invalid integer casting for id
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    # Run application on port 5000 with debug mode active
    app.run(debug=True, port=5000)
