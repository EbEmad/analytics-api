from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel):
    id: int



class EventListSchema(BaseModel):
    items: list[EventSchema]