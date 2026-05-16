#!/usr/bin/python3
"""
Flask application that reads data from a JSON file 
and renders it dynamically using Jinja loops and conditions.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Read items from items.json and render them in items.html template.
    """
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            # Safely fetch the list of items, default to empty list if not found
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback to an empty list if file is missing or corrupted
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    # Run the application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)
