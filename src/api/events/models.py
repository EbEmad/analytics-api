#from pydantic import BaseModel, Field
from typing import List, Optional
from typing import List
from sqlmodel import SQLModel, Field

class EventModel(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    #id:int
    page: Optional[str]=''
    description: Optional[str]=''


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str]=Field(default="my description")

class EventUpdateSchema(SQLModel):
    description: str
    page: Optional[str]=''


class EventlistSchema(SQLModel):
    results: List[EventModel]
    count: int