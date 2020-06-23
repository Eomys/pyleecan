# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/CellMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.CellMat.add_cell import add_cell
except ImportError as error:
    add_cell = error

try:
    from ..Methods.Mesh.CellMat.get_all_connectivity import get_all_connectivity
except ImportError as error:
    get_all_connectivity = error

try:
    from ..Methods.Mesh.CellMat.get_all_node_tags import get_all_node_tags
except ImportError as error:
    get_all_node_tags = error

try:
    from ..Methods.Mesh.CellMat.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.CellMat.get_group import get_group
except ImportError as error:
    get_group = error

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
    # cf Methods.Mesh.CellMat.get_all_connectivity
    if isinstance(get_all_connectivity, ImportError):
        get_all_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CellMat method get_all_connectivity: "
                    + str(get_all_connectivity)
                )
            )
        )
    else:
        get_all_connectivity = get_all_connectivity
    # cf Methods.Mesh.CellMat.get_all_node_tags
    if isinstance(get_all_node_tags, ImportError):
        get_all_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CellMat method get_all_node_tags: "
                    + str(get_all_node_tags)
                )
            )
        )
    else:
        get_all_node_tags = get_all_node_tags
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
    # cf Methods.Mesh.CellMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use CellMat method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
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
        connectivity=None,
        nb_cell=0,
        nb_pt_per_cell=0,
        group=None,
        indice=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            connectivity = obj.connectivity
            nb_cell = obj.nb_cell
            nb_pt_per_cell = obj.nb_pt_per_cell
            group = obj.group
            indice = obj.indice
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "nb_cell" in list(init_dict.keys()):
                nb_cell = init_dict["nb_cell"]
            if "nb_pt_per_cell" in list(init_dict.keys()):
                nb_pt_per_cell = init_dict["nb_pt_per_cell"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
        # Initialisation by argument
        self.parent = None
        # connectivity can be None, a ndarray or a list
        set_array(self, "connectivity", connectivity)
        self.nb_cell = nb_cell
        self.nb_pt_per_cell = nb_pt_per_cell
        # group can be None, a ndarray or a list
        set_array(self, "group", group)
        # indice can be None, a ndarray or a list
        set_array(self, "indice", indice)

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
            "group = "
            + linesep
            + str(self.group).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        CellMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
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
        if not array_equal(other.group, self.group):
            return False
        if not array_equal(other.indice, self.indice):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        CellMat_dict = dict()
        if self.connectivity is None:
            CellMat_dict["connectivity"] = None
        else:
            CellMat_dict["connectivity"] = self.connectivity.tolist()
        CellMat_dict["nb_cell"] = self.nb_cell
        CellMat_dict["nb_pt_per_cell"] = self.nb_pt_per_cell
        if self.group is None:
            CellMat_dict["group"] = None
        else:
            CellMat_dict["group"] = self.group.tolist()
        if self.indice is None:
            CellMat_dict["indice"] = None
        else:
            CellMat_dict["indice"] = self.indice.tolist()
        # The class name is added to the dict fordeserialisation purpose
        CellMat_dict["__class__"] = "CellMat"
        return CellMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.nb_cell = None
        self.nb_pt_per_cell = None
        self.group = None
        self.indice = None

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("connectivity", value, "ndarray")
        self._connectivity = value

    # Matrix of connectivity for one element type
    # Type : ndarray
    connectivity = property(
        fget=_get_connectivity,
        fset=_set_connectivity,
        doc=u"""Matrix of connectivity for one element type""",
    )

    def _get_nb_cell(self):
        """getter of nb_cell"""
        return self._nb_cell

    def _set_nb_cell(self, value):
        """setter of nb_cell"""
        check_var("nb_cell", value, "int")
        self._nb_cell = value

    # Total number of elements
    # Type : int
    nb_cell = property(
        fget=_get_nb_cell, fset=_set_nb_cell, doc=u"""Total number of elements"""
    )

    def _get_nb_pt_per_cell(self):
        """getter of nb_pt_per_cell"""
        return self._nb_pt_per_cell

    def _set_nb_pt_per_cell(self, value):
        """setter of nb_pt_per_cell"""
        check_var("nb_pt_per_cell", value, "int")
        self._nb_pt_per_cell = value

    # Define the number of node per element
    # Type : int
    nb_pt_per_cell = property(
        fget=_get_nb_pt_per_cell,
        fset=_set_nb_pt_per_cell,
        doc=u"""Define the number of node per element""",
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("group", value, "ndarray")
        self._group = value

    # Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.
    # Type : ndarray
    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.""",
    )

    def _get_indice(self):
        """getter of indice"""
        return self._indice

    def _set_indice(self, value):
        """setter of indice"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indice", value, "ndarray")
        self._indice = value

    # Element indices
    # Type : ndarray
    indice = property(fget=_get_indice, fset=_set_indice, doc=u"""Element indices""")
