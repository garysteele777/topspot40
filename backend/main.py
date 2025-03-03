from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.track import Track  # ✅ Corrected import
from backend.database import get_db
from pydantic import BaseModel

app = FastAPI()

class TrackCreate(BaseModel):
    rank: int
    category: str
    genre: str
    track_name: str
    artist_name: str
    year_released: str
    intro: str
    detail: str
    track_id: str
    artist_id: str
    album_artwork: str
    duration_ms: int
    formatted_duration: str

@app.post("/add-track/")
async def add_track(track: TrackCreate, db: AsyncSession = Depends(get_db)):
    new_track = Track(
        rank=track.rank,
        category=track.category,
        genre=track.genre,
        track_name=track.track_name,
        artist_name=track.artist_name,
        year_released=track.year_released,
        intro=track.intro,
        detail=track.detail,
        track_id=track.track_id,
        artist_id=track.artist_id,
        album_artwork=track.album_artwork,
        duration_ms=track.duration_ms,
        formatted_duration=track.formatted_duration,
    )

    db.add(new_track)
    await db.commit()
    await db.refresh(new_track)
    return {"message": "Track added successfully", "track": new_track}
