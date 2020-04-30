from logging import Filter, DEBUG, INFO, WARNING, ERROR, CRITICAL

"""
File containing every Pyleecan loggers.
The choice between LOGGING_CONFIG_CONSOLE and LOGGING_CONFIG_FILE is made in pyleecan.__init__.py
"""

# Default level in every loggers
DEFAULT_LEVEL = "INFO"


class LevelFilter(Filter):
    """Class to filter a unique log level"""

    def __init__(self, level):
        """
        LevelFilter constructor
        
        Parameters: 
            level : int
                log level to keep
        """
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


# LOGGING_CONFIG_CONSOLE display every logs in the console
LOGGING_CONFIG_CONSOLE = {
    "version": 1,
    # Define loggers
    "loggers": {
        "": {"level": "NOTSET", "handlers": []},  # root logger
        "Pyleecan": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": [  # Different handler enable to use differents formats, and to handle different stream (stdout, stderr,...)
                "debug_console_handler",
                "info_console_handler",
                "warning_console_handler",
                "error_console_handler",
                "critical_console_handler",
            ],
        },
        "Pyleecan.Output": {"level": DEFAULT_LEVEL, "propagate": True, "handlers": []},
        "Pyleecan.Simulation": {
            "level": DEFAULT_LEVEL,
            "propagate": True,
            "handlers": [],
        },
        "Pyleecan.Machine": {"level": DEFAULT_LEVEL, "propagate": True, "handlers": []},
        "Pyleecan.OutElec": {
            "level": DEFAULT_LEVEL,
            "propagate": True,
            "handlers": [],  # Different handler enable to use differents formats, and to handle different stream (stdout, stderr,...)
        },
        "Pyleecan.OutMag": {"level": DEFAULT_LEVEL, "propagate": True, "handlers": []},
        "Pyleecan.OutStruct": {
            "level": DEFAULT_LEVEL,
            "propagate": True,
            "handlers": [],
        },
        "Pyleecan.OutGeo": {"level": DEFAULT_LEVEL, "propagate": True, "handlers": []},
        "Pyleecan.OptiGenAlg": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["opti_file_handler"],  # <-- redirection in a file
        },
    },
    # Handlers definition
    "handlers": {
        "debug_console_handler": {
            "level": "DEBUG",
            "formatter": "default_formatter",
            "filters": ["debug_filter"],
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "info_console_handler": {
            "level": "INFO",
            "formatter": "default_formatter",
            "filters": ["info_filter"],
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "warning_console_handler": {
            "level": "WARNING",
            "formatter": "default_formatter",
            "filters": ["warning_filter"],
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "error_console_handler": {
            "level": "ERROR",
            "formatter": "default_formatter",
            "filters": ["error_filter"],
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "critical_console_handler": {
            "level": "CRITICAL",
            "formatter": "default_formatter",
            "filters": ["critical_filter"],
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "opti_file_handler": {  # <------- FileHandler
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",  # log file
            "mode": "a",
        },
        #         'info_rotating_file_handler': {
        #             'level': 'INFO',
        #             'formatter': 'info',
        #             'class': 'logging.handlers.RotatingFileHandler',
        #             'filename': 'info.log',
        #             'mode': 'a',
        #             'maxBytes': 1048576,
        #             'backupCount': 10
        #         },
    },
    # Define filters
    "filters": {
        "debug_filter": {"()": LevelFilter, "level": DEBUG},
        "info_filter": {"()": LevelFilter, "level": INFO},
        "warning_filter": {"()": LevelFilter, "level": WARNING},
        "error_filter": {"()": LevelFilter, "level": ERROR},
        "critical_filter": {"()": LevelFilter, "level": CRITICAL},
    },
    # Define formatters
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s-%(levelname)s-%(name)s: %(message)s"
        },
        "file_formatter": {"format": "%(asctime)s-%(levelname)s-%(name)s: %(message)s"},
    },
}

# LOGGING_CONFIG_CONSOLE display every logs in the console
LOGGING_CONFIG_FILE = {
    "version": 1,
    # Define loggers
    "loggers": {
        "": {"level": "NOTSET", "handlers": []},  # root logger
        "Pyleecan": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["Pyleecan_fh"],
        },
        "Pyleecan.Output": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["Output_fh"],
        },
        "Pyleecan.Simulation": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["Simulation_fh"],
        },
        "Pyleecan.Machine": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["Machine_fh"],
        },
        "Pyleecan.OutElec": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["OutElec_fh"],
        },
        "Pyleecan.OutMag": {"level": DEFAULT_LEVEL, "propagate": False, "handlers": []},
        "Pyleecan.OutStruct": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["OutStruct_fh"],
        },
        "Pyleecan.OutGeo": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["OutGeo_fh"],
        },
        "Pyleecan.OptiGenAlg": {
            "level": DEFAULT_LEVEL,
            "propagate": False,
            "handlers": ["opti_file_handler"],  # <-- redirection in a file
        },
    },
    # Handlers definition
    "handlers": {
        #         'info_rotating_file_handler': {
        #             'level': 'INFO',
        #             'formatter': 'info',
        #             'class': 'logging.handlers.RotatingFileHandler',
        #             'filename': 'info.log',
        #             'mode': 'a',
        #             'maxBytes': 1048576,
        #             'backupCount': 10
        #         },
        "Pyleecan_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "Output_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "Simulation_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "OutElec_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "OutMag_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "OutStruct_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "Machine_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        "Opti_fh": {
            "level": "DEBUG",
            "formatter": "file_formatter",
            "class": "logging.FileHandler",
            "filename": "Pyleecan_optimization.log",
            "mode": "a",
        },
        #         'info_rotating_file_handler': {
        #             'level': 'INFO',
        #             'formatter': 'info',
        #             'class': 'logging.handlers.RotatingFileHandler',
        #             'filename': 'info.log',
        #             'mode': 'a',
        #             'maxBytes': 1048576,
        #             'backupCount': 10
        #         },
    },
    # Define filters
    "filters": {
        "debug_filter": {"()": LevelFilter, "level": DEBUG},
        "info_filter": {"()": LevelFilter, "level": INFO},
        "warning_filter": {"()": LevelFilter, "level": WARNING},
        "error_filter": {"()": LevelFilter, "level": ERROR},
        "critical_filter": {"()": LevelFilter, "level": CRITICAL},
    },
    # Define formatters
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s-%(levelname)s-%(name)s: %(message)s"
        },
        "file_formatter": {"format": "%(asctime)s-%(levelname)s-%(name)s: %(message)s"},
    },
}
