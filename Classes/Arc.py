# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Line import Line

from pyleecan.Methods.Geometry.Arc.draw_FEMM import draw_FEMM

from pyleecan.Classes.check import InitUnKnowClassError


class Arc(Line):
    """Abstract class for arc"""

    VERSION = 1

    # cf Methods.Geometry.Arc.draw_FEMM
    draw_FEMM = draw_FEMM
    # save method is available in all object
    save = save

    def __init__(self, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["label"])
            # Overwrite default value with init_dict content
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # Call Line init
        super(Arc, self).__init__(label=label)
        # The class is frozen (in Line init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Arc_str = ""
        # Get the properties inherited from Line
        Arc_str += super(Arc, self).__str__() + linesep
        return Arc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Line
        if not super(Arc, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Line
        Arc_dict = super(Arc, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Arc_dict["__class__"] = "Arc"
        return Arc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Line
        super(Arc, self)._set_None()


