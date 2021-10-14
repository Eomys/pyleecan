# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/NodeMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/NodeMat
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
    from ..Methods.Mesh.NodeMat.add_node import add_node
except ImportError as error:
    add_node = error

try:
    from ..Methods.Mesh.NodeMat.get_coord import get_coord
except ImportError as error:
    get_coord = error

try:
    from ..Methods.Mesh.NodeMat.is_exist import is_exist
except ImportError as error:
    is_exist = error

try:
    from ..Methods.Mesh.NodeMat.get_indice import get_indice
except ImportError as error:
    get_indice = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class NodeMat(FrozenClass):
    """Class to define nodes coordinates and getter."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.NodeMat.add_node
    if isinstance(add_node, ImportError):
        add_node = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method add_node: " + str(add_node))
            )
        )
    else:
        add_node = add_node
    # cf Methods.Mesh.NodeMat.get_coord
    if isinstance(get_coord, ImportError):
        get_coord = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method get_coord: " + str(get_coord))
            )
        )
    else:
        get_coord = get_coord
    # cf Methods.Mesh.NodeMat.is_exist
    if isinstance(is_exist, ImportError):
        is_exist = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method is_exist: " + str(is_exist))
            )
        )
    else:
        is_exist = is_exist
    # cf Methods.Mesh.NodeMat.get_indice
    if isinstance(get_indice, ImportError):
        get_indice = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method get_indice: " + str(get_indice))
            )
        )
    else:
        get_indice = get_indice
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        coordinate=[],
        nb_node=0,
        delta=1e-10,
        indice=None,
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
            if "coordinate" in list(init_dict.keys()):
                coordinate = init_dict["coordinate"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
            if "delta" in list(init_dict.keys()):
                delta = init_dict["delta"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.coordinate = coordinate
        self.nb_node = nb_node
        self.delta = delta
        self.indice = indice

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        NodeMat_str = ""
        if self.parent is None:
            NodeMat_str += "parent = None " + linesep
        else:
            NodeMat_str += "parent = " + str(type(self.parent)) + " object" + linesep
        NodeMat_str += (
            "coordinate = "
            + linesep
            + str(self.coordinate).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        NodeMat_str += "nb_node = " + str(self.nb_node) + linesep
        NodeMat_str += "delta = " + str(self.delta) + linesep
        NodeMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return NodeMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.coordinate, self.coordinate):
            return False
        if other.nb_node != self.nb_node:
            return False
        if other.delta != self.delta:
            return False
        if not array_equal(other.indice, self.indice):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if not array_equal(other.coordinate, self.coordinate):
            diff_list.append(name + ".coordinate")
        if other._nb_node != self._nb_node:
            diff_list.append(name + ".nb_node")
        if other._delta != self._delta:
            diff_list.append(name + ".delta")
        if not array_equal(other.indice, self.indice):
            diff_list.append(name + ".indice")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.coordinate)
        S += getsizeof(self.nb_node)
        S += getsizeof(self.delta)
        S += getsizeof(self.indice)
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

        NodeMat_dict = dict()
        if self.coordinate is None:
            NodeMat_dict["coordinate"] = None
        else:
            if type_handle_ndarray == 0:
                NodeMat_dict["coordinate"] = self.coordinate.tolist()
            elif type_handle_ndarray == 1:
                NodeMat_dict["coordinate"] = self.coordinate.copy()
            elif type_handle_ndarray == 2:
                NodeMat_dict["coordinate"] = self.coordinate
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        NodeMat_dict["nb_node"] = self.nb_node
        NodeMat_dict["delta"] = self.delta
        if self.indice is None:
            NodeMat_dict["indice"] = None
        else:
            if type_handle_ndarray == 0:
                NodeMat_dict["indice"] = self.indice.tolist()
            elif type_handle_ndarray == 1:
                NodeMat_dict["indice"] = self.indice.copy()
            elif type_handle_ndarray == 2:
                NodeMat_dict["indice"] = self.indice
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        NodeMat_dict["__class__"] = "NodeMat"
        return NodeMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coordinate = None
        self.nb_node = None
        self.delta = None
        self.indice = None

    def _get_coordinate(self):
        """getter of coordinate"""
        return self._coordinate

    def _set_coordinate(self, value):
        """setter of coordinate"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("coordinate", value, "ndarray")
        self._coordinate = value

    coordinate = property(
        fget=_get_coordinate,
        fset=_set_coordinate,
        doc=u"""Nodes coordinates

        :Type: ndarray
        """,
    )

    def _get_nb_node(self):
        """getter of nb_node"""
        return self._nb_node

    def _set_nb_node(self, value):
        """setter of nb_node"""
        check_var("nb_node", value, "int")
        self._nb_node = value

    nb_node = property(
        fget=_get_nb_node,
        fset=_set_nb_node,
        doc=u"""Total number of nodes

        :Type: int
        """,
    )

    def _get_delta(self):
        """getter of delta"""
        return self._delta

    def _set_delta(self, value):
        """setter of delta"""
        check_var("delta", value, "float")
        self._delta = value

    delta = property(
        fget=_get_delta,
        fset=_set_delta,
        doc=u"""Sensibility for node searching

        :Type: float
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
        doc=u"""Nodes unique indices

        :Type: ndarray
        """,
    )
