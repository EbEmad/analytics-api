# api/events/routing.py
from fastapi import APIRouter
from .schemas import EventSchema,EventListSchema
router = APIRouter()

@router.get("/")
def read_events()->EventListSchema:
    return {"items": [{'id':1},{'id': 2},{'id': 3}]}


@router.get("/{event_id}")
def get_event(event_id:int)->EventSchema:
    return {"id":event_id}