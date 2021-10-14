# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ParamExplorerInterval.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ParamExplorerInterval
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
    from ..Methods.Simulation.ParamExplorerInterval.get_value import get_value
except ImportError as error:
    get_value = error

try:
    from ..Methods.Simulation.ParamExplorerInterval.get_min import get_min
except ImportError as error:
    get_min = error

try:
    from ..Methods.Simulation.ParamExplorerInterval.get_max import get_max
except ImportError as error:
    get_max = error

try:
    from ..Methods.Simulation.ParamExplorerInterval.get_N import get_N
except ImportError as error:
    get_N = error


from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class ParamExplorerInterval(ParamExplorer):
    """Define a set of value (for parameter sweep) on interval"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ParamExplorerInterval.get_value
    if isinstance(get_value, ImportError):
        get_value = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerInterval method get_value: "
                    + str(get_value)
                )
            )
        )
    else:
        get_value = get_value
    # cf Methods.Simulation.ParamExplorerInterval.get_min
    if isinstance(get_min, ImportError):
        get_min = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerInterval method get_min: " + str(get_min)
                )
            )
        )
    else:
        get_min = get_min
    # cf Methods.Simulation.ParamExplorerInterval.get_max
    if isinstance(get_max, ImportError):
        get_max = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerInterval method get_max: " + str(get_max)
                )
            )
        )
    else:
        get_max = get_max
    # cf Methods.Simulation.ParamExplorerInterval.get_N
    if isinstance(get_N, ImportError):
        get_N = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerInterval method get_N: " + str(get_N)
                )
            )
        )
    else:
        get_N = get_N
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        min_value=0,
        max_value=1,
        N=4,
        type_value_gen=0,
        type_value=0,
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
            if "min_value" in list(init_dict.keys()):
                min_value = init_dict["min_value"]
            if "max_value" in list(init_dict.keys()):
                max_value = init_dict["max_value"]
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "type_value_gen" in list(init_dict.keys()):
                type_value_gen = init_dict["type_value_gen"]
            if "type_value" in list(init_dict.keys()):
                type_value = init_dict["type_value"]
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
        self.min_value = min_value
        self.max_value = max_value
        self.N = N
        self.type_value_gen = type_value_gen
        self.type_value = type_value
        # Call ParamExplorer init
        super(ParamExplorerInterval, self).__init__(
            name=name, symbol=symbol, unit=unit, setter=setter, getter=getter
        )
        # The class is frozen (in ParamExplorer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ParamExplorerInterval_str = ""
        # Get the properties inherited from ParamExplorer
        ParamExplorerInterval_str += super(ParamExplorerInterval, self).__str__()
        ParamExplorerInterval_str += "min_value = " + str(self.min_value) + linesep
        ParamExplorerInterval_str += "max_value = " + str(self.max_value) + linesep
        ParamExplorerInterval_str += "N = " + str(self.N) + linesep
        ParamExplorerInterval_str += (
            "type_value_gen = " + str(self.type_value_gen) + linesep
        )
        ParamExplorerInterval_str += "type_value = " + str(self.type_value) + linesep
        return ParamExplorerInterval_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ParamExplorer
        if not super(ParamExplorerInterval, self).__eq__(other):
            return False
        if other.min_value != self.min_value:
            return False
        if other.max_value != self.max_value:
            return False
        if other.N != self.N:
            return False
        if other.type_value_gen != self.type_value_gen:
            return False
        if other.type_value != self.type_value:
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
        diff_list.extend(super(ParamExplorerInterval, self).compare(other, name=name))
        if other._min_value != self._min_value:
            diff_list.append(name + ".min_value")
        if other._max_value != self._max_value:
            diff_list.append(name + ".max_value")
        if other._N != self._N:
            diff_list.append(name + ".N")
        if other._type_value_gen != self._type_value_gen:
            diff_list.append(name + ".type_value_gen")
        if other._type_value != self._type_value:
            diff_list.append(name + ".type_value")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ParamExplorer
        S += super(ParamExplorerInterval, self).__sizeof__()
        S += getsizeof(self.min_value)
        S += getsizeof(self.max_value)
        S += getsizeof(self.N)
        S += getsizeof(self.type_value_gen)
        S += getsizeof(self.type_value)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from ParamExplorer
        ParamExplorerInterval_dict = super(ParamExplorerInterval, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ParamExplorerInterval_dict["min_value"] = self.min_value
        ParamExplorerInterval_dict["max_value"] = self.max_value
        ParamExplorerInterval_dict["N"] = self.N
        ParamExplorerInterval_dict["type_value_gen"] = self.type_value_gen
        ParamExplorerInterval_dict["type_value"] = self.type_value
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ParamExplorerInterval_dict["__class__"] = "ParamExplorerInterval"
        return ParamExplorerInterval_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.min_value = None
        self.max_value = None
        self.N = None
        self.type_value_gen = None
        self.type_value = None
        # Set to None the properties inherited from ParamExplorer
        super(ParamExplorerInterval, self)._set_None()

    def _get_min_value(self):
        """getter of min_value"""
        return self._min_value

    def _set_min_value(self, value):
        """setter of min_value"""
        check_var("min_value", value, "float")
        self._min_value = value

    min_value = property(
        fget=_get_min_value,
        fset=_set_min_value,
        doc=u"""Minumum value of the interval

        :Type: float
        """,
    )

    def _get_max_value(self):
        """getter of max_value"""
        return self._max_value

    def _set_max_value(self, value):
        """setter of max_value"""
        check_var("max_value", value, "float")
        self._max_value = value

    max_value = property(
        fget=_get_max_value,
        fset=_set_max_value,
        doc=u"""Maximum value of the interval

        :Type: float
        """,
    )

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=2)
        self._N = value

    N = property(
        fget=_get_N,
        fset=_set_N,
        doc=u"""Number of value to take in the interval

        :Type: int
        :min: 2
        """,
    )

    def _get_type_value_gen(self):
        """getter of type_value_gen"""
        return self._type_value_gen

    def _set_type_value_gen(self, value):
        """setter of type_value_gen"""
        check_var("type_value_gen", value, "int", Vmin=0, Vmax=1)
        self._type_value_gen = value

    type_value_gen = property(
        fget=_get_type_value_gen,
        fset=_set_type_value_gen,
        doc=u"""How to generate the value list. 0: linspace, 1: random (Not available yet)

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_type_value(self):
        """getter of type_value"""
        return self._type_value

    def _set_type_value(self, value):
        """setter of type_value"""
        check_var("type_value", value, "int", Vmin=0, Vmax=1)
        self._type_value = value

    type_value = property(
        fget=_get_type_value,
        fset=_set_type_value,
        doc=u"""Type of the value: 0:float, 1:int

        :Type: int
        :min: 0
        :max: 1
        """,
    )
