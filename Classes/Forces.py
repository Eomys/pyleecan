# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class Forces(FrozenClass):
    """Force module abstract object"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, is_MTag=True, is_VWP=False, is_comp_teeth_forces=False, is_comp_nodal_forces=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["is_MTag", "is_VWP", "is_comp_teeth_forces", "is_comp_nodal_forces"])
            # Overwrite default value with init_dict content
            if "is_MTag" in list(init_dict.keys()):
                is_MTag = init_dict["is_MTag"]
            if "is_VWP" in list(init_dict.keys()):
                is_VWP = init_dict["is_VWP"]
            if "is_comp_teeth_forces" in list(init_dict.keys()):
                is_comp_teeth_forces = init_dict["is_comp_teeth_forces"]
            if "is_comp_nodal_forces" in list(init_dict.keys()):
                is_comp_nodal_forces = init_dict["is_comp_nodal_forces"]
        # Initialisation by argument
        self.parent = None
        self.is_MTag = is_MTag
        self.is_VWP = is_VWP
        self.is_comp_teeth_forces = is_comp_teeth_forces
        self.is_comp_nodal_forces = is_comp_nodal_forces

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Forces_str = ""
        if self.parent is None:
            Forces_str += "parent = None " + linesep
        else:
            Forces_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Forces_str += "is_MTag = " + str(self.is_MTag) + linesep
        Forces_str += "is_VWP = " + str(self.is_VWP) + linesep
        Forces_str += "is_comp_teeth_forces = " + str(self.is_comp_teeth_forces) + linesep
        Forces_str += "is_comp_nodal_forces = " + str(self.is_comp_nodal_forces)
        return Forces_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_MTag != self.is_MTag:
            return False
        if other.is_VWP != self.is_VWP:
            return False
        if other.is_comp_teeth_forces != self.is_comp_teeth_forces:
            return False
        if other.is_comp_nodal_forces != self.is_comp_nodal_forces:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Forces_dict = dict()
        Forces_dict["is_MTag"] = self.is_MTag
        Forces_dict["is_VWP"] = self.is_VWP
        Forces_dict["is_comp_teeth_forces"] = self.is_comp_teeth_forces
        Forces_dict["is_comp_nodal_forces"] = self.is_comp_nodal_forces
        # The class name is added to the dict fordeserialisation purpose
        Forces_dict["__class__"] = "Force"
        return Forces_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_MTag = None
        self.is_VWP = None
        self.is_comp_teeth_forces = None
        self.is_comp_nodal_forces = None

    def _get_is_MTag(self):
        """getter of is_MTag"""
        return self._is_MTag

    def _set_is_MTag(self, value):
        """setter of is_MTag"""
        check_var("is_MTag", value, "bool")
        self._is_MTag = value

    # 1 to compute airgap surface forces
    # Type : bool
    is_MTag = property(fget=_get_is_MTag, fset=_set_is_MTag,
                       doc=u"""1 to compute airgap surface forces""")

    def _get_is_VWP(self):
        """getter of is_VWP"""
        return self._is_VWP

    def _set_is_VWP(self, value):
        """setter of is_VWP"""
        check_var("is_VWP", value, "bool")
        self._is_VWP = value

    # 1 to compute nodal forces
    # Type : bool
    is_VWP = property(fget=_get_is_VWP, fset=_set_is_VWP,
                      doc=u"""1 to compute nodal forces""")

    def _get_is_comp_teeth_forces(self):
        """getter of is_comp_teeth_forces"""
        return self._is_comp_teeth_forces

    def _set_is_comp_teeth_forces(self, value):
        """setter of is_comp_teeth_forces"""
        check_var("is_comp_teeth_forces", value, "bool")
        self._is_comp_teeth_forces = value

    # 1 to compute lumped tooth forces
    # Type : bool
    is_comp_teeth_forces = property(fget=_get_is_comp_teeth_forces, fset=_set_is_comp_teeth_forces,
                                    doc=u"""1 to compute lumped tooth forces""")

    def _get_is_comp_nodal_forces(self):
        """getter of is_comp_nodal_forces"""
        return self._is_comp_nodal_forces

    def _set_is_comp_nodal_forces(self, value):
        """setter of is_comp_nodal_forces"""
        check_var("is_comp_nodal_forces", value, "bool")
        self._is_comp_nodal_forces = value

    # 1 to compute lumped tooth forces
    # Type : bool
    is_comp_nodal_forces = property(fget=_get_is_comp_nodal_forces, fset=_set_is_comp_nodal_forces,
                                    doc=u"""1 to compute lumped tooth forces""")
