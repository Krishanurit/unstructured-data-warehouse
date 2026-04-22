from extraction.ocr_extractor import extract_text
from extraction.nlp_processor import process_text
from extraction.entity_extractor import extract_entities, group_entities


def run_feature_pipeline(file_path):
    """Full extraction pipeline"""

    print(f"📂 Processing file: {file_path}")

    # Step 1: Extract text (OCR / PDF)
    text = extract_text(file_path)

    if not text:
        print("⚠️ No text extracted")
        return {}

    # Step 2: NLP processing
    nlp_output = process_text(text)

    # Step 3: Named Entity Recognition
    entities = extract_entities(text)
    grouped_entities = group_entities(entities)

    # Combine all outputs
    final_output = {
        "file_name": file_path,
        "text": text,
        "keywords": nlp_output.get("keywords", []),
        "sentiment": nlp_output.get("sentiment", "neutral"),
        "category": nlp_output.get("category", "general"),
        "entities": grouped_entities
    }

    return final_output


if __name__ == "__main__":
    sample = "data/sample/test.png"

    result = run_feature_pipeline(sample)

    print("Final Output:\n", result)