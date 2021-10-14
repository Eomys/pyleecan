# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMagElmer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMagElmer
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
from .OutInternal import OutInternal

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutMagElmer.clean import clean
except ImportError as error:
    clean = error


from ._check import InitUnKnowClassError


class OutMagElmer(OutInternal):
    """Class to store outputs related to MagElmer magnetic model"""

    VERSION = 1

    # cf Methods.Output.OutMagElmer.clean
    if isinstance(clean, ImportError):
        clean = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMagElmer method clean: " + str(clean))
            )
        )
    else:
        clean = clean
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, FEA_dict=None, init_dict=None, init_str=None):
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
            if "FEA_dict" in list(init_dict.keys()):
                FEA_dict = init_dict["FEA_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.FEA_dict = FEA_dict
        # Call OutInternal init
        super(OutMagElmer, self).__init__()
        # The class is frozen (in OutInternal init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutMagElmer_str = ""
        # Get the properties inherited from OutInternal
        OutMagElmer_str += super(OutMagElmer, self).__str__()
        OutMagElmer_str += "FEA_dict = " + str(self.FEA_dict) + linesep
        return OutMagElmer_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutInternal
        if not super(OutMagElmer, self).__eq__(other):
            return False
        if other.FEA_dict != self.FEA_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OutInternal
        diff_list.extend(super(OutMagElmer, self).compare(other, name=name))
        if other._FEA_dict != self._FEA_dict:
            diff_list.append(name + ".FEA_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OutInternal
        S += super(OutMagElmer, self).__sizeof__()
        if self.FEA_dict is not None:
            for key, value in self.FEA_dict.items():
                S += getsizeof(value) + getsizeof(key)
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

        # Get the properties inherited from OutInternal
        OutMagElmer_dict = super(OutMagElmer, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OutMagElmer_dict["FEA_dict"] = (
            self.FEA_dict.copy() if self.FEA_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutMagElmer_dict["__class__"] = "OutMagElmer"
        return OutMagElmer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEA_dict = None
        # Set to None the properties inherited from OutInternal
        super(OutMagElmer, self)._set_None()

    def _get_FEA_dict(self):
        """getter of FEA_dict"""
        return self._FEA_dict

    def _set_FEA_dict(self, value):
        """setter of FEA_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEA_dict", value, "dict")
        self._FEA_dict = value

    FEA_dict = property(
        fget=_get_FEA_dict,
        fset=_set_FEA_dict,
        doc=u"""dictionary containing the main FEA parameters

        :Type: dict
        """,
    )
