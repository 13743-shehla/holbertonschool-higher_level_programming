#!/usr/bin/python3
"""Script to initialize the SQLite database with seed data."""
import sqlite3


def create_database():
    """Create products.db and populate the Products table."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data if any to avoid duplication during testing
    cursor.execute('DELETE FROM Products')
    
    # Insert seed data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
