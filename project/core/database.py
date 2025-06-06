# core/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# Motor de base de datos (engine) usando la URL de configuración
engine = create_engine(settings.database_url, echo=settings.debug)

# Session local para gestionar transacciones y sesiones con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()

# Función para obtener una sesión DB para usar en dependencias FastAPI o en servicios
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
