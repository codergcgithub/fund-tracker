from app.core.config import settings
from app.mds.providers.alpha_vantage import AlphaVantageService
from app.mds.providers.finnhub import FinnhubService
from app.mds.providers.yfinance import YFinanceService

class ProviderFactory:
    """Factory class to dynamically load the selected market data provider."""
    
    _providers = {}
          
    def __init__(self, provider_name: str = settings.DEFAULT_MDS_PROVIDER):
        """Initialize the factory by fetching the selected provider from the database."""
        self.selected_provider_name = provider_name.lower()
        self.provider_instance = self._initialize_provider()
    
    def _initialize_provider(self):
        """Initialize and return the selected provider instance."""
        if self.selected_provider_name in self._providers:
            return self._providers[self.selected_provider_name]()
        else:
            raise ValueError(f"Invalid provider: {self.selected_provider_name}")
    
    
    def get_provider(self):
        """Return the initialized provider instance."""
        return self.provider_instance

    @classmethod
    def register_provider(cls, name, provider_class):
        """Dynamically register a new provider."""
        cls._providers[name.lower()] = provider_class
        
ProviderFactory.register_provider("alpha_vantage", AlphaVantageService)
ProviderFactory.register_provider("finnhub", FinnhubService)        
ProviderFactory.register_provider("yfinance", YFinanceService)