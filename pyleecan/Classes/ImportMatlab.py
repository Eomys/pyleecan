# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMatlab.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMatlab
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
    from ..Methods.Import.ImportMatlab.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportMatlab(ImportMatrix):
    """Import the data from a mat file"""

    VERSION = 1

    # cf Methods.Import.ImportMatlab.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportMatlab method get_data: " + str(get_data))
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
        var_name="",
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
            if "var_name" in list(init_dict.keys()):
                var_name = init_dict["var_name"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.file_path = file_path
        self.var_name = var_name
        # Call ImportMatrix init
        super(ImportMatlab, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportMatlab_str = ""
        # Get the properties inherited from ImportMatrix
        ImportMatlab_str += super(ImportMatlab, self).__str__()
        ImportMatlab_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        ImportMatlab_str += 'var_name = "' + str(self.var_name) + '"' + linesep
        return ImportMatlab_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportMatlab, self).__eq__(other):
            return False
        if other.file_path != self.file_path:
            return False
        if other.var_name != self.var_name:
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
        diff_list.extend(super(ImportMatlab, self).compare(other, name=name))
        if other._file_path != self._file_path:
            diff_list.append(name + ".file_path")
        if other._var_name != self._var_name:
            diff_list.append(name + ".var_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportMatlab, self).__sizeof__()
        S += getsizeof(self.file_path)
        S += getsizeof(self.var_name)
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
        ImportMatlab_dict = super(ImportMatlab, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportMatlab_dict["file_path"] = self.file_path
        ImportMatlab_dict["var_name"] = self.var_name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportMatlab_dict["__class__"] = "ImportMatlab"
        return ImportMatlab_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        self.var_name = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportMatlab, self)._set_None()

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

    def _get_var_name(self):
        """getter of var_name"""
        return self._var_name

    def _set_var_name(self, value):
        """setter of var_name"""
        check_var("var_name", value, "str")
        self._var_name = value

    var_name = property(
        fget=_get_var_name,
        fset=_set_var_name,
        doc=u"""Name of the variable to load

        :Type: str
        """,
    )
