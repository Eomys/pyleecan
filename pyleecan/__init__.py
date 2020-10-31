# -*- coding: utf-8 -*-
from .loggers import LOGGING_CONFIG_CONSOLE, LOGGING_CONFIG_FILE
from logging.config import dictConfig
from os.path import isdir


dictConfig(LOGGING_CONFIG_CONSOLE)

__version__ = "1.0.2"
