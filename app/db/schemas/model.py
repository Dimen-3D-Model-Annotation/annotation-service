from pydantic import BaseModel

class ModelCreate(BaseModel):
    model_name: str
    file_path: str

    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
class ModelResponse(BaseModel):
    model_name: str
    file_path: str
    
    class Config:
        protected_namespaces = ()  # Disable namespace protection
        from_attributes = True
        
