from typing import List
import logging
from app.core.middleware import logging_middleware
from fastapi import FastAPI, HTTPException, Request, Response
from starlette.background import BackgroundTask
from pydantic import BaseModel

app = FastAPI(title="FundTracker API")
app.middleware("http")(logging_middleware)

