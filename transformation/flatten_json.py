def flatten_json(nested_json, parent_key='', sep='_'):
    """Flatten nested JSON into a single level dictionary"""
    items = []

    for key, value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for i, item in enumerate(value):
                items.extend(
                    flatten_json({f"{new_key}_{i}": item}).items()
                )
        else:
            items.append((new_key, value))

    return dict(items)


if __name__ == "__main__":
    sample = {
        "file": "test.pdf",
        "data": {
            "category": "finance",
            "keywords": ["invoice", "payment"]
        }
    }

    print(flatten_json(sample))