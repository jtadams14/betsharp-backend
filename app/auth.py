from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

auth_router = APIRouter()

SECRET_KEY = "your_secret_key_here"  # Replace with a real key in production
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fake in-memory database
fake_users_db = {}

class User(BaseModel):
    username: str
    password: str

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode = {"sub": username, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@auth_router.post("/register")
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered.")
    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.username] = hashed_password
    return {"message": "User registered successfully."}

@auth_router.post("/login")
def login(user: User):
    if user.username not in fake_users_db:
        raise HTTPException(status_code=400, detail="Invalid credentials.")
    hashed_password = fake_users_db[user.username]
    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials.")
    token = create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}
