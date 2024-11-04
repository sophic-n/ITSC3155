# controllers/recipes.py
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import RecipeCreate, RecipeUpdate

def create(db: Session, recipe: RecipeCreate):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe: RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.update(recipe.dict(exclude_unset=True))
    db.commit()
    return db_recipe.first()

def delete(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}
