import re

def to_lowercase(text):
    return text.lower()


def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()


def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


def clean_text_pipeline(text):
    """Main cleaning pipeline"""
    if not text:
        return ""

    text = to_lowercase(text)
    text = remove_special_characters(text)
    text = remove_extra_spaces(text)

    return text


if __name__ == "__main__":
    sample = "Hello!!! This   is   SAMPLE text... 123"
    print(clean_text_pipeline(sample))