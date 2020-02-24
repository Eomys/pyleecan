# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/SlotUD.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.SlotUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error


from pyleecan.Classes._check import InitUnKnowClassError


class SlotUD(Slot):
    """"User defined" Slot from a point list. """

    VERSION = 1

    # cf Methods.Slot.SlotUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # save method is available in all object
    save = save

    def __init__(self, point_list=[], is_sym=False, Zs=36, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["point_list", "is_sym", "Zs"])
            # Overwrite default value with init_dict content
            if "point_list" in list(init_dict.keys()):
                point_list = init_dict["point_list"]
            if "is_sym" in list(init_dict.keys()):
                is_sym = init_dict["is_sym"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.point_list = point_list
        self.is_sym = is_sym
        # Call Slot init
        super(SlotUD, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotUD_str = ""
        # Get the properties inherited from Slot
        SlotUD_str += super(SlotUD, self).__str__()
        SlotUD_str += (
            "point_list = "
            + linesep
            + str(self.point_list).replace(linesep, linesep + "\t")
            + linesep
        )
        SlotUD_str += "is_sym = " + str(self.is_sym) + linesep
        return SlotUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotUD, self).__eq__(other):
            return False
        if other.point_list != self.point_list:
            return False
        if other.is_sym != self.is_sym:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Slot
        SlotUD_dict = super(SlotUD, self).as_dict()
        SlotUD_dict["point_list"] = self.point_list
        SlotUD_dict["is_sym"] = self.is_sym
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotUD_dict["__class__"] = "SlotUD"
        return SlotUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.point_list = None
        self.is_sym = None
        # Set to None the properties inherited from Slot
        super(SlotUD, self)._set_None()

    def _get_point_list(self):
        """getter of point_list"""
        return self._point_list

    def _set_point_list(self, value):
        """setter of point_list"""
        check_var("point_list", value, "list")
        self._point_list = value

    # Coordinates of the slot points (will be connected in order with Segments)
    # Type : list
    point_list = property(
        fget=_get_point_list,
        fset=_set_point_list,
        doc=u"""Coordinates of the slot points (will be connected in order with Segments)""",
    )

    def _get_is_sym(self):
        """getter of is_sym"""
        return self._is_sym

    def _set_is_sym(self, value):
        """setter of is_sym"""
        check_var("is_sym", value, "bool")
        self._is_sym = value

    # True to enter only half of the point coordinates
    # Type : bool
    is_sym = property(
        fget=_get_is_sym,
        fset=_set_is_sym,
        doc=u"""True to enter only half of the point coordinates""",
    )
