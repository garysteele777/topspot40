from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.track import Track
from database import get_db
from schemas.track import TrackCreate, TrackResponse

router = APIRouter(prefix="/tracks", tags=["Tracks"])

@router.post("/", response_model=TrackResponse)
async def add_track(track: TrackCreate, db: AsyncSession = Depends(get_db)):
    new_track = Track(**track.dict())
    db.add(new_track)
    await db.commit()
    await db.refresh(new_track)
    return new_track

@router.get("/", response_model=list[TrackResponse])
async def get_tracks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Track))
    tracks = result.scalars().all()
    return tracks

