import pytest
from unittest.mock import patch
from app.mds.providers.yfinance import yfinanceService

@pytest.fixture
def yfinance_service():
    return yfinanceService()

def test_connect(yfinance_service):
    with patch('builtins.print') as mocked_print:
        yfinance_service.connect()
        mocked_print.assert_called_with("Connecting to app.mds.providers.yfinance API...")

def test_get_price_exception(yfinance_service):
    symbol = "AAPL"
    
    with patch.object(yfinance_service.client, 'Ticker', side_effect=Exception("Test Exception")):
        price = yfinance_service.get_price(symbol)
        assert price is None


def test_get_historical_data_exception(yfinance_service):
    symbol = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    
    with patch.object(yfinance_service.client, 'Ticker', side_effect=Exception("Test Exception")):
        data = yfinance_service.get_historical_data(symbol, start_date, end_date)
        assert data == []


