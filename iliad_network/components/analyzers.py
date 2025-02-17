from collections import defaultdict

import pandas as pd
from textblob import TextBlob

from iliad_network.components.protocols import PreProcessor


class SentimentAnalyzer:
    def __init__(self, preprocessor: PreProcessor) -> None:
        self.preprocessor = preprocessor

    def build_cooccurrence_matrix(self, sentences: list[str]) -> pd.DataFrame:
        # Create a dictionary to store co-occurrences
        cooccurrence_dict: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

        # Loop over sentences
        for sentence in sentences:
            # Extract character mentions in the sentence
            mentioned_characters = set(self.preprocessor.extract_characters(sentence))

            # If multiple characters are mentioned, increment co-occurrence counts
            for char1 in mentioned_characters:
                for char2 in mentioned_characters:
                    if char1 != char2:
                        cooccurrence_dict[char1][char2] += 1

        # Convert the dictionary into a DataFrame for easy viewing
        cooccurrence_df = pd.DataFrame.from_dict(cooccurrence_dict).fillna(0)
        return cooccurrence_df

    def analyze_sentiment(self, sentence: str) -> float:
        blob = TextBlob(sentence)
        return blob.sentiment.polarity  # Returns sentiment score (-1 to 1)

    def analyze(self, sentences: list[str], character: str) -> list[tuple[str, float]]:
        # List to store sentiment scores for each character's sentence
        character_sentiments: list[tuple[str, float]] = []

        for sentence in sentences:
            # Check if the character is mentioned in the sentence
            if character in sentence:
                sentiment_score = self.analyze_sentiment(sentence)
                character_sentiments.append((sentence, sentiment_score))

        return character_sentiments
