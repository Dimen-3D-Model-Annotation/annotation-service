from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.db.base import Base

class Annotation(Base):
    __tablename__ = "annotations"
    __table_args__ = {'schema': 'project_workspace'}

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("project_workspace.models.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, nullable=False)
    position = Column(JSONB, nullable=False)  # Storing JSON for 3D position
    normal = Column(JSONB, nullable=False)    # Storing JSON for 3D normal vector
    annotation_text = Column(String, nullable=False)
    scene_id = Column(Integer, ForeignKey("project_workspace.scenes.id", ondelete="CASCADE"), nullable=False)
    annotation_type = Column(String, nullable=False)
    user_role = Column(String, nullable=False)
    username = Column(String, nullable=False)
    
    model = relationship("Model", back_populates="annotations")
    scene = relationship("Scene", back_populates="annotations")
    