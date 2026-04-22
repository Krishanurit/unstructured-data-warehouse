from preprocessing.clean_text import clean_text_pipeline
from preprocessing.remove_noise import noise_removal_pipeline
from preprocessing.normalize import normalize_text_pipeline


def preprocess_text(text):
    """Full preprocessing pipeline"""
    if not text:
        return ""

    # Step 1: Clean text
    text = clean_text_pipeline(text)

    # Step 2: Remove noise
    text = noise_removal_pipeline(text)

    # Step 3: Normalize
    text = normalize_text_pipeline(text)

    return text


if __name__ == "__main__":
    sample = """
    Visit https://example.com NOW!!!
    Contact: test@email.com
    This is    SAMPLE text 123!!!
    """

    processed = preprocess_text(sample)
    print(processed)