-- Total records
SELECT COUNT(*) AS total_records FROM fact_data;

-- Top 10 keywords
SELECT keyword, COUNT(*) AS frequency
FROM fact_data
GROUP BY keyword
ORDER BY frequency DESC
LIMIT 10;

-- Sentiment distribution
SELECT sentiment, COUNT(*) AS count
FROM fact_data
GROUP BY sentiment;

-- Category-wise analysis
SELECT c.category_name, COUNT(*) AS total
FROM fact_data f
JOIN dim_category c ON f.category_id = c.category_id
GROUP BY c.category_name;

-- File-wise details
SELECT df.file_name, f.keyword, f.sentiment
FROM fact_data f
JOIN dim_file df ON f.file_id = df.file_id;