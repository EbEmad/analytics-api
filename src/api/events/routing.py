from fastapi import APIRouter
from .schemas import EventSchema, EventlistSchema
router=APIRouter()
# /api/events
@router.get("/")
def read_events()->EventlistSchema:
    return {
        "result":[{'id':1},{'id':2},{'id':3}],
        "count": 2003
    }

@router.get("/{event_id}")
def get_events(event_id:int)->EventSchema:
    # a sinhle row
    return {
        "id":event_id
    }