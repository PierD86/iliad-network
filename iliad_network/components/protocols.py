from typing import Protocol

from iliad_network.components.data_models import PoemText


class Reader(Protocol):
    def run(self) -> PoemText:
        pass


class PreProcessor(Protocol):
    def clean_text(self, text: str) -> tuple[list[str], list[str]]:
        pass

    def extract_characters(self, text: str) -> list[str]:
        pass


class Analyzer(Protocol):
    def analyze(self, sentences: list[str], character: str) -> list[tuple[str, float]]:
        pass
