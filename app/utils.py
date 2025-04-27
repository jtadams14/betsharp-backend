from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

# Password hashing utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# JWT token utilities
SECRET_KEY = "your_secret_key_here"  # Replace with your secret key
ALGORITHM = "HS256"

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode = {"sub": username, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
