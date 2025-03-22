from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .DB import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create an alarm
@app.post("/alarms/", response_model=schemas.Alarm)
def create_alarm(alarm: schemas.AlarmCreate, db: Session = Depends(get_db)):
    return crud.create_alarm(db=db, alarm=alarm)

# Get an alarm by ID
@app.get("/alarms/{alarm_id}", response_model=schemas.Alarm)
def read_alarm(alarm_id: int, db: Session = Depends(get_db)):
    db_alarm = crud.get_alarm(db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return db_alarm

# Get all alarms
@app.get("/alarms/", response_model=list[schemas.Alarm])
def read_alarms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alarms = crud.get_alarms(db, skip=skip, limit=limit)
    return alarms

# Update an alarm
@app.put("/alarms/{alarm_id}", response_model=schemas.Alarm)
def update_alarm(alarm_id: int, alarm: schemas.AlarmCreate, db: Session = Depends(get_db)):
    db_alarm = crud.update_alarm(db, alarm_id=alarm_id, alarm=alarm)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return db_alarm

# Delete an alarm
@app.delete("/alarms/{alarm_id}", response_model=schemas.Alarm)
def delete_alarm(alarm_id: int, db: Session = Depends(get_db)):
    db_alarm = crud.delete_alarm(db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return db_alarm