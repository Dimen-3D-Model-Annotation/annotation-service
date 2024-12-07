from pydantic import BaseModel

class ModelCreate(BaseModel):
    model_name: str
    scene_id: int
    file_path: str

    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
class ModelResponse(BaseModel):
    id: int
    model_name: str
    scene_id: int
    file_path: str
    
    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
