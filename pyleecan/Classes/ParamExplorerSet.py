# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ParamExplorerSet.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ParamExplorerSet
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .ParamExplorer import ParamExplorer

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ParamExplorerSet.get_value import get_value
except ImportError as error:
    get_value = error

try:
    from ..Methods.Simulation.ParamExplorerSet.as_dict import as_dict
except ImportError as error:
    as_dict = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_min import get_min
except ImportError as error:
    get_min = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_max import get_max
except ImportError as error:
    get_max = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_N import get_N
except ImportError as error:
    get_N = error

try:
    from ..Methods.Simulation.ParamExplorerSet._set_value import _set_value
except ImportError as error:
    _set_value = error


from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class ParamExplorerSet(ParamExplorer):
    """Define a parameter set (for parameter sweep) from a list"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ParamExplorerSet.get_value
    if isinstance(get_value, ImportError):
        get_value = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_value: " + str(get_value)
                )
            )
        )
    else:
        get_value = get_value
    # cf Methods.Simulation.ParamExplorerSet.as_dict
    if isinstance(as_dict, ImportError):
        as_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method as_dict: " + str(as_dict)
                )
            )
        )
    else:
        as_dict = as_dict
    # cf Methods.Simulation.ParamExplorerSet.get_min
    if isinstance(get_min, ImportError):
        get_min = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_min: " + str(get_min)
                )
            )
        )
    else:
        get_min = get_min
    # cf Methods.Simulation.ParamExplorerSet.get_max
    if isinstance(get_max, ImportError):
        get_max = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_max: " + str(get_max)
                )
            )
        )
    else:
        get_max = get_max
    # cf Methods.Simulation.ParamExplorerSet.get_N
    if isinstance(get_N, ImportError):
        get_N = property(
            fget=lambda x: raise_(
                ImportError("Can't use ParamExplorerSet method get_N: " + str(get_N))
            )
        )
    else:
        get_N = get_N
    # cf Methods.Simulation.ParamExplorerSet._set_value
    if isinstance(_set_value, ImportError):
        _set_value = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method _set_value: " + str(_set_value)
                )
            )
        )
    else:
        _set_value = _set_value
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        value=-1,
        name="",
        symbol="",
        unit="",
        setter=None,
        getter=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "value" in list(init_dict.keys()):
                value = init_dict["value"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "setter" in list(init_dict.keys()):
                setter = init_dict["setter"]
            if "getter" in list(init_dict.keys()):
                getter = init_dict["getter"]
        # Set the properties (value check and convertion are done in setter)
        self.value = value
        # Call ParamExplorer init
        super(ParamExplorerSet, self).__init__(
            name=name, symbol=symbol, unit=unit, setter=setter, getter=getter
        )
        # The class is frozen (in ParamExplorer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ParamExplorerSet_str = ""
        # Get the properties inherited from ParamExplorer
        ParamExplorerSet_str += super(ParamExplorerSet, self).__str__()
        ParamExplorerSet_str += (
            "value = "
            + linesep
            + str(self.value).replace(linesep, linesep + "\t")
            + linesep
        )
        return ParamExplorerSet_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ParamExplorer
        if not super(ParamExplorerSet, self).__eq__(other):
            return False
        if other.value != self.value:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ParamExplorer
        diff_list.extend(super(ParamExplorerSet, self).compare(other, name=name))
        if other._value != self._value:
            diff_list.append(name + ".value")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ParamExplorer
        S += super(ParamExplorerSet, self).__sizeof__()
        if self.value is not None:
            for value in self.value:
                S += getsizeof(value)
        return S

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.value = None
        # Set to None the properties inherited from ParamExplorer
        super(ParamExplorerSet, self)._set_None()

    def _get_value(self):
        """getter of value"""
        return self._value

    value = property(
        fget=_get_value,
        fset=_set_value,
        doc=u"""List containing the different parameter values to explore

        :Type: list
        """,
    )
