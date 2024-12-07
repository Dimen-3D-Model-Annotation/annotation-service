from pydantic import BaseModel
from typing import Dict

class Position(BaseModel):
    x: float
    y: float
    z: float


class Normal(BaseModel):
    x: float
    y: float
    z: float


class AnnotationCreate(BaseModel):
    model_id: int
    position: Dict[str, float]
    annotation_text: str
    normal: Dict[str, float]
    user_id: int
    scene_id: int
    annotation_type: str
    user_role: str
    username: str

    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
        
class AnnotationUpdate(BaseModel):
    annotation_text: str
    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
    
        
class AnnotationResponse(BaseModel):
    id: int
    model_id: int
    position: Dict[str, float]
    annotation_text: str
    normal: Dict[str, float]
    user_id: int
    scene_id: int
    annotation_type: str
    user_role: str
    username: str

    
    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
