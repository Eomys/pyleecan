# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/ModelBH_linear_sat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/ModelBH_linear_sat
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Material.ModelBH_linear_sat.get_BH import get_BH
except ImportError as error:
    get_BH = error

try:
    from ..Methods.Material.ModelBH_linear_sat.BH_func import BH_func
except ImportError as error:
    BH_func = error


from ._check import InitUnKnowClassError


class ModelBH_linear_sat(ModelBH):
    """Abstract class for BH curve model """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Material.ModelBH_linear_sat.get_BH
    if isinstance(get_BH, ImportError):
        get_BH = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ModelBH_linear_sat method get_BH: " + str(get_BH)
                )
            )
        )
    else:
        get_BH = get_BH
    # cf Methods.Material.ModelBH_linear_sat.BH_func
    if isinstance(BH_func, ImportError):
        BH_func = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ModelBH_linear_sat method BH_func: " + str(BH_func)
                )
            )
        )
    else:
        BH_func = BH_func
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Bs=None,
        mu_a=None,
        param1=1.89,
        param2=240,
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
            if "Bs" in list(init_dict.keys()):
                Bs = init_dict["Bs"]
            if "mu_a" in list(init_dict.keys()):
                mu_a = init_dict["mu_a"]
            if "param1" in list(init_dict.keys()):
                param1 = init_dict["param1"]
            if "param2" in list(init_dict.keys()):
                param2 = init_dict["param2"]
            if "Bmax" in list(init_dict.keys()):
                Bmax = init_dict["Bmax"]
            if "Hmax" in list(init_dict.keys()):
                Hmax = init_dict["Hmax"]
            if "delta" in list(init_dict.keys()):
                delta = init_dict["delta"]
        # Set the properties (value check and convertion are done in setter)
        self.Bs = Bs
        self.mu_a = mu_a
        self.param1 = param1
        self.param2 = param2
        # Call ModelBH init
        super(ModelBH_linear_sat, self).__init__(Bmax=Bmax, Hmax=Hmax, delta=delta)
        # The class is frozen (in ModelBH init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ModelBH_linear_sat_str = ""
        # Get the properties inherited from ModelBH
        ModelBH_linear_sat_str += super(ModelBH_linear_sat, self).__str__()
        ModelBH_linear_sat_str += "Bs = " + str(self.Bs) + linesep
        ModelBH_linear_sat_str += "mu_a = " + str(self.mu_a) + linesep
        ModelBH_linear_sat_str += "param1 = " + str(self.param1) + linesep
        ModelBH_linear_sat_str += "param2 = " + str(self.param2) + linesep
        return ModelBH_linear_sat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ModelBH
        if not super(ModelBH_linear_sat, self).__eq__(other):
            return False
        if other.Bs != self.Bs:
            return False
        if other.mu_a != self.mu_a:
            return False
        if other.param1 != self.param1:
            return False
        if other.param2 != self.param2:
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
        diff_list.extend(super(ModelBH_linear_sat, self).compare(other, name=name))
        if other._Bs != self._Bs:
            diff_list.append(name + ".Bs")
        if other._mu_a != self._mu_a:
            diff_list.append(name + ".mu_a")
        if other._param1 != self._param1:
            diff_list.append(name + ".param1")
        if other._param2 != self._param2:
            diff_list.append(name + ".param2")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ModelBH
        S += super(ModelBH_linear_sat, self).__sizeof__()
        S += getsizeof(self.Bs)
        S += getsizeof(self.mu_a)
        S += getsizeof(self.param1)
        S += getsizeof(self.param2)
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
        ModelBH_linear_sat_dict = super(ModelBH_linear_sat, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ModelBH_linear_sat_dict["Bs"] = self.Bs
        ModelBH_linear_sat_dict["mu_a"] = self.mu_a
        ModelBH_linear_sat_dict["param1"] = self.param1
        ModelBH_linear_sat_dict["param2"] = self.param2
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ModelBH_linear_sat_dict["__class__"] = "ModelBH_linear_sat"
        return ModelBH_linear_sat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Bs = None
        self.mu_a = None
        self.param1 = None
        self.param2 = None
        # Set to None the properties inherited from ModelBH
        super(ModelBH_linear_sat, self)._set_None()

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
        doc=u"""Saturation flux density

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
        doc=u"""Linear permeability

        :Type: float
        """,
    )

    def _get_param1(self):
        """getter of param1"""
        return self._param1

    def _set_param1(self, value):
        """setter of param1"""
        check_var("param1", value, "float")
        self._param1 = value

    param1 = property(
        fget=_get_param1,
        fset=_set_param1,
        doc=u"""Init value for Bs for fitting algorithm

        :Type: float
        """,
    )

    def _get_param2(self):
        """getter of param2"""
        return self._param2

    def _set_param2(self, value):
        """setter of param2"""
        check_var("param2", value, "float")
        self._param2 = value

    param2 = property(
        fget=_get_param2,
        fset=_set_param2,
        doc=u"""Init value for mu_a for fitting algorithm

        :Type: float
        """,
    )
