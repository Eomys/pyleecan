# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMatrixVal.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMatrixVal
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportMatrixVal.get_data import get_data
except ImportError as error:
    get_data = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ImportMatrixVal(ImportMatrix):
    """Import directly the value from the object"""

    VERSION = 1

    # cf Methods.Import.ImportMatrixVal.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportMatrixVal method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, value=None, is_transpose=False, init_dict=None, init_str=None):
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
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.value = value
        # Call ImportMatrix init
        super(ImportMatrixVal, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportMatrixVal_str = ""
        # Get the properties inherited from ImportMatrix
        ImportMatrixVal_str += super(ImportMatrixVal, self).__str__()
        ImportMatrixVal_str += (
            "value = "
            + linesep
            + str(self.value).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ImportMatrixVal_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportMatrixVal, self).__eq__(other):
            return False
        if not array_equal(other.value, self.value):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ImportMatrix
        diff_list.extend(super(ImportMatrixVal, self).compare(other, name=name))
        if not array_equal(other.value, self.value):
            diff_list.append(name + ".value")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportMatrixVal, self).__sizeof__()
        S += getsizeof(self.value)
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

        # Get the properties inherited from ImportMatrix
        ImportMatrixVal_dict = super(ImportMatrixVal, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.value is None:
            ImportMatrixVal_dict["value"] = None
        else:
            if type_handle_ndarray == 0:
                ImportMatrixVal_dict["value"] = self.value.tolist()
            elif type_handle_ndarray == 1:
                ImportMatrixVal_dict["value"] = self.value.copy()
            elif type_handle_ndarray == 2:
                ImportMatrixVal_dict["value"] = self.value
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportMatrixVal_dict["__class__"] = "ImportMatrixVal"
        return ImportMatrixVal_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.value = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportMatrixVal, self)._set_None()

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("value", value, "ndarray")
        self._value = value

    value = property(
        fget=_get_value,
        fset=_set_value,
        doc=u"""The matrix to return

        :Type: ndarray
        """,
    )
