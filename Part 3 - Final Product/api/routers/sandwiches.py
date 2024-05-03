from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import sandwiches as controller
from ..schemas import sandwiches as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Sandwiches'],
    prefix="/sandwiches"
)


@router.post("/", response_model=schema.Sandwich)
def create_sandwich(request: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create_sandwich(db=db, request=request)


@router.get("/", response_model=list[schema.Sandwich])
def read_all_sandwiches(db: Session = Depends(get_db)):
    return controller.read_all_sandwiches(db)


@router.get("/{sandwich_id}", response_model=schema.Sandwich)
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.read_one_sandwich(db, sandwich_id=sandwich_id)


@router.put("/{sandwich_id}", response_model=schema.Sandwich)
def update_sandwich(sandwich_id: int, request: schema.SandwichUpdate, db: Session = Depends(get_db)):
    return controller.update_sandwich(db=db, request=request, sandwich_id=sandwich_id)


@router.delete("/{sandwich_id}")
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.delete_sandwich(db=db, sandwich_id=sandwich_id)