# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/EndWinding.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/EndWinding
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
    from ..Methods.Machine.EndWinding.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Machine.EndWinding.comp_inductance import comp_inductance
except ImportError as error:
    comp_inductance = error


from ._check import InitUnKnowClassError


class EndWinding(FrozenClass):
    """Abstract Class of the machine's end winding"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.EndWinding.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EndWinding method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Machine.EndWinding.comp_inductance
    if isinstance(comp_inductance, ImportError):
        comp_inductance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EndWinding method comp_inductance: "
                    + str(comp_inductance)
                )
            )
        )
    else:
        comp_inductance = comp_inductance
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Lew_enforced=0, init_dict=None, init_str=None):
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
            if "Lew_enforced" in list(init_dict.keys()):
                Lew_enforced = init_dict["Lew_enforced"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Lew_enforced = Lew_enforced

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EndWinding_str = ""
        if self.parent is None:
            EndWinding_str += "parent = None " + linesep
        else:
            EndWinding_str += "parent = " + str(type(self.parent)) + " object" + linesep
        EndWinding_str += "Lew_enforced = " + str(self.Lew_enforced) + linesep
        return EndWinding_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Lew_enforced != self.Lew_enforced:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Lew_enforced != self._Lew_enforced:
            diff_list.append(name + ".Lew_enforced")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Lew_enforced)
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

        EndWinding_dict = dict()
        EndWinding_dict["Lew_enforced"] = self.Lew_enforced
        # The class name is added to the dict for deserialisation purpose
        EndWinding_dict["__class__"] = "EndWinding"
        return EndWinding_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Lew_enforced = None

    def _get_Lew_enforced(self):
        """getter of Lew_enforced"""
        return self._Lew_enforced

    def _set_Lew_enforced(self, value):
        """setter of Lew_enforced"""
        check_var("Lew_enforced", value, "float", Vmin=0)
        self._Lew_enforced = value

    Lew_enforced = property(
        fget=_get_Lew_enforced,
        fset=_set_Lew_enforced,
        doc=u"""Enforced end-winding lekage inductance

        :Type: float
        :min: 0
        """,
    )
