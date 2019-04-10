# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Conductor import Conductor

from pyleecan.Methods.Machine.CondType22.comp_surface_active import comp_surface_active
from pyleecan.Methods.Machine.CondType22.comp_surface import comp_surface

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class CondType22(Conductor):
    """conductor with only surface definition without specifc shape nor isolation"""

    VERSION = 1

    # cf Methods.Machine.CondType22.comp_surface_active
    comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType22.comp_surface
    comp_surface = comp_surface
    # save method is available in all object
    save = save

    def __init__(self, Sbar=0.01, cond_mat=-1, ins_mat=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if cond_mat == -1:
            cond_mat = Material()
        if ins_mat == -1:
            ins_mat = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Sbar", "cond_mat", "ins_mat"])
            # Overwrite default value with init_dict content
            if "Sbar" in list(init_dict.keys()):
                Sbar = init_dict["Sbar"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Initialisation by argument
        self.Sbar = Sbar
        # Call Conductor init
        super(CondType22, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        CondType22_str = ""
        # Get the properties inherited from Conductor
        CondType22_str += super(CondType22, self).__str__() + linesep
        CondType22_str += "Sbar = " + str(self.Sbar)
        return CondType22_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType22, self).__eq__(other):
            return False
        if other.Sbar != self.Sbar:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Conductor
        CondType22_dict = super(CondType22, self).as_dict()
        CondType22_dict["Sbar"] = self.Sbar
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        CondType22_dict["__class__"] = "CondType22"
        return CondType22_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Sbar = None
        # Set to None the properties inherited from Conductor
        super(CondType22, self)._set_None()

    def _get_Sbar(self):
        """getter of Sbar"""
        return self._Sbar

    def _set_Sbar(self, value):
        """setter of Sbar"""
        check_var("Sbar", value, "float", Vmin=0)
        self._Sbar = value

    # Surface of the Slot
    # Type : float, min = 0
    Sbar = property(fget=_get_Sbar, fset=_set_Sbar,
                    doc=u"""Surface of the Slot""")
