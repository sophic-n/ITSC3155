# controllers/resources.py
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import ResourceCreate, ResourceUpdate

def create(db: Session, resource: ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_resource.update(resource.dict(exclude_unset=True))
    db.commit()
    return db_resource.first()

def delete(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted successfully"}
