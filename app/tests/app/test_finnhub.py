import pytest
from unittest.mock import patch, MagicMock
from app.mds.providers.finnhub import FinnhubService

@pytest.fixture
def finnhub_service():
    with patch('app.mds.providers.finnhub.os.getenv') as mock_getenv:
        mock_getenv.return_value = 'test_api_key'
        service = FinnhubService()
        yield service

def test_init_no_api_key():
    with patch('app.mds.providers.finnhub.os.getenv', return_value=None):
        with pytest.raises(ValueError, match="API key not found for"):
            FinnhubService()

def test_get_price(finnhub_service):
    mock_quote = {'c': 100.0}
    finnhub_service.client.quote = MagicMock(return_value=mock_quote)
    price = finnhub_service.get_price('AAPL')
    assert price == 100.0

def test_get_price_no_data(finnhub_service):
    mock_quote = {}
    finnhub_service.client.quote = MagicMock(return_value=mock_quote)
    price = finnhub_service.get_price('AAPL')
    assert price is None
