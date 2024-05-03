from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Recipes'],
    prefix="/recipes"
)


@router.post("/", response_model=schema.Recipe)
def create_recipe(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create_recipe(db=db, request=request)


@router.get("/", response_model=list[schema.Recipe])
def read_all_recipes(db: Session = Depends(get_db)):
    return controller.read_all_recipes(db)


@router.get("/{recipe_id}", response_model=schema.Recipe)
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return controller.read_one_recipe(db, recipe_id=recipe_id)


@router.put("/{recipe_id}", response_model=schema.Recipe)
def update_recipe(recipe_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    return controller.update_recipe(db=db, request=request, recipe_id=recipe_id)


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return controller.delete_recipe(db=db, recipe_id=recipe_id)