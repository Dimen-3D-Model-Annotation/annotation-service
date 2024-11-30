from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.model import Model
from app.db.schemas.model import ModelCreate
from app.db.session import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError

async def create_model_in_db(model: ModelCreate, db: AsyncSession = Depends(get_db)):
    new_model = Model(model_name=model.model_name, file_path=model.file_path)
    
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



# async def get_model_from_db(model_id: int, db: AsyncSession = Depends(get_db)):
#     result = await db.execute(select(Model.file_path).where(Model.id == model_id))
    
#     file_path = result.scalar()
#     if not file_path:
#         return {"error": "Model not found"}
#     return {"file_path": file_path}
