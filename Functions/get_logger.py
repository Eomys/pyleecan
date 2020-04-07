from logging import getLogger


def get_logger(obj):
    """Get the object logger or its parent's one

    Parameters
    ----------
    obj : 
        A pyleecan object
    
    Returns
    -------
    logger : logging.Logger
        Pyleecan object dedicated logger
    """

    if hasattr(obj, "logger_name"):  # Object logger
        return getLogger(obj.logger_name)
    elif obj.parent != None:  # Parent logger
        return obj.parent.get_logger()
    else:  # Default logger
        return getLogger("Pyleecan")
