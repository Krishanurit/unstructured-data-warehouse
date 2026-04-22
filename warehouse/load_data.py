from warehouse.connections import get_connection
from datetime import datetime


def insert_file(conn, file_name, file_type):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO dim_file (file_name, file_type, ingestion_time)
        VALUES (?, ?, ?)
    """, (file_name, file_type, datetime.now()))

    return cursor.lastrowid


def insert_category(conn, category_name):
    cursor = conn.cursor()

    # Check if category exists
    cursor.execute("SELECT category_id FROM dim_category WHERE category_name = ?", (category_name,))
    result = cursor.fetchone()

    if result:
        return result[0]

    cursor.execute("""
        INSERT INTO dim_category (category_name)
        VALUES (?)
    """, (category_name,))

    return cursor.lastrowid


def insert_fact(conn, file_id, category_id, keyword, sentiment):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO fact_data (file_id, category_id, keyword, sentiment)
        VALUES (?, ?, ?, ?)
    """, (file_id, category_id, keyword, sentiment))


def load_to_warehouse(file_name, file_type, extracted_data):
    """
    extracted_data example:
    {
        "category": "finance",
        "keywords": ["invoice", "payment"],
        "sentiment": "positive"
    }
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert dimension data
        file_id = insert_file(conn, file_name, file_type)
        category_id = insert_category(conn, extracted_data.get("category", "unknown"))

        # Insert fact data
        keywords = extracted_data.get("keywords", [])
        sentiment = extracted_data.get("sentiment", "neutral")

        for keyword in keywords:
            insert_fact(conn, file_id, category_id, keyword, sentiment)

        conn.commit()
        print(f"✅ Loaded into warehouse: {file_name}")

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        conn.rollback()

    finally:
        conn.close()