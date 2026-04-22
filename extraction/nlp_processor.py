import nltk
from textblob import TextBlob
from collections import Counter

# Download required resources (run once)
# nltk.download('punkt')
# nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


STOPWORDS = set(stopwords.words("english"))


def extract_keywords(text, top_n=5):
    """Extract top keywords based on frequency"""
    words = word_tokenize(text.lower())

    filtered_words = [
        word for word in words
        if word.isalnum() and word not in STOPWORDS
    ]

    freq = Counter(filtered_words)
    keywords = [word for word, _ in freq.most_common(top_n)]

    return keywords


def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


def categorize_text(text):
    """Simple rule-based categorization"""
    text = text.lower()

    if any(word in text for word in ["invoice", "payment", "bank"]):
        return "finance"
    elif any(word in text for word in ["error", "fail", "warning"]):
        return "system"
    elif any(word in text for word in ["order", "product", "customer"]):
        return "ecommerce"
    else:
        return "general"


def process_text(text):
    """Full NLP pipeline"""
    if not text:
        return {}

    keywords = extract_keywords(text)
    sentiment = analyze_sentiment(text)
    category = categorize_text(text)

    return {
        "keywords": keywords,
        "sentiment": sentiment,
        "category": category
    }


if __name__ == "__main__":
    sample = "Customer payment received successfully for invoice 123"
    result = process_text(sample)
    print(result)