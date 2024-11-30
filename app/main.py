from fastapi import FastAPI
from app.api.routes.models import router

app = FastAPI()

# Include API routes
app.include_router(router, prefix="/models", tags=["models"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
