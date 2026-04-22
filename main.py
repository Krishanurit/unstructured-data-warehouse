from ingestion.ingest_files import ingest_files
from ingestion.file_handler import process_file
from preprocessing.preprocess_pipeline import preprocess_text

import os

PROCESSED_PATH = "data/processed/"
EXTRACTED_PATH = "data/extracted/"

def run_pipeline():
    print("🚀 Starting Pipeline...")

    # Step 1: Ingest files
    ingest_files()

    # Step 2: Process each file
    for file_name in os.listdir(PROCESSED_PATH):
        file_path = os.path.join(PROCESSED_PATH, file_name)

        print(f"\n📂 Processing: {file_name}")

        # Step 3: Extract raw text
        raw_text = process_file(file_path)

        if not raw_text:
            print("⚠️ No text extracted")
            continue

        # Step 4: Preprocess text
        clean_text = preprocess_text(raw_text)

        # Step 5: Save output
        output_file = os.path.join(EXTRACTED_PATH, file_name + ".txt")
        os.makedirs(EXTRACTED_PATH, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(clean_text)

        print(f"✅ Saved: {output_file}")

    print("\n🎉 Pipeline Completed!")


if __name__ == "__main__":
    run_pipeline()