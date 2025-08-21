from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    mode: Literal["debug", "development", "production"] = "development"
    logging_level_override: str | None = None


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()
