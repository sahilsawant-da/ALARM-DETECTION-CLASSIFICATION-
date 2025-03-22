from pydantic import BaseModel
from datetime import datetime

class AlarmBase(BaseModel):
    sensor_name: str
    description: str
    is_critical: bool
    timestamp: datetime

class AlarmCreate(AlarmBase):
    pass

class Alarm(AlarmBase):
    id: int

    class Config:
        from_attributes = True