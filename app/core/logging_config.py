import logging
from logging.config import dictConfig


class LogConfig:
    """Logging configuration to be set for the server"""

    VERSION = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    }
    loggers = {
        "app": {"handlers": ["default"], "level": "INFO"},
    }


dictConfig(
    {
        "version": LogConfig.VERSION,
        "disable_existing_loggers": LogConfig.disable_existing_loggers,
        "formatters": LogConfig.formatters,
        "handlers": LogConfig.handlers,
        "loggers": LogConfig.loggers,
    },
)

logger = logging.getLogger("app")
