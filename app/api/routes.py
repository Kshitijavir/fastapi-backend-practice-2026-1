from fastapi import APIRouter, status
from pydantic import BaseModel


router = APIRouter(prefix="/api", tags=["default"])


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    version: str = "1.0.0"


@router.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    """Welcome endpoint."""
    return {
        "message": "FastAPI Backend Practice 2026",
        "version": "1.0.0"
    }


@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint with structured response."""
    return HealthResponse(status="healthy")
