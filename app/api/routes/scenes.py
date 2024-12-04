from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.scene_service import create_scene_in_db
from app.services.scene_service import get_scene_from_db
from app.services.scene_service import get_all_scenes_from_db
from app.services.scene_service import delete_scene_from_db
from app.db.schemas.scene import SceneCreate, SceneResponse
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/")
async def create_scene(scene: SceneCreate, db: Session = Depends(get_db)):
    return await create_scene_in_db(db=db, scene=scene)

@router.get("/{scene_id}", response_model=SceneResponse)
async def get_scene(scene_id: int, db: Session = Depends(get_db)):
    return await get_scene_from_db(db=db, scene_id=scene_id)

@router.get("/", response_model=List[SceneResponse])
async def get_scenes(db: Session = Depends(get_db)):
    return await get_all_scenes_from_db(db=db)

@router.delete("/{scene_id}")
async def delete_scene(scene_id: int, db: Session = Depends(get_db)):
    return await delete_scene_from_db(db=db, scene_id=scene_id)