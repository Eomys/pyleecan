# Init conventions for input generation
ROT_DIR_REF = -1
CURRENT_DIR_REF = -1
PHASE_DIR_REF = -1


class InputError(Exception):
    """Raised when the input data are incomplete or incorrect"""

    pass
