from fastapi import FastAPI                        # FastAPI framework to build the app
from database import Base, engine                  # Our DB base class + engine from database.py
import models                                      # Import models so tables can be created
from auth import router as auth_router             # Import Auth router (register/login)
from books import router as books_router           # Import Books router (CRUD books)
from reviews import router as reviews_router       # Import Reviews router (CRUD reviews)


# Create all tables in DB (if not exist) using models and Base
Base.metadata.create_all(bind=engine)


# Initialize FastAPI app
app = FastAPI(title="Book Review API")


# Attach routers (auth, books, reviews) → endpoints grouped by tags
app.include_router(auth_router)
app.include_router(books_router)
app.include_router(reviews_router)


# Run with uvicorn if executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



















# from fastapi import FastAPI
# import uvicorn
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse


# app = FastAPI()

# app.mount("/static", StaticFiles(directory="favcon"), name="favcon")

# @app.get("/")
# def read_app():
#     message = {
#         "Name": "Qasim",
#         "Profession": "Software Engineer",
#         "Message": "Static files are ready!"
#     }
#     return message

# # Special route for favicon.ico

# @app.get("/favicon.ico", include_in_schema=False)
# async def favicon():
#     return FileResponse("favcon/favicon.ico")


