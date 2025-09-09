from pydantic import BaseModel,Field
from typing import List,Optional
from sqlmodel import SQLModel,Field
from datetime import datetime,timezone
from zoneinfo import ZoneInfo

def get_date():
    datetime.now(ZoneInfo("Africa/Cairo"))
class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str]=Field(default="")


class EventUpdateSchema(SQLModel):
    description: str


class EventModel(SQLModel,table=True):
    id: Optional[int]=Field(default=None,primary_key=True)
    page:Optional[str]=""
    description: Optional[str]=""
    created_at: datetime=Field(
        default_factory=get_date,
        sa_type=SQLModel.DateTime(timezone=True),
    )



class EventListSchema(SQLModel):
    items: list[EventModel]