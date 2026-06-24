import pandas as pd
from transformation.flatten_json import flatten_json


def json_to_dataframe(json_data):
    """Convert JSON to pandas DataFrame"""

    if isinstance(json_data, dict):
        json_data = [json_data]

    flattened_data = [flatten_json(item) for item in json_data]

    df = pd.DataFrame(flattened_data)

    return df


def save_to_csv(df, file_path):
    """Save DataFrame to CSV"""
    df.to_csv(file_path, index=False)
    print(f"✅ Saved table to {file_path}")


if __name__ == "__main__":
    sample = {
        "file_name": "test.pdf",
        "category": "finance",
        "keywords": ["invoice", "payment"],
        "sentiment": "positive"
    }

    df = json_to_dataframe(sample)
    print(df) 