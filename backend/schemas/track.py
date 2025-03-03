from pydantic import BaseModel

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

class TrackResponse(TrackCreate):
    id: int

    class Config:
        orm_mode = True
