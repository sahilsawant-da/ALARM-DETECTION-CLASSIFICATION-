from sqlalchemy.orm import Session
from . import models, schemas

def create_alarm(db: Session, alarm: schemas.AlarmCreate):
    db_alarm = models.Alarm(**alarm.model_dump())
    db.add(db_alarm)
    db.commit()
    db.refresh(db_alarm)
    return db_alarm

def get_alarm(db: Session, alarm_id: int):
    return db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()

def get_alarms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Alarm).offset(skip).limit(limit).all()

def update_alarm(db: Session, alarm_id: int, alarm: schemas.AlarmCreate):
    db_alarm = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    if db_alarm:
        for key, value in alarm.model_dump().items():
            setattr(db_alarm, key, value)
        db.commit()
        db.refresh(db_alarm)
    return db_alarm

def delete_alarm(db: Session, alarm_id: int):
    db_alarm = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    if db_alarm:
        db.delete(db_alarm)
        db.commit()
    return db_alarm