import os
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.types import DateTime, Date, Time, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, mapped_column
# from sqlalchemy.dialects.postgresql import JSONB


# Base class
class Base(DeclarativeBase):
    pass


# table: facility info
class Facility(Base):
    __tablename__ = "facility"
    id = mapped_column(Integer, primary_key=True) # primary id
    timestamp = mapped_column(DateTime, default=func.now()) # db timestamp
    facilityName = mapped_column(String, nullable=False)
    facilityRegisterUrl = mapped_column(String, nullable=False)
    facilityId = mapped_column(String, nullable=False, index=True)
    facilityInfo = mapped_column(String, nullable=False)
    facilityUsage = mapped_column(String, nullable=False, index=True)
    facilityManager = mapped_column(String, nullable=False)
    facilityRegisterDate = mapped_column(Date, nullable=False)
    resourceInfo = mapped_column(String, nullable=False)
    refreshDateTime = mapped_column(DateTime, nullable=False) # last refresh datetime


# table: resource info
class Resource(Base):
    __tablename__ = "resource"
    id = mapped_column(Integer, primary_key=True) # primary id
    timestamp = mapped_column(DateTime, default=func.now()) # db timestamp
    resourceId = mapped_column(String, nullable=False)
    resourceName = mapped_column(String, nullable=False)
    resourceLocation = mapped_column(String, nullable=True) # nullable
    resourceBldg = mapped_column(String, nullable=True)     # nullable
    resourceFloor = mapped_column(String, nullable=True)    # nullable
    resourceRoom = mapped_column(String, nullable=True)     # nullable
    resourceCapacity = mapped_column(String, nullable=True) # nullable
    facilityId = mapped_column(String, nullable=False)


# table: user info
class User(Base):
    __tablename__ = "user"
    email = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    phone = mapped_column(String, nullable=True)
    refreshDateTime = mapped_column(DateTime, nullable=False) # last refresh datetime


# table: reservation history for each user
class UserReservation(Base):
    __tablename__ = "userreservation"
    id = mapped_column(Integer, primary_key=True)
    reserverEmail = mapped_column(String, nullable=False)
    reservationOrder = mapped_column(String, nullable=False)
    facilityId = mapped_column(String, nullable=False)
    reservationId = mapped_column(String, nullable=False)
    facilityName = mapped_column(String, nullable=False)
    resourceName = mapped_column(String, nullable=True) # nullable (신규회원추첨)
    checkinDate = mapped_column(Date, nullable=False)
    checkinTime = mapped_column(Time, nullable=True)    # nullable (신규회원추첨)
    checkoutDate = mapped_column(Date, nullable=False)
    checkoutTime = mapped_column(Time, nullable=True)   # nullable (신규회원추첨)
    bookDate = mapped_column(Date, nullable=False)
    bookTime = mapped_column(Time, nullable=False)
    cancelDeadlineDate = mapped_column(Date, nullable=False)
    cancelDeadlineTime = mapped_column(Time, nullable=False)
    reservationStatus = mapped_column(String, nullable=False) # 배정 | 종료_미배정 | 취소_사용자취소 등등



# table: current reservation for each facility
class Reservation(Base):
    __tablename__ = "reservation"
    id = mapped_column(Integer, primary_key=True)
    reservationId = mapped_column(String, nullable=False)
    facilityId = mapped_column(String, nullable=False)
    startDateTime = mapped_column(DateTime, nullable=False)
    endDateTime = mapped_column(DateTime, nullable=False)
    isReserved = mapped_column(Boolean, nullable=False)
    resourceId = mapped_column(String, nullable=False)
    resourceName = mapped_column(String, nullable=False)
    reserverName = mapped_column(String, nullable=False)


# get DB url from environmant variables
POSTGRES_DB_URL= os.environ["POSTGRES_DB_URL"]

# create db connection
engine = create_engine(POSTGRES_DB_URL, echo=True)

# create schema (using table metadata and engine)
Base.metadata.create_all(engine)