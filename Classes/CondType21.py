# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/CondType21.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.get_logger import get_logger
from pyleecan.Functions.save import save
from pyleecan.Classes.Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.CondType21.comp_surface_active import (
        comp_surface_active,
    )
except ImportError as error:
    comp_surface_active = error

try:
    from pyleecan.Methods.Machine.CondType21.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Machine.CondType21.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Machine.CondType21.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from pyleecan.Methods.Machine.CondType21.plot import plot
except ImportError as error:
    plot = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class CondType21(Conductor):
    """single rectangular conductor \nhas to be used for LamSquirrelCages's conductor"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType21.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType21.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType21.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType21.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType21.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType21 method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Hbar=0.01, Wbar=0.01, Wins=0, cond_mat=-1, ins_mat=-1, init_dict=None
    ):
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
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Hbar" in list(init_dict.keys()):
                Hbar = init_dict["Hbar"]
            if "Wbar" in list(init_dict.keys()):
                Wbar = init_dict["Wbar"]
            if "Wins" in list(init_dict.keys()):
                Wins = init_dict["Wins"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Initialisation by argument
        self.Hbar = Hbar
        self.Wbar = Wbar
        self.Wins = Wins
        # Call Conductor init
        super(CondType21, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        CondType21_str = ""
        # Get the properties inherited from Conductor
        CondType21_str += super(CondType21, self).__str__()
        CondType21_str += "Hbar = " + str(self.Hbar) + linesep
        CondType21_str += "Wbar = " + str(self.Wbar) + linesep
        CondType21_str += "Wins = " + str(self.Wins) + linesep
        return CondType21_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType21, self).__eq__(other):
            return False
        if other.Hbar != self.Hbar:
            return False
        if other.Wbar != self.Wbar:
            return False
        if other.Wins != self.Wins:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Conductor
        CondType21_dict = super(CondType21, self).as_dict()
        CondType21_dict["Hbar"] = self.Hbar
        CondType21_dict["Wbar"] = self.Wbar
        CondType21_dict["Wins"] = self.Wins
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        CondType21_dict["__class__"] = "CondType21"
        return CondType21_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hbar = None
        self.Wbar = None
        self.Wins = None
        # Set to None the properties inherited from Conductor
        super(CondType21, self)._set_None()

    def _get_Hbar(self):
        """getter of Hbar"""
        return self._Hbar

    def _set_Hbar(self, value):
        """setter of Hbar"""
        check_var("Hbar", value, "float", Vmin=0)
        self._Hbar = value

    # Bar height
    # Type : float, min = 0
    Hbar = property(fget=_get_Hbar, fset=_set_Hbar, doc=u"""Bar height""")

    def _get_Wbar(self):
        """getter of Wbar"""
        return self._Wbar

    def _set_Wbar(self, value):
        """setter of Wbar"""
        check_var("Wbar", value, "float", Vmin=0)
        self._Wbar = value

    # Bar width
    # Type : float, min = 0
    Wbar = property(fget=_get_Wbar, fset=_set_Wbar, doc=u"""Bar width""")

    def _get_Wins(self):
        """getter of Wins"""
        return self._Wins

    def _set_Wins(self, value):
        """setter of Wins"""
        check_var("Wins", value, "float", Vmin=0)
        self._Wins = value

    # Width of insulation
    # Type : float, min = 0
    Wins = property(fget=_get_Wins, fset=_set_Wins, doc=u"""Width of insulation""")
