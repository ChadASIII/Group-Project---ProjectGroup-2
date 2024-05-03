from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Customer(
        customer_name=request.customer_name,
        customer_email=request.customer_email,
        customer_phone_number=request.customer_phone_number,
        customer_address=request.customer_address,
        customer_rating=request.customer_rating,
        customer_review=request.customer_review
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all_customers(db: Session):
    try:
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one_customer(db: Session, customer_email):
    try:
        item = db.query(model.Customer).filter(model.Customer.customer_email == customer_email).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update_customer(db: Session, customer_email, request):
    try:
        item = db.query(model.Customer).filter(model.Customer.customer_email == customer_email)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete_customer(db: Session, customer_email):
    try:
        item = db.query(model.Customer).filter(model.Customer.customer_email == customer_email)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)