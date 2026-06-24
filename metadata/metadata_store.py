import os
import sqlite3
from datetime import datetime


DB_PATH = "metadata/metadata.db"


def create_connection():
    """Create database connection"""
    return sqlite3.connect(DB_PATH)


def create_metadata_table():
    """Create metadata table if not exists"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_type TEXT,
        file_size INTEGER,
        file_path TEXT,
        ingestion_time TEXT
    )
    """)

    conn.commit()
    conn.close()


def get_file_metadata(file_path):
    """Extract metadata from file"""
    file_stats = os.stat(file_path)

    return {
        "file_name": os.path.basename(file_path),
        "file_type": os.path.splitext(file_path)[1],
        "file_size": file_stats.st_size,
        "file_path": file_path,
        "ingestion_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def insert_metadata(metadata):
    """Insert metadata into database"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO file_metadata 
    (file_name, file_type, file_size, file_path, ingestion_time)
    VALUES (?, ?, ?, ?, ?)
    """, (
        metadata["file_name"],
        metadata["file_type"],
        metadata["file_size"],
        metadata["file_path"],
        metadata["ingestion_time"]
    ))

    conn.commit()
    conn.close()


def store_file_metadata(file_path):
    """Main function to store metadata"""
    create_metadata_table()
    metadata = get_file_metadata(file_path)
    insert_metadata(metadata)
    print(f"✅ Metadata stored for: {metadata['file_name']}")


if __name__ == "__main__":
    sample_file = "data/sample/test.txt"
    if os.path.exists(sample_file):
        store_file_metadata(sample_file)
    else:
        print("Sample file not found!")