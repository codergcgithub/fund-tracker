from ..mds_base import MarketDataService
from dotenv import load_dotenv
import os
import requests
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
        print("Connecting to FinnhubService API...")
        pass

    def get_price(self, symbol: str) -> float:
        print(f"Retrieving quote for {symbol} from FinnhubService...")
        data = self.client.quote(str)
        if "c" in data and data["c"]:
            return float(data["c"])
        else:
            return None

    def get_historical_data(self, symbol: str, start_date: str, end_date: str):
        print(f"Retrieving historical data for {symbol} from FinnhubService...")
        pass

    def disconnect(self):
        print("Disconnecting from FinnhubService API...")
        pass
