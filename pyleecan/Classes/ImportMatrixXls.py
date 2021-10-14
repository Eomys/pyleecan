# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMatrixXls.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMatrixXls
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
from .ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportMatrixXls.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportMatrixXls(ImportMatrix):
    """Import the data from an xls file"""

    VERSION = 1

    # cf Methods.Import.ImportMatrixXls.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportMatrixXls method get_data: " + str(get_data)
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

    def __init__(
        self,
        file_path="",
        sheet="",
        skiprows=0,
        usecols=None,
        axes_colrows=None,
        is_allsheets=False,
        is_transpose=False,
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
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
            if "sheet" in list(init_dict.keys()):
                sheet = init_dict["sheet"]
            if "skiprows" in list(init_dict.keys()):
                skiprows = init_dict["skiprows"]
            if "usecols" in list(init_dict.keys()):
                usecols = init_dict["usecols"]
            if "axes_colrows" in list(init_dict.keys()):
                axes_colrows = init_dict["axes_colrows"]
            if "is_allsheets" in list(init_dict.keys()):
                is_allsheets = init_dict["is_allsheets"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.file_path = file_path
        self.sheet = sheet
        self.skiprows = skiprows
        self.usecols = usecols
        self.axes_colrows = axes_colrows
        self.is_allsheets = is_allsheets
        # Call ImportMatrix init
        super(ImportMatrixXls, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportMatrixXls_str = ""
        # Get the properties inherited from ImportMatrix
        ImportMatrixXls_str += super(ImportMatrixXls, self).__str__()
        ImportMatrixXls_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        ImportMatrixXls_str += 'sheet = "' + str(self.sheet) + '"' + linesep
        ImportMatrixXls_str += "skiprows = " + str(self.skiprows) + linesep
        ImportMatrixXls_str += 'usecols = "' + str(self.usecols) + '"' + linesep
        ImportMatrixXls_str += "axes_colrows = " + str(self.axes_colrows) + linesep
        ImportMatrixXls_str += "is_allsheets = " + str(self.is_allsheets) + linesep
        return ImportMatrixXls_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportMatrixXls, self).__eq__(other):
            return False
        if other.file_path != self.file_path:
            return False
        if other.sheet != self.sheet:
            return False
        if other.skiprows != self.skiprows:
            return False
        if other.usecols != self.usecols:
            return False
        if other.axes_colrows != self.axes_colrows:
            return False
        if other.is_allsheets != self.is_allsheets:
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
        diff_list.extend(super(ImportMatrixXls, self).compare(other, name=name))
        if other._file_path != self._file_path:
            diff_list.append(name + ".file_path")
        if other._sheet != self._sheet:
            diff_list.append(name + ".sheet")
        if other._skiprows != self._skiprows:
            diff_list.append(name + ".skiprows")
        if other._usecols != self._usecols:
            diff_list.append(name + ".usecols")
        if other._axes_colrows != self._axes_colrows:
            diff_list.append(name + ".axes_colrows")
        if other._is_allsheets != self._is_allsheets:
            diff_list.append(name + ".is_allsheets")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportMatrixXls, self).__sizeof__()
        S += getsizeof(self.file_path)
        S += getsizeof(self.sheet)
        S += getsizeof(self.skiprows)
        S += getsizeof(self.usecols)
        if self.axes_colrows is not None:
            for key, value in self.axes_colrows.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_allsheets)
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
        ImportMatrixXls_dict = super(ImportMatrixXls, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportMatrixXls_dict["file_path"] = self.file_path
        ImportMatrixXls_dict["sheet"] = self.sheet
        ImportMatrixXls_dict["skiprows"] = self.skiprows
        ImportMatrixXls_dict["usecols"] = self.usecols
        ImportMatrixXls_dict["axes_colrows"] = (
            self.axes_colrows.copy() if self.axes_colrows is not None else None
        )
        ImportMatrixXls_dict["is_allsheets"] = self.is_allsheets
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportMatrixXls_dict["__class__"] = "ImportMatrixXls"
        return ImportMatrixXls_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        self.sheet = None
        self.skiprows = None
        self.usecols = None
        self.axes_colrows = None
        self.is_allsheets = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportMatrixXls, self)._set_None()

    def _get_file_path(self):
        """getter of file_path"""
        return self._file_path

    def _set_file_path(self, value):
        """setter of file_path"""
        check_var("file_path", value, "str")
        self._file_path = value

    file_path = property(
        fget=_get_file_path,
        fset=_set_file_path,
        doc=u"""Path of the file to load

        :Type: str
        """,
    )

    def _get_sheet(self):
        """getter of sheet"""
        return self._sheet

    def _set_sheet(self, value):
        """setter of sheet"""
        check_var("sheet", value, "str")
        self._sheet = value

    sheet = property(
        fget=_get_sheet,
        fset=_set_sheet,
        doc=u"""Name of the sheet to load

        :Type: str
        """,
    )

    def _get_skiprows(self):
        """getter of skiprows"""
        return self._skiprows

    def _set_skiprows(self, value):
        """setter of skiprows"""
        check_var("skiprows", value, "int", Vmin=0)
        self._skiprows = value

    skiprows = property(
        fget=_get_skiprows,
        fset=_set_skiprows,
        doc=u"""To skip some rows in the file (header)

        :Type: int
        :min: 0
        """,
    )

    def _get_usecols(self):
        """getter of usecols"""
        return self._usecols

    def _set_usecols(self, value):
        """setter of usecols"""
        check_var("usecols", value, "str")
        self._usecols = value

    usecols = property(
        fget=_get_usecols,
        fset=_set_usecols,
        doc=u"""list of Excel column letters and column ranges (e.g. "A:E" or "A,C,E:F")

        :Type: str
        """,
    )

    def _get_axes_colrows(self):
        """getter of axes_colrows"""
        return self._axes_colrows

    def _set_axes_colrows(self, value):
        """setter of axes_colrows"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_colrows", value, "dict")
        self._axes_colrows = value

    axes_colrows = property(
        fget=_get_axes_colrows,
        fset=_set_axes_colrows,
        doc=u"""To read axes in first line/column

        :Type: dict
        """,
    )

    def _get_is_allsheets(self):
        """getter of is_allsheets"""
        return self._is_allsheets

    def _set_is_allsheets(self, value):
        """setter of is_allsheets"""
        check_var("is_allsheets", value, "bool")
        self._is_allsheets = value

    is_allsheets = property(
        fget=_get_is_allsheets,
        fset=_set_is_allsheets,
        doc=u"""To read all sheets in a 3D matrix

        :Type: bool
        """,
    )
