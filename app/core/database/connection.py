from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config.settings import settings
from app.api.v1.cats.models import Breed, Kitten
from app.core.database.base import Base
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
