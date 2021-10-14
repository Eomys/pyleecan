# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotWind.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotWind
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
from .LamSlot import LamSlot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotWind.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotWind.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlotWind.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSlotWind.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlotWind.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamSlotWind.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamSlotWind.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlotWind.plot_winding import plot_winding
except ImportError as error:
    plot_winding = error

try:
    from ..Methods.Machine.LamSlotWind.comp_fill_factor import comp_fill_factor
except ImportError as error:
    comp_fill_factor = error

try:
    from ..Methods.Machine.LamSlotWind.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from ..Methods.Machine.LamSlotWind.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error

try:
    from ..Methods.Machine.LamSlotWind.comp_wind_function import comp_wind_function
except ImportError as error:
    comp_wind_function = error

try:
    from ..Methods.Machine.LamSlotWind.plot_mmf_unit import plot_mmf_unit
except ImportError as error:
    plot_mmf_unit = error

try:
    from ..Methods.Machine.LamSlotWind.comp_resistance_wind import comp_resistance_wind
except ImportError as error:
    comp_resistance_wind = error

try:
    from ..Methods.Machine.LamSlotWind.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSlotWind.comp_mmf_unit import comp_mmf_unit
except ImportError as error:
    comp_mmf_unit = error

try:
    from ..Methods.Machine.LamSlotWind.comp_rot_dir import comp_rot_dir
except ImportError as error:
    comp_rot_dir = error

try:
    from ..Methods.Machine.LamSlotWind.comp_lengths_winding import comp_lengths_winding
except ImportError as error:
    comp_lengths_winding = error

try:
    from ..Methods.Machine.LamSlotWind.comp_number_phase_eq import comp_number_phase_eq
except ImportError as error:
    comp_number_phase_eq = error

try:
    from ..Methods.Machine.LamSlotWind.comp_periodicity import comp_periodicity
except ImportError as error:
    comp_periodicity = error

try:
    from ..Methods.Machine.LamSlotWind.set_pole_pair_number import set_pole_pair_number
except ImportError as error:
    set_pole_pair_number = error


from ._check import InitUnKnowClassError
from .Winding import Winding
from .Slot import Slot
from .Material import Material
from .Hole import Hole
from .Notch import Notch
from .Bore import Bore


