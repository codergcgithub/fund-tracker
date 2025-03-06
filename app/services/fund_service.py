from datetime import datetime
from typing import List, Dict, Any
import uuid
from app.mds.provider_factory import ProviderFactory
from app.models.models import Fund, Asset


class FundService:
    def __init__(self):
        self.mds_provider = ProviderFactory().get_provider()
        self.funds = []

    # Helper to generate asset current price
    def get_asset_current_price(self, symbol: str) -> float:
        try:
            price = self.mds_provider.get_price(symbol)
            return price
        except Exception as e:
            print(f"Error retrieving price for {symbol}: {e}")
            return 0.0

    def add_asset(self, fund_id: str, symbol: str, purchase_price: float, units: float, purchase_date: str) -> Dict[str, Any]:
        fund = next((f for f in self.funds if f['id'] == fund_id), None)
        if not fund:
            raise ValueError(f"Fund with ID {fund_id} not found")
        
        prc = self.get_asset_current_price(symbol.upper())
        
        new_asset = Asset(
            id=f'asset-{int(datetime.now().timestamp())}',
            symbol=symbol.upper(),
            purchasePrice=purchase_price,
            units=units,
            purchaseDate=purchase_date,
            currentPrice= prc,
            market_value=round(units*prc,2),
            percent_change=round(((prc-purchase_price)/purchase_price)*100,2)
        ).model_dump()
        
        fund['assets'].append(new_asset)
        fund['nav'] = self.calculate_fund_nav(fund)
        return new_asset

    # Create a new fund
    def create_fund(self, name: str, cash_balance: float) -> Dict[str, Any]:
        new_fund = Fund(
            id=str(uuid.uuid4()),
            name=name,
            cashBalance=cash_balance,
            assets=[],
            nav=cash_balance,
            createdAt=datetime.now().isoformat()
        ).model_dump()
        
        self.funds.append(new_fund)
        return new_fund

    # Load sample data
    def load_sample_data(self) -> None:
        if not self.funds:
            # Create a couple of sample funds
            tech_fund = self.create_fund("Technology Growth", 25000)
            self.add_asset(tech_fund['id'], 'AAPL', 170.12, 15, '2023-06-15')
            self.add_asset(tech_fund['id'], 'MSFT', 380.45, 10, '2023-07-22')
            self.add_asset(tech_fund['id'], 'GOOGL', 140.87, 12, '2023-08-10')
            
            diversified_fund = self.create_fund("Diversified Portfolio", 50000)
            self.add_asset(diversified_fund['id'], 'AMZN', 175.35, 8, '2023-05-05')
            self.add_asset(diversified_fund['id'], 'JPM', 195.20, 15, '2023-04-12')
            self.add_asset(diversified_fund['id'], 'NVDA', 410.75, 5, '2023-03-28')

    # Helper to calculate fund's total value
    def calculate_fund_nav(self, fund: Dict[str, Any]) -> float:
        assets_value = sum(
            (asset.get('currentPrice', self.get_asset_current_price(asset['symbol'])) * asset['units'])
            for asset in fund['assets']
        )
        return round(assets_value + fund['cashBalance'], 2)

    # Get all funds with summary information
    def get_all_funds_summary(self) -> List[Dict[str, Any]]:
        result = []
        
        for fund in self.funds:
            #need to recalculate with the latest prices
            total_value = self.calculate_fund_nav(fund)
            
            # Calculate initial investment
            initial_investment = sum(
                (asset['purchasePrice'] * asset['units']) 
                for asset in fund['assets']
            ) + fund['cashBalance']
            
            # Calculate performance
            value_change = total_value - initial_investment
            percent_change = (value_change / initial_investment) * 100 if initial_investment > 0 else 0
            
            result.append({
                'id': fund['id'],
                'name': fund['name'],
                'nav': total_value,
                'performance': {
                    'percentChange': round(percent_change, 2),
                    'valueChange': round(value_change, 2)
                }
            })
        
        return result

    # Get detailed information for a specific fund
    def get_fund_details(self, fund_id: str) -> Dict[str, Any]:
        fund = next((f for f in self.funds if f['id'] == fund_id), None)
        if not fund:
            raise ValueError(f"Fund with ID {fund_id} not found")
        
        # Update current prices for all assets
        updated_fund = dict(fund)
        updated_fund['assets'] = [
            {**asset, 'currentPrice': self.get_asset_current_price(asset['symbol'])}
            for asset in fund['assets']
        ]
        
        return updated_fund
