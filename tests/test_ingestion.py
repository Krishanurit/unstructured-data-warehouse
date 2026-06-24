import os
from ingestion.ingest_files import ingest_files, create_directories

def test_ingestion():
    """Test ingestion process"""
    print("Running ingestion test...")

    create_directories()

    # Create a dummy file in raw folder
    test_file_path = "data/raw/test_file.txt"
    with open(test_file_path, "w") as f:
        f.write("Sample test data")

    ingest_files()

    # Check if file moved
    processed_files = os.listdir("data/processed/")
    assert len(processed_files) > 0, "Ingestion failed!"

    print("✅ Ingestion test passed")


if __name__ == "__main__":
    test_ingestion()