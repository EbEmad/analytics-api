from pydantic import BaseModel, Field
from typing import List, Optional
from typing import List


class EventSchema(BaseModel):
    id: int
    page: Optional[str]=''
    description: Optional[str]=''


class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str]=Field(default="my description")

class EventUpdateSchema(BaseModel):
    description: str
    page: Optional[str]=''


class EventlistSchema(BaseModel):
    results: List[EventSchema]
    count: int