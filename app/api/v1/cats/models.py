from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database.base import Base


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    kittens = relationship("Kitten", back_populates="breed")


class Kitten(Base):
    __tablename__ = "kittens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age_months = Column(Integer)
    color = Column(String)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey("breeds.id"))
    breed = relationship("Breed", back_populates="kittens")
