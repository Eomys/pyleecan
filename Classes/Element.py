# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.Element.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from pyleecan.Methods.Mesh.Element.get_node_tags import get_node_tags
except ImportError as error:
    get_node_tags = error

try:
    from pyleecan.Methods.Mesh.Element.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from pyleecan.Methods.Mesh.Element.convert_element import convert_element
except ImportError as error:
    convert_element = error

try:
    from pyleecan.Methods.Mesh.Element.add_element import add_element
except ImportError as error:
    add_element = error


from pyleecan.Classes.check import InitUnKnowClassError


class Element(FrozenClass):
    """Abstract class to define connectivity and getter."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.Element.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use Element method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.Element.get_node_tags
    if isinstance(get_node_tags, ImportError):
        get_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Element method get_node_tags: " + str(get_node_tags)
                )
            )
        )
    else:
        get_node_tags = get_node_tags
    # cf Methods.Mesh.Element.get_node2element
    if isinstance(get_node2element, ImportError):
        get_node2element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Element method get_node2element: "
                    + str(get_node2element)
                )
            )
        )
    else:
        get_node2element = get_node2element
    # cf Methods.Mesh.Element.convert_element
    if isinstance(convert_element, ImportError):
        convert_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Element method convert_element: " + str(convert_element)
                )
            )
        )
    else:
        convert_element = convert_element
    # cf Methods.Mesh.Element.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use Element method add_element: " + str(add_element))
            )
        )
    else:
        add_element = add_element
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

        Element_str = ""
        if self.parent is None:
            Element_str += "parent = None " + linesep
        else:
            Element_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return Element_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Element_dict = dict()
        # The class name is added to the dict fordeserialisation purpose
        Element_dict["__class__"] = "Element"
        return Element_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
