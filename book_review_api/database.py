# ----------- Imports -----------
from sqlalchemy import create_engine              # SQLAlchemy function → creates DB engine (connection)
from sqlalchemy.ext.declarative import declarative_base   # Function → generates base class for models
from sqlalchemy.orm import sessionmaker           # Factory function → creates DB sessions


# ----------- Database setup -----------
DATABASE_URL = "sqlite:///./books.db"   # DB connection string (SQLite file stored as books.db)

# Engine → manages actual connection to DB
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}   # Needed for SQLite (threading issue fix)
)

# SessionLocal → class factory to create session objects (DB transactions)
SessionLocal = sessionmaker(
    autocommit=False,   # Transactions won’t auto-commit
    autoflush=False,    # Don’t auto-flush changes until commit
    bind=engine         # Link sessions to our DB engine
)

# Base class → all ORM models (tables) will inherit from this
Base = declarative_base()


# ----------- Dependency for FastAPI routes -----------
def get_db():                 # Function → provides DB session (used with Depends in FastAPI)
    db = SessionLocal()       # Create a new DB session
    try:
        yield db              # Provide session to route
    finally:
        db.close()            # Always close session after request is done


# ----------- Quick test (command line) -----------
# Run this in terminal to check DB setup:
# python -c "from database import Base; print('DB Ready!')"

