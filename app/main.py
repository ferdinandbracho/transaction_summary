from fastapi import FastAPI
from app.api.v1.api import api_router
import app.config as config

# Init fastAPI APP
app = FastAPI(
    title=config.PROJECT_NAME
)

# Include router
app.include_router(api_router)


