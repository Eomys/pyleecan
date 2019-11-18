# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class Mesh(FrozenClass):
    """Gather the mesh storage format"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, name=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["name"])
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
        # Initialisation by argument
        self.parent = None
        self.name = name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Mesh_str = ""
        if self.parent is None:
            Mesh_str += "parent = None " + linesep
        else:
            Mesh_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Mesh_str += 'name = "' + str(self.name) + '"'
        return Mesh_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Mesh_dict = dict()
        Mesh_dict["name"] = self.name
        # The class name is added to the dict fordeserialisation purpose
        Mesh_dict["__class__"] = "Mesh"
        return Mesh_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # (Optional) Descriptive name of the mesh
    # Type : str
    name = property(fget=_get_name, fset=_set_name,
                    doc=u"""(Optional) Descriptive name of the mesh""")
