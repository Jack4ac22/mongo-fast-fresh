from fastapi import FastAPI, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from pymongo import MongoClient
from config import settings
from features.books.book_router import router as book_router
from features.users.user_router import router as user_router
from features.security.auth import router as auth_router


# from routes import router as book_router
# from routers.user_router import router as user_router
# from routers.auth import router as auth

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(settings.atlas_uri)
    app.database = app.mongodb_client[settings.db_name]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return "it is working"


app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(user_router, tags=["users"], prefix="/users")
app.include_router(auth_router)
