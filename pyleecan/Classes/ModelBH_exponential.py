# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/ModelBH_exponential.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/ModelBH_exponential
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


class ModelBH_exponential(FrozenClass):
    """Abstract class for BH curve model """

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Bs=None, mu_a=None, init_dict=None, init_str=None):
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
            if "Bs" in list(init_dict.keys()):
                Bs = init_dict["Bs"]
            if "mu_a" in list(init_dict.keys()):
                mu_a = init_dict["mu_a"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Bs = Bs
        self.mu_a = mu_a

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ModelBH_exponential_str = ""
        if self.parent is None:
            ModelBH_exponential_str += "parent = None " + linesep
        else:
            ModelBH_exponential_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        ModelBH_exponential_str += "Bs = " + str(self.Bs) + linesep
        ModelBH_exponential_str += "mu_a = " + str(self.mu_a) + linesep
        return ModelBH_exponential_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Bs != self.Bs:
            return False
        if other.mu_a != self.mu_a:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Bs != self._Bs:
            diff_list.append(name + ".Bs")
        if other._mu_a != self._mu_a:
            diff_list.append(name + ".mu_a")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Bs)
        S += getsizeof(self.mu_a)
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

        ModelBH_exponential_dict = dict()
        ModelBH_exponential_dict["Bs"] = self.Bs
        ModelBH_exponential_dict["mu_a"] = self.mu_a
        # The class name is added to the dict for deserialisation purpose
        ModelBH_exponential_dict["__class__"] = "ModelBH_exponential"
        return ModelBH_exponential_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Bs = None
        self.mu_a = None

    def _get_Bs(self):
        """getter of Bs"""
        return self._Bs

    def _set_Bs(self, value):
        """setter of Bs"""
        check_var("Bs", value, "float")
        self._Bs = value

    Bs = property(
        fget=_get_Bs,
        fset=_set_Bs,
        doc=u"""BH curve parameter

        :Type: float
        """,
    )

    def _get_mu_a(self):
        """getter of mu_a"""
        return self._mu_a

    def _set_mu_a(self, value):
        """setter of mu_a"""
        check_var("mu_a", value, "float")
        self._mu_a = value

    mu_a = property(
        fget=_get_mu_a,
        fset=_set_mu_a,
        doc=u"""Saturation permeability parameter

        :Type: float
        """,
    )
