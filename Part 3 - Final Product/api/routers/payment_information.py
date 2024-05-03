from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment_information as controller
from ..schemas import payment_information as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payment Information'],
    prefix="/paymentinformation"
)

@router.post("/", response_model=schema.PaymentInformation)
def create_payment_information(request: schema.PaymentInformationCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PaymentInformation])
def read_all_payment_information(db: Session = Depends(get_db)):
    return controller.read_all_payment_information(db)


@router.get("/{card_info}", response_model=schema.PaymentInformation)
def read_one_payment_information(card_info: str, db: Session = Depends(get_db)):
    return controller.read_one_payment_information(db, card_info=card_info)


@router.put("/{card_info}", response_model=schema.PaymentInformation)
def update_payment_information(card_info: str, request: schema.PaymentInformationUpdate, db: Session = Depends(get_db)):
    return controller.update_payment_information(db=db, request=request, card_info=card_info)


@router.delete("/{card_info}")
def delete_payment_information(card_info: str, db: Session = Depends(get_db)):
    return controller.delete_payment_information(db=db, card_info=card_info)