import re

def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)


def remove_emails(text):
    return re.sub(r'\S+@\S+', '', text)


def remove_numbers(text):
    return re.sub(r'\d+', '', text)


def remove_stopwords(text):
    """Basic stopword removal (can improve with NLP later)"""
    stopwords = {'the', 'is', 'in', 'and', 'to', 'of', 'a', 'for', 'on'}
    words = text.split()
    filtered = [word for word in words if word not in stopwords]
    return " ".join(filtered)


def noise_removal_pipeline(text):
    """Main noise removal pipeline"""
    if not text:
        return ""

    text = remove_urls(text)
    text = remove_emails(text)
    text = remove_numbers(text)
    text = remove_stopwords(text)

    return text


if __name__ == "__main__":
    sample = "Contact me at test@gmail.com or visit https://example.com"
    print(noise_removal_pipeline(sample))