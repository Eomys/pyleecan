# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Shaft.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Shaft
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
    from ..Methods.Machine.Shaft.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.Shaft.comp_mass import comp_mass
except ImportError as error:
    comp_mass = error

try:
    from ..Methods.Machine.Shaft.plot import plot
except ImportError as error:
    plot = error


from ._check import InitUnKnowClassError
from .Material import Material


class Shaft(FrozenClass):
    """machine shaft"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Shaft.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Shaft method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.Shaft.comp_mass
    if isinstance(comp_mass, ImportError):
        comp_mass = property(
            fget=lambda x: raise_(
                ImportError("Can't use Shaft method comp_mass: " + str(comp_mass))
            )
        )
    else:
        comp_mass = comp_mass
    # cf Methods.Machine.Shaft.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Shaft method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Lshaft=0.442, mat_type=-1, Drsh=0.045, init_dict=None, init_str=None
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
            if "Lshaft" in list(init_dict.keys()):
                Lshaft = init_dict["Lshaft"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Drsh" in list(init_dict.keys()):
                Drsh = init_dict["Drsh"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Lshaft = Lshaft
        self.mat_type = mat_type
        self.Drsh = Drsh

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Shaft_str = ""
        if self.parent is None:
            Shaft_str += "parent = None " + linesep
        else:
            Shaft_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Shaft_str += "Lshaft = " + str(self.Lshaft) + linesep
        if self.mat_type is not None:
            tmp = self.mat_type.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Shaft_str += "mat_type = " + tmp
        else:
            Shaft_str += "mat_type = None" + linesep + linesep
        Shaft_str += "Drsh = " + str(self.Drsh) + linesep
        return Shaft_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Lshaft != self.Lshaft:
            return False
        if other.mat_type != self.mat_type:
            return False
        if other.Drsh != self.Drsh:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Lshaft != self._Lshaft:
            diff_list.append(name + ".Lshaft")
        if (other.mat_type is None and self.mat_type is not None) or (
            other.mat_type is not None and self.mat_type is None
        ):
            diff_list.append(name + ".mat_type None mismatch")
        elif self.mat_type is not None:
            diff_list.extend(
                self.mat_type.compare(other.mat_type, name=name + ".mat_type")
            )
        if other._Drsh != self._Drsh:
            diff_list.append(name + ".Drsh")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Lshaft)
        S += getsizeof(self.mat_type)
        S += getsizeof(self.Drsh)
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

        Shaft_dict = dict()
        Shaft_dict["Lshaft"] = self.Lshaft
        if self.mat_type is None:
            Shaft_dict["mat_type"] = None
        else:
            Shaft_dict["mat_type"] = self.mat_type.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Shaft_dict["Drsh"] = self.Drsh
        # The class name is added to the dict for deserialisation purpose
        Shaft_dict["__class__"] = "Shaft"
        return Shaft_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Lshaft = None
        if self.mat_type is not None:
            self.mat_type._set_None()
        self.Drsh = None

    def _get_Lshaft(self):
        """getter of Lshaft"""
        return self._Lshaft

    def _set_Lshaft(self, value):
        """setter of Lshaft"""
        check_var("Lshaft", value, "float", Vmin=0)
        self._Lshaft = value

    Lshaft = property(
        fget=_get_Lshaft,
        fset=_set_Lshaft,
        doc=u"""length of the rotor shaft [m] (used for weight & cost estimation only)

        :Type: float
        :min: 0
        """,
    )

    def _get_mat_type(self):
        """getter of mat_type"""
        return self._mat_type

    def _set_mat_type(self, value):
        """setter of mat_type"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "mat_type"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Material()
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    mat_type = property(
        fget=_get_mat_type,
        fset=_set_mat_type,
        doc=u"""Shaft's Material

        :Type: Material
        """,
    )

    def _get_Drsh(self):
        """getter of Drsh"""
        return self._Drsh

    def _set_Drsh(self, value):
        """setter of Drsh"""
        check_var("Drsh", value, "float", Vmin=0)
        self._Drsh = value

    Drsh = property(
        fget=_get_Drsh,
        fset=_set_Drsh,
        doc=u"""diameter of the rotor shaft [m], used to estimate bearing diameter for friction losses

        :Type: float
        :min: 0
        """,
    )
