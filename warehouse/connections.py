import sqlite3

DB_PATH = "warehouse/data_warehouse.db"


def get_connection():
    """Create and return database connection"""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None