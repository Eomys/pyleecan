# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Elmer/ElmerResults.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Elmer/ElmerResults
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

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


class ElmerResults(FrozenClass):
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

    def __init__(self, data=-1, file="", columns=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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
            if "columns" in list(init_dict.keys()):
                columns = init_dict["columns"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.data = data
        self.file = file
        self.columns = columns

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ElmerResults_str = ""
        if self.parent is None:
            ElmerResults_str += "parent = None " + linesep
        else:
            ElmerResults_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        ElmerResults_str += "data = " + str(self.data) + linesep
        ElmerResults_str += 'file = "' + str(self.file) + '"' + linesep
        ElmerResults_str += (
            "columns = "
            + linesep
            + str(self.columns).replace(linesep, linesep + "\t")
            + linesep
        )
        return ElmerResults_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.data != self.data:
            return False
        if other.file != self.file:
            return False
        if other.columns != self.columns:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        ElmerResults_dict = dict()
        ElmerResults_dict["data"] = self.data.copy() if self.data is not None else None
        ElmerResults_dict["file"] = self.file
        ElmerResults_dict["columns"] = (
            self.columns.copy() if self.columns is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        ElmerResults_dict["__class__"] = "ElmerResults"
        return ElmerResults_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.data = None
        self.file = None
        self.columns = None

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
