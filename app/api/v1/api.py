from fastapi import APIRouter
from app.api.v1.endpoints import transaction

# Init Router
api_router = APIRouter()

# Including summary router
api_router.include_router(transaction.router, tags=['Summary Transactions'])
