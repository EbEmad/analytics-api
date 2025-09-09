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



@router.get("/{event_id}",response_model=EventModel)
def get_event(event_id:int,session:Session=Depends(get_session))->EventModel:
    query=select(EventModel).where(EventModel.id==event_id)
    result=session.exec(query).first()
    return result



@router.put("/{event_id}",response_model=EventModel)
def update_event(event_id:int,payload:EventUpdateSchema,session:Session=Depends(get_session)):
    query=select(EventModel).where(EventModel.id==event_id)
    obj=session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404,detail="Event not found")
    data=payload.model_dump()
    for k,v in data.items():
        setattr(obj,k,v)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

# @router.delete("/{event_id}")
# def update_event(event_id:int,payload:dict={})->EventModel:
#     return {"id":event_id}