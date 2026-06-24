from extraction.ocr_extractor import extract_text_from_image
from extraction.nlp_processor import process_text

def test_extraction():
    """Test OCR + NLP pipeline"""
    print("Running extraction test...")

    # Use a sample image with text
    image_path = "data/sample/test.png"

    # OCR
    text = extract_text_from_image(image_path)

    print("Extracted Text:", text)

    # NLP
    features = process_text(text)

    print("NLP Output:", features)

    assert text is not None
    assert isinstance(features, dict)

    print("✅ Extraction test passed")


if __name__ == "__main__":
    test_extraction() 