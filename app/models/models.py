from decimal import Decimal
from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class Asset(BaseModel):
    id: str
    symbol: str
    purchasePrice: float
    units: float
    purchaseDate: date
    currentPrice: Optional[float] = None
    market_value: Optional[float] = None
    percent_change: Optional[float] = None

   
class Fund(BaseModel):
    id: str
    name: str
    assets: List[Asset]
    cashBalance: float
    nav: float
    createdAt: str
