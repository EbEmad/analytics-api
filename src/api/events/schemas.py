from pydantic import BaseModel, Field
from typing import List


class EventSchema(BaseModel):
    id: int


class EventlistSchema(BaseModel):
    result: list[EventSchema]
    count: int