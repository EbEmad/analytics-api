# api/events/routing.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    return {"items": [1, 2, 3]}
