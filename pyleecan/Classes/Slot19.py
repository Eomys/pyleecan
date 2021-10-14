# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/Slot19.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/Slot19
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
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.Slot19._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.Slot19.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.Slot19.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.Slot19.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.Slot19.comp_angle_bottom import comp_angle_bottom
except ImportError as error:
    comp_angle_bottom = error

try:
    from ..Methods.Slot.Slot19.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.Slot19.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error


from ._check import InitUnKnowClassError


class Slot19(Slot):
    """trapezoidal slot with rounded bottom"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.Slot19._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot19 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.Slot19.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot19 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.Slot19.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot19 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.Slot19.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot19 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.Slot19.comp_angle_bottom
    if isinstance(comp_angle_bottom, ImportError):
        comp_angle_bottom = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot19 method comp_angle_bottom: "
                    + str(comp_angle_bottom)
                )
            )
        )
    else:
        comp_angle_bottom = comp_angle_bottom
    # cf Methods.Slot.Slot19.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot19 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.Slot19.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot19 method comp_surface: " + str(comp_surface)
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
        self,
        W0=0.013,
        H0=0.02,
        W1=0.01,
        Wx_is_rad=False,
        Zs=36,
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
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "Wx_is_rad" in list(init_dict.keys()):
                Wx_is_rad = init_dict["Wx_is_rad"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.H0 = H0
        self.W1 = W1
        self.Wx_is_rad = Wx_is_rad
        # Call Slot init
        super(Slot19, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Slot19_str = ""
        # Get the properties inherited from Slot
        Slot19_str += super(Slot19, self).__str__()
        Slot19_str += "W0 = " + str(self.W0) + linesep
        Slot19_str += "H0 = " + str(self.H0) + linesep
        Slot19_str += "W1 = " + str(self.W1) + linesep
        Slot19_str += "Wx_is_rad = " + str(self.Wx_is_rad) + linesep
        return Slot19_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(Slot19, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.W1 != self.W1:
            return False
        if other.Wx_is_rad != self.Wx_is_rad:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(super(Slot19, self).compare(other, name=name))
        if other._W0 != self._W0:
            diff_list.append(name + ".W0")
        if other._H0 != self._H0:
            diff_list.append(name + ".H0")
        if other._W1 != self._W1:
            diff_list.append(name + ".W1")
        if other._Wx_is_rad != self._Wx_is_rad:
            diff_list.append(name + ".Wx_is_rad")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(Slot19, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.H0)
        S += getsizeof(self.W1)
        S += getsizeof(self.Wx_is_rad)
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

        # Get the properties inherited from Slot
        Slot19_dict = super(Slot19, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Slot19_dict["W0"] = self.W0
        Slot19_dict["H0"] = self.H0
        Slot19_dict["W1"] = self.W1
        Slot19_dict["Wx_is_rad"] = self.Wx_is_rad
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Slot19_dict["__class__"] = "Slot19"
        return Slot19_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.W1 = None
        self.Wx_is_rad = None
        # Set to None the properties inherited from Slot
        super(Slot19, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Slot top width

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
        doc=u"""Slot height

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
        doc=u"""Slot bottom width.

        :Type: float
        :min: 0
        """,
    )

    def _get_Wx_is_rad(self):
        """getter of Wx_is_rad"""
        return self._Wx_is_rad

    def _set_Wx_is_rad(self, value):
        """setter of Wx_is_rad"""
        check_var("Wx_is_rad", value, "bool")
        self._Wx_is_rad = value

    Wx_is_rad = property(
        fget=_get_Wx_is_rad,
        fset=_set_Wx_is_rad,
        doc=u"""Wx unit, 0 for m, 1 for rad

        :Type: bool
        """,
    )
