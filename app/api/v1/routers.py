from fastapi import APIRouter
from app.api.v1.cats.routes import router as cats_router

main_api_router = APIRouter()

# List of individual routers to be included in the main API router.
api_routers = [cats_router]

# Include each router from the list into the main API router.
for api_router in api_routers:

    main_api_router.include_router(api_router)

