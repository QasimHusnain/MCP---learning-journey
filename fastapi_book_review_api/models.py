# ----------- Imports -----------
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float   # SQLAlchemy column types & foreign keys
from sqlalchemy.orm import relationship   # SQLAlchemy function for table relationships
from database import Base   # Custom Base (from declarative_base) → all models inherit from it


# ----------- User table -----------
class User(Base):                      # Class → defines "users" table, inherits from Base
    __tablename__ = "users"            # Table name in DB

    # Columns (table fields)
    id = Column(Integer, primary_key=True, index=True)   # Integer PK, indexed
    username = Column(String, unique=True, index=True)   # Username, unique + indexed
    email = Column(String, unique=True, index=True)      # Email, unique + indexed
    password = Column(String)                            # Password (hashed string)

    # Relationship → one user can have many reviews
    reviews = relationship("Review", back_populates="user")


# ----------- Book table -----------
class Book(Base):                      # Class → defines "books" table
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)   # Primary key
    title = Column(String, index=True)                  # Book title (indexed for search)
    author = Column(String)                             # Book author
    description = Column(Text)                          # Longer text (book description)

    # Relationship → one book can have many reviews
    reviews = relationship("Review", back_populates="book")


# ----------- Review table -----------
class Review(Base):                    # Class → defines "reviews" table
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)   # Primary key
    content = Column(Text)                              # Review text
    rating = Column(Float)                              # Rating (decimal/float)
    user_id = Column(Integer, ForeignKey("users.id"))   # FK → links to users table
    book_id = Column(Integer, ForeignKey("books.id"))   # FK → links to books table

    # Relationships (many-to-one)
    user = relationship("User", back_populates="reviews")   # Review belongs to a user
    book = relationship("Book", back_populates="reviews")   # Review belongs to a book
