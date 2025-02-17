from unittest.mock import MagicMock, patch

import pytest

from iliad_network.components.analyzers import SentimentAnalyzer
from iliad_network.components.preprocessors import TextPreProcessor


@pytest.fixture
def sentiment_analyzer() -> SentimentAnalyzer:
    # Mocking the preprocessor
    preprocessor: MagicMock = MagicMock(spec=TextPreProcessor)
    return SentimentAnalyzer(preprocessor=preprocessor)


def test_build_cooccurrence_matrix(sentiment_analyzer: SentimentAnalyzer) -> None:
    sentences: list[str] = [
        "Alice and Bob are friends.",
        "Alice and Charlie are friends.",
        "Bob and Charlie have a disagreement.",
    ]

    # Mock the extract_characters method properly using patch.object
    with patch.object(
        sentiment_analyzer.preprocessor, "extract_characters"
    ) as mock_extract_characters:
        mock_extract_characters.side_effect = [
            ["Alice", "Bob"],  # First sentence: Alice and Bob
            ["Alice", "Charlie"],  # Second sentence: Alice and Charlie
            ["Bob", "Charlie"],  # Third sentence: Bob and Charlie
        ]

        # Call the method
        cooccurrence_matrix = sentiment_analyzer.build_cooccurrence_matrix(sentences)

        # Assertions
        assert not cooccurrence_matrix.empty
        assert cooccurrence_matrix.loc["Alice", "Bob"] == 1
        assert cooccurrence_matrix.loc["Bob", "Charlie"] == 1
        assert cooccurrence_matrix.loc["Alice", "Charlie"] == 1


def test_analyze_sentiment(sentiment_analyzer: SentimentAnalyzer) -> None:
    sentence: str = "I love programming in Python!"

    # Call the method
    sentiment_score: float = sentiment_analyzer.analyze_sentiment(sentence)

    # Assertion for sentiment score (it should be positive)
    assert sentiment_score > 0


def test_analyze(sentiment_analyzer: SentimentAnalyzer) -> None:
    sentences: list[str] = [
        "Alice is very happy.",
        "Bob is feeling sad.",
        "Alice loves chocolate.",
        "Charlie is excited for the weekend.",
    ]
    character: str = "Alice"

    # Use patch.object to mock the analyze_sentiment method
    with patch.object(sentiment_analyzer, "analyze_sentiment", return_value=0.5):
        # Call the method
        character_sentiments: list[tuple[str, float]] = sentiment_analyzer.analyze(
            sentences, character
        )

    # Assertions
    assert len(character_sentiments) == 2  # Should only have 2 sentences for "Alice"
    assert character_sentiments == [
        ("Alice is very happy.", 0.5),
        ("Alice loves chocolate.", 0.5),
    ]
