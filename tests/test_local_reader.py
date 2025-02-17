from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from iliad_network.components.data_models import PoemText
from iliad_network.components.protocols import Reader
from iliad_network.components.readers import LocalReader

# Mocking a sample poem text
MOCK_POEM_TEXT: str = """
Sing, O goddess, the anger of Achilles son of Peleus, that brought
countless ills upon the Achaeans. Many a brave soul did it send hurrying
down to Hades, and many a hero did it yield a prey to dogs and vultures,
for so were the counsels of Jove fulfilled from the day on which the son of
Atreus, king of men, and great Achilles, first fell out with one another.
"""


# Test case for LocalReader
@pytest.fixture
def local_reader() -> Reader:
    # Creating an instance of LocalReader for testing
    return LocalReader(local_path=Path("test_poem.txt"))


def test_run_read_poem(local_reader: Reader) -> None:
    # Test that the poem text is correctly read and cleaned
    with patch("builtins.open", mock_open(read_data=MOCK_POEM_TEXT)):
        poem_text: PoemText = local_reader.run()

    assert poem_text.content == MOCK_POEM_TEXT.strip()


def test_run_file_not_found(local_reader: Reader) -> None:
    # Test for file not found error
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            local_reader.run()
