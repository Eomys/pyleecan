# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Force import Force

from pyleecan.Methods.Simulation.ForceMT.comp_force import comp_force
from pyleecan.Methods.Simulation.ForceMT.comp_force_nodal import comp_force_nodal

from pyleecan.Classes.check import InitUnKnowClassError


class ForceMT(Force):
    """Force Maxwell tensor model"""

    VERSION = 1

    # cf Methods.Simulation.ForceMT.comp_force
    comp_force = comp_force
    # cf Methods.Simulation.ForceMT.comp_force_nodal
    comp_force_nodal = comp_force_nodal
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
        # Call Force init
        super(ForceMT, self).__init__(is_comp_nodal_force=is_comp_nodal_force)
        # The class is frozen (in Force init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ForceMT_str = ""
        # Get the properties inherited from Force
        ForceMT_str += super(ForceMT, self).__str__() + linesep
        return ForceMT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Force
        if not super(ForceMT, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Force
        ForceMT_dict = super(ForceMT, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ForceMT_dict["__class__"] = "ForceMT"
        return ForceMT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Force
        super(ForceMT, self)._set_None()


