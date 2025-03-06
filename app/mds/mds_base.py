from abc import ABC, abstractmethod


class MarketDataService(ABC):
    """
    Abstract base class for market data providers.
    """

    @abstractmethod
    def connect(self):
        """Establish a connection to the market data source."""
        pass

    @abstractmethod
    def get_price(self, symbol: str) -> float:
        """Fetch the latest price for a given symbol."""
        pass

    @abstractmethod
    def get_historical_data(self, symbol: str, start_date: str, end_date: str):
        """Retrieve historical market data."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the connection."""
        pass
