# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/ModelBH_arctangent.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/ModelBH_arctangent
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
from .ModelBH import ModelBH

from ._check import InitUnKnowClassError


class ModelBH_arctangent(ModelBH):
    """Abstract class for BH curve model """

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        k=None,
        mu_a=None,
        Bmax=2.31,
        Hmax=None,
        delta=100,
        init_dict=None,
        init_str=None,
    ):
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
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "mu_a" in list(init_dict.keys()):
                mu_a = init_dict["mu_a"]
            if "Bmax" in list(init_dict.keys()):
                Bmax = init_dict["Bmax"]
            if "Hmax" in list(init_dict.keys()):
                Hmax = init_dict["Hmax"]
            if "delta" in list(init_dict.keys()):
                delta = init_dict["delta"]
        # Set the properties (value check and convertion are done in setter)
        self.k = k
        self.mu_a = mu_a
        # Call ModelBH init
        super(ModelBH_arctangent, self).__init__(Bmax=Bmax, Hmax=Hmax, delta=delta)
        # The class is frozen (in ModelBH init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ModelBH_arctangent_str = ""
        # Get the properties inherited from ModelBH
        ModelBH_arctangent_str += super(ModelBH_arctangent, self).__str__()
        ModelBH_arctangent_str += "k = " + str(self.k) + linesep
        ModelBH_arctangent_str += "mu_a = " + str(self.mu_a) + linesep
        return ModelBH_arctangent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ModelBH
        if not super(ModelBH_arctangent, self).__eq__(other):
            return False
        if other.k != self.k:
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

        # Check the properties inherited from ModelBH
        diff_list.extend(super(ModelBH_arctangent, self).compare(other, name=name))
        if other._k != self._k:
            diff_list.append(name + ".k")
        if other._mu_a != self._mu_a:
            diff_list.append(name + ".mu_a")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ModelBH
        S += super(ModelBH_arctangent, self).__sizeof__()
        S += getsizeof(self.k)
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

        # Get the properties inherited from ModelBH
        ModelBH_arctangent_dict = super(ModelBH_arctangent, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ModelBH_arctangent_dict["k"] = self.k
        ModelBH_arctangent_dict["mu_a"] = self.mu_a
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ModelBH_arctangent_dict["__class__"] = "ModelBH_arctangent"
        return ModelBH_arctangent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k = None
        self.mu_a = None
        # Set to None the properties inherited from ModelBH
        super(ModelBH_arctangent, self)._set_None()

    def _get_k(self):
        """getter of k"""
        return self._k

    def _set_k(self, value):
        """setter of k"""
        check_var("k", value, "float")
        self._k = value

    k = property(
        fget=_get_k,
        fset=_set_k,
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
