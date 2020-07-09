# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/NodeMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Node import Node

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
    from ..Methods.Mesh.NodeMat.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from ..Methods.Mesh.NodeMat.is_exist import is_exist
except ImportError as error:
    is_exist = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class NodeMat(Node):
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
    # cf Methods.Mesh.NodeMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.NodeMat.is_exist
    if isinstance(is_exist, ImportError):
        is_exist = property(
            fget=lambda x: raise_(
                ImportError("Can't use NodeMat method is_exist: " + str(is_exist))
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
        coordinate=None,
        nb_node=0,
        tag=None,
        delta=1e-10,
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
            coordinate = obj.coordinate
            nb_node = obj.nb_node
            tag = obj.tag
            delta = obj.delta
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "coordinate" in list(init_dict.keys()):
                coordinate = init_dict["coordinate"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
            if "tag" in list(init_dict.keys()):
                tag = init_dict["tag"]
            if "delta" in list(init_dict.keys()):
                delta = init_dict["delta"]
        # Initialisation by argument
        # coordinate can be None, a ndarray or a list
        set_array(self, "coordinate", coordinate)
        self.nb_node = nb_node
        # tag can be None, a ndarray or a list
        set_array(self, "tag", tag)
        self.delta = delta
        # Call Node init
        super(NodeMat, self).__init__()
        # The class is frozen (in Node init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        NodeMat_str = ""
        # Get the properties inherited from Node
        NodeMat_str += super(NodeMat, self).__str__()
        NodeMat_str += (
            "coordinate = "
            + linesep
            + str(self.coordinate).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        NodeMat_str += "nb_node = " + str(self.nb_node) + linesep
        NodeMat_str += (
            "tag = "
            + linesep
            + str(self.tag).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        NodeMat_str += "delta = " + str(self.delta) + linesep
        return NodeMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Node
        if not super(NodeMat, self).__eq__(other):
            return False
        if not array_equal(other.coordinate, self.coordinate):
            return False
        if other.nb_node != self.nb_node:
            return False
        if not array_equal(other.tag, self.tag):
            return False
        if other.delta != self.delta:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Node
        NodeMat_dict = super(NodeMat, self).as_dict()
        if self.coordinate is None:
            NodeMat_dict["coordinate"] = None
        else:
            NodeMat_dict["coordinate"] = self.coordinate.tolist()
        NodeMat_dict["nb_node"] = self.nb_node
        if self.tag is None:
            NodeMat_dict["tag"] = None
        else:
            NodeMat_dict["tag"] = self.tag.tolist()
        NodeMat_dict["delta"] = self.delta
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        NodeMat_dict["__class__"] = "NodeMat"
        return NodeMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coordinate = None
        self.nb_node = None
        self.tag = None
        self.delta = None
        # Set to None the properties inherited from Node
        super(NodeMat, self)._set_None()

    def _get_coordinate(self):
        """getter of coordinate"""
        return self._coordinate

    def _set_coordinate(self, value):
        """setter of coordinate"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("coordinate", value, "ndarray")
        self._coordinate = value

    # Nodes coordinates
    # Type : ndarray
    coordinate = property(
        fget=_get_coordinate, fset=_set_coordinate, doc=u"""Nodes coordinates"""
    )

    def _get_nb_node(self):
        """getter of nb_node"""
        return self._nb_node

    def _set_nb_node(self, value):
        """setter of nb_node"""
        check_var("nb_node", value, "int")
        self._nb_node = value

    # Total number of nodes
    # Type : int
    nb_node = property(
        fget=_get_nb_node, fset=_set_nb_node, doc=u"""Total number of nodes"""
    )

    def _get_tag(self):
        """getter of tag"""
        return self._tag

    def _set_tag(self, value):
        """setter of tag"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("tag", value, "ndarray")
        self._tag = value

    # Node tags
    # Type : ndarray
    tag = property(fget=_get_tag, fset=_set_tag, doc=u"""Node tags""")

    def _get_delta(self):
        """getter of delta"""
        return self._delta

    def _set_delta(self, value):
        """setter of delta"""
        check_var("delta", value, "float")
        self._delta = value

    # Sensibility for node searching
    # Type : float
    delta = property(
        fget=_get_delta, fset=_set_delta, doc=u"""Sensibility for node searching"""
    )
