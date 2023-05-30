# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotM18_2.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotM18_2
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotM18_2._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotM18_2.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotM18_2.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotM18_2.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotM18_2.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotM18_2.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotM18_2.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotM18_2.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Slot.SlotM18_2.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotM18_2.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error

try:
    from ..Methods.Slot.SlotM18_2.is_airgap_active import is_airgap_active
except ImportError as error:
    is_airgap_active = error

try:
    from ..Methods.Slot.SlotM18_2.is_full_pitch_active import is_full_pitch_active
except ImportError as error:
    is_full_pitch_active = error

try:
    from ..Methods.Slot.SlotM18_2.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error


from numpy import isnan
from ._check import InitUnKnowClassError


class SlotM18_2(Slot):
    """Double Polar Ring magnet"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotM18_2._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotM18_2.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotM18_2.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotM18_2 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotM18_2.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotM18_2.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotM18_2.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotM18_2.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotM18_2.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Slot.SlotM18_2.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotM18_2.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method plot_schematics: "
                    + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # cf Methods.Slot.SlotM18_2.is_airgap_active
    if isinstance(is_airgap_active, ImportError):
        is_airgap_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method is_airgap_active: "
                    + str(is_airgap_active)
                )
            )
        )
    else:
        is_airgap_active = is_airgap_active
    # cf Methods.Slot.SlotM18_2.is_full_pitch_active
    if isinstance(is_full_pitch_active, ImportError):
        is_full_pitch_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method is_full_pitch_active: "
                    + str(is_full_pitch_active)
                )
            )
        )
    else:
        is_full_pitch_active = is_full_pitch_active
    # cf Methods.Slot.SlotM18_2.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM18_2 method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Hmag_bore=0.001,
        Hmag_gap=0.001,
        Zs=36,
        wedge_mat=None,
        is_bore=True,
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
            if "Hmag_bore" in list(init_dict.keys()):
                Hmag_bore = init_dict["Hmag_bore"]
            if "Hmag_gap" in list(init_dict.keys()):
                Hmag_gap = init_dict["Hmag_gap"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.Hmag_bore = Hmag_bore
        self.Hmag_gap = Hmag_gap
        # Call Slot init
        super(SlotM18_2, self).__init__(Zs=Zs, wedge_mat=wedge_mat, is_bore=is_bore)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotM18_2_str = ""
        # Get the properties inherited from Slot
        SlotM18_2_str += super(SlotM18_2, self).__str__()
        SlotM18_2_str += "Hmag_bore = " + str(self.Hmag_bore) + linesep
        SlotM18_2_str += "Hmag_gap = " + str(self.Hmag_gap) + linesep
        return SlotM18_2_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotM18_2, self).__eq__(other):
            return False
        if other.Hmag_bore != self.Hmag_bore:
            return False
        if other.Hmag_gap != self.Hmag_gap:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(
            super(SlotM18_2, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Hmag_bore is not None
            and self._Hmag_bore is not None
            and isnan(other._Hmag_bore)
            and isnan(self._Hmag_bore)
        ):
            pass
        elif other._Hmag_bore != self._Hmag_bore:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Hmag_bore)
                    + ", other="
                    + str(other._Hmag_bore)
                    + ")"
                )
                diff_list.append(name + ".Hmag_bore" + val_str)
            else:
                diff_list.append(name + ".Hmag_bore")
        if (
            other._Hmag_gap is not None
            and self._Hmag_gap is not None
            and isnan(other._Hmag_gap)
            and isnan(self._Hmag_gap)
        ):
            pass
        elif other._Hmag_gap != self._Hmag_gap:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Hmag_gap)
                    + ", other="
                    + str(other._Hmag_gap)
                    + ")"
                )
                diff_list.append(name + ".Hmag_gap" + val_str)
            else:
                diff_list.append(name + ".Hmag_gap")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotM18_2, self).__sizeof__()
        S += getsizeof(self.Hmag_bore)
        S += getsizeof(self.Hmag_gap)
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
        SlotM18_2_dict = super(SlotM18_2, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        SlotM18_2_dict["Hmag_bore"] = self.Hmag_bore
        SlotM18_2_dict["Hmag_gap"] = self.Hmag_gap
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotM18_2_dict["__class__"] = "SlotM18_2"
        return SlotM18_2_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Hmag_bore_val = self.Hmag_bore
        Hmag_gap_val = self.Hmag_gap
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Hmag_bore=Hmag_bore_val,
            Hmag_gap=Hmag_gap_val,
            Zs=Zs_val,
            wedge_mat=wedge_mat_val,
            is_bore=is_bore_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hmag_bore = None
        self.Hmag_gap = None
        # Set to None the properties inherited from Slot
        super(SlotM18_2, self)._set_None()

    def _get_Hmag_bore(self):
        """getter of Hmag_bore"""
        return self._Hmag_bore

    def _set_Hmag_bore(self, value):
        """setter of Hmag_bore"""
        check_var("Hmag_bore", value, "float", Vmin=0)
        self._Hmag_bore = value

    Hmag_bore = property(
        fget=_get_Hmag_bore,
        fset=_set_Hmag_bore,
        doc=u"""Height of the magnet near the bore

        :Type: float
        :min: 0
        """,
    )

    def _get_Hmag_gap(self):
        """getter of Hmag_gap"""
        return self._Hmag_gap

    def _set_Hmag_gap(self, value):
        """setter of Hmag_gap"""
        check_var("Hmag_gap", value, "float", Vmin=0)
        self._Hmag_gap = value

    Hmag_gap = property(
        fget=_get_Hmag_gap,
        fset=_set_Hmag_gap,
        doc=u"""Height of the magnet near the airgap

        :Type: float
        :min: 0
        """,
    )
