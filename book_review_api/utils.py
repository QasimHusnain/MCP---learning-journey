from passlib.context import CryptContext      # From passlib → helps with hashing passwords
from jose import jwt                          # From python-jose → handles JWT encoding/decoding
from datetime import datetime, timedelta      # For token expiry calculation


SECRET_KEY = "mysecretkey"  # Secret used to sign JWTs (⚠️ should be strong & hidden in .env)
ALGORITHM = "HS256"         # Algorithm used for JWT encoding
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Default expiry time for tokens


# Create password hashing context → bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):             # Function to hash plain text password
    return pwd_context.hash(password)         # Returns hashed version


def verify_password(plain_password, hashed_password):  # Check if entered password matches hash
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):  # Create JWT token
    to_encode = data.copy()                     # Copy input data (e.g., {"sub": email})
    expire = datetime.utcnow() + (              # Calculate expiry time
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})           # Add expiry to payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Return signed JWT
