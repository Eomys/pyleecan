# -*- coding: utf-8 -*-
from .loggers import gen_logger_config_dict, DEFAULT_LOG_NAME, GUI_LOG_NAME
from logging.config import dictConfig
from os.path import isdir

# Init default loggers
log_dict = gen_logger_config_dict(DEFAULT_LOG_NAME)
log_dict["loggers"][""] = {"level": "NOTSET", "handlers": []}  # root logger
log_dict["loggers"][GUI_LOG_NAME] = {
    "level": "DEBUG",
    "propagate": True,
    "handlers": [],
}
dictConfig(log_dict)

__version__ = "1.0.4"
