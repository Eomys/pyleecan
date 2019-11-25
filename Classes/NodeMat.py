# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Node import Node

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.NodeMat.get_node import get_node
except ImportError as error:
    get_node = error


from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class NodeMat(Node):
    """Class to define nodes coordinates and getter."""

    VERSION = 1

    # cf Methods.Mesh.NodeMat.get_node
    if isinstance(get_node, ImportError):
        get_node = property(fget=lambda x: raise_(ImportError("Can't use NodeMat method get_node: " + str(get_node))))
    else:
        get_node = get_node
    # save method is available in all object
    save = save

    def __init__(self, coordinate=None, nb_node=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["coordinate", "nb_node"])
            # Overwrite default value with init_dict content
            if "coordinate" in list(init_dict.keys()):
                coordinate = init_dict["coordinate"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
        # Initialisation by argument
        # coordinate can be None, a ndarray or a list
        set_array(self, "coordinate", coordinate)
        self.nb_node = nb_node
        # Call Node init
        super(NodeMat, self).__init__()
        # The class is frozen (in Node init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        NodeMat_str = ""
        # Get the properties inherited from Node
        NodeMat_str += super(NodeMat, self).__str__() + linesep
        NodeMat_str += "coordinate = " + linesep + str(self.coordinate) + linesep + linesep
        NodeMat_str += "nb_node = " + str(self.nb_node)
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
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        NodeMat_dict["__class__"] = "NodeMat"
        return NodeMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coordinate = None
        self.nb_node = None
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

    # Nodes coordinates (X, Y, Z)
    # Type : ndarray
    coordinate = property(fget=_get_coordinate, fset=_set_coordinate,
                          doc=u"""Nodes coordinates (X, Y, Z)""")

    def _get_nb_node(self):
        """getter of nb_node"""
        return self._nb_node

    def _set_nb_node(self, value):
        """setter of nb_node"""
        check_var("nb_node", value, "int")
        self._nb_node = value

    # Total number of nodes
    # Type : int
    nb_node = property(fget=_get_nb_node, fset=_set_nb_node,
                       doc=u"""Total number of nodes""")
