import pytest
import os
from unittest.mock import patch, MagicMock
from app.mds.providers.alpha_vantage import AlphaVantageService

@pytest.fixture
def alpha_vantage_service():
    with patch.dict(os.environ, {'ALPHAVANTAGE_API_KEY': 'test_api_key'}):
        return AlphaVantageService()

def test_init_no_api_key():
    with patch.dict(os.environ, {'ALPHAVANTAGE_API_KEY': ''}):
        with pytest.raises(ValueError, match='API key not found for'):
            AlphaVantageService()

def test_get_price_success(alpha_vantage_service):
    symbol = 'AAPL'
    mock_response = {
        'Global Quote': {
            '05. price': '150.00'
        }
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value = MagicMock(status_code=200, json=lambda: mock_response)
        price = alpha_vantage_service.get_price(symbol)
        assert price == 150.00

def test_get_price_no_quote(alpha_vantage_service):
    symbol = 'AAPL'
    mock_response = {}
    with patch('requests.get') as mock_get:
        mock_get.return_value = MagicMock(status_code=200, json=lambda: mock_response)
        price = alpha_vantage_service.get_price(symbol)
        assert price is None


