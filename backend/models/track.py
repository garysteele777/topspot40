from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    track_name = Column(String, nullable=False)
    artist_name = Column(String, nullable=False)
    year_released = Column(String, nullable=False)
    intro = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    track_id = Column(String, nullable=False)
    artist_id = Column(String, nullable=False)
    album_artwork = Column(String, nullable=False)
    duration_ms = Column(Integer, nullable=False)
    formatted_duration = Column(String, nullable=True)  # Can be NULL
