import random
from decimal import Decimal

class data_source:
    def __init__(self):
        pass

class MarketDataService:
    def __init__(self, data_source):
        self.data_source = data_source

    def get_quote(self, symbol):
        """
        Mock market data service that returns a random price
        In production, this would call a real market data API
        """
        # Generate a random price between 80% and 120% of 100
        price = random.uniform(80, 120)
        return Decimal(str(round(price, 2)))