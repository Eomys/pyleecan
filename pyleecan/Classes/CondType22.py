# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType22.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType22
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
from .Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.CondType22.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType22.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error


from ._check import InitUnKnowClassError
from .Material import Material


class CondType22(Conductor):
    """conductor with only surface definition without specifc shape nor isolation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType22.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType22 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType22.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType22 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Sbar=0.01, cond_mat=-1, ins_mat=-1, init_dict=None, init_str=None
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
            if "Sbar" in list(init_dict.keys()):
                Sbar = init_dict["Sbar"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Sbar = Sbar
        # Call Conductor init
        super(CondType22, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType22_str = ""
        # Get the properties inherited from Conductor
        CondType22_str += super(CondType22, self).__str__()
        CondType22_str += "Sbar = " + str(self.Sbar) + linesep
        return CondType22_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType22, self).__eq__(other):
            return False
        if other.Sbar != self.Sbar:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Conductor
        diff_list.extend(super(CondType22, self).compare(other, name=name))
        if other._Sbar != self._Sbar:
            diff_list.append(name + ".Sbar")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType22, self).__sizeof__()
        S += getsizeof(self.Sbar)
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

        # Get the properties inherited from Conductor
        CondType22_dict = super(CondType22, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType22_dict["Sbar"] = self.Sbar
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType22_dict["__class__"] = "CondType22"
        return CondType22_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Sbar = None
        # Set to None the properties inherited from Conductor
        super(CondType22, self)._set_None()

    def _get_Sbar(self):
        """getter of Sbar"""
        return self._Sbar

    def _set_Sbar(self, value):
        """setter of Sbar"""
        check_var("Sbar", value, "float", Vmin=0)
        self._Sbar = value

    Sbar = property(
        fget=_get_Sbar,
        fset=_set_Sbar,
        doc=u"""Surface of the Slot

        :Type: float
        :min: 0
        """,
    )
