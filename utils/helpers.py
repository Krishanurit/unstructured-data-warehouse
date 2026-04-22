import os
import json
from datetime import datetime


def create_folder(path):
    """Create folder if it does not exist"""
    os.makedirs(path, exist_ok=True)


def get_timestamp():
    """Return current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_json(data, file_path):
    """Save dictionary as JSON file"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False


def load_json(file_path):
    """Load JSON file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None


def get_file_extension(file_path):
    """Get file extension"""
    return os.path.splitext(file_path)[1].lower()


def is_file_exists(file_path):
    """Check if file exists"""
    return os.path.exists(file_path)


def safe_read_file(file_path):
    """Safely read file content"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def safe_write_file(file_path, content):
    """Safely write content to file"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False