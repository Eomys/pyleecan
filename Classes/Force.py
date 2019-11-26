# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class Force(FrozenClass):
    """Forces module abstract object"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, is_comp_nodal_force=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["is_comp_nodal_force"])
            # Overwrite default value with init_dict content
            if "is_comp_nodal_force" in list(init_dict.keys()):
                is_comp_nodal_force = init_dict["is_comp_nodal_force"]
        # Initialisation by argument
        self.parent = None
        self.is_comp_nodal_force = is_comp_nodal_force

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Force_str = ""
        if self.parent is None:
            Force_str += "parent = None " + linesep
        else:
            Force_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Force_str += "is_comp_nodal_force = " + str(self.is_comp_nodal_force)
        return Force_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_comp_nodal_force != self.is_comp_nodal_force:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Force_dict = dict()
        Force_dict["is_comp_nodal_force"] = self.is_comp_nodal_force
        # The class name is added to the dict fordeserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_comp_nodal_force = None

    def _get_is_comp_nodal_force(self):
        """getter of is_comp_nodal_force"""
        return self._is_comp_nodal_force

    def _set_is_comp_nodal_force(self, value):
        """setter of is_comp_nodal_force"""
        check_var("is_comp_nodal_force", value, "bool")
        self._is_comp_nodal_force = value

    # 1 to compute lumped tooth forces
    # Type : bool
    is_comp_nodal_force = property(
        fget=_get_is_comp_nodal_force,
        fset=_set_is_comp_nodal_force,
        doc=u"""1 to compute lumped tooth forces""",
    )
