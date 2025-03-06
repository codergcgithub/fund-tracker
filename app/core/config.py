
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #App settings
    API_V1_STR: str = "/api/v1"
    DEFAULT_MDS_PROVIDER: str = 'yfinance'


settings = Settings()