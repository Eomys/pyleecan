# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class MatElectrical(FrozenClass):
    """material electrical properties"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, rho=1, epsr=1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["rho", "epsr"])
            # Overwrite default value with init_dict content
            if "rho" in list(init_dict.keys()):
                rho = init_dict["rho"]
            if "epsr" in list(init_dict.keys()):
                epsr = init_dict["epsr"]
        # Initialisation by argument
        self.parent = None
        self.rho = rho
        self.epsr = epsr

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatElectrical_str = ""
        if self.parent is None:
            MatElectrical_str += "parent = None " + linesep
        else:
            MatElectrical_str += "parent = " + str(type(self.parent)) + " object" + linesep
        MatElectrical_str += "rho = " + str(self.rho) + linesep
        MatElectrical_str += "epsr = " + str(self.epsr)
        return MatElectrical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rho != self.rho:
            return False
        if other.epsr != self.epsr:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatElectrical_dict = dict()
        MatElectrical_dict["rho"] = self.rho
        MatElectrical_dict["epsr"] = self.epsr
        # The class name is added to the dict fordeserialisation purpose
        MatElectrical_dict["__class__"] = "MatElectrical"
        return MatElectrical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rho = None
        self.epsr = None

    def _get_rho(self):
        """getter of rho"""
        return self._rho

    def _set_rho(self, value):
        """setter of rho"""
        check_var("rho", value, "float", Vmin=0)
        self._rho = value

    # Resistivity at 20°C
    # Type : float, min = 0
    rho = property(fget=_get_rho, fset=_set_rho,
                   doc=u"""Resistivity at 20°C""")

    def _get_epsr(self):
        """getter of epsr"""
        return self._epsr

    def _set_epsr(self, value):
        """setter of epsr"""
        check_var("epsr", value, "float", Vmin=0)
        self._epsr = value

    # Relative dielectric constant
    # Type : float, min = 0
    epsr = property(fget=_get_epsr, fset=_set_epsr,
                    doc=u"""Relative dielectric constant""")
