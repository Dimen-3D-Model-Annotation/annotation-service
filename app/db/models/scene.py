from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Scene(Base):
    __tablename__ = "scenes"
    __table_args__ = {'schema': 'project_workspace'}

    id = Column(Integer, primary_key=True, index=True)
    scene_name = Column(String, index=True, nullable=False)
    
    # Relationships
    models = relationship("Model", back_populates="scene", cascade="all, delete-orphan")
    annotations = relationship("Annotation", back_populates="scene", cascade="all, delete-orphan")
    