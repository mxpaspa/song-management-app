from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from .database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    body = Column(String(1024))

    def as_dictionary(self):
        song = {
            "id": 1,
            "file": {
                "id": 7,
                "name": "Shady_Grove.mp3"
            }
        }
        return song

class Song(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    song = relationship("Song", backref="song", uselist=False)


    def as_dictionary(self):
        files = {"id": 7, "name": "Shady_Grove.mp3"}
        return files
