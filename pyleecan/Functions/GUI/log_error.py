import traceback
from logging import getLogger

from PySide2.QtWidgets import QMessageBox, QWidget
from ...loggers import GUI_LOG_NAME


def log_error(widget, error_message, logger=None, is_popup=True, is_warning=False):
    """Handle errors in try except to show the trace to help for debugging

    Parameters
    ----------
    widget: object
        object that throw the error
    error_message: str
        the message that will be show in the Messagebox
    logger: logger object
        where the logger is
    is_popup : bool
        True to open a QMessageBox
    is_warning : bool
        True to use a Warning message box instead of critical
    """

    if logger is None:
        logger = getLogger(GUI_LOG_NAME)
    # Log the error message and source
    logger.error(error_message)
    if widget is not None:
        if is_warning:
            logger.debug("Warning in widget " + str(type(widget)))
        else:
            logger.debug("Error in widget " + str(type(widget)))
    # Add trace to the logger
    text_exception = traceback.format_exc()
    exceptions_details = "".join(text_exception).split(r"\n")
    for exception_line in exceptions_details:
        logger.debug(exception_line)

    # QDialog is not compatible with QMessageBox critical
    if is_popup:
        if not isinstance(widget, QWidget):
            widget = QWidget()
        if is_warning:
            QMessageBox().warning(
                widget,
                "Warning",
                error_message,
            )
        else:
            QMessageBox().critical(
                widget,
                "Error",
                error_message,
            )
