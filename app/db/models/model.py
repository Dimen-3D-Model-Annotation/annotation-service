from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Model(Base):
    __tablename__ = "models"
    __table_args__ = {'schema': 'project_workspace'}

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, index=True)
    scene_id = Column(Integer, ForeignKey("project_workspace.scenes.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String, nullable=False)
    # user_id = Column(Integer, nullable=True)
    
    # Relationships
    annotations = relationship("Annotation", back_populates="model", cascade="all, delete-orphan")
    scene = relationship("Scene", back_populates="models")
