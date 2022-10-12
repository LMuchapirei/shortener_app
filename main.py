import secrets
import validators
from fastapi  import Depends,FastAPI,HTTPException
from schemas import URLBase
from sqlalchemy.orm import Session
import models
from .database import SessionLocal,engine


app= FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return "Welcome to the URL Shortner API 😂"

def raise_bad_request(message):
    raise HTTPException(status_code=400,detail=message)


@app.post("/url")
def create_url(url:URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"