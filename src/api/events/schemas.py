from pydantic import BaseModel,Field
from typing import List,Optional
from sqlmodel import SQLModel,Field


class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str]=Field(default="")


class EventUpdateSchema(BaseModel):
    description: str


class EventSchema(BaseModel):
    id: int
    page:Optional[str]=""
    description: Optional[str]=""



class EventListSchema(BaseModel):
    items: list[EventSchema]