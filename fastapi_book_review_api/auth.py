# ----------- Imports -----------
from fastapi import APIRouter, Depends, HTTPException, status   # FastAPI classes & helpers
from sqlalchemy.orm import Session   # SQLAlchemy class for DB session
from database import get_db          # Custom function → provides DB session
from schemas import UserCreate, UserOut, Token   # Custom Pydantic schemas
from models import User              # Custom SQLAlchemy model (users table)
from utils import hash_password, verify_password, create_access_token  # Custom auth utilities


# ----------- Router setup -----------
router = APIRouter(prefix="/auth", tags=["Auth"])   # Router instance for auth endpoints


# ----------- Register endpoint -----------
@router.post("/register", response_model=UserOut)   # POST /auth/register, response shaped by UserOut
def register(user: UserCreate, db: Session = Depends(get_db)):   # Function → takes validated user + DB session
    db_user = db.query(User).filter(User.email == user.email).first()   # Query DB for existing email
    if db_user:   # If email found → already registered
        raise HTTPException(status_code=400, detail="Email already registered")   # Raise 400 error

    hashed_pw = hash_password(user.password)   # Hash the plain password
    new_user = User(username=user.username, email=user.email, password=hashed_pw)   # Create new user object

    db.add(new_user)   # Stage new user for DB insert
    db.commit()        # Commit → save in DB
    db.refresh(new_user)   # Refresh object with DB data (e.g., id)
    return new_user    # Return user (FastAPI converts with UserOut schema)


# ----------- Login endpoint -----------
@router.post("/login", response_model=Token)   # POST /auth/login, response shaped by Token
def login(user: UserCreate, db: Session = Depends(get_db)):   # Function → takes login data + DB session
    db_user = db.query(User).filter(User.email == user.email).first()   # Fetch user by email

    if not db_user or not verify_password(user.password, db_user.password):   # Check user + password
        raise HTTPException(   # If invalid → 401 Unauthorized
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": db_user.email})   # Create JWT token with email as subject
    return {"access_token": token, "token_type": "bearer"}   # Return token to client
