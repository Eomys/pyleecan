# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Node import Node

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.NodeMat.get_coord import get_coord
except ImportError as error:
    get_coord = error

try:
    from pyleecan.Methods.Mesh.NodeMat.get_group import get_group
except ImportError as error:
    get_group = error


from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class NodeMat(Node):
    """Class to define nodes coordinates and getter."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
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
    # save method is available in all object
    save = save

    def __init__(self, coordinate=None, nb_node=None, node_tag=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["coordinate", "nb_node", "node_tag"])
            # Overwrite default value with init_dict content
            if "coordinate" in list(init_dict.keys()):
                coordinate = init_dict["coordinate"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
            if "node_tag" in list(init_dict.keys()):
                node_tag = init_dict["node_tag"]
        # Initialisation by argument
        # coordinate can be None, a ndarray or a list
        set_array(self, "coordinate", coordinate)
        self.nb_node = nb_node
        # node_tag can be None, a ndarray or a list
        set_array(self, "node_tag", node_tag)
        # Call Node init
        super(NodeMat, self).__init__()
        # The class is frozen (in Node init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        NodeMat_str = ""
        # Get the properties inherited from Node
        NodeMat_str += super(NodeMat, self).__str__() + linesep
        NodeMat_str += (
            "coordinate = " + linesep + str(self.coordinate) + linesep + linesep
        )
        NodeMat_str += "nb_node = " + str(self.nb_node) + linesep
        NodeMat_str += "node_tag = " + linesep + str(self.node_tag)
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
        if not array_equal(other.node_tag, self.node_tag):
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
        if self.node_tag is None:
            NodeMat_dict["node_tag"] = None
        else:
            NodeMat_dict["node_tag"] = self.node_tag.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        NodeMat_dict["__class__"] = "NodeMat"
        return NodeMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coordinate = None
        self.nb_node = None
        self.node_tag = None
        # Set to None the properties inherited from Node
        super(NodeMat, self)._set_None()

    def _get_coordinate(self):
        """getter of coordinate"""
        return self._coordinate

    def _set_coordinate(self, value):
        """setter of coordinate"""
        if type(value) is list:
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

    def _get_node_tag(self):
        """getter of node_tag"""
        return self._node_tag

    def _set_node_tag(self, value):
        """setter of node_tag"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("node_tag", value, "ndarray")
        self._node_tag = value

    # Node tags
    # Type : ndarray
    node_tag = property(fget=_get_node_tag, fset=_set_node_tag, doc=u"""Node tags""")
