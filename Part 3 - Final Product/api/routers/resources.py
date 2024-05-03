from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import resources as controller
from ..schemas import resources as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Resources'],
    prefix="/resources"
)


@router.post("/", response_model=schema.Resource)
def create_resource(request: schema.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create_resource(db=db, request=request)


@router.get("/", response_model=list[schema.Resource])
def read_all_resources(db: Session = Depends(get_db)):
    return controller.read_all_resources(db)


@router.get("/{resource_id}", response_model=schema.Resource)
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    return controller.read_one_resource(db, resource_id=resource_id)


@router.put("/{resource_id}", response_model=schema.Resource)
def update_resource(resource_id: int, request: schema.ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update_resource(db=db, request=request, resource_id=resource_id)


@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return controller.delete_resource(db=db, resource_id=resource_id)