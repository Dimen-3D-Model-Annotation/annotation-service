from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.db.base import Base

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, future=True, echo=True)

async_session = sessionmaker(
    bind=engine, autocommit=False, autoflush=False, class_=AsyncSession
)


async def create_tables_if_not_exists():
    async with engine.begin() as conn:
        # Use run_sync to inspect on a sync connection
        await conn.run_sync(check_and_create_tables)


def check_and_create_tables(conn):
    inspector = inspect(conn)
    # Check if the tables exist using the inspector
    if not inspector.has_table('models'):
        Base.metadata.create_all(conn)  # Create the table if it doesn't exist
    if not inspector.has_table('annotations'):
        Base.metadata.create_all(conn)
    if not inspector.has_table('scenes'):
        Base.metadata.create_all(conn)


async def get_db():
    async with async_session() as session:
        # Ensure tables are created if they don't exist
        await create_tables_if_not_exists()
        yield session
        
