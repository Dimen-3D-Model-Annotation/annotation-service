from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

# Define the base class for SQLAlchemy models
Base: DeclarativeMeta = declarative_base()

# Import all models here for Alembic to recognize them
# from app.db.models.model import Model
