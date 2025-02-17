from pathlib import Path

from iliad_network.components.data_models import PoemText
from iliad_network.config import paths


class LocalReader:
    def __init__(self, local_path: Path = paths.DATA_PATH / "the-iliad-poem.txt"):
        self.local_path = local_path

    def run(self) -> PoemText:
        with open(self.local_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        clean_text = "".join(lines).strip()
        return PoemText(content=clean_text)
