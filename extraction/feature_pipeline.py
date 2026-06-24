from extraction.nlp_processor import process_text
from extraction.entity_extractor import extract_entities, group_entities
from extraction.ocr_extractor import extract_text
from ingestion.file_handler import process_file
import os


def run_feature_pipeline(file_path):
    """Full extraction pipeline (FIXED)"""

    print(f"Processing file: {file_path}")

    # 🔥 IMPORTANT: use correct method
    _, ext = os.path.splitext(file_path)

    if ext in [".txt", ".log"]:
        text = process_file(file_path)   # ✅ use file_handler
    else:
        text = extract_text(file_path)   # OCR for image/pdf

    if not text:
        print("No text extracted")
        return {}

    # NLP
    nlp_output = process_text(text)

    # NER
    entities = extract_entities(text)
    grouped_entities = group_entities(entities)

    return {
        "text": text,
        "keywords": nlp_output.get("keywords", []),
        "sentiment": nlp_output.get("sentiment", "neutral"),
        "category": nlp_output.get("category", "general"),
        "entities": grouped_entities
    }