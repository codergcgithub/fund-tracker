from app.core.middleware import logging_middleware
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(title="FundTracker API")
app.middleware("http")(logging_middleware)

app.include_router(api_router, prefix=settings.API_V1_STR)