from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.model_service import create_model_in_db
from app.services.model_service import get_model_from_db
from app.services.model_service import get_all_models_from_db
from app.services.model_service import delete_model_from_db
from app.services.model_service import get_models_by_scene_id
from app.db.schemas.model import ModelCreate, ModelResponse
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/")
async def create_model(model: ModelCreate, db: Session = Depends(get_db)):
    return await create_model_in_db(db=db, model=model)

@router.get("/{model_id}", response_model=ModelResponse)
async def get_model(model_id: int, db: Session = Depends(get_db)):
    return await get_model_from_db(db=db, model_id=model_id)

@router.get("/", response_model=List[ModelResponse])
async def get_models(db: Session = Depends(get_db)):
    return await get_all_models_from_db(db=db)

@router.delete("/{model_id}")
async def delete_model(model_id: int, db: Session = Depends(get_db)):
    return await delete_model_from_db(db=db, model_id=model_id)

@router.get("/{scene_id}", response_model=List[ModelResponse])
async def get_models_by_scene(scene_id: int, db: Session = Depends(get_db)):
    return await get_models_by_scene_id(db=db, scene_id=scene_id)

