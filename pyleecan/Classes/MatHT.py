# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatHT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatHT
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


class MatHT(FrozenClass):
    """Material Heat Transfer properties"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        lambda_x=1,
        lambda_y=1,
        lambda_z=1,
        Cp=1,
        alpha=0.00393,
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
            if "lambda_x" in list(init_dict.keys()):
                lambda_x = init_dict["lambda_x"]
            if "lambda_y" in list(init_dict.keys()):
                lambda_y = init_dict["lambda_y"]
            if "lambda_z" in list(init_dict.keys()):
                lambda_z = init_dict["lambda_z"]
            if "Cp" in list(init_dict.keys()):
                Cp = init_dict["Cp"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.lambda_x = lambda_x
        self.lambda_y = lambda_y
        self.lambda_z = lambda_z
        self.Cp = Cp
        self.alpha = alpha

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MatHT_str = ""
        if self.parent is None:
            MatHT_str += "parent = None " + linesep
        else:
            MatHT_str += "parent = " + str(type(self.parent)) + " object" + linesep
        MatHT_str += "lambda_x = " + str(self.lambda_x) + linesep
        MatHT_str += "lambda_y = " + str(self.lambda_y) + linesep
        MatHT_str += "lambda_z = " + str(self.lambda_z) + linesep
        MatHT_str += "Cp = " + str(self.Cp) + linesep
        MatHT_str += "alpha = " + str(self.alpha) + linesep
        return MatHT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.lambda_x != self.lambda_x:
            return False
        if other.lambda_y != self.lambda_y:
            return False
        if other.lambda_z != self.lambda_z:
            return False
        if other.Cp != self.Cp:
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
        if other._lambda_x != self._lambda_x:
            diff_list.append(name + ".lambda_x")
        if other._lambda_y != self._lambda_y:
            diff_list.append(name + ".lambda_y")
        if other._lambda_z != self._lambda_z:
            diff_list.append(name + ".lambda_z")
        if other._Cp != self._Cp:
            diff_list.append(name + ".Cp")
        if other._alpha != self._alpha:
            diff_list.append(name + ".alpha")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.lambda_x)
        S += getsizeof(self.lambda_y)
        S += getsizeof(self.lambda_z)
        S += getsizeof(self.Cp)
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

        MatHT_dict = dict()
        MatHT_dict["lambda_x"] = self.lambda_x
        MatHT_dict["lambda_y"] = self.lambda_y
        MatHT_dict["lambda_z"] = self.lambda_z
        MatHT_dict["Cp"] = self.Cp
        MatHT_dict["alpha"] = self.alpha
        # The class name is added to the dict for deserialisation purpose
        MatHT_dict["__class__"] = "MatHT"
        return MatHT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.lambda_x = None
        self.lambda_y = None
        self.lambda_z = None
        self.Cp = None
        self.alpha = None

    def _get_lambda_x(self):
        """getter of lambda_x"""
        return self._lambda_x

    def _set_lambda_x(self, value):
        """setter of lambda_x"""
        check_var("lambda_x", value, "float", Vmin=0)
        self._lambda_x = value

    lambda_x = property(
        fget=_get_lambda_x,
        fset=_set_lambda_x,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_lambda_y(self):
        """getter of lambda_y"""
        return self._lambda_y

    def _set_lambda_y(self, value):
        """setter of lambda_y"""
        check_var("lambda_y", value, "float", Vmin=0)
        self._lambda_y = value

    lambda_y = property(
        fget=_get_lambda_y,
        fset=_set_lambda_y,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_lambda_z(self):
        """getter of lambda_z"""
        return self._lambda_z

    def _set_lambda_z(self, value):
        """setter of lambda_z"""
        check_var("lambda_z", value, "float", Vmin=0)
        self._lambda_z = value

    lambda_z = property(
        fget=_get_lambda_z,
        fset=_set_lambda_z,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Cp(self):
        """getter of Cp"""
        return self._Cp

    def _set_Cp(self, value):
        """setter of Cp"""
        check_var("Cp", value, "float", Vmin=0)
        self._Cp = value

    Cp = property(
        fget=_get_Cp,
        fset=_set_Cp,
        doc=u"""specific heat capacity

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
        doc=u"""thermal expansion coefficient

        :Type: float
        :min: 0
        """,
    )
