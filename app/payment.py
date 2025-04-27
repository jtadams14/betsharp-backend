from fastapi import APIRouter
from pydantic import BaseModel
import random

payment_router = APIRouter()

class PaymentResult(BaseModel):
    message: str
    access_granted: bool

@payment_router.post("/purchase")
def purchase_day_pass():
    # Simulate successful payment
    success = random.choice([True, True, True, False])  # 75% chance of success
    if success:
        return PaymentResult(message="Payment successful. Access granted for 24 hours.", access_granted=True)
    else:
        return PaymentResult(message="Payment failed. Please try again.", access_granted=False)

