from pathlib import Path

from pydantic import BaseModel, field_validator

from iliad_network.config import paths


class PoemText(BaseModel):
    content: str

    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Poem content cannot be empty.")
        if len(value) < 10:  # Example: Ensure the text has at least 10 characters
            raise ValueError("Poem content is too short.")
        return value


class LocalReader:
    def __init__(self, local_path: Path = paths.DATA_PATH / "the-iliad-poem.txt"):
        self.local_path = local_path

    def run(self) -> PoemText:
        with open(self.local_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        clean_text = "".join(lines).strip()
        return PoemText(content=clean_text)
