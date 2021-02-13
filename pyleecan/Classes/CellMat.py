# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/CellMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/CellMat
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.CellMat.add_cell import add_cell
except ImportError as error:
    add_cell = error

try:
    from ..Methods.Mesh.CellMat.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.CellMat.get_point2cell import get_point2cell
except ImportError as error:
    get_point2cell = error

try:
    from ..Methods.Mesh.CellMat.is_exist import is_exist
except ImportError as error:
    is_exist = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Interpolation import Interpolation


class CellMat(FrozenClass):
    """Define the connectivity under matricial format containing one type of element (example: only triangles with 3 nodes). """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.CellMat.add_cell
    if isinstance(add_cell, ImportError):
        add_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use CellMat method add_cell: " + str(add_cell))
            )
        )
    else:
        add_cell = add_cell
    # cf Methods.Mesh.CellMat.get_connectivity
    if isinstance(get_connectivity, ImportError):
        get_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CellMat method get_connectivity: "
                    + str(get_connectivity)
                )
            )
        )
    else:
        get_connectivity = get_connectivity
    # cf Methods.Mesh.CellMat.get_point2cell
    if isinstance(get_point2cell, ImportError):
        get_point2cell = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CellMat method get_point2cell: " + str(get_point2cell)
                )
            )
        )
    else:
        get_point2cell = get_point2cell
    # cf Methods.Mesh.CellMat.is_exist
    if isinstance(is_exist, ImportError):
        is_exist = property(
            fget=lambda x: raise_(
                ImportError("Can't use CellMat method is_exist: " + str(is_exist))
            )
        )
    else:
        is_exist = is_exist
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        connectivity=[],
        nb_cell=0,
        nb_pt_per_cell=0,
        indice=[],
        interpolation=-1,
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
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "nb_cell" in list(init_dict.keys()):
                nb_cell = init_dict["nb_cell"]
            if "nb_pt_per_cell" in list(init_dict.keys()):
                nb_pt_per_cell = init_dict["nb_pt_per_cell"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
            if "interpolation" in list(init_dict.keys()):
                interpolation = init_dict["interpolation"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.connectivity = connectivity
        self.nb_cell = nb_cell
        self.nb_pt_per_cell = nb_pt_per_cell
        self.indice = indice
        self.interpolation = interpolation

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CellMat_str = ""
        if self.parent is None:
            CellMat_str += "parent = None " + linesep
        else:
            CellMat_str += "parent = " + str(type(self.parent)) + " object" + linesep
        CellMat_str += (
            "connectivity = "
            + linesep
            + str(self.connectivity).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        CellMat_str += "nb_cell = " + str(self.nb_cell) + linesep
        CellMat_str += "nb_pt_per_cell = " + str(self.nb_pt_per_cell) + linesep
        CellMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        if self.interpolation is not None:
            tmp = (
                self.interpolation.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            CellMat_str += "interpolation = " + tmp
        else:
            CellMat_str += "interpolation = None" + linesep + linesep
        return CellMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.connectivity, self.connectivity):
            return False
        if other.nb_cell != self.nb_cell:
            return False
        if other.nb_pt_per_cell != self.nb_pt_per_cell:
            return False
        if not array_equal(other.indice, self.indice):
            return False
        if other.interpolation != self.interpolation:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.connectivity)
        S += getsizeof(self.nb_cell)
        S += getsizeof(self.nb_pt_per_cell)
        S += getsizeof(self.indice)
        S += getsizeof(self.interpolation)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        CellMat_dict = dict()
        if self.connectivity is None:
            CellMat_dict["connectivity"] = None
        else:
            CellMat_dict["connectivity"] = self.connectivity.tolist()
        CellMat_dict["nb_cell"] = self.nb_cell
        CellMat_dict["nb_pt_per_cell"] = self.nb_pt_per_cell
        if self.indice is None:
            CellMat_dict["indice"] = None
        else:
            CellMat_dict["indice"] = self.indice.tolist()
        if self.interpolation is None:
            CellMat_dict["interpolation"] = None
        else:
            CellMat_dict["interpolation"] = self.interpolation.as_dict(**kwargs)
        # The class name is added to the dict for deserialisation purpose
        CellMat_dict["__class__"] = "CellMat"
        return CellMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.nb_cell = None
        self.nb_pt_per_cell = None
        self.indice = None
        if self.interpolation is not None:
            self.interpolation._set_None()

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("connectivity", value, "ndarray")
        self._connectivity = value

    connectivity = property(
        fget=_get_connectivity,
        fset=_set_connectivity,
        doc=u"""Matrix of connectivity for one element type

        :Type: ndarray
        """,
    )

    def _get_nb_cell(self):
        """getter of nb_cell"""
        return self._nb_cell

    def _set_nb_cell(self, value):
        """setter of nb_cell"""
        check_var("nb_cell", value, "int")
        self._nb_cell = value

    nb_cell = property(
        fget=_get_nb_cell,
        fset=_set_nb_cell,
        doc=u"""Total number of elements

        :Type: int
        """,
    )

    def _get_nb_pt_per_cell(self):
        """getter of nb_pt_per_cell"""
        return self._nb_pt_per_cell

    def _set_nb_pt_per_cell(self, value):
        """setter of nb_pt_per_cell"""
        check_var("nb_pt_per_cell", value, "int")
        self._nb_pt_per_cell = value

    nb_pt_per_cell = property(
        fget=_get_nb_pt_per_cell,
        fset=_set_nb_pt_per_cell,
        doc=u"""Define the number of node per element

        :Type: int
        """,
    )

    def _get_indice(self):
        """getter of indice"""
        return self._indice

    def _set_indice(self, value):
        """setter of indice"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indice", value, "ndarray")
        self._indice = value

    indice = property(
        fget=_get_indice,
        fset=_set_indice,
        doc=u"""Element indices

        :Type: ndarray
        """,
    )

    def _get_interpolation(self):
        """getter of interpolation"""
        return self._interpolation

    def _set_interpolation(self, value):
        """setter of interpolation"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "interpolation"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Interpolation()
        check_var("interpolation", value, "Interpolation")
        self._interpolation = value

        if self._interpolation is not None:
            self._interpolation.parent = self

    interpolation = property(
        fget=_get_interpolation,
        fset=_set_interpolation,
        doc=u"""Define FEA interpolation

        :Type: Interpolation
        """,
    )
