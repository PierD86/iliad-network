from typing import Protocol

from spacy import language

from iliad_network.components.data_models import PoemText


class Reader(Protocol):
    def run(self) -> PoemText:
        pass


class PreProcessor(Protocol):
    def clean_text(self, text: str) -> tuple[list[str], list[str]]:
        pass

    def extract_characters(self, text: str) -> list[str]:
        pass

    nlp_model: language


class Analyzer(Protocol):
    def analyze(self, sentences: list[str], character: str) -> list[tuple[str, float]]:
        pass

    def analyze_sentiment(self, sentence: str) -> float:
        pass

    preprocessor: PreProcessor
