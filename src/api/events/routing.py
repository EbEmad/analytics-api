# api/events/routing.py
from fastapi import APIRouter,Depends
import os
from api.db.session import get_session
from sqlmodel import Session,select
from .models import EventModel,EventListSchema,EventCreateSchema,EventUpdateSchema
router = APIRouter()

@router.post("/",response_model=EventModel)
def create_event(payload:EventCreateSchema,session:Session=Depends(get_session)):
    data=payload.model_dump()
    print(f"data:{data}")
    obj=EventModel.model_validate(data)
    print(f"obj:{obj}")
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
@router.get("/",response_model=EventListSchema)
def read_events(session:Session=Depends(get_session)):
    # a bunch of items in a table
    #query="select * from eventmodel"
    query=select(EventModel).order_by(EventModel.id.asc()).limit(10)
    result=session.exec(query).all()
    print(os.environ.get("DATABASE_URL"))
    return {"items": result}


# @router.post("/")
# def read_event(payload:EventCreateSchema)->EventSchema:
#     print(payload.page)
#     return {
#         "id": 123,
#         "page":payload.page
#         }



@router.get("/{event_id}")
def get_event(event_id:int)->EventModel:
    return {"id":event_id}



@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema)->EventModel:
    data=payload.model_dump()
    return {"id":event_id,**data}


# @router.delete("/{event_id}")
# def update_event(event_id:int,payload:dict={})->EventModel:
#     return {"id":event_id}