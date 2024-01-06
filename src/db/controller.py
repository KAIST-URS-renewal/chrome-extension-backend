from sqlalchemy import select
from sqlalchemy.orm import Session
from .schema import Facility, Resource, User, FacilityReservation
        

'''(1) facility Router'''

# register new facility
def db_register_facility(infos: dict, db: Session):
    for info in infos.infos:
        # usage가 없는 경우, 여러 개인 경우도 고려하기
        for usage in info.facilityUsage.split(','):
            facility = Facility(
                    facilityName = info.facilityName,
                    facilityRegisterUrl = info.facilityRegisterUrl,
                    facilityId = info.facilityId,
                    facilityInfo = info.facilityInfo,
                    facilityUsage = usage,
                    facilityManager = info.facilityManager,
                    facilityRegisterDate = info.facilityRegisterDate,
                    resourceInfo = info.resourceInfo
                )
            db.add(facility)
    db.commit()
    return

# search facilities
def db_query_facility(id: str, usage: str, info: str, db: Session):
    results = db.scalars(
        select(Facility).
        where((not id or Facility.facilityId == id),
            (not usage or Facility.facilityUsage == usage),
            (not info or Facility.facilityInfo.contains(info)))
        ).all()
    return results


'''(2) resource Router'''

# register new resource
def db_register_resource(infos: dict, db: Session):
    for info in infos.infos:
        if not info:
            continue
        resource = Resource(
            resourceId = info.resourceId,
            resourceName = info.resourceName,
            resourceLocation = info.resourceLocation,
            resourceBldg = info.resourceBldg,
            resourceFloor = info.resourceFloor,
            resourceRoom = info.resourceRoom,
            resourceCapacity = info.resourceCapacity,
            facilityId = info.facilityId
            )
        db.add(resource)
    db.commit()
    return


# search resources
def db_query_resource(rscId: str, facId: str, db: Session):
    results = db.scalars(
            select(Resource).
            where((not rscId or Resource.resourceId == rscId),
                    (not facId or Resource.facilityId == facId))
        ).all()
    return results


'''(3) user Router'''

# add new user
def db_insert_user(info: dict, db: Session):
    result = db.scalars(
            select(User).
            where(User.userEmail == info.userEmail)
        ).first()
    if (result == None):
        user = User(
            userEmail = info.userEmail,
            userName = info.userName,
            userPhone = info.userPhone
        )
        db.add(user)
        db.commit()
    return


'''(4) reservation Router (미완성)'''

# insert new data
def db_insert_data(info, db: Session):
    db.add(FacilityReservation(data=info))
    db.commit()
    return

# query data
def db_query_data(query, db: Session):
    results = db.scalars(
            select(FacilityReservation).
            where(FacilityReservation.data["tag"].astext==query.tag)
        ).all()
    return results

# delete data
def db_delete_data(query, db: Session):
    result = db.scalars(
            select(Reservation).
            where(Reservation.data["tag"].astext==query.tag)
        ).first()
    db.delete(result)
    db.commit()
    return
