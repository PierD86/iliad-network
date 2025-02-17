import spacy


class TextPreProcessor:
    def __init__(self, model_name: str = "en_core_web_sm") -> None:
        self.model_name = model_name
        if not spacy.util.is_package(model_name):
            print(f"Model '{model_name}' not installed. Download on going...")
            spacy.cli.download(model_name)
        self.nlp_model = spacy.load(model_name)

    def clean_text(self, text: str) -> tuple[list[str], list[str]]:
        # Clean up unnecessary spaces and newlines
        text = text.replace("\n", " ").strip()
        # Tokenize the text using spaCy
        doc = self.nlp_model(text)
        # Return the list of sentences and words (tokens)
        sentences = [sent.text for sent in doc.sents]
        words = [token.text for token in doc]
        return sentences, words

    def extract_characters(self, text: str) -> list[str]:
        doc = self.nlp_model(text)
        characters = set()  # Use a set to avoid duplicates
        # Extract named entities (persons) from the text
        for ent in doc.ents:
            if ent.label_ == "PERSON":  # Filter only person entities
                characters.add(ent.text)
        return list(characters)
