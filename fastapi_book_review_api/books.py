# ----------- Imports -----------
from fastapi import APIRouter, Depends, HTTPException   # FastAPI classes & helpers
from sqlalchemy.orm import Session   # SQLAlchemy class for DB session
from database import get_db          # Custom function → provides DB session
from schemas import BookCreate, BookOut   # Custom Pydantic schemas for books
from models import Book              # Custom SQLAlchemy model (books table)
from typing import List              # Typing helper for lists (used in response_model)


# ----------- Router setup -----------
router = APIRouter(prefix="/books", tags=["Books"])   # Router instance for book endpoints


# ----------- Get all books -----------
@router.get("/", response_model=List[BookOut])   # GET /books/, returns list of books
def get_books(db: Session = Depends(get_db)):    # Function → takes DB session
    return db.query(Book).all()   # Query DB → return all book records


# ----------- Get a book by ID -----------
@router.get("/{id}", response_model=BookOut)   # GET /books/{id}, returns single book
def get_book(id: int, db: Session = Depends(get_db)):   # Function → id param + DB session
    book = db.query(Book).filter(Book.id == id).first()   # Query DB → find book by id
    if not book:   # If no book found
        raise HTTPException(status_code=404, detail="Book not found")   # Raise 404 error
    return book   # Return found book


# ----------- Create a new book -----------
@router.post("/", response_model=BookOut)   # POST /books/, creates new book
def create_book(book: BookCreate, db: Session = Depends(get_db)):   # Function → book data + DB session
    new_book = Book(**book.dict())   # Create Book object from request data
    db.add(new_book)   # Stage book for DB insert
    db.commit()        # Commit → save in DB
    db.refresh(new_book)   # Refresh object with DB values (e.g., id)
    return new_book   # Return created book
