from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="FastAPI Backend Practice",
    version="1.0.0",
    description="Professional FastAPI backend scaffold"
)

app.include_router(api_router)
