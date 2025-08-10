import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_requirements(text):
    """
    Extracts actions (verbs) and inputs (nouns) from a requirement sentence.
    Returns a list of (action, inputs) tuples for multiple verbs.
    """
    doc = nlp(text)
    results = []

    # Identify verbs (actions) and their related nouns (inputs)
    for token in doc:
        if token.pos_ == "VERB":  # Found an action
            action = token.lemma_.capitalize()
            # Find related nouns (direct objects, prepositional objects)
            inputs = [child.text for child in token.children if child.pos_ in ["NOUN", "PROPN"]]
            results.append((action, inputs))

    return results
