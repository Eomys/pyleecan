# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.Node.get_node import get_node
except ImportError as error:
    get_node = error


from pyleecan.Classes.check import InitUnKnowClassError


class Node(FrozenClass):
    """Abstract class to define nodes coordinates and getter."""

    VERSION = 1

    # cf Methods.Mesh.Node.get_node
    if isinstance(get_node, ImportError):
        get_node = property(fget=lambda x: raise_(ImportError("Can't use Node method get_node: " + str(get_node))))
    else:
        get_node = get_node
    # save method is available in all object
    save = save

    def __init__(self, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, [])
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Node_str = ""
        if self.parent is None:
            Node_str += "parent = None " + linesep
        else:
            Node_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return Node_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Node_dict = dict()
        # The class name is added to the dict fordeserialisation purpose
        Node_dict["__class__"] = "Node"
        return Node_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""



