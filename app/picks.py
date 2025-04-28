from fastapi import APIRouter

picks_router = APIRouter()

@picks_router.get("/")
def get_free_picks():
    return [
        {"track": "Remington Park", "race_number": 1, "horse_name": "Dashin Dynasty", "confidence": 90.0},
        {"track": "Busan", "race_number": 4, "horse_name": "Wondaehan Kkum", "confidence": 87.0},
    ]

@picks_router.get("/premium")
def get_premium_picks():
    return [
        {"track": "Churchill Downs", "race_number": 3, "horse_name": "Speedy Spirit", "confidence": 92.5},
        {"track": "Santa Anita", "race_number": 5, "horse_name": "Golden Streak", "confidence": 95.0},
    ]
