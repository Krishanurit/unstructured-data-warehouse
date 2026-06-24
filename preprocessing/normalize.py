import re

def normalize_whitespace(text):
    """Ensure consistent spacing"""
    return re.sub(r'\s+', ' ', text).strip()


def normalize_case(text):
    """Convert text to lowercase"""
    return text.lower()


def normalize_punctuation(text):
    """Standardize punctuation spacing"""
    text = re.sub(r'\s*([.,!?])\s*', r'\1 ', text)
    return text.strip()


def normalize_text_pipeline(text):
    """Main normalization pipeline"""
    if not text:
        return ""

    text = normalize_case(text)
    text = normalize_whitespace(text)
    text = normalize_punctuation(text)

    return text


if __name__ == "__main__":
    sample = "Hello   WORLD!!   This is   TEXT."
    print(normalize_text_pipeline(sample))