import hashlib
from jose import jwt
from passlib.context import CryptContext

SECRET = "secret"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ ALWAYS SAFE PASSWORD HANDLING
def hash_password(password: str):
    # convert to fixed length first
    safe_password = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(safe_password)


def verify_password(plain, hashed):
    safe_password = hashlib.sha256(plain.encode()).hexdigest()
    return pwd_context.verify(safe_password, hashed)


def create_token(data: dict):
    return jwt.encode(data, SECRET, algorithm="HS256")
