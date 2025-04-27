from fastapi import FastAPI
from app.auth import auth_router
from app.picks import picks_router
from app.payment import payment_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(picks_router, prefix="/picks", tags=["Picks"])
app.include_router(payment_router, prefix="/payment", tags=["Payment"])

@app.get("/")
def read_root():
    return {"message": "Welcome to BetSharp API!"}
