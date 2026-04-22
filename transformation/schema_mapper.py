def map_to_schema(extracted_data):
    """
    Map extracted JSON data to warehouse schema format
    """

    mapped_data = {
        "file_name": extracted_data.get("file_name", "unknown"),
        "file_type": extracted_data.get("file_type", "unknown"),
        "category": extracted_data.get("category", "general"),
        "keywords": extracted_data.get("keywords", []),
        "sentiment": extracted_data.get("sentiment", "neutral")
    }

    return mapped_data


def validate_schema(mapped_data):
    """Validate required fields"""

    required_fields = ["file_name", "category", "keywords"]

    for field in required_fields:
        if field not in mapped_data or mapped_data[field] is None:
            print(f"⚠️ Missing field: {field}")
            return False

    return True


if __name__ == "__main__":
    sample = {
        "file_name": "test.pdf",
        "category": "finance",
        "keywords": ["invoice", "payment"],
        "sentiment": "positive"
    }

    mapped = map_to_schema(sample)
    print("Mapped Data:", mapped)

    print("Valid:", validate_schema(mapped)) 