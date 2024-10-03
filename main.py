"""
Main Application Entry Point.

This module initializes the FastAPI application, sets up CORS, initializes the
database, and configures the API routes.
It also contains the startup event where the database is initialized and a
default admin user is created.
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.v1.routers import main_api_router
from app.core.config.settings import settings
from app.core.database.connection import init_db
import uvicorn

# Set up FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up main api router
app.include_router(main_api_router, prefix=settings.API_V1_ENDPOINT)


@app.on_event("startup")
async def startup_event():
    init_db()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
