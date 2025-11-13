import logging
from functools import lru_cache

from .settings import get_app_settings


@lru_cache
def get_log_config() -> dict:
    app_settings = get_app_settings()

    print("Starting app in mode:", app_settings.mode)

    other_level = logging.INFO
    match app_settings.mode:
        case "debug":
            level = logging.DEBUG
        case "development":
            level = logging.INFO
        case "production":
            level = logging.WARNING
            other_level = logging.WARNING
        case _:
            raise ValueError(f"Unknown mode: {app_settings.mode}")

    if app_settings.logging_level_override is not None:
        print("Overriding logging level to:", app_settings.logging_level_override)
        level = logging.getLevelNamesMapping().get(app_settings.logging_level_override.upper(), level)

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
