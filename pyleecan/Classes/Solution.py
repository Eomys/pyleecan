# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/Solution.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.Solution.get_field import get_field
except ImportError as error:
    get_field = error


from ._check import InitUnKnowClassError


class Solution(FrozenClass):
    """Abstract class for solution related classes."""

    VERSION = 1

    # cf Methods.Mesh.Solution.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError("Can't use Solution method get_field: " + str(get_field))
            )
        )
    else:
        get_field = get_field
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert init_dict == {"__class__": "Solution"}
        if init_str is not None:  # Initialisation by str
            assert type(init_str) is str
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Solution_str = ""
        if self.parent is None:
            Solution_str += "parent = None " + linesep
        else:
            Solution_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return Solution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Solution_dict = dict()
        # The class name is added to the dict fordeserialisation purpose
        Solution_dict["__class__"] = "Solution"
        return Solution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
