from pydantic import BaseModel, field_validator


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
