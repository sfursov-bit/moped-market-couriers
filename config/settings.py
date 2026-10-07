from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///./moped_market.db"

    geocoder_provider: Literal["osm", "dadata", "yandex", "none"] = "osm"
    dadata_api_key: str = ""
    dadata_secret_key: str = ""
    yandex_geocoder_api_key: str = ""
    geocode_cache_ttl_hours: int = 720

    avito_use_playwright: bool = True
    avito_delay_min_sec: float = 2.0
    avito_delay_max_sec: float = 4.0
    avito_request_timeout_sec: int = 30
    avito_max_pages_rental: int = 20
    avito_max_pages_other: int = 15
    avito_concurrency: int = 1
    proxy_list: str = ""
    respect_robots: bool = False
    user_agent_rotate: bool = True

    data_dir: Path = Path("./data")
    raw_html_dir: Path = Path("./data/raw_html")
    cache_dir: Path = Path("./data/cache")

    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    workers: int = 2


settings = Settings()
settings.data_dir.mkdir(exist_ok=True)
settings.raw_html_dir.mkdir(exist_ok=True)
settings.cache_dir.mkdir(exist_ok=True)
