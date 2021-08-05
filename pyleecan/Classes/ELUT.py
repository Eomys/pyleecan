# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ELUT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ELUT
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ELUT.get_parameters import get_parameters
except ImportError as error:
    get_parameters = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ELUT(FrozenClass):
    """Abstract class for Electrical Look Up Table (ELUT)"""

    VERSION = 1

    # cf Methods.Simulation.ELUT.get_parameters
    if isinstance(get_parameters, ImportError):
        get_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT method get_parameters: " + str(get_parameters)
                )
            )
        )
    else:
        get_parameters = get_parameters
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Rs=None,
        Ls=None,
        Tsta_ref=20,
        K_RSE_sta=None,
        K_ISE_sta=None,
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
            if "Rs" in list(init_dict.keys()):
                Rs = init_dict["Rs"]
            if "Ls" in list(init_dict.keys()):
                Ls = init_dict["Ls"]
            if "Tsta_ref" in list(init_dict.keys()):
                Tsta_ref = init_dict["Tsta_ref"]
            if "K_RSE_sta" in list(init_dict.keys()):
                K_RSE_sta = init_dict["K_RSE_sta"]
            if "K_ISE_sta" in list(init_dict.keys()):
                K_ISE_sta = init_dict["K_ISE_sta"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Rs = Rs
        self.Ls = Ls
        self.Tsta_ref = Tsta_ref
        self.K_RSE_sta = K_RSE_sta
        self.K_ISE_sta = K_ISE_sta

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ELUT_str = ""
        if self.parent is None:
            ELUT_str += "parent = None " + linesep
        else:
            ELUT_str += "parent = " + str(type(self.parent)) + " object" + linesep
        ELUT_str += "Rs = " + str(self.Rs) + linesep
        ELUT_str += "Ls = " + str(self.Ls) + linesep
        ELUT_str += "Tsta_ref = " + str(self.Tsta_ref) + linesep
        ELUT_str += (
            "K_RSE_sta = "
            + linesep
            + str(self.K_RSE_sta).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_str += (
            "K_ISE_sta = "
            + linesep
            + str(self.K_ISE_sta).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ELUT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Rs != self.Rs:
            return False
        if other.Ls != self.Ls:
            return False
        if other.Tsta_ref != self.Tsta_ref:
            return False
        if not array_equal(other.K_RSE_sta, self.K_RSE_sta):
            return False
        if not array_equal(other.K_ISE_sta, self.K_ISE_sta):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Rs != self._Rs:
            diff_list.append(name + ".Rs")
        if other._Ls != self._Ls:
            diff_list.append(name + ".Ls")
        if other._Tsta_ref != self._Tsta_ref:
            diff_list.append(name + ".Tsta_ref")
        if not array_equal(other.K_RSE_sta, self.K_RSE_sta):
            diff_list.append(name + ".K_RSE_sta")
        if not array_equal(other.K_ISE_sta, self.K_ISE_sta):
            diff_list.append(name + ".K_ISE_sta")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Rs)
        S += getsizeof(self.Ls)
        S += getsizeof(self.Tsta_ref)
        S += getsizeof(self.K_RSE_sta)
        S += getsizeof(self.K_ISE_sta)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        ELUT_dict = dict()
        ELUT_dict["Rs"] = self.Rs
        ELUT_dict["Ls"] = self.Ls
        ELUT_dict["Tsta_ref"] = self.Tsta_ref
        if self.K_RSE_sta is None:
            ELUT_dict["K_RSE_sta"] = None
        else:
            ELUT_dict["K_RSE_sta"] = self.K_RSE_sta.tolist()
        if self.K_ISE_sta is None:
            ELUT_dict["K_ISE_sta"] = None
        else:
            ELUT_dict["K_ISE_sta"] = self.K_ISE_sta.tolist()
        # The class name is added to the dict for deserialisation purpose
        ELUT_dict["__class__"] = "ELUT"
        return ELUT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Rs = None
        self.Ls = None
        self.Tsta_ref = None
        self.K_RSE_sta = None
        self.K_ISE_sta = None

    def _get_Rs(self):
        """getter of Rs"""
        return self._Rs

    def _set_Rs(self, value):
        """setter of Rs"""
        check_var("Rs", value, "float")
        self._Rs = value

    Rs = property(
        fget=_get_Rs,
        fset=_set_Rs,
        doc=u"""DC phase winding resistance at Tsta_ref 

        :Type: float
        """,
    )

    def _get_Ls(self):
        """getter of Ls"""
        return self._Ls

    def _set_Ls(self, value):
        """setter of Ls"""
        check_var("Ls", value, "float")
        self._Ls = value

    Ls = property(
        fget=_get_Ls,
        fset=_set_Ls,
        doc=u"""Phase winding leakage inductance

        :Type: float
        """,
    )

    def _get_Tsta_ref(self):
        """getter of Tsta_ref"""
        return self._Tsta_ref

    def _set_Tsta_ref(self, value):
        """setter of Tsta_ref"""
        check_var("Tsta_ref", value, "float")
        self._Tsta_ref = value

    Tsta_ref = property(
        fget=_get_Tsta_ref,
        fset=_set_Tsta_ref,
        doc=u"""Stator winding average temperature associated to Rs, Ls parameters

        :Type: float
        """,
    )

    def _get_K_RSE_sta(self):
        """getter of K_RSE_sta"""
        return self._K_RSE_sta

    def _set_K_RSE_sta(self, value):
        """setter of K_RSE_sta"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("K_RSE_sta", value, "ndarray")
        self._K_RSE_sta = value

    K_RSE_sta = property(
        fget=_get_K_RSE_sta,
        fset=_set_K_RSE_sta,
        doc=u"""Stator winding Resistance Skin Effect factor function of frequency

        :Type: ndarray
        """,
    )

    def _get_K_ISE_sta(self):
        """getter of K_ISE_sta"""
        return self._K_ISE_sta

    def _set_K_ISE_sta(self, value):
        """setter of K_ISE_sta"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("K_ISE_sta", value, "ndarray")
        self._K_ISE_sta = value

    K_ISE_sta = property(
        fget=_get_K_ISE_sta,
        fset=_set_K_ISE_sta,
        doc=u"""Stator winding Inductance Skin Effect factor function of frequency

        :Type: ndarray
        """,
    )
