from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.annotation_service import create_annotation_in_db
# from app.services.annotation_service import get_annotation_from_db
from app.services.annotation_service import update_annotation_in_db
from app.services.annotation_service import get_annotations_by_model_id
from app.services.annotation_service import get_annotations_by_scene_id
from app.services.annotation_service import delete_annotation_from_db
from app.db.schemas.annotation import AnnotationCreate, AnnotationResponse, AnnotationUpdate
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/")
async def create_annotation(annotation: AnnotationCreate, db: AsyncSession = Depends(get_db)):
    return await create_annotation_in_db(db=db, annotation_data=annotation)

# @router.get("/{annotation_id}", response_model=AnnotationResponse)
# async def get_annotation(annotation_id: int, db: Session = Depends(get_db)):
#     return await get_annotation_from_db(db=db, annotation_id=annotation_id)

@router.get("/{model_id}", response_model=List[AnnotationResponse])
async def get_annotations(model_id: int, db: AsyncSession = Depends(get_db)):
    return await get_annotations_by_model_id(db=db, model_id=model_id)


@router.get("/{scene_id}", response_model=List[AnnotationResponse])
async def get_annotations_by_scene(scene_id: int, db: AsyncSession = Depends(get_db)):
    return await get_annotations_by_scene_id(db=db, scene_id=scene_id)

@router.delete("/{annotation_id}")
async def delete_annotation(annotation_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_annotation_from_db(db=db, annotation_id=annotation_id)

@router.put("/{annotation_id}")
async def update_annotation(annotation_id: int, annotation_data: AnnotationUpdate, db: AsyncSession = Depends(get_db)):
    return await update_annotation_in_db(db=db, annotation_data=annotation_data, annotation_id=annotation_id)
