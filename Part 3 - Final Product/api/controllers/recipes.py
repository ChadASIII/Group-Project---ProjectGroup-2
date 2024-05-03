from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import recipes as model
from sqlalchemy.exc import SQLAlchemyError

def create_recipe(db: Session, request):
    new_item = model.Recipe(
        resource_id=request.resource_id,
        sandwich_id=request.sandwich_id,
        amount=request.amount
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all_recipes(db: Session):
    try:
        result = db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one_recipe(db: Session, recipe_id):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update_recipe(db: Session, recipe_id, request):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete_recipe(db: Session, recipe_id):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
