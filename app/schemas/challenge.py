from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class ChallengeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    slug: str
    title: str
    summary: str | None
    difficulty: str
    tags: list[str]
    is_premium: bool
    challenge_type: str | None
    ai_category: str | None
    created_at: datetime