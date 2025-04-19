from pydantic import BaseModel, Field
from typing import List


class EventSchema(BaseModel):
    id: int


class EventCreateSchema(BaseModel):
    path: str

class EventUpdateSchema(BaseModel):
    description: str


class EventlistSchema(BaseModel):
    results: List[EventSchema]
    count: int