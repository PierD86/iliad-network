from unittest.mock import MagicMock

import pytest

from iliad_network.components.preprocessors import TextPreProcessor


@pytest.fixture
def text_preprocessor() -> TextPreProcessor:
    # Create a fixture for TextPreProcessor with a mocked spaCy model
    preprocessor = TextPreProcessor(model_name="en_core_web_sm")
    return preprocessor


def test_clean_text(text_preprocessor: TextPreProcessor) -> None:
    text: str = "Hello World! This is a test.  \n\nLet's clean this text!"

    # Mock the NLP model's behavior (for tokenizing and sentence splitting)
    mock_doc: MagicMock = MagicMock()

    # Mock sentences
    mock_doc.sents = [
        MagicMock(text="Hello World!"),
        MagicMock(text="This is a test."),
        MagicMock(text="Let's clean this text!"),
    ]

    # Mock the tokens (words) for each sentence
    mock_word_tokens_1: list[MagicMock] = [
        MagicMock(text="Hello"),
        MagicMock(text="World"),
    ]
    mock_word_tokens_2: list[MagicMock] = [
        MagicMock(text="This"),
        MagicMock(text="is"),
        MagicMock(text="a"),
        MagicMock(text="test"),
    ]
    mock_word_tokens_3: list[MagicMock] = [
        MagicMock(text="Let's"),
        MagicMock(text="clean"),
        MagicMock(text="this"),
        MagicMock(text="text!"),
    ]

    # Mock the __iter__ method for token iteration
    mock_doc.__iter__.return_value = mock_word_tokens_1 + mock_word_tokens_2 + mock_word_tokens_3

    # Mock NLP model to return mock_doc
    text_preprocessor.nlp_model = MagicMock(return_value=mock_doc)

    # Run the test
    sentences, words = text_preprocessor.clean_text(text)

    # Assert the sentences and words are correct
    assert sentences == ["Hello World!", "This is a test.", "Let's clean this text!"]
    assert words == [
        "Hello",
        "World",
        "This",
        "is",
        "a",
        "test",
        "Let's",
        "clean",
        "this",
        "text!",
    ]
