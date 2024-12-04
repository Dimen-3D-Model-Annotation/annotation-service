from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.db.models.scene import Scene
from app.db.schemas.scene import SceneCreate
from app.db.session import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import NoResultFound


async def create_scene_in_db(scene: SceneCreate, db: AsyncSession = Depends(get_db)):
    new_scene = Scene(scene_name=scene.scene_name)
    try:
        # Add the new Scene to the session
        db.add(new_scene)
        # Commit the transaction to the database
        await db.commit()
        # Refresh the instance to get the ID from the database
        await db.refresh(new_scene)
        return new_scene
    except SQLAlchemyError as e:
        # If something goes wrong, handle the error and raise a 500 HTTPException
        await db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")



async def get_scene_from_db(scene_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Scene).where(Scene.id == scene_id)  # Create the query
    result = await db.execute(stmt)  # Execute the query
    scene = result.scalar_one_or_none()  # Fetch a single result or None if not found
    return scene
    



async def get_all_scenes_from_db(db: AsyncSession = Depends(get_db)):
    stmt = select(Scene)
    result = await db.execute(stmt)
    # Extract results from the executed statement
    return result.scalars().all()



async def delete_scene_from_db(scene_id: int, db: Session = Depends(get_db)):
    try:
        # Find the Scene by its ID
        scene = db.query(Scene).filter(scene.id == scene_id).one()

        # Delete the Scene
        db.delete(scene)
        db.commit()

        return {"message": f"Scene with ID {scene_id} has been deleted successfully."}
    except NoResultFound:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Scene with ID {scene_id} not found.")

