from ..mds_base import MarketDataService
from dotenv import load_dotenv
import os
import requests

load_dotenv()


class AlphaVantageService(MarketDataService):
    # Implement the MarketDataService abstract methods
    # initialize constructor
    def __init__(self):
        self.baseurl = "https://www.alphavantage.co/query?"
        self.apikey = os.getenv("ALPHAVANTAGE_API_KEY")
        if not self.apikey:
            raise ValueError("API key not found for".join(__name__))

    def connect(self):
        print(f"Connecting to {__name__} API...")
        pass

    def get_price(self, symbol: str) -> float:
        print(f"Retrieving quote for {symbol} from {__name__}...")
        url = (
            self.baseurl + f"function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.apikey}"
        )
        res = requests.get(url)
        data = res.json()
        if "Global Quote" in data and data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            return None

    def get_historical_data(self, symbol: str, start_date: str, end_date: str):
        print(f"Retrieving historical data for {symbol} from {__name__}...")
        pass

    def disconnect(self):
        print(f"Disconnecting from {__name__} API...")
        pass
