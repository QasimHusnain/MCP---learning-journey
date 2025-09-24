📚 Book Review API
==================

A simple **FastAPI** project where users can **register, login, add books, and write reviews**.\
Built with **FastAPI, SQLAlchemy, Pydantic, and JWT authentication**.

* * * * *

🚀 Features
-----------

-   👤 User registration & login with password hashing

-   🔑 JWT authentication for secure access

-   📘 CRUD operations on books (create, read, list)

-   ✍️ Add and fetch reviews for books

-   🗄️ SQLite database for storage

* * * * *

🛠️ Tech Stack
--------------

-   **FastAPI** → web framework

-   **SQLite** → database (file: `books.db`)

-   **SQLAlchemy** → ORM for database models

-   **Pydantic** → request & response validation

-   **Passlib** → password hashing

-   **Python-Jose** → JWT token handling

* * * * *

📂 Project Structure
--------------------

`.
├── app.py           # Main FastAPI app (entry point)
├── database.py      # Database setup (engine, session, Base)
├── models.py        # SQLAlchemy models (User, Book, Review)
├── schemas.py       # Pydantic schemas (validation)
├── utils.py         # Security utils (hash, verify, JWT)
├── auth.py          # Auth routes (register/login)
├── books.py         # Book routes (list, get, create)
├── reviews.py       # Review routes (add, fetch by book)
└── books.db         # SQLite database file`

* * * * *

⚙️ Installation & Setup
-----------------------

1.  **Clone the repo**

    `git clone https://github.com/your-username/book-review-api.git
    cd book-review-api`

2.  **Create virtual environment (recommended)**

    `python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows`

3.  **Install dependencies**

    `pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] pydantic`

4.  **Run the server**

    `uvicorn app:app --reload`

* * * * *

📡 API Endpoints
----------------

### 🔐 Auth

-   `POST /auth/register` → Register new user

-   `POST /auth/login` → Login & get JWT

### 📘 Books

-   `GET /books/` → Get all books

-   `GET /books/{id}` → Get book by ID

-   `POST /books/` → Create new book

### ✍️ Reviews

-   `GET /reviews/book/{book_id}` → Get all reviews for a book

-   `POST /reviews/book/{book_id}` → Add review to a book

* * * * *

🧪 Testing with cURL
--------------------

### Add a Book

`curl -X POST "http://127.0.0.1:8000/books/"\
  -H "Content-Type: application/json"\
  -d '{"title": "Atomic Habits", "author": "James Clear", "description": "Small changes, big results"}'`

### Add a Review

`curl -X POST "http://127.0.0.1:8000/reviews/book/1"\
  -H "Content-Type: application/json"\
  -d '{"content": "Amazing book!", "rating": 4.8}'`

* * * * *

📖 Notes
--------

-   Database is stored in `books.db` (SQLite file).

-   Default review is linked to `user_id=1` (you can improve by adding JWT auth).

-   Change `SECRET_KEY` in `utils.py` for production use.