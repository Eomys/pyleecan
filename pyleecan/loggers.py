from logging import Filter, DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging.config import dictConfig
from os import makedirs
from os.path import isdir

# Default level in every loggers
DEFAULT_LOG_NAME = "Pyleecan"
GUI_LOG_NAME = DEFAULT_LOG_NAME + ".GUI"
SUB_LOG_LIST = ["Machine", "Electrical", "Magnetics", "Force", "Structural", "Loss"]

CONSOLE_LEVEL = INFO
CONSOLE_FORMAT = "[%(asctime)s] %(message)s"
CONSOLE_DATE_FORMAT = "%H:%M:%S"

FILE_LEVEL = DEBUG
FILE_FORMAT = "%(asctime)s-%(levelname)7s: %(message)s [%(name)s]"
FILE_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def gen_logger_config_dict(logger_name):
    module = __import__(
        "pyleecan", globals=globals(), locals=locals(), fromlist=["USER_DIR"], level=0,
    )
    USER_DIR = module.USER_DIR
    if not isdir(USER_DIR):
        makedirs(USER_DIR)
    log_config_dict = {
        "version": 1,
        # Define loggers
        "loggers": {
            logger_name: {  # Default logger
                "level": "DEBUG",
                "propagate": False,
                "handlers": [
                    "console_handler",
                    "file_handler",
                ],  # Different handler enable to use differents formats, and to handle different stream (stdout, stderr,...)
            },
        },
        # Handlers definition
        "handlers": {
            "console_handler": {
                "level": CONSOLE_LEVEL,
                "formatter": "console_formatter",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "file_handler": {  # <------- FileHandler
                "level": FILE_LEVEL,
                "formatter": "file_formatter",
                "class": "logging.FileHandler",
                "filename": USER_DIR + "/Pyleecan.log",  # log file
                "mode": "a",
            },
        },
        # Define formatters
        "formatters": {
            "console_formatter": {
                "format": CONSOLE_FORMAT,
                "datefmt": CONSOLE_DATE_FORMAT,
            },
            "file_formatter": {"format": FILE_FORMAT, "datefmt": FILE_DATE_FORMAT},
        },
        "disable_existing_loggers": False,
    }

    for log in SUB_LOG_LIST:
        log_config_dict["loggers"][logger_name + "." + log] = {
            "level": "DEBUG",
            "propagate": True,
            "handlers": [],
        }
    return log_config_dict


def init_default_log():
    # Init default loggers
    log_dict = gen_logger_config_dict(DEFAULT_LOG_NAME)
    log_dict["loggers"][""] = {"level": "NOTSET", "handlers": []}  # root logger
    log_dict["loggers"][GUI_LOG_NAME] = {
        "level": "DEBUG",
        "propagate": True,
        "handlers": [],
    }
    dictConfig(log_dict)
