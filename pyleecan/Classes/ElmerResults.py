# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Elmer/ElmerResults.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Elmer/ElmerResults
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
from .Elmer import Elmer

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Elmer.ElmerResults.load_data import load_data
except ImportError as error:
    load_data = error

try:
    from ..Methods.Elmer.ElmerResults.load_columns import load_columns
except ImportError as error:
    load_columns = error

try:
    from ..Methods.Elmer.ElmerResults.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ElmerResults(Elmer):
    """Class to get 'SaveScalars' and 'SaveLine' data"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Elmer.ElmerResults.load_data
    if isinstance(load_data, ImportError):
        load_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElmerResults method load_data: " + str(load_data)
                )
            )
        )
    else:
        load_data = load_data
    # cf Methods.Elmer.ElmerResults.load_columns
    if isinstance(load_columns, ImportError):
        load_columns = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElmerResults method load_columns: " + str(load_columns)
                )
            )
        )
    else:
        load_columns = load_columns
    # cf Methods.Elmer.ElmerResults.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElmerResults method get_data: " + str(get_data))
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        data=-1,
        file="",
        usecols=-1,
        columns=-1,
        is_scalars=False,
        logger_name="Pyleecan.Elmer",
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
            if "data" in list(init_dict.keys()):
                data = init_dict["data"]
            if "file" in list(init_dict.keys()):
                file = init_dict["file"]
            if "usecols" in list(init_dict.keys()):
                usecols = init_dict["usecols"]
            if "columns" in list(init_dict.keys()):
                columns = init_dict["columns"]
            if "is_scalars" in list(init_dict.keys()):
                is_scalars = init_dict["is_scalars"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.data = data
        self.file = file
        self.usecols = usecols
        self.columns = columns
        self.is_scalars = is_scalars
        # Call Elmer init
        super(ElmerResults, self).__init__(logger_name=logger_name)
        # The class is frozen (in Elmer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ElmerResults_str = ""
        # Get the properties inherited from Elmer
        ElmerResults_str += super(ElmerResults, self).__str__()
        ElmerResults_str += "data = " + str(self.data) + linesep
        ElmerResults_str += 'file = "' + str(self.file) + '"' + linesep
        ElmerResults_str += (
            "usecols = "
            + linesep
            + str(self.usecols).replace(linesep, linesep + "\t")
            + linesep
        )
        ElmerResults_str += (
            "columns = "
            + linesep
            + str(self.columns).replace(linesep, linesep + "\t")
            + linesep
        )
        ElmerResults_str += "is_scalars = " + str(self.is_scalars) + linesep
        return ElmerResults_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Elmer
        if not super(ElmerResults, self).__eq__(other):
            return False
        if other.data != self.data:
            return False
        if other.file != self.file:
            return False
        if other.usecols != self.usecols:
            return False
        if other.columns != self.columns:
            return False
        if other.is_scalars != self.is_scalars:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Elmer
        diff_list.extend(super(ElmerResults, self).compare(other, name=name))
        if other._data != self._data:
            diff_list.append(name + ".data")
        if other._file != self._file:
            diff_list.append(name + ".file")
        if other._usecols != self._usecols:
            diff_list.append(name + ".usecols")
        if other._columns != self._columns:
            diff_list.append(name + ".columns")
        if other._is_scalars != self._is_scalars:
            diff_list.append(name + ".is_scalars")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Elmer
        S += super(ElmerResults, self).__sizeof__()
        if self.data is not None:
            for key, value in self.data.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.file)
        if self.usecols is not None:
            for value in self.usecols:
                S += getsizeof(value)
        if self.columns is not None:
            for value in self.columns:
                S += getsizeof(value)
        S += getsizeof(self.is_scalars)
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

        # Get the properties inherited from Elmer
        ElmerResults_dict = super(ElmerResults, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ElmerResults_dict["data"] = self.data.copy() if self.data is not None else None
        ElmerResults_dict["file"] = self.file
        ElmerResults_dict["usecols"] = (
            self.usecols.copy() if self.usecols is not None else None
        )
        ElmerResults_dict["columns"] = (
            self.columns.copy() if self.columns is not None else None
        )
        ElmerResults_dict["is_scalars"] = self.is_scalars
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ElmerResults_dict["__class__"] = "ElmerResults"
        return ElmerResults_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.data = None
        self.file = None
        self.usecols = None
        self.columns = None
        self.is_scalars = None
        # Set to None the properties inherited from Elmer
        super(ElmerResults, self)._set_None()

    def _get_data(self):
        """getter of data"""
        return self._data

    def _set_data(self, value):
        """setter of data"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("data", value, "dict")
        self._data = value

    data = property(
        fget=_get_data,
        fset=_set_data,
        doc=u"""Dict with simulation results

        :Type: dict
        """,
    )

    def _get_file(self):
        """getter of file"""
        return self._file

    def _set_file(self, value):
        """setter of file"""
        check_var("file", value, "str")
        self._file = value

    file = property(
        fget=_get_file,
        fset=_set_file,
        doc=u"""Filename of the results data file

        :Type: str
        """,
    )

    def _get_usecols(self):
        """getter of usecols"""
        return self._usecols

    def _set_usecols(self, value):
        """setter of usecols"""
        if type(value) is int and value == -1:
            value = list()
        check_var("usecols", value, "list")
        self._usecols = value

    usecols = property(
        fget=_get_usecols,
        fset=_set_usecols,
        doc=u"""List integers (starting with 1) of columns to load. If usecols is not set all columns are loaded.

        :Type: list
        """,
    )

    def _get_columns(self):
        """getter of columns"""
        return self._columns

    def _set_columns(self, value):
        """setter of columns"""
        if type(value) is int and value == -1:
            value = list()
        check_var("columns", value, "list")
        self._columns = value

    columns = property(
        fget=_get_columns,
        fset=_set_columns,
        doc=u"""List of columns data names

        :Type: list
        """,
    )

    def _get_is_scalars(self):
        """getter of is_scalars"""
        return self._is_scalars

    def _set_is_scalars(self, value):
        """setter of is_scalars"""
        check_var("is_scalars", value, "bool")
        self._is_scalars = value

    is_scalars = property(
        fget=_get_is_scalars,
        fset=_set_is_scalars,
        doc=u"""Determin if data are 'SaveScalars' data, else 'SaveLine' data are assumed

        :Type: bool
        """,
    )
