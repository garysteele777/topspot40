from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Load database URL (print for debugging if needed)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:your_secure_password@localhost/topspot40")

# ✅ Create Async Engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Bind engine to session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# ✅ Dependency for getting DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ✅ Import Base (ensure this is after engine setup)
from models.track import Base

# ✅ Function to initialize database tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
