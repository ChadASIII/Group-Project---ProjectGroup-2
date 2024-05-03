from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=["Customers"],
    prefix="/customers"
)


@router.post("/", response_model=schema.Customer)
def create_customer(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Customer])
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all_customers(db)


@router.get("/{customer_email}", response_model=schema.Customer)
def read_one_customer(customer_email: str, db: Session = Depends(get_db)):
    return controller.read_one_customer(db, customer_email=customer_email)


@router.put("/{customer_email}", response_model=schema.Customer)
def update_customer(customer_email: str, request: schema.Customer, db: Session = Depends(get_db)):
    return controller.update_customer(db=db, request=request, customer_email=customer_email)


@router.delete("/{customer_email}")
def delete_customer(customer_email: str, db: Session = Depends(get_db)):
    return controller.delete_customer(db=db, customer_email=customer_email)