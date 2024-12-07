from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.annotation import Annotation
from app.db.schemas.annotation import AnnotationCreate
from app.db.schemas.annotation import AnnotationUpdate
from app.db.session import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError


async def create_annotation_in_db(annotation_data: AnnotationCreate, db: AsyncSession = Depends(get_db)):
    
    new_annotation = Annotation(
        model_id=annotation_data.model_id,
        user_id=annotation_data.user_id,
        position=annotation_data.position,  # Already a dictionary
        normal=annotation_data.normal,      # Already a dictionary
        annotation_text=annotation_data.annotation_text,
        scene_id=annotation_data.scene_id,
        annotation_type=annotation_data.annotation_type,
        user_role=annotation_data.user_role,
        username=annotation_data.username
    )
    
    try:
        # Add the new model to the session
        db.add(new_annotation)
        # Commit the transaction to the database
        await db.commit()
        # Refresh the instance to get the ID from the database
        await db.refresh(new_annotation)
        
        # annotation_data = {
        #     "id": new_annotation.id,
        #     "model_id": new_annotation.model_id,
        #     "user_id": new_annotation.user_id,
        #     "position": new_annotation.position,
        #     "normal": new_annotation.normal,
        #     "annotation_text": new_annotation.annotation_text,
        # }
        # print(f"Annotation Data: {annotation_data}")
        
        return new_annotation
    
    except SQLAlchemyError as e:
        await db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


# async def get_annotation_from_db(annotation_id: int, db: AsyncSession = Depends(get_db)):
#     try:
#         # Query the database for the model with the specified ID
#         annotation = db.query(Annotation).filter(Annotation.id == annotation_id).one()
#         return annotation
#     except NoResultFound:
#         from fastapi import HTTPException
#         raise HTTPException(status_code=404, detail=f"Annotation with ID {annotation_id} not found.")



async def get_annotations_by_model_id(model_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Annotation).where(Annotation.model_id == model_id)
    result = await db.execute(stmt)
    # Extract results from the executed statement
    return result.scalars().all()


async def get_annotations_by_scene_id(scene_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Annotation).where(Annotation.scene_id == scene_id)
    result = await db.execute(stmt)
    # Extract results from the executed statement
    return result.scalars().all()



# Delete Annotation
async def delete_annotation_from_db(annotation_id: int, db: AsyncSession = Depends(get_db)):
    try:
        # Fetch the annotation
        stmt = select(Annotation).where(Annotation.id == annotation_id)
        result = await db.execute(stmt)
        annotation = result.scalars().first()

        if annotation:
            await db.delete(annotation)
            await db.commit()
            return {"message": "Annotation deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Annotation not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Update Annotation
async def update_annotation_in_db(annotation_id: int, annotation_data: AnnotationUpdate, db: AsyncSession = Depends(get_db)):
    try:
        # Fetch the annotation
        stmt = select(Annotation).where(Annotation.id == annotation_id)
        result = await db.execute(stmt)
        annotation = result.scalars().first()

        if annotation:
            # Update fields
            annotation.annotation_text = annotation_data.annotation_text

            await db.commit()
            await db.refresh(annotation)
            return annotation
        else:
            raise HTTPException(status_code=404, detail="Annotation not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

