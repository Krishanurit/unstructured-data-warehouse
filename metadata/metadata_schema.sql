-- Metadata Table Schema

CREATE TABLE IF NOT EXISTS file_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    file_type TEXT,
    file_size INTEGER,
    file_path TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);