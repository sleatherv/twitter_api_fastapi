from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from models import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field()
    by: User = Field(...)
