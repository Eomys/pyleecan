# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatElectrical.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatElectrical
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class MatElectrical(FrozenClass):
    """material electrical properties"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, rho=1, epsr=1, alpha=1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "rho" in list(init_dict.keys()):
                rho = init_dict["rho"]
            if "epsr" in list(init_dict.keys()):
                epsr = init_dict["epsr"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.rho = rho
        self.epsr = epsr
        self.alpha = alpha

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._rho != self._rho:
            diff_list.append(name + ".rho")
        if other._epsr != self._epsr:
            diff_list.append(name + ".epsr")
        if other._alpha != self._alpha:
            diff_list.append(name + ".alpha")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.rho)
        S += getsizeof(self.epsr)
        S += getsizeof(self.alpha)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        MatElectrical_dict = dict()
        MatElectrical_dict["rho"] = self.rho
        MatElectrical_dict["epsr"] = self.epsr
        MatElectrical_dict["alpha"] = self.alpha
        # The class name is added to the dict for deserialisation purpose
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

    rho = property(
        fget=_get_rho,
        fset=_set_rho,
        doc=u"""Resistivity at 20 deg C

        :Type: float
        :min: 0
        """,
    )

    def _get_epsr(self):
        """getter of epsr"""
        return self._epsr

    def _set_epsr(self, value):
        """setter of epsr"""
        check_var("epsr", value, "float", Vmin=0)
        self._epsr = value

    epsr = property(
        fget=_get_epsr,
        fset=_set_epsr,
        doc=u"""Relative dielectric constant

        :Type: float
        :min: 0
        """,
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float", Vmin=0)
        self._alpha = value

    alpha = property(
        fget=_get_alpha,
        fset=_set_alpha,
        doc=u"""Thermal Coefficient

        :Type: float
        :min: 0
        """,
    )
