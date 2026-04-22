-- Dimension Table: File Info
CREATE TABLE IF NOT EXISTS dim_file (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT,
    file_type TEXT,
    ingestion_time TIMESTAMP
);

-- Dimension Table: Category
CREATE TABLE IF NOT EXISTS dim_category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT
);

-- Fact Table: Extracted Insights
CREATE TABLE IF NOT EXISTS fact_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    category_id INTEGER,
    keyword TEXT,
    sentiment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES dim_file(file_id),
    FOREIGN KEY (category_id) REFERENCES dim_category(category_id)
);