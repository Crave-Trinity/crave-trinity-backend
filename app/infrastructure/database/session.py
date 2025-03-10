"""
SQLAlchemy session configuration.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings  # Import the settings instance

# Use the same name: settings.SQLALCHEMY_DATABASE_URI
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
