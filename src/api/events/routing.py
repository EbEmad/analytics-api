from fastapi import APIRouter

router=APIRouter()
# /api/events
@router.get("/")
def read_events():
    return {
        "result":[1,2,3]
    }