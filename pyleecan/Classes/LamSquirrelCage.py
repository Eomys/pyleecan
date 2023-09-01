# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSquirrelCage.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSquirrelCage
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
from .LamSlotWind import LamSlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSquirrelCage.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSquirrelCage.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_length_ring import comp_length_ring
except ImportError as error:
    comp_length_ring = error

try:
    from ..Methods.Machine.LamSquirrelCage.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_number_phase_eq import (
        comp_number_phase_eq,
    )
except ImportError as error:
    comp_number_phase_eq = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_surface_ring import comp_surface_ring
except ImportError as error:
    comp_surface_ring = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_resistance_wind import (
        comp_resistance_wind,
    )
except ImportError as error:
    comp_resistance_wind = error

try:
    from ..Methods.Machine.LamSquirrelCage.get_name_phase import get_name_phase
except ImportError as error:
    get_name_phase = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSquirrelCage.plot_schematics_scr import (
        plot_schematics_scr,
    )
except ImportError as error:
    plot_schematics_scr = error

try:
    from ..Methods.Machine.LamSquirrelCage.plot_side import plot_side
except ImportError as error:
    plot_side = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LamSquirrelCage(LamSlotWind):
    """squirrel cages lamination"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSquirrelCage.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSquirrelCage.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCage method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSquirrelCage.comp_length_ring
    if isinstance(comp_length_ring, ImportError):
        comp_length_ring = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_length_ring: "
                    + str(comp_length_ring)
                )
            )
        )
    else:
        comp_length_ring = comp_length_ring
    # cf Methods.Machine.LamSquirrelCage.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCage method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSquirrelCage.comp_number_phase_eq
    if isinstance(comp_number_phase_eq, ImportError):
        comp_number_phase_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_number_phase_eq: "
                    + str(comp_number_phase_eq)
                )
            )
        )
    else:
        comp_number_phase_eq = comp_number_phase_eq
    # cf Methods.Machine.LamSquirrelCage.comp_surface_ring
    if isinstance(comp_surface_ring, ImportError):
        comp_surface_ring = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_surface_ring: "
                    + str(comp_surface_ring)
                )
            )
        )
    else:
        comp_surface_ring = comp_surface_ring
    # cf Methods.Machine.LamSquirrelCage.comp_resistance_wind
    if isinstance(comp_resistance_wind, ImportError):
        comp_resistance_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_resistance_wind: "
                    + str(comp_resistance_wind)
                )
            )
        )
    else:
        comp_resistance_wind = comp_resistance_wind
    # cf Methods.Machine.LamSquirrelCage.get_name_phase
    if isinstance(get_name_phase, ImportError):
        get_name_phase = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method get_name_phase: "
                    + str(get_name_phase)
                )
            )
        )
    else:
        get_name_phase = get_name_phase
    # cf Methods.Machine.LamSquirrelCage.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSquirrelCage.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # cf Methods.Machine.LamSquirrelCage.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSquirrelCage.plot_schematics_scr
    if isinstance(plot_schematics_scr, ImportError):
        plot_schematics_scr = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method plot_schematics_scr: "
                    + str(plot_schematics_scr)
                )
            )
        )
    else:
        plot_schematics_scr = plot_schematics_scr
    # cf Methods.Machine.LamSquirrelCage.plot_side
    if isinstance(plot_side, ImportError):
        plot_side = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method plot_side: " + str(plot_side)
                )
            )
        )
    else:
        plot_side = plot_side
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Hscr=0.03,
        Lscr=0.015,
        ring_mat=-1,
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
        skew=None,
        bore=None,
        yoke=None,
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
            if "Hscr" in list(init_dict.keys()):
                Hscr = init_dict["Hscr"]
            if "Lscr" in list(init_dict.keys()):
                Lscr = init_dict["Lscr"]
            if "ring_mat" in list(init_dict.keys()):
                ring_mat = init_dict["ring_mat"]
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
            if "skew" in list(init_dict.keys()):
                skew = init_dict["skew"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
            if "yoke" in list(init_dict.keys()):
                yoke = init_dict["yoke"]
        # Set the properties (value check and convertion are done in setter)
        self.Hscr = Hscr
        self.Lscr = Lscr
        self.ring_mat = ring_mat
        # Call LamSlotWind init
        super(LamSquirrelCage, self).__init__(
            Ksfill=Ksfill,
            winding=winding,
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
            skew=skew,
            bore=bore,
            yoke=yoke,
        )
        # The class is frozen (in LamSlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSquirrelCage_str = ""
        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_str += super(LamSquirrelCage, self).__str__()
        LamSquirrelCage_str += "Hscr = " + str(self.Hscr) + linesep
        LamSquirrelCage_str += "Lscr = " + str(self.Lscr) + linesep
        if self.ring_mat is not None:
            tmp = self.ring_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSquirrelCage_str += "ring_mat = " + tmp
        else:
            LamSquirrelCage_str += "ring_mat = None" + linesep + linesep
        return LamSquirrelCage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotWind
        if not super(LamSquirrelCage, self).__eq__(other):
            return False
        if other.Hscr != self.Hscr:
            return False
        if other.Lscr != self.Lscr:
            return False
        if other.ring_mat != self.ring_mat:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamSlotWind
        diff_list.extend(
            super(LamSquirrelCage, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Hscr is not None
            and self._Hscr is not None
            and isnan(other._Hscr)
            and isnan(self._Hscr)
        ):
            pass
        elif other._Hscr != self._Hscr:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Hscr) + ", other=" + str(other._Hscr) + ")"
                )
                diff_list.append(name + ".Hscr" + val_str)
            else:
                diff_list.append(name + ".Hscr")
        if (
            other._Lscr is not None
            and self._Lscr is not None
            and isnan(other._Lscr)
            and isnan(self._Lscr)
        ):
            pass
        elif other._Lscr != self._Lscr:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Lscr) + ", other=" + str(other._Lscr) + ")"
                )
                diff_list.append(name + ".Lscr" + val_str)
            else:
                diff_list.append(name + ".Lscr")
        if (other.ring_mat is None and self.ring_mat is not None) or (
            other.ring_mat is not None and self.ring_mat is None
        ):
            diff_list.append(name + ".ring_mat None mismatch")
        elif self.ring_mat is not None:
            diff_list.extend(
                self.ring_mat.compare(
                    other.ring_mat,
                    name=name + ".ring_mat",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlotWind
        S += super(LamSquirrelCage, self).__sizeof__()
        S += getsizeof(self.Hscr)
        S += getsizeof(self.Lscr)
        S += getsizeof(self.ring_mat)
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

        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_dict = super(LamSquirrelCage, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LamSquirrelCage_dict["Hscr"] = self.Hscr
        LamSquirrelCage_dict["Lscr"] = self.Lscr
        if self.ring_mat is None:
            LamSquirrelCage_dict["ring_mat"] = None
        else:
            LamSquirrelCage_dict["ring_mat"] = self.ring_mat.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSquirrelCage_dict["__class__"] = "LamSquirrelCage"
        return LamSquirrelCage_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Hscr_val = self.Hscr
        Lscr_val = self.Lscr
        if self.ring_mat is None:
            ring_mat_val = None
        else:
            ring_mat_val = self.ring_mat.copy()
        Ksfill_val = self.Ksfill
        if self.winding is None:
            winding_val = None
        else:
            winding_val = self.winding.copy()
        if self.slot is None:
            slot_val = None
        else:
            slot_val = self.slot.copy()
        L1_val = self.L1
        if self.mat_type is None:
            mat_type_val = None
        else:
            mat_type_val = self.mat_type.copy()
        Nrvd_val = self.Nrvd
        Wrvd_val = self.Wrvd
        Kf1_val = self.Kf1
        is_internal_val = self.is_internal
        Rint_val = self.Rint
        Rext_val = self.Rext
        is_stator_val = self.is_stator
        if self.axial_vent is None:
            axial_vent_val = None
        else:
            axial_vent_val = list()
            for obj in self.axial_vent:
                axial_vent_val.append(obj.copy())
        if self.notch is None:
            notch_val = None
        else:
            notch_val = list()
            for obj in self.notch:
                notch_val.append(obj.copy())
        if self.skew is None:
            skew_val = None
        else:
            skew_val = self.skew.copy()
        if self.bore is None:
            bore_val = None
        else:
            bore_val = self.bore.copy()
        if self.yoke is None:
            yoke_val = None
        else:
            yoke_val = self.yoke.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Hscr=Hscr_val,
            Lscr=Lscr_val,
            ring_mat=ring_mat_val,
            Ksfill=Ksfill_val,
            winding=winding_val,
            slot=slot_val,
            L1=L1_val,
            mat_type=mat_type_val,
            Nrvd=Nrvd_val,
            Wrvd=Wrvd_val,
            Kf1=Kf1_val,
            is_internal=is_internal_val,
            Rint=Rint_val,
            Rext=Rext_val,
            is_stator=is_stator_val,
            axial_vent=axial_vent_val,
            notch=notch_val,
            skew=skew_val,
            bore=bore_val,
            yoke=yoke_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hscr = None
        self.Lscr = None
        if self.ring_mat is not None:
            self.ring_mat._set_None()
        # Set to None the properties inherited from LamSlotWind
        super(LamSquirrelCage, self)._set_None()

    def _get_Hscr(self):
        """getter of Hscr"""
        return self._Hscr

    def _set_Hscr(self, value):
        """setter of Hscr"""
        check_var("Hscr", value, "float", Vmin=0)
        self._Hscr = value

    Hscr = property(
        fget=_get_Hscr,
        fset=_set_Hscr,
        doc=u"""short circuit ring section radial height [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Lscr(self):
        """getter of Lscr"""
        return self._Lscr

    def _set_Lscr(self, value):
        """setter of Lscr"""
        check_var("Lscr", value, "float", Vmin=0)
        self._Lscr = value

    Lscr = property(
        fget=_get_Lscr,
        fset=_set_Lscr,
        doc=u"""short circuit ring section axial length

        :Type: float
        :min: 0
        """,
    )

    def _get_ring_mat(self):
        """getter of ring_mat"""
        return self._ring_mat

    def _set_ring_mat(self, value):
        """setter of ring_mat"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "ring_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Material = import_class("pyleecan.Classes", "Material", "ring_mat")
            value = Material()
        check_var("ring_mat", value, "Material")
        self._ring_mat = value

        if self._ring_mat is not None:
            self._ring_mat.parent = self

    ring_mat = property(
        fget=_get_ring_mat,
        fset=_set_ring_mat,
        doc=u"""Material of the Rotor short circuit ring

        :Type: Material
        """,
    )
