from typing import List, Optional
from pydantic import BaseModel

class Asset(BaseModel):
    id: int
    name: str
    symbol: str
    price: float
    quantity: float
    total: float