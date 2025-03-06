from typing import Dict, List, Union
from ..mds_base import MarketDataService
from dotenv import load_dotenv
import yfinance as yf


load_dotenv()


class YFinanceService(MarketDataService):
    # Implement the MarketDataService abstract methods
    # initialize constructor
    def __init__(self):
        self.client=yf

    def connect(self):
        print(f"Connecting to {__name__} API...")
        pass

    def get_price(self, symbol: str) -> float:
        print(f"Retrieving quote for {symbol} from {__name__}...")
        try:
            ticker = self.client.Ticker(symbol)
            price=ticker.history(period="1d")["Close"].iloc[-1]
            return round(price,2)
        except Exception as e:
            print(f"Error retrieving price for {symbol} from {__name__}: {e}")
            return None

    def get_historical_data(self, symbol: str, start_date: str, end_date: str) -> List[Dict[str, Union[str, float]]]:
        print(f"Retrieving historical data for {symbol} from {__name__}...")
        try:
            ticker = self.client.Ticker(symbol)
            data=ticker.history(start=start_date, end=end_date)
            return data[['Close']].reset_index().to_dict(orient="records")
        except Exception as e:
            print(f"Error retrieving price for {symbol} from {__name__}: {e}")
            return []

    def disconnect(self):
        print(f"Disconnecting from {__name__} API...")
        pass
