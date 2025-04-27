from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import random

picks_router = APIRouter()

# Dummy data to simulate picks
sample_free_picks = [
    {"track": "Remington Park", "race_number": 1, "horse_name": "Dashin Dynasty", "confidence": 90},
    {"track": "Busan", "race_number": 4, "horse_name": "Wondaehan Kkum", "confidence": 87},
]

sample_paid_picks = [
    {"track": "Remington Park", "race_number": 2, "horse_name": "Lightning Bolt", "confidence": 92},
    {"track": "Busan", "race_number": 5, "horse_name": "Thunder Strike", "confidence": 89},
]

class Pick(BaseModel):
    track: str
    race_number: int
    horse_name: str
    confidence: float

@picks_router.get("/free", response_model=List[Pick])
def get_free_picks():
    return random.sample(sample_free_picks, k=2)

@picks_router.get("/paid", response_model=List[Pick])
def get_paid_picks():
    return random.sample(sample_paid_picks, k=2)
