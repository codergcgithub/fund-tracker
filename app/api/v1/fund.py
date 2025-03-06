from fastapi import HTTPException
from fastapi import APIRouter

from typing import List, Dict, Any

from app.schemas.fund_schema import AssetCreate, FundCreate
from app.services.fund_service import FundService

router = APIRouter()
fund_service = FundService()

@router.get("/", response_model=List[Dict[str, Any]])
async def api_get_funds():
    fund_service.load_sample_data()
    return fund_service.get_all_funds_summary()

@router.post("/", response_model=Dict[str, Any])
async def api_create_fund(fund: FundCreate):
    new_fund = fund_service.create_fund(fund.name, fund.cashBalance)
    return new_fund

@router.get("/{fund_id}", response_model=Dict[str, Any])
async def api_get_fund(fund_id: str):
    try:
        return fund_service.get_fund_details(fund_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{fund_id}/assets", response_model=Dict[str, Any])
async def api_add_asset(fund_id: str, asset: AssetCreate):
    try:
        new_asset = fund_service.add_asset(
            fund_id, 
            asset.symbol, 
            asset.purchasePrice, 
            asset.units, 
            asset.purchaseDate
        )
        return new_asset
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
