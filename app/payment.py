from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

payment_router = APIRouter()

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    source: str  # Normally a token from Stripe.js
    description: str

@payment_router.post("/charge")
def create_charge(payment_request: PaymentRequest):
    # In real life, integrate with Stripe API here.
    if payment_request.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero.")
    
    return {
        "status": "success",
        "message": f"Charged {payment_request.amount} {payment_request.currency} for {payment_request.description}"
    }
