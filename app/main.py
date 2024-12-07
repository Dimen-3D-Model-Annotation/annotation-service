from fastapi import FastAPI
from app.api.routes.models import router as model_router
from app.api.routes.annotations import router as annotation_router
from app.api.routes.scenes import router as scene_router

app = FastAPI()

# Include API routes
app.include_router(model_router, prefix="/models", tags=["models"])
app.include_router(annotation_router, prefix="/annotations", tags=["annotations"])
app.include_router(scene_router, prefix="/scenes", tags=["scenes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