class LamSlotWind(LamSlot):
    """Lamination with Slot filled with winding"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotWind.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotWind.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotWind method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlotWind.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSlotWind.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotWind.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotWind.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlotWind.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotWind method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlotWind.plot_winding
    if isinstance(plot_winding, ImportError):
        plot_winding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method plot_winding: " + str(plot_winding)
                )
            )
        )
    else:
        plot_winding = plot_winding
    # cf Methods.Machine.LamSlotWind.comp_fill_factor
    if isinstance(comp_fill_factor, ImportError):
        comp_fill_factor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_fill_factor: "
                    + str(comp_fill_factor)
                )
            )
        )
    else:
        comp_fill_factor = comp_fill_factor
    # cf Methods.Machine.LamSlotWind.comp_output_geo
    if isinstance(comp_output_geo, ImportError):
        comp_output_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_output_geo: "
                    + str(comp_output_geo)
                )
            )
        )
    else:
        comp_output_geo = comp_output_geo
    # cf Methods.Machine.LamSlotWind.get_polar_eq
    if isinstance(get_polar_eq, ImportError):
        get_polar_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method get_polar_eq: " + str(get_polar_eq)
                )
            )
        )
    else:
        get_polar_eq = get_polar_eq
    # cf Methods.Machine.LamSlotWind.comp_wind_function
    if isinstance(comp_wind_function, ImportError):
        comp_wind_function = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_wind_function: "
                    + str(comp_wind_function)
                )
            )
        )
    else:
        comp_wind_function = comp_wind_function
    # cf Methods.Machine.LamSlotWind.plot_mmf_unit
    if isinstance(plot_mmf_unit, ImportError):
        plot_mmf_unit = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method plot_mmf_unit: " + str(plot_mmf_unit)
                )
            )
        )
    else:
        plot_mmf_unit = plot_mmf_unit
    # cf Methods.Machine.LamSlotWind.comp_resistance_wind
    if isinstance(comp_resistance_wind, ImportError):
        comp_resistance_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_resistance_wind: "
                    + str(comp_resistance_wind)
                )
            )
        )
    else:
        comp_resistance_wind = comp_resistance_wind
    # cf Methods.Machine.LamSlotWind.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSlotWind.comp_mmf_unit
    if isinstance(comp_mmf_unit, ImportError):
        comp_mmf_unit = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_mmf_unit: " + str(comp_mmf_unit)
                )
            )
        )
    else:
        comp_mmf_unit = comp_mmf_unit
    # cf Methods.Machine.LamSlotWind.comp_rot_dir
    if isinstance(comp_rot_dir, ImportError):
        comp_rot_dir = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_rot_dir: " + str(comp_rot_dir)
                )
            )
        )
    else:
        comp_rot_dir = comp_rot_dir
    # cf Methods.Machine.LamSlotWind.comp_lengths_winding
    if isinstance(comp_lengths_winding, ImportError):
        comp_lengths_winding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_lengths_winding: "
                    + str(comp_lengths_winding)
                )
            )
        )
    else:
        comp_lengths_winding = comp_lengths_winding
    # cf Methods.Machine.LamSlotWind.comp_number_phase_eq
    if isinstance(comp_number_phase_eq, ImportError):
        comp_number_phase_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_number_phase_eq: "
                    + str(comp_number_phase_eq)
                )
            )
        )
    else:
        comp_number_phase_eq = comp_number_phase_eq
    # cf Methods.Machine.LamSlotWind.comp_periodicity
    if isinstance(comp_periodicity, ImportError):
        comp_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method comp_periodicity: "
                    + str(comp_periodicity)
                )
            )
        )
    else:
        comp_periodicity = comp_periodicity
    # cf Methods.Machine.LamSlotWind.set_pole_pair_number
    if isinstance(set_pole_pair_number, ImportError):
        set_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method set_pole_pair_number: "
                    + str(set_pole_pair_number)
                )
            )
        )
    else:
        set_pole_pair_number = set_pole_pair_number
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Ksfill=None,
        winding=-1,
        slot=-1,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=-1,
        notch=-1,
        yoke_notch=-1,
        bore=None,
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
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "slot" in list(init_dict.keys()):
                slot = init_dict["slot"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
            if "yoke_notch" in list(init_dict.keys()):
                yoke_notch = init_dict["yoke_notch"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
        # Set the properties (value check and convertion are done in setter)
        self.Ksfill = Ksfill
        self.winding = winding
        # Call LamSlot init
        super(LamSlotWind, self).__init__(
            slot=slot,
            L1=L1,
            mat_type=mat_type,
            Nrvd=Nrvd,
            Wrvd=Wrvd,
            Kf1=Kf1,
            is_internal=is_internal,
            Rint=Rint,
            Rext=Rext,
            is_stator=is_stator,
            axial_vent=axial_vent,
            notch=notch,
            yoke_notch=yoke_notch,
            bore=bore,
        )
        # The class is frozen (in LamSlot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSlotWind_str = ""
        # Get the properties inherited from LamSlot
        LamSlotWind_str += super(LamSlotWind, self).__str__()
        LamSlotWind_str += "Ksfill = " + str(self.Ksfill) + linesep
        if self.winding is not None:
            tmp = self.winding.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSlotWind_str += "winding = " + tmp
        else:
            LamSlotWind_str += "winding = None" + linesep + linesep
        return LamSlotWind_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlot
        if not super(LamSlotWind, self).__eq__(other):
            return False
        if other.Ksfill != self.Ksfill:
            return False
        if other.winding != self.winding:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamSlot
        diff_list.extend(super(LamSlotWind, self).compare(other, name=name))
        if other._Ksfill != self._Ksfill:
            diff_list.append(name + ".Ksfill")
        if (other.winding is None and self.winding is not None) or (
            other.winding is not None and self.winding is None
        ):
            diff_list.append(name + ".winding None mismatch")
        elif self.winding is not None:
            diff_list.extend(
                self.winding.compare(other.winding, name=name + ".winding")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlot
        S += super(LamSlotWind, self).__sizeof__()
        S += getsizeof(self.Ksfill)
        S += getsizeof(self.winding)
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

        # Get the properties inherited from LamSlot
        LamSlotWind_dict = super(LamSlotWind, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LamSlotWind_dict["Ksfill"] = self.Ksfill
        if self.winding is None:
            LamSlotWind_dict["winding"] = None
        else:
            LamSlotWind_dict["winding"] = self.winding.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSlotWind_dict["__class__"] = "LamSlotWind"
        return LamSlotWind_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Ksfill = None
        if self.winding is not None:
            self.winding._set_None()
        # Set to None the properties inherited from LamSlot
        super(LamSlotWind, self)._set_None()

    def _get_Ksfill(self):
        """getter of Ksfill"""
        return self._Ksfill

    def _set_Ksfill(self, value):
        """setter of Ksfill"""
        check_var("Ksfill", value, "float", Vmin=0, Vmax=1)
        self._Ksfill = value

    Ksfill = property(
        fget=_get_Ksfill,
        fset=_set_Ksfill,
        doc=u"""Imposed Slot Fill factor (if None, will be computed according to the winding and the slot)

        :Type: float
        :min: 0
        :max: 1
        """,
    )

    def _get_winding(self):
        """getter of winding"""
        return self._winding

    def _set_winding(self, value):
        """setter of winding"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "winding"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Winding()
        check_var("winding", value, "Winding")
        self._winding = value

        if self._winding is not None:
            self._winding.parent = self

    winding = property(
        fget=_get_winding,
        fset=_set_winding,
        doc=u"""Lamination's Winding

        :Type: Winding
        """,
    )
