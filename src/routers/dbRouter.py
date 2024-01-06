from fastapi import APIRouter, Depends
from src.db.session import get_db
from src.db.controller import *
from src.types.dataTypes import *


# define routers
facilityRouter = APIRouter(prefix="/facility")
resourceRouter = APIRouter(prefix="/resource")
userRouter = APIRouter(prefix="/user")
reserveRouter = APIRouter(prefix="/reserve")


'''(1) facility Router'''

# register new facility
@facilityRouter.post("", response_model=DefaultOutput)
def register_facility(infos: RegisterFacilities, db: Session = Depends(get_db)):
    db_register_facility(infos, db)
    return {"status": 200, "msg": "Insert Success."}


# search facilities
@facilityRouter.get("", response_model=List[RegisterFacility])
def search_facility(facilityId=None, facilityUsage=None, facilityInfo=None, db: Session = Depends(get_db)):
    result = db_query_facility(facilityId, facilityUsage, facilityInfo, db)
    return result


'''(2) resource Router'''

# register new resource
@resourceRouter.post("", response_model=DefaultOutput)
def register_resource(infos: RegisterResources, db: Session = Depends(get_db)):
    db_register_resource(infos, db)
    return {"status": 200, "msg": "Insert Success."}


# search resources
@resourceRouter.get("", response_model=List[RegisterResource])
def search_resource(resourceId=None, facilityId=None, db: Session = Depends(get_db)):
    result = db_query_resource(resourceId, facilityId, db)
    return result


'''(3) user Router'''

# add new user info
@userRouter.post("", response_model=DefaultOutput)
def add_user(info: AddUser, db: Session = Depends(get_db)):
    db_insert_user(info, db)
    return {"status": 200, "msg": "Insert Success."}


'''(4) reservation Router'''

# add new reservation
@reserveRouter.post("", response_model=DefaultOutput)
def add_reservation(info: RegisterFacility, db: Session = Depends(get_db)):
    db_insert_data(info, db)
    return {"status": 200, "msg": "Insert Success."}


# search reservations
@reserveRouter.get("", response_model=SearchOutput)
def search_reservation(query: SearchInput, db: Session = Depends(get_db)):
    results = db_query_data(query, db)
    return {"result": [result.data for result in results]}


# remove reservation
@reserveRouter.delete("", response_model=DefaultOutput)
def remove_reservation(query: RemoveInput, db: Session = Depends(get_db)):
    db_delete_data(query, db)
    return {"status": 200, "msg": "Delete Success."}
