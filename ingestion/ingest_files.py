import os
import shutil
from datetime import datetime

# Supported file types
SUPPORTED_EXTENSIONS = ['.pdf', '.txt', '.log', '.png', '.jpg', '.jpeg']

# Paths
RAW_DATA_PATH = "data/raw/"
INGESTED_PATH = "data/processed/"

def create_directories():
    """Create required directories if not exist"""
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    os.makedirs(INGESTED_PATH, exist_ok=True)

def is_supported_file(filename):
    """Check if file type is supported"""
    _, ext = os.path.splitext(filename)
    return ext.lower() in SUPPORTED_EXTENSIONS

def ingest_files():
    """Main ingestion function"""
    print("🚀 Starting ingestion process...")

    for file_name in os.listdir(RAW_DATA_PATH):
        file_path = os.path.join(RAW_DATA_PATH, file_name)

        if os.path.isfile(file_path) and is_supported_file(file_name):
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"{timestamp}_{file_name}"
                destination = os.path.join(INGESTED_PATH, new_name)

                # Move file
                shutil.move(file_path, destination)

                print(f"✅ Ingested: {file_name} → {new_name}")

            except Exception as e:
                print(f"❌ Error processing {file_name}: {e}")

        else:
            print(f"⚠️ Skipped unsupported file: {file_name}")

    print("✅ Ingestion completed.")

if __name__ == "__main__":
    create_directories()
    ingest_files()