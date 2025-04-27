from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Pick(BaseModel):
    track: str
    race_number: int
    horse_name: str
    confidence: float
