from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    DB_URL: str
    TEST_DB_URL: str
    db_echo: bool = False

    SECRET_KEY: str
    ALGORITHM: str

    MODE: Literal["DEV", "TEST", "PROD"]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
