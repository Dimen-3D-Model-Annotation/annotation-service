from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.model_service import create_model_in_db
# from app.services.model_service import get_model_from_db
from app.db.schemas.model import ModelCreate, ModelResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/")
async def create_model(model: ModelCreate, db: Session = Depends(get_db)):
    return await create_model_in_db(db=db, model=model)

# @router.get("/{model_id}")
# async def get_model(model_id: int, db: Session = Depends(get_db)):
#     return await get_model_from_db(db=db, model_id=model_id)
