# controllers/sandwiches.py
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import SandwichCreate, SandwichUpdate

def create(db: Session, sandwich: SandwichCreate):
    db_sandwich = models.Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_sandwich.update(sandwich.dict(exclude_unset=True))
    db.commit()
    return db_sandwich.first()

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    db.delete(db_sandwich)
    db.commit()
    return {"message": "Sandwich deleted successfully"}
