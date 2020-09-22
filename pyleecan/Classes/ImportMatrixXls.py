# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMatrixXls.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMatrixXls
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
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
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        file_path="",
        sheet="",
        skiprows=0,
        usecols=None,
        is_transpose=False,
        init_dict=None,
        init_str=None,
    ):
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
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
            if "sheet" in list(init_dict.keys()):
                sheet = init_dict["sheet"]
            if "skiprows" in list(init_dict.keys()):
                skiprows = init_dict["skiprows"]
            if "usecols" in list(init_dict.keys()):
                usecols = init_dict["usecols"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.file_path = file_path
        self.sheet = sheet
        self.skiprows = skiprows
        self.usecols = usecols
        # Call ImportMatrix init
        super(ImportMatrixXls, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportMatrixXls_str = ""
        # Get the properties inherited from ImportMatrix
        ImportMatrixXls_str += super(ImportMatrixXls, self).__str__()
        ImportMatrixXls_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        ImportMatrixXls_str += 'sheet = "' + str(self.sheet) + '"' + linesep
        ImportMatrixXls_str += "skiprows = " + str(self.skiprows) + linesep
        ImportMatrixXls_str += 'usecols = "' + str(self.usecols) + '"' + linesep
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportMatrixXls_dict = super(ImportMatrixXls, self).as_dict()
        ImportMatrixXls_dict["file_path"] = self.file_path
        ImportMatrixXls_dict["sheet"] = self.sheet
        ImportMatrixXls_dict["skiprows"] = self.skiprows
        ImportMatrixXls_dict["usecols"] = self.usecols
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportMatrixXls_dict["__class__"] = "ImportMatrixXls"
        return ImportMatrixXls_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        self.sheet = None
        self.skiprows = None
        self.usecols = None
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
        doc=u"""To select the range of column to use

        :Type: str
        """,
    )
