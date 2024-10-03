from pydantic import BaseModel


class KittenBase(BaseModel):
    name: str
    age_months: int
    color: str
    description: str
    breed_id: int


class KittenCreate(KittenBase):
    pass


class Kitten(KittenBase):
    id: int

    class Config:
        orm_mode = True


class BreedBase(BaseModel):
    name: str


class Breed(BreedBase):
    id: int

    class Config:
        orm_mode = True


class BreedCreate(BreedBase):
    name: str

    class Config:
        orm_mode = True
