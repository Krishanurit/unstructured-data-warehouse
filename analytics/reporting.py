import sqlite3
import pandas as pd
from warehouse.connections import get_connection


def fetch_data(query):
    """Execute query and return DataFrame"""
    conn = get_connection()
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        conn.close()


def generate_keyword_report():
    """Top keywords report"""
    query = """
    SELECT keyword, COUNT(*) AS frequency
    FROM fact_data
    GROUP BY keyword
    ORDER BY frequency DESC
    LIMIT 10;
    """

    df = fetch_data(query)
    print("\n📊 Top Keywords:\n", df)
    return df


def generate_sentiment_report():
    """Sentiment distribution report"""
    query = """
    SELECT sentiment, COUNT(*) AS count
    FROM fact_data
    GROUP BY sentiment;
    """

    df = fetch_data(query)
    print("\n📊 Sentiment Distribution:\n", df)
    return df


def generate_category_report():
    """Category-wise report"""
    query = """
    SELECT c.category_name, COUNT(*) AS total
    FROM fact_data f
    JOIN dim_category c ON f.category_id = c.category_id
    GROUP BY c.category_name;
    """

    df = fetch_data(query)
    print("\n📊 Category Distribution:\n", df)
    return df


def save_report(df, file_name):
    """Save report to CSV"""
    if df is not None:
        file_path = f"analytics/{file_name}"
        df.to_csv(file_path, index=False)
        print(f"✅ Report saved: {file_path}")


if __name__ == "__main__":
    k = generate_keyword_report()
    s = generate_sentiment_report()
    c = generate_category_report()

    save_report(k, "keywords_report.csv")
    save_report(s, "sentiment_report.csv")
    save_report(c, "category_report.csv")