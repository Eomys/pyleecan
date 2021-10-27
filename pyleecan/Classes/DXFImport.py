# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/DXFImport.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/DXFImport
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.DXFImport.get_surfaces import get_surfaces
except ImportError as error:
    get_surfaces = error


from ._check import InitUnKnowClassError


class DXFImport(FrozenClass):
    """Use a DXF to define a lamination"""

    VERSION = 1

    # cf Methods.Simulation.DXFImport.get_surfaces
    if isinstance(get_surfaces, ImportError):
        get_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use DXFImport method get_surfaces: " + str(get_surfaces)
                )
            )
        )
    else:
        get_surfaces = get_surfaces
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, file_path="", surf_dict=-1, BC_list=-1, init_dict=None, init_str=None
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
            if "surf_dict" in list(init_dict.keys()):
                surf_dict = init_dict["surf_dict"]
            if "BC_list" in list(init_dict.keys()):
                BC_list = init_dict["BC_list"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.file_path = file_path
        self.surf_dict = surf_dict
        self.BC_list = BC_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        DXFImport_str = ""
        if self.parent is None:
            DXFImport_str += "parent = None " + linesep
        else:
            DXFImport_str += "parent = " + str(type(self.parent)) + " object" + linesep
        DXFImport_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        DXFImport_str += "surf_dict = " + str(self.surf_dict) + linesep
        DXFImport_str += (
            "BC_list = "
            + linesep
            + str(self.BC_list).replace(linesep, linesep + "\t")
            + linesep
        )
        return DXFImport_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.file_path != self.file_path:
            return False
        if other.surf_dict != self.surf_dict:
            return False
        if other.BC_list != self.BC_list:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._file_path != self._file_path:
            diff_list.append(name + ".file_path")
        if other._surf_dict != self._surf_dict:
            diff_list.append(name + ".surf_dict")
        if other._BC_list != self._BC_list:
            diff_list.append(name + ".BC_list")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.file_path)
        if self.surf_dict is not None:
            for key, value in self.surf_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.BC_list is not None:
            for value in self.BC_list:
                S += getsizeof(value)
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

        DXFImport_dict = dict()
        DXFImport_dict["file_path"] = self.file_path
        DXFImport_dict["surf_dict"] = (
            self.surf_dict.copy() if self.surf_dict is not None else None
        )
        DXFImport_dict["BC_list"] = (
            self.BC_list.copy() if self.BC_list is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        DXFImport_dict["__class__"] = "DXFImport"
        return DXFImport_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        self.surf_dict = None
        self.BC_list = None

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
        doc=u"""Path to the DXF file to import

        :Type: str
        """,
    )

    def _get_surf_dict(self):
        """getter of surf_dict"""
        return self._surf_dict

    def _set_surf_dict(self, value):
        """setter of surf_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("surf_dict", value, "dict")
        self._surf_dict = value

    surf_dict = property(
        fget=_get_surf_dict,
        fset=_set_surf_dict,
        doc=u"""dictionary to assign the surfaces: key=complex reference point coordinate, value=label of the surface

        :Type: dict
        """,
    )

    def _get_BC_list(self):
        """getter of BC_list"""
        return self._BC_list

    def _set_BC_list(self, value):
        """setter of BC_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("BC_list", value, "list")
        self._BC_list = value

    BC_list = property(
        fget=_get_BC_list,
        fset=_set_BC_list,
        doc=u"""List of tuple to apply boundary conditions (complex reference point coordinate, is_arc, label of the BC to apply)

        :Type: list
        """,
    )
