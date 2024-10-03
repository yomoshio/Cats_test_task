from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.cats import models, schemas


def get_breeds(db: Session):
    return db.query(models.Breed).all()


def get_kittens(db: Session):
    return db.query(models.Kitten).all()


def get_kittens_by_breed(db: Session, breed_id: int):
    kittens = db.query(models.Kitten).filter(models.Kitten.breed_id == breed_id).all()
    if not kittens:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kitten not found")
    return kittens


def get_kitten(db: Session, kitten_id: int):
    kitten = db.query(models.Kitten).filter(models.Kitten.id == kitten_id).first()
    if not kitten:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kitten not found")
    return kitten


def create_kitten(db: Session, kitten: schemas.KittenCreate):
    db_kitten = models.Kitten(**kitten.dict())
    db.add(db_kitten)
    db.commit()
    db.refresh(db_kitten)
    return db_kitten


def create_breed(db: Session, breed: schemas.BreedCreate):
    db_breed = models.Breed(name=breed.name)
    db.add(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed


def delete_breed(db: Session, breed_id: int):
    db_breed = db.query(models.Breed).filter(models.Breed.id == breed_id).first()
    if not db_breed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Breed not found")
    db.delete(db_breed)
    db.commit()
    return db_breed


def update_kitten(db: Session, kitten_id: int, kitten: schemas.KittenCreate):
    db_kitten = db.query(models.Kitten).filter(models.Kitten.id == kitten_id).first()

    if not db_kitten:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kitten not found")

    # Обновляем поля котенка
    db_kitten.name = kitten.name
    db_kitten.age_months = kitten.age_months
    db_kitten.color = kitten.color
    db_kitten.description = kitten.description
    db_kitten.breed_id = kitten.breed_id
    db.commit()
    db.refresh(db_kitten)

    return db_kitten


def delete_kitten(db: Session, kitten_id: int):
    db_kitten = db.query(models.Kitten).filter(models.Kitten.id == kitten_id).first()
    if not db_kitten:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kitten not found")

    db.delete(db_kitten)
    db.commit()

    return db_kitten
