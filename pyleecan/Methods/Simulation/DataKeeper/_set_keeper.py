from ....Classes._check import CheckTypeError
from ntpath import basename
from ....Functions.path_tools import abs_file_path
from ....Generator import PYTHON_DEFAULT_ENCODING

# Import numpy to be usable in the fct/lambda
import numpy as np
from numpy import sqrt, pi


def _set_keeper(self, value):
    """setter of keeper"""
    # Create the function if setter is defined as a string (e.g. simu.machine.rotor.slot.W0)
    if isinstance(value, str) and value[:4] == "simu":
        value_split = value.split(".")
        value = (
            "lambda simu, val: setattr(eval('"
            + ".".join(value_split[:-1])
            + "'), '"
            + value_split[-1]
            + "', val"
            + ")"
        )
    if value is None:
        self._keeper_str = None
        self._keeper_func = None
    elif isinstance(value, str) and "lambda" in value:
        self._keeper_str = value
        self._keeper_func = eval(value)
    elif isinstance(value, str) and value[-3:] == ".py":
        if "<" in value and ">" in value:
            # path like "<PARAM_DIR>/keeper_rotor.py"
            self._keeper_str = value
            value = abs_file_path(value)
        else:  # Direct path
            self._keeper_str = value
        f = open(value, "r", encoding=PYTHON_DEFAULT_ENCODING)
        exec(f.read(), globals())
        f.close()
        self._keeper_func = eval(basename(value[:-3]))
    elif callable(value):
        self._keeper_str = None
        self._keeper_func = value
    else:
        raise CheckTypeError(
            "For property keeper Expected function or str (path to python file or lambda), got: "
            + str(type(value))
        )
