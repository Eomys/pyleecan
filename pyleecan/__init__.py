# -*- coding: utf-8 -*-
from .loggers import LOGGING_CONFIG_CONSOLE, LOGGING_CONFIG_FILE
from logging.config import dictConfig
from .definitions import PYLEECAN_USER_DIR
from os.path import isdir

dictConfig(LOGGING_CONFIG_CONSOLE)  ##

if not isdir(PYLEECAN_USER_DIR):  # Create Pyleecan user folder
    from .definitions import create_folder

    create_folder()
