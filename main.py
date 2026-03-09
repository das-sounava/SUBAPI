from fastapi import FastAPI
import models
from database import engine
from routes import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Subscription API")

app.include_router(api_router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Subscription-Based Content API!",
        "documentation": "Visit http://127.0.0.1:8000/docs for the interactive API documentation."
    }
