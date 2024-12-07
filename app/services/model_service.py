from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.model import Model
from app.db.schemas.model import ModelCreate
from app.db.session import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError


async def create_model_in_db(model: ModelCreate, db: AsyncSession = Depends(get_db)):
    new_model = Model(model_name=model.model_name, file_path=model.file_path, scene_id=model.scene_id)
    try:
        # Add the new model to the session
        db.add(new_model)
        # Commit the transaction to the database
        await db.commit()
        # Refresh the instance to get the ID from the database
        await db.refresh(new_model)
        return new_model
    except SQLAlchemyError as e:
        # If something goes wrong, handle the error and raise a 500 HTTPException
        await db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")



async def get_model_from_db(model_id: int, db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Model).where(Model.id == model_id)
        result = await db.execute(stmt)
        model = result.scalar_one_or_none()

        if model is None:
            raise HTTPException(status_code=404, detail=f"Model with ID {model_id} not found.")
        
        return model

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")



async def get_all_models_from_db(db: AsyncSession = Depends(get_db)):
    try:
        # Create the query to select all models
        stmt = select(Model)
        
        # Execute the query asynchronously
        result = await db.execute(stmt)
        
        # Fetch all results
        models = result.scalars().all()

        return models
    
    except Exception as e:
        # Handle any exceptions and return a 500 error
        raise HTTPException(status_code=500, detail="Internal server error")



async def get_models_by_scene_id(scene_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Model).where(Model.scene_id == scene_id)
    result = await db.execute(stmt)
    # Extract results from the executed statement
    return result.scalars().all()


async def delete_model_from_db(model_id: int, db: AsyncSession = Depends(get_db)):
    try:
        # Find the model by its ID
        stmt = select(Model).filter(Model.id == model_id)
        result = await db.execute(stmt)
        model = result.scalars().first()

        if not model:
            raise HTTPException(status_code=404, detail=f"Model with ID {model_id} not found.")
        
        # Delete the model
        await db.delete(model)
        await db.commit()

        return {"message": f"Model with ID {model_id} has been deleted successfully."}
    
    except Exception as e:
        # Handle any exceptions and return a 500 error
        raise HTTPException(status_code=500, detail="Internal server error")


