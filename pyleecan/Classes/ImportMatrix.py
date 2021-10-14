# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMatrix.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMatrix
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
from .Import import Import

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportMatrix.edit_matrix import edit_matrix
except ImportError as error:
    edit_matrix = error


from ._check import InitUnKnowClassError


class ImportMatrix(Import):
    """Abstract class to Import/Generate 1D or D matrix"""

    VERSION = 1

    # cf Methods.Import.ImportMatrix.edit_matrix
    if isinstance(edit_matrix, ImportError):
        edit_matrix = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportMatrix method edit_matrix: " + str(edit_matrix)
                )
            )
        )
    else:
        edit_matrix = edit_matrix
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, is_transpose=False, init_dict=None, init_str=None):
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
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.is_transpose = is_transpose
        # Call Import init
        super(ImportMatrix, self).__init__()
        # The class is frozen (in Import init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportMatrix_str = ""
        # Get the properties inherited from Import
        ImportMatrix_str += super(ImportMatrix, self).__str__()
        ImportMatrix_str += "is_transpose = " + str(self.is_transpose) + linesep
        return ImportMatrix_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Import
        if not super(ImportMatrix, self).__eq__(other):
            return False
        if other.is_transpose != self.is_transpose:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Import
        diff_list.extend(super(ImportMatrix, self).compare(other, name=name))
        if other._is_transpose != self._is_transpose:
            diff_list.append(name + ".is_transpose")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Import
        S += super(ImportMatrix, self).__sizeof__()
        S += getsizeof(self.is_transpose)
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

        # Get the properties inherited from Import
        ImportMatrix_dict = super(ImportMatrix, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportMatrix_dict["is_transpose"] = self.is_transpose
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportMatrix_dict["__class__"] = "ImportMatrix"
        return ImportMatrix_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_transpose = None
        # Set to None the properties inherited from Import
        super(ImportMatrix, self)._set_None()

    def _get_is_transpose(self):
        """getter of is_transpose"""
        return self._is_transpose

    def _set_is_transpose(self, value):
        """setter of is_transpose"""
        check_var("is_transpose", value, "bool")
        self._is_transpose = value

    is_transpose = property(
        fget=_get_is_transpose,
        fset=_set_is_transpose,
        doc=u"""1 to transpose the Imported/Generated matrix

        :Type: bool
        """,
    )
