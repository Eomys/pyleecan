# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Elements import Elements

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class Triangles(Elements):
    """Store triangle elements for 2D mesh"""

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
        # Call Elements init
        super(Triangles, self).__init__(connectivity=connectivity, solution_dict=solution_dict)
        # The class is frozen (in Elements init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Triangles_str = ""
        # Get the properties inherited from Elements
        Triangles_str += super(Triangles, self).__str__() + linesep
        return Triangles_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Elements
        if not super(Triangles, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Elements
        Triangles_dict = super(Triangles, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Triangles_dict["__class__"] = "Triangles"
        return Triangles_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Elements
        super(Triangles, self)._set_None()


