from preprocessing.preprocess_pipeline import preprocess_text

def test_preprocessing():
    """Test preprocessing pipeline"""
    print("Running preprocessing test...")

    sample_text = "Hello!!! Visit https://test.com NOW!!! Contact me at test@email.com"

    processed = preprocess_text(sample_text)

    print("Processed Text:", processed)

    assert processed is not None
    assert len(processed) > 0

    print("✅ Preprocessing test passed")


if __name__ == "__main__":
    test_preprocessing()