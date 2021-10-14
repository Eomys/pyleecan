# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/VentilationTrap.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/VentilationTrap
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
from .Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.VentilationTrap.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.VentilationTrap.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.VentilationTrap.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.VentilationTrap.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.VentilationTrap.get_center import get_center
except ImportError as error:
    get_center = error


from ._check import InitUnKnowClassError
from .Material import Material


class VentilationTrap(Hole):
    """Trapezoidal axial ventilation ducts"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.VentilationTrap.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.VentilationTrap.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use VentilationTrap method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.VentilationTrap.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method comp_radius: " + str(comp_radius)
                )
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.VentilationTrap.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method comp_surface: "
                    + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.VentilationTrap.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method get_center: " + str(get_center)
                )
            )
        )
    else:
        get_center = get_center
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        D0=1,
        H0=1,
        W1=1,
        W2=1,
        Zh=36,
        mat_void=-1,
        magnetization_dict_offset=None,
        Alpha0=0,
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
            if "D0" in list(init_dict.keys()):
                D0 = init_dict["D0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
            if "magnetization_dict_offset" in list(init_dict.keys()):
                magnetization_dict_offset = init_dict["magnetization_dict_offset"]
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
        # Set the properties (value check and convertion are done in setter)
        self.D0 = D0
        self.H0 = H0
        self.W1 = W1
        self.W2 = W2
        # Call Hole init
        super(VentilationTrap, self).__init__(
            Zh=Zh,
            mat_void=mat_void,
            magnetization_dict_offset=magnetization_dict_offset,
            Alpha0=Alpha0,
        )
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VentilationTrap_str = ""
        # Get the properties inherited from Hole
        VentilationTrap_str += super(VentilationTrap, self).__str__()
        VentilationTrap_str += "D0 = " + str(self.D0) + linesep
        VentilationTrap_str += "H0 = " + str(self.H0) + linesep
        VentilationTrap_str += "W1 = " + str(self.W1) + linesep
        VentilationTrap_str += "W2 = " + str(self.W2) + linesep
        return VentilationTrap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(VentilationTrap, self).__eq__(other):
            return False
        if other.D0 != self.D0:
            return False
        if other.H0 != self.H0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Hole
        diff_list.extend(super(VentilationTrap, self).compare(other, name=name))
        if other._D0 != self._D0:
            diff_list.append(name + ".D0")
        if other._H0 != self._H0:
            diff_list.append(name + ".H0")
        if other._W1 != self._W1:
            diff_list.append(name + ".W1")
        if other._W2 != self._W2:
            diff_list.append(name + ".W2")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Hole
        S += super(VentilationTrap, self).__sizeof__()
        S += getsizeof(self.D0)
        S += getsizeof(self.H0)
        S += getsizeof(self.W1)
        S += getsizeof(self.W2)
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

        # Get the properties inherited from Hole
        VentilationTrap_dict = super(VentilationTrap, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        VentilationTrap_dict["D0"] = self.D0
        VentilationTrap_dict["H0"] = self.H0
        VentilationTrap_dict["W1"] = self.W1
        VentilationTrap_dict["W2"] = self.W2
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VentilationTrap_dict["__class__"] = "VentilationTrap"
        return VentilationTrap_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.D0 = None
        self.H0 = None
        self.W1 = None
        self.W2 = None
        # Set to None the properties inherited from Hole
        super(VentilationTrap, self)._set_None()

    def _get_D0(self):
        """getter of D0"""
        return self._D0

    def _set_D0(self, value):
        """setter of D0"""
        check_var("D0", value, "float", Vmin=0)
        self._D0 = value

    D0 = property(
        fget=_get_D0,
        fset=_set_D0,
        doc=u"""Hole height

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc=u"""Radius of the hole bottom

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc=u"""Hole small basis

        :Type: float
        :min: 0
        """,
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    W2 = property(
        fget=_get_W2,
        fset=_set_W2,
        doc=u"""Hole large basis

        :Type: float
        :min: 0
        """,
    )
