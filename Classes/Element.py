# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class Element(FrozenClass):
    """Store one element of the mesh defined by several nodes"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, connectivity=None, solution_dict=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["connectivity", "solution_dict"])
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "solution_dict" in list(init_dict.keys()):
                solution_dict = init_dict["solution_dict"]
        # Initialisation by argument
        self.parent = None
        # connectivity can be None, a ndarray or a list
        set_array(self, "connectivity", connectivity)
        self.solution_dict = solution_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Element_str = ""
        if self.parent is None:
            Element_str += "parent = None " + linesep
        else:
            Element_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Element_str += "connectivity = " + linesep + str(self.connectivity) + linesep + linesep
        Element_str += "solution_dict = " + str(self.solution_dict)
        return Element_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.connectivity, self.connectivity):
            return False
        if other.solution_dict != self.solution_dict:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Element_dict = dict()
        if self.connectivity is None:
            Element_dict["connectivity"] = None
        else:
            Element_dict["connectivity"] = self.connectivity.tolist()
        Element_dict["solution_dict"] = self.solution_dict
        # The class name is added to the dict fordeserialisation purpose
        Element_dict["__class__"] = "Element"
        return Element_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.solution_dict = None

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

    # List of node composing the element
    # Type : ndarray
    connectivity = property(fget=_get_connectivity, fset=_set_connectivity,
                            doc=u"""List of node composing the element""")

    def _get_solution_dict(self):
        """getter of solution_dict"""
        return self._solution_dict

    def _set_solution_dict(self, value):
        """setter of solution_dict"""
        check_var("solution_dict", value, "dict")
        self._solution_dict = value

    # Dictionary contraining the FEA solution related to the element
    # Type : dict
    solution_dict = property(fget=_get_solution_dict, fset=_set_solution_dict,
                             doc=u"""Dictionary contraining the FEA solution related to the element""")
