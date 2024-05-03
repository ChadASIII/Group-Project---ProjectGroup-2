from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_information as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.PaymentInformation(
        transaction_status=request.transaction_status,
        payment_type=request.payment_type,
        card_information=request.card_information,
        promotion_code=request.promotion_code,
        promotion_expiration=request.promotion_expiration,
        order_id=request.order_id
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all_payment_information(db: Session):
    try:
        result = db.query(model.PaymentInformation).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one_payment_information(db: Session, card_info):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_information == card_info).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update_payment_information(db: Session, card_info, request):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_information == card_info)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete_payment_information(db: Session, card_info):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_information == card_info)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)