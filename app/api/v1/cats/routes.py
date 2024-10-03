from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database.connection import get_db
from app.api.v1.cats import logic, schemas


router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/kittens/", response_model=list[schemas.Kitten])
def read_kittens(db: Session = Depends(get_db)):
    return logic.get_kittens(db)


@router.get("/kittens/{kitten_id}", response_model=schemas.Kitten)
def read_kitten(kitten_id: int, db: Session = Depends(get_db)):
    return logic.get_kitten(db, kitten_id)


@router.post("/kittens/", response_model=schemas.Kitten)
def create_kitten(kitten: schemas.KittenCreate, db: Session = Depends(get_db)):
    return logic.create_kitten(db, kitten)


@router.put("/kittens/{kitten_id}", response_model=schemas.Kitten)
def update_kitten(kitten_id: int, kitten: schemas.KittenCreate, db: Session = Depends(get_db)):
    return logic.update_kitten(db, kitten_id, kitten)


@router.delete("/kittens/{kitten_id}")
def delete_kitten(kitten_id: int, db: Session = Depends(get_db)):
    return logic.delete_kitten(db, kitten_id)


@router.get("/breeds/", response_model=list[schemas.Breed])
def get_breeds(db: Session = Depends(get_db)):
    return logic.get_breeds(db)


@router.post("/breeds/", response_model=schemas.BreedCreate)
def create_breed(breed: schemas.BreedCreate, db: Session = Depends(get_db)):
    return logic.create_breed(db=db, breed=breed)


@router.delete("/breeds/{breed_id}")
def delete_breed(breed_id: int, db: Session = Depends(get_db)):
    return logic.delete_breed(db=db, breed_id=breed_id)
