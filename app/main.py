from fastapi import FastAPI
from app.api.routes import router
from app.db.session import engine, Base
from app.models.lead import Lead

app = FastAPI(title="AI Lead Management API")

# Create DB tables
Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}