# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Mesh/Node.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.Node.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from pyleecan.Methods.Mesh.Node.get_coord import get_coord
except ImportError as error:
    get_coord = error


from pyleecan.Classes.check import InitUnKnowClassError


class Node(FrozenClass):
    """Abstract class to define nodes. It must have at least a method get_coord to get nodes coordinates for given node tags/number, and a method get_group to create a new objet Node based on a set of given elements."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.Node.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use Node method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.Node.get_coord
    if isinstance(get_coord, ImportError):
        get_coord = property(
            fget=lambda x: raise_(
                ImportError("Can't use Node method get_coord: " + str(get_coord))
            )
        )
    else:
        get_coord = get_coord
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
