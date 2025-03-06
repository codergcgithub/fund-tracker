from fastapi import APIRouter

from app.api.v1.fund import router as fund_router

api_router = APIRouter()

api_router.include_router(fund_router, prefix='/fund')
