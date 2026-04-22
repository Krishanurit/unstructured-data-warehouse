import spacy

# Load spaCy model (make sure it's installed)
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """Extract named entities from text"""
    if not text:
        return []

    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities


def group_entities(entities):
    """Group entities by type"""
    grouped = {}

    for ent in entities:
        label = ent["label"]
        if label not in grouped:
            grouped[label] = []

        grouped[label].append(ent["text"])

    return grouped


if __name__ == "__main__":
    sample = "Apple Inc. is based in California and was founded by Steve Jobs."

    entities = extract_entities(sample)
    grouped = group_entities(entities)

    print("Entities:", entities)
    print("Grouped:", grouped)