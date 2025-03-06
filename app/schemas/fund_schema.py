
from datetime import date
from pydantic import BaseModel, field_validator

# Model schemas for API requests
class AssetCreate(BaseModel):
    symbol: str
    purchasePrice: float
    units: float
    purchaseDate: date
    
    @field_validator('purchaseDate')
    def validate_past_date(cls, v):
        if v > date.today():
            raise ValueError('Purchase date cannot be in the future')
        return v
    
class FundCreate(BaseModel):
    name: str
    cashBalance: float