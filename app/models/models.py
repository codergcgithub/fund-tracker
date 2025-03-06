from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel

class Asset(BaseModel):
    id: int
    name: str
    symbol: str
    purchasePrice: float
    units: float
    purchaseDate: str
    current_price: Optional[Decimal] = None
    market_value: Optional[Decimal] = None
    percent_change: Optional[float] = None

   
class Fund(BaseModel):
    id: int
    name: str
    assets: List[Asset]
    cashBalance: float
    nav: float
