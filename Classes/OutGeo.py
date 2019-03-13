# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class OutGeo(FrozenClass):
    """Gather the geometrical and the global outputs"""

    VERSION = 1

    def __init__(self, name_phase_stator=None, name_phase_rotor=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["name_phase_stator", "name_phase_rotor"])
            # Overwrite default value with init_dict content
            if "name_phase_stator" in list(init_dict.keys()):
                name_phase_stator = init_dict["name_phase_stator"]
            if "name_phase_rotor" in list(init_dict.keys()):
                name_phase_rotor = init_dict["name_phase_rotor"]
        # Initialisation by argument
        self.parent = None
        self.name_phase_stator = name_phase_stator
        self.name_phase_rotor = name_phase_rotor

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutGeo_str = ""
        if self.parent is None:
            OutGeo_str += "parent = None " + linesep
        else:
            OutGeo_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutGeo_str += (
            "name_phase_stator = " + linesep + str(self.name_phase_stator) + linesep
        )
        OutGeo_str += "name_phase_rotor = " + linesep + str(self.name_phase_rotor)
        return OutGeo_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name_phase_stator != self.name_phase_stator:
            return False
        if other.name_phase_rotor != self.name_phase_rotor:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutGeo_dict = dict()
        OutGeo_dict["name_phase_stator"] = self.name_phase_stator
        OutGeo_dict["name_phase_rotor"] = self.name_phase_rotor
        # The class name is added to the dict fordeserialisation purpose
        OutGeo_dict["__class__"] = "OutGeo"
        return OutGeo_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name_phase_stator = None
        self.name_phase_rotor = None

    def _get_name_phase_stator(self):
        """getter of name_phase_stator"""
        return self._name_phase_stator

    def _set_name_phase_stator(self, value):
        """setter of name_phase_stator"""
        check_var("name_phase_stator", value, "list")
        self._name_phase_stator = value

    # Name of the phases of the stator
    # Type : list
    name_phase_stator = property(
        fget=_get_name_phase_stator,
        fset=_set_name_phase_stator,
        doc=u"""Name of the phases of the stator""",
    )

    def _get_name_phase_rotor(self):
        """getter of name_phase_rotor"""
        return self._name_phase_rotor

    def _set_name_phase_rotor(self, value):
        """setter of name_phase_rotor"""
        check_var("name_phase_rotor", value, "list")
        self._name_phase_rotor = value

    # Name of the phases of the rotor
    # Type : list
    name_phase_rotor = property(
        fget=_get_name_phase_rotor,
        fset=_set_name_phase_rotor,
        doc=u"""Name of the phases of the rotor""",
    )
