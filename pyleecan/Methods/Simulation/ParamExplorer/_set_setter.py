from os.path import isfile
from importlib import import_module
from ....Classes._check import CheckTypeError
from ntpath import basename


def _set_setter(self, value):
    """setter of setter"""
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
        self._setter_str = None
        self._setter_func = None
    elif isinstance(value, str) and "lambda" in value:
        self._setter_str = value
        self._setter_func = eval(value)
    elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
        self._setter_str = value
        f = open(value, "r")
        exec(f.read(), globals())
        self._setter_func = eval(basename(value[:-3]))
    elif callable(value):
        self._setter_str = None
        self._setter_func = value
    else:
        raise CheckTypeError(
            "For property setter Expected function or str (path to python file or lambda), got: "
            + str(type(value))
        )
