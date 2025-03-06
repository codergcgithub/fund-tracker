from ..mds_base import MarketDataService
from dotenv import load_dotenv
import os
from app.utils.caching import timed_lru_cache
import finnhub


load_dotenv()


class FinnhubService(MarketDataService):
    # Implement the MarketDataService abstract methods
    # initialize constructor
    def __init__(self):
        self.apikey = os.getenv("FINNHUB_API_KEY")
        if not self.apikey:
            raise ValueError("API key not found for".join(__name__))
        self.client=finnhub.Client(api_key=self.apikey)

    def connect(self):
        print(f"Connecting to {__name__} API...")
        pass
    
    @timed_lru_cache(60)
    def get_price(self, symbol: str) -> float:
        print(f"Retrieving quote for {symbol} from {__name__}...")
        data = self.client.quote(symbol)
        print(data)
        try:
            if "c" in data and data["c"]:
                return float(data["c"])
            else:
                return None
        except Exception as e:
            print(f"Error retrieving price for {symbol} from {__name__}: {e}")
            return None

    def get_historical_data(self, symbol: str, start_date: str, end_date: str):
        print(f"Retrieving historical data for {symbol} from {__name__}...")
        pass

    def disconnect(self):
        print(f"Disconnecting from {__name__} API...")
        pass
