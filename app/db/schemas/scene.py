from pydantic import BaseModel

class SceneCreate(BaseModel):
    scene_name: str

    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
class SceneResponse(BaseModel):
    id: int
    scene_name: str
    
    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
