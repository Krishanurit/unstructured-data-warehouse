import os

from ingestion.ingest_files import ingest_files
from ingestion.file_handler import process_file

from preprocessing.preprocess_pipeline import preprocess_text

from extraction.feature_pipeline import run_feature_pipeline

from transformation.schema_mapper import map_to_schema, validate_schema

from warehouse.load_data import load_to_warehouse

from config.paths import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    EXTRACTED_DATA_PATH,
    path_config
)


def run_pipeline():
    print("Starting Pipeline...")

    # Ensure folders exist
    path_config.ensure_directories()

    # Step 1: Ingest files (raw → processed)
    ingest_files()

    # Step 2: Process each file
    for file_name in os.listdir(PROCESSED_DATA_PATH):
        file_path = os.path.join(PROCESSED_DATA_PATH, file_name)

        print(f"\nProcessing: {file_name}")

        # Step 3: Extract raw text
        raw_text = process_file(file_path)

        if not raw_text:
            print("Warning: No text extracted")
            continue

        # Step 4: Preprocess text
        clean_text = preprocess_text(raw_text)

        # Step 5: Feature extraction (OCR + NLP + NER)
        features = run_feature_pipeline(file_path)

        if not features:
            print("Warning: Feature extraction failed")
            continue

        # Step 6: Map to schema
        mapped_data = map_to_schema({
            "file_name": file_name,
            "file_type": os.path.splitext(file_name)[1],
            **features
        })

        if not validate_schema(mapped_data):
            print("Warning: Schema validation failed")
            continue

        # Step 7: Save extracted output (optional)
        os.makedirs(EXTRACTED_DATA_PATH, exist_ok=True)
        output_file = os.path.join(EXTRACTED_DATA_PATH, file_name + ".txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(clean_text)

        # Step 8: Load into Data Warehouse
        load_to_warehouse(
            file_name=mapped_data["file_name"],
            file_type=mapped_data["file_type"],
            extracted_data=mapped_data
        )

        print(f"Done: {file_name}")

    print("\nPipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()