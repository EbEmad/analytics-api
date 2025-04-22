
import sqlmodel
from sqlmodel import SQLModel, create_engine
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL not set")
engine=sqlmodel.create_engine(DATABASE_URL) 



#engine=??

def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)