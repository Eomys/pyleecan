# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/ModelBH.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/ModelBH
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Material.ModelBH.get_BH import get_BH
except ImportError as error:
    get_BH = error

try:
    from ..Methods.Material.ModelBH.fit_model import fit_model
except ImportError as error:
    fit_model = error


from ._check import InitUnKnowClassError


class ModelBH(FrozenClass):
    """Abstract class for BH curve model """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Material.ModelBH.get_BH
    if isinstance(get_BH, ImportError):
        get_BH = property(
            fget=lambda x: raise_(
                ImportError("Can't use ModelBH method get_BH: " + str(get_BH))
            )
        )
    else:
        get_BH = get_BH
    # cf Methods.Material.ModelBH.fit_model
    if isinstance(fit_model, ImportError):
        fit_model = property(
            fget=lambda x: raise_(
                ImportError("Can't use ModelBH method fit_model: " + str(fit_model))
            )
        )
    else:
        fit_model = fit_model
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Bmax=2.31, Hmax=None, delta=100, init_dict=None, init_str=None):
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
            if "Bmax" in list(init_dict.keys()):
                Bmax = init_dict["Bmax"]
            if "Hmax" in list(init_dict.keys()):
                Hmax = init_dict["Hmax"]
            if "delta" in list(init_dict.keys()):
                delta = init_dict["delta"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Bmax = Bmax
        self.Hmax = Hmax
        self.delta = delta

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ModelBH_str = ""
        if self.parent is None:
            ModelBH_str += "parent = None " + linesep
        else:
            ModelBH_str += "parent = " + str(type(self.parent)) + " object" + linesep
        ModelBH_str += "Bmax = " + str(self.Bmax) + linesep
        ModelBH_str += "Hmax = " + str(self.Hmax) + linesep
        ModelBH_str += "delta = " + str(self.delta) + linesep
        return ModelBH_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Bmax != self.Bmax:
            return False
        if other.Hmax != self.Hmax:
            return False
        if other.delta != self.delta:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Bmax != self._Bmax:
            diff_list.append(name + ".Bmax")
        if other._Hmax != self._Hmax:
            diff_list.append(name + ".Hmax")
        if other._delta != self._delta:
            diff_list.append(name + ".delta")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Bmax)
        S += getsizeof(self.Hmax)
        S += getsizeof(self.delta)
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

        ModelBH_dict = dict()
        ModelBH_dict["Bmax"] = self.Bmax
        ModelBH_dict["Hmax"] = self.Hmax
        ModelBH_dict["delta"] = self.delta
        # The class name is added to the dict for deserialisation purpose
        ModelBH_dict["__class__"] = "ModelBH"
        return ModelBH_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Bmax = None
        self.Hmax = None
        self.delta = None

    def _get_Bmax(self):
        """getter of Bmax"""
        return self._Bmax

    def _set_Bmax(self, value):
        """setter of Bmax"""
        check_var("Bmax", value, "float")
        self._Bmax = value

    Bmax = property(
        fget=_get_Bmax,
        fset=_set_Bmax,
        doc=u"""Max value of B for extrapolation

        :Type: float
        """,
    )

    def _get_Hmax(self):
        """getter of Hmax"""
        return self._Hmax

    def _set_Hmax(self, value):
        """setter of Hmax"""
        check_var("Hmax", value, "float")
        self._Hmax = value

    Hmax = property(
        fget=_get_Hmax,
        fset=_set_Hmax,
        doc=u"""Max value of H for extrapolation

        :Type: float
        """,
    )

    def _get_delta(self):
        """getter of delta"""
        return self._delta

    def _set_delta(self, value):
        """setter of delta"""
        check_var("delta", value, "float")
        self._delta = value

    delta = property(
        fget=_get_delta,
        fset=_set_delta,
        doc=u"""Step value for H

        :Type: float
        """,
    )
