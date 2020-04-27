# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Material/MatElectrical.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class MatElectrical(FrozenClass):
    """material electrical properties"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, rho=1, epsr=1, alpha=1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object
        - __init__ (init_str = s) s must be a string
        s is the file path to load """

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            rho = obj.rho
            epsr = obj.epsr
            alpha = obj.alpha
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "rho" in list(init_dict.keys()):
                rho = init_dict["rho"]
            if "epsr" in list(init_dict.keys()):
                epsr = init_dict["epsr"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Initialisation by argument
        self.parent = None
        self.rho = rho
        self.epsr = epsr
        self.alpha = alpha

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatElectrical_str = ""
        if self.parent is None:
            MatElectrical_str += "parent = None " + linesep
        else:
            MatElectrical_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MatElectrical_str += "rho = " + str(self.rho) + linesep
        MatElectrical_str += "epsr = " + str(self.epsr) + linesep
        MatElectrical_str += "alpha = " + str(self.alpha) + linesep
        return MatElectrical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rho != self.rho:
            return False
        if other.epsr != self.epsr:
            return False
        if other.alpha != self.alpha:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatElectrical_dict = dict()
        MatElectrical_dict["rho"] = self.rho
        MatElectrical_dict["epsr"] = self.epsr
        MatElectrical_dict["alpha"] = self.alpha
        # The class name is added to the dict fordeserialisation purpose
        MatElectrical_dict["__class__"] = "MatElectrical"
        return MatElectrical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rho = None
        self.epsr = None
        self.alpha = None

    def _get_rho(self):
        """getter of rho"""
        return self._rho

    def _set_rho(self, value):
        """setter of rho"""
        check_var("rho", value, "float", Vmin=0)
        self._rho = value

    # Resistivity at 20 deg C
    # Type : float, min = 0
    rho = property(fget=_get_rho, fset=_set_rho, doc=u"""Resistivity at 20 deg C""")

    def _get_epsr(self):
        """getter of epsr"""
        return self._epsr

    def _set_epsr(self, value):
        """setter of epsr"""
        check_var("epsr", value, "float", Vmin=0)
        self._epsr = value

    # Relative dielectric constant
    # Type : float, min = 0
    epsr = property(
        fget=_get_epsr, fset=_set_epsr, doc=u"""Relative dielectric constant"""
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float", Vmin=0)
        self._alpha = value

    # Thermal Coefficient
    # Type : float, min = 0
    alpha = property(fget=_get_alpha, fset=_set_alpha, doc=u"""Thermal Coefficient""")
