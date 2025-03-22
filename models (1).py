from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .DB import Base

class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String, index=True)
    description = Column(String)
    is_critical = Column(Boolean, default=False)
    timestamp = Column(DateTime)