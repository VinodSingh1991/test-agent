"""
Main FastAPI application entry point.
"""
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from loguru import logger

from design_system_agent.api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    # Log configuration
    logger.info(f"Starting Design System Agent API v{app.version}")
    logger.info(f"OpenAI API Key: {'✓ Set' if os.getenv('OPENAI_API_KEY') else '✗ Not Set'}")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    
    # Check if summary dataset exists, generate if AUTO_GENERATE_DATASET is enabled
    auto_generate = os.getenv("AUTO_GENERATE_DATASET", "false").lower() == "true"
    if auto_generate:
        logger.info("Auto dataset generation is disabled. Run generate_dataset.py manually to create dataset.")
        logger.info("Dataset path: dataset/crm_query_dataset.json")
    
    # Initialize services here (vector store, LLM client, etc.)
    yield
    
    # Cleanup here
    logger.info("Shutting down Design System Agent API")


# Get environment settings
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Determine CORS origins based on environment
if ENVIRONMENT == "production":
    # In production, specify allowed origins
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []
else:
    # In development, allow all origins
    CORS_ORIGINS = ["*"]

app = FastAPI(
    title="Design System Agent API",
    description="AI-powered design system assistant for component generation and recommendations",
    version="0.1.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception Handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error("Validation error: {}", repr(exc))
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Global exception: {}", repr(exc), exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


# Include routers
app.include_router(router, prefix="/api/v1", tags=["design-system"])


@app.get("/")
async def root():
    return {
        "message": "Design System Agent API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "design-system-agent",
        "version": "0.1.0"
    }


if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {API_HOST}:{API_PORT}")
    uvicorn.run(
        "main:app",
        host=API_HOST,
        port=API_PORT,
        reload=ENVIRONMENT != "production",
        log_level="info"
    )
