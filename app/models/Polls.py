from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import List, Optional
from app.models.Choice import Choice


class PollCreate(BaseModel):
    """
    Poll write data model.
    """

    title: str = Field(min_length=5, max_length=50)
    options: List[str]
    expires_at: Optional[datetime] = None

    @field_validator("options")
    @classmethod
    def validate_options(cls, v: List[str]) -> List[str]:
        if len(v) < 2 or len(v) > 5:
            raise ValueError("A poll must contain between 2 and 5 choices.")

    def create_poll(self) -> "Poll":
        """
        Create a new Poll instance with auto-incrementing labesl for Choices, e.g. 1, 2, 3

        Thil will be used int the POST /polls/create endpoint.
        """

        choices = [
            Choice(description=desc, label=index + 1) for index, desc in self.options
        ]


class Poll(BaseModel):
    """
    Poll read data model, with uuid and creation date.
    """

    id: UUID = Field(default_factory=uuid4)
    options: List[Choice]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
