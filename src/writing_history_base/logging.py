import logging
from functools import lru_cache
from typing import Literal

from .settings import get_app_settings


@lru_cache
def get_log_config(mode: Literal["debug", "development", "production"]) -> dict:
    app_settings = get_app_settings()

    print("Starting app in mode:", mode)

    match mode:
        case "debug":
            level = logging.DEBUG
        case "development":
            level = logging.INFO
        case "production":
            level = logging.WARNING

    if app_settings.logging_level_override is not None:
        print("Overriding logging level to:", app_settings.logging_level_override)
        level = logging.getLevelName(app_settings.logging_level_override)

    other_level = logging.INFO if level == logging.DEBUG else level

    return {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "default": {
                "level": level,
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",  # Default is stderr
            },
        },
        "loggers": {
            "": {  # root logger
                "level": other_level,
                "handlers": ["default"],
                "propagate": False,
            },
            "uvicorn.error": {
                "level": other_level,
                "handlers": ["default"],
            },
            "uvicorn.access": {
                "level": other_level,
                "handlers": ["default"],
            },
            "app": {
                "level": level,
                "handlers": ["default"],
                "propagate": False,
            },
        },
    }
