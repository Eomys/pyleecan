# -*- coding: utf-8 -*-

import sys
from logging import ERROR, INFO, basicConfig, getLogger
from matplotlib import use
from ..Classes.GUIOption import GUIOption
from ..definitions import config_dict
from os.path import abspath, dirname, join, normpath

# Set Matplotlib backend
use("Qt5Agg")  # Use PySide2 backend


class StreamToLogger(object):
    """Fake file-like stream object that redirects writes to a logger instance."""

    def __init__(self, logger, log_level=INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ""

    def write(self, buf):
        """

        Parameters
        ----------
        buf :


        Returns
        -------

        """
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        """ """
        pass


gui_option = GUIOption()
gui_option.unit.unit_m = config_dict["GUI"]["UNIT_M"]  # Use mm
gui_option.unit.unit_m2 = config_dict["GUI"]["UNIT_M2"]  # Use mm²

# Default config for all logger
basicConfig(
    level=INFO,
    # Format log like: "2013-03-08 11:37:31,311 : INFO : Hello"
    format="%(asctime)s : %(levelname)s : %(message)s",
    datefmt="%m-%d %H:%M",
    filename="pyleecan_gui.log",
    filemode="a",
)

# Setup logger
GUI_logger = getLogger("GUI_logger")

# stdout_logger = getLogger("STDOUT")
# sl = StreamToLogger(stdout_logger, INFO)
# sys.stdout = sl

# stderr_logger = getLogger("STDERR")
# sl = StreamToLogger(stderr_logger, ERROR)
# sys.stderr = sl


def my_excepthook(type, value, tback):
    """When an exception occurs: Log the error and continue (doesn't kill the
    GUI)

    Parameters
    ----------
    type :

    value :

    tback :


    Returns
    -------

    """
    # log the exception here (Not needed with stderr redirect)

    # then call the default handler
    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook
