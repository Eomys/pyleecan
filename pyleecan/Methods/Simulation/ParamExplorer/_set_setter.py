from os import linesep
from logging import getLogger
from ....Classes._check import check_var, raise_

from inspect import getsource
from cloudpickle import dumps, loads
from ....Classes._check import CheckTypeError
from ....Classes._check import InitUnKnowClassError


def _set_setter(self, value):
    """setter of setter"""
    # Create the function if setter is defined as a string (e.g. simu.machine.rotor.slot.W0)
    if isinstance(value, str):
        if not value.startswith("simu"):
            raise Exception("Setter string must start with 'simu'")

        *objs, attr = value.split(".")

        accessor = ".".join(objs)
        value = lambda simu, val: setattr(eval(accessor), attr, val)

    try:
        check_var("func", value, "list")
    except CheckTypeError:
        check_var("func", value, "function")
    if isinstance(value, list):  # Load function from saved dict
        self._setter = [loads(value[0].encode("ISO-8859-2")), value[1]]
    elif value is None:
        self._setter = [None, None]
    elif callable(value):
        self._setter = [value, getsource(value)]
    else:
        raise TypeError(
            "Expected function or list from a saved file, got: " + str(type(value))
        )
