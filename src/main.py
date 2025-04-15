from typing import Union
from api.events.routing import router as events_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(events_router,prefix="/api/events")
# /api/events



@app.get("/")
def read_root():
    return {"Hello": "Eng : Ebrahim Emad Abdallah Besara"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}