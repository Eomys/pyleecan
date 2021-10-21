# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiObjective.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiObjective
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
from .DataKeeper import DataKeeper

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class OptiObjective(DataKeeper):
    """Class to distinguish normal DataKeeper from optimization objectives """

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        symbol="",
        unit="",
        keeper=None,
        error_keeper=None,
        result=-1,
        result_ref=None,
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
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "keeper" in list(init_dict.keys()):
                keeper = init_dict["keeper"]
            if "error_keeper" in list(init_dict.keys()):
                error_keeper = init_dict["error_keeper"]
            if "result" in list(init_dict.keys()):
                result = init_dict["result"]
            if "result_ref" in list(init_dict.keys()):
                result_ref = init_dict["result_ref"]
        # Set the properties (value check and convertion are done in setter)
        # Call DataKeeper init
        super(OptiObjective, self).__init__(
            name=name,
            symbol=symbol,
            unit=unit,
            keeper=keeper,
            error_keeper=error_keeper,
            result=result,
            result_ref=result_ref,
        )
        # The class is frozen (in DataKeeper init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiObjective_str = ""
        # Get the properties inherited from DataKeeper
        OptiObjective_str += super(OptiObjective, self).__str__()
        return OptiObjective_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from DataKeeper
        if not super(OptiObjective, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from DataKeeper
        diff_list.extend(super(OptiObjective, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from DataKeeper
        S += super(OptiObjective, self).__sizeof__()
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

        # Get the properties inherited from DataKeeper
        OptiObjective_dict = super(OptiObjective, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiObjective_dict["__class__"] = "OptiObjective"
        return OptiObjective_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from DataKeeper
        super(OptiObjective, self)._set_None()
