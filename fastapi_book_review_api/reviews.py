# ----------- Imports -----------
from fastapi import APIRouter, Depends, HTTPException   # FastAPI tools → Router, dependency injection, error handling
from sqlalchemy.orm import Session                     # SQLAlchemy session type
from database import get_db                            # Custom DB session dependency
from schemas import ReviewCreate, ReviewOut            # Pydantic schemas (input + output for reviews)
from models import Review, Book                        # SQLAlchemy models (tables)
from typing import List                                # Typing support for list response


# ----------- Router setup -----------
router = APIRouter(prefix="/reviews", tags=["Reviews"])   # Prefix all routes with /reviews


# ----------- GET reviews by book -----------
@router.get("/book/{book_id}", response_model=List[ReviewOut])   # GET → list of reviews for a book
def get_reviews(book_id: int, db: Session = Depends(get_db)):    # book_id comes from URL, db session auto-injected
    return db.query(Review).filter(Review.book_id == book_id).all()   # Query all reviews where book_id matches


# ----------- POST add review to a book -----------
@router.post("/book/{book_id}", response_model=ReviewOut)        # POST → add a new review for a book
def add_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):  # book_id from URL, review from body
    book = db.query(Book).filter(Book.id == book_id).first()      # Check if book exists
    if not book:                                                  # If no book found → raise error
        raise HTTPException(status_code=404, detail="Book not found")

    # Create new Review object (user_id hardcoded = 1 for now, later replace with JWT user)
    new_review = Review(
        content=review.content,
        rating=review.rating,
        book_id=book_id,
        user_id=1
    )

    db.add(new_review)       # Add to session
    db.commit()              # Commit transaction
    db.refresh(new_review)   # Refresh object with DB data (id, etc.)
    return new_review        # Return review object (auto converted by response_model)
