from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Model(Base):
    __tablename__ = "models"
    __table_args__ = {'schema': 'project_workspace'}

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, index=True)
    file_path = Column(String, nullable=False)
    # user_id = Column(Integer, nullable=True)
    
