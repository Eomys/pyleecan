# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Lamination.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Lamination
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
    from ..Methods.Machine.Lamination.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.Lamination.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.Lamination.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Machine.Lamination.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.Lamination.comp_radius_mec import comp_radius_mec
except ImportError as error:
    comp_radius_mec = error

try:
    from ..Methods.Machine.Lamination.comp_surface_axial_vent import (
        comp_surface_axial_vent,
    )
except ImportError as error:
    comp_surface_axial_vent = error

try:
    from ..Methods.Machine.Lamination.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.Lamination.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.Lamination.get_bore_line import get_bore_line
except ImportError as error:
    get_bore_line = error

try:
    from ..Methods.Machine.Lamination.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Machine.Lamination.get_Ryoke import get_Ryoke
except ImportError as error:
    get_Ryoke = error

try:
    from ..Methods.Machine.Lamination.get_name_phase import get_name_phase
except ImportError as error:
    get_name_phase = error

try:
    from ..Methods.Machine.Lamination.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.Lamination.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from ..Methods.Machine.Lamination.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error

try:
    from ..Methods.Machine.Lamination.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error

try:
    from ..Methods.Machine.Lamination.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.Lamination.get_notch_list import get_notch_list
except ImportError as error:
    get_notch_list = error

try:
    from ..Methods.Machine.Lamination.comp_angle_q_axis import comp_angle_q_axis
except ImportError as error:
    comp_angle_q_axis = error

try:
    from ..Methods.Machine.Lamination.comp_radius_mid_yoke import comp_radius_mid_yoke
except ImportError as error:
    comp_radius_mid_yoke = error

try:
    from ..Methods.Machine.Lamination.get_yoke_desc import get_yoke_desc
except ImportError as error:
    get_yoke_desc = error

try:
    from ..Methods.Machine.Lamination.get_bore_desc import get_bore_desc
except ImportError as error:
    get_bore_desc = error

try:
    from ..Methods.Machine.Lamination.comp_point_ref import comp_point_ref
except ImportError as error:
    comp_point_ref = error

try:
    from ..Methods.Machine.Lamination.get_label import get_label
except ImportError as error:
    get_label = error

try:
    from ..Methods.Machine.Lamination.get_yoke_side_line import get_yoke_side_line
except ImportError as error:
    get_yoke_side_line = error


from ._check import InitUnKnowClassError
from .Material import Material
from .Hole import Hole
from .Notch import Notch
from .Bore import Bore


class Lamination(FrozenClass):
    """abstract class for lamination"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Lamination.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.Lamination.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Lamination method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.Lamination.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Machine.Lamination.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.Lamination.comp_radius_mec
    if isinstance(comp_radius_mec, ImportError):
        comp_radius_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_radius_mec: "
                    + str(comp_radius_mec)
                )
            )
        )
    else:
        comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.Lamination.comp_surface_axial_vent
    if isinstance(comp_surface_axial_vent, ImportError):
        comp_surface_axial_vent = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_surface_axial_vent: "
                    + str(comp_surface_axial_vent)
                )
            )
        )
    else:
        comp_surface_axial_vent = comp_surface_axial_vent
    # cf Methods.Machine.Lamination.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.Lamination.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.Lamination.get_bore_line
    if isinstance(get_bore_line, ImportError):
        get_bore_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_bore_line: " + str(get_bore_line)
                )
            )
        )
    else:
        get_bore_line = get_bore_line
    # cf Methods.Machine.Lamination.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Lamination method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Machine.Lamination.get_Ryoke
    if isinstance(get_Ryoke, ImportError):
        get_Ryoke = property(
            fget=lambda x: raise_(
                ImportError("Can't use Lamination method get_Ryoke: " + str(get_Ryoke))
            )
        )
    else:
        get_Ryoke = get_Ryoke
    # cf Methods.Machine.Lamination.get_name_phase
    if isinstance(get_name_phase, ImportError):
        get_name_phase = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_name_phase: " + str(get_name_phase)
                )
            )
        )
    else:
        get_name_phase = get_name_phase
    # cf Methods.Machine.Lamination.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Lamination method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.Lamination.comp_output_geo
    if isinstance(comp_output_geo, ImportError):
        comp_output_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_output_geo: "
                    + str(comp_output_geo)
                )
            )
        )
    else:
        comp_output_geo = comp_output_geo
    # cf Methods.Machine.Lamination.get_polar_eq
    if isinstance(get_polar_eq, ImportError):
        get_polar_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_polar_eq: " + str(get_polar_eq)
                )
            )
        )
    else:
        get_polar_eq = get_polar_eq
    # cf Methods.Machine.Lamination.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method is_outwards: " + str(is_outwards)
                )
            )
        )
    else:
        is_outwards = is_outwards
    # cf Methods.Machine.Lamination.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_height_yoke: "
                    + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.Lamination.get_notch_list
    if isinstance(get_notch_list, ImportError):
        get_notch_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_notch_list: " + str(get_notch_list)
                )
            )
        )
    else:
        get_notch_list = get_notch_list
    # cf Methods.Machine.Lamination.comp_angle_q_axis
    if isinstance(comp_angle_q_axis, ImportError):
        comp_angle_q_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_angle_q_axis: "
                    + str(comp_angle_q_axis)
                )
            )
        )
    else:
        comp_angle_q_axis = comp_angle_q_axis
    # cf Methods.Machine.Lamination.comp_radius_mid_yoke
    if isinstance(comp_radius_mid_yoke, ImportError):
        comp_radius_mid_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_radius_mid_yoke: "
                    + str(comp_radius_mid_yoke)
                )
            )
        )
    else:
        comp_radius_mid_yoke = comp_radius_mid_yoke
    # cf Methods.Machine.Lamination.get_yoke_desc
    if isinstance(get_yoke_desc, ImportError):
        get_yoke_desc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_yoke_desc: " + str(get_yoke_desc)
                )
            )
        )
    else:
        get_yoke_desc = get_yoke_desc
    # cf Methods.Machine.Lamination.get_bore_desc
    if isinstance(get_bore_desc, ImportError):
        get_bore_desc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_bore_desc: " + str(get_bore_desc)
                )
            )
        )
    else:
        get_bore_desc = get_bore_desc
    # cf Methods.Machine.Lamination.comp_point_ref
    if isinstance(comp_point_ref, ImportError):
        comp_point_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method comp_point_ref: " + str(comp_point_ref)
                )
            )
        )
    else:
        comp_point_ref = comp_point_ref
    # cf Methods.Machine.Lamination.get_label
    if isinstance(get_label, ImportError):
        get_label = property(
            fget=lambda x: raise_(
                ImportError("Can't use Lamination method get_label: " + str(get_label))
            )
        )
    else:
        get_label = get_label
    # cf Methods.Machine.Lamination.get_yoke_side_line
    if isinstance(get_yoke_side_line, ImportError):
        get_yoke_side_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Lamination method get_yoke_side_line: "
                    + str(get_yoke_side_line)
                )
            )
        )
    else:
        get_yoke_side_line = get_yoke_side_line
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        self.parent = None
        self.L1 = L1
        self.mat_type = mat_type
        self.Nrvd = Nrvd
        self.Wrvd = Wrvd
        self.Kf1 = Kf1
        self.is_internal = is_internal
        self.Rint = Rint
        self.Rext = Rext
        self.is_stator = is_stator
        self.axial_vent = axial_vent
        self.notch = notch
        self.yoke_notch = yoke_notch
        self.bore = bore

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Lamination_str = ""
        if self.parent is None:
            Lamination_str += "parent = None " + linesep
        else:
            Lamination_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Lamination_str += "L1 = " + str(self.L1) + linesep
        if self.mat_type is not None:
            tmp = self.mat_type.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Lamination_str += "mat_type = " + tmp
        else:
            Lamination_str += "mat_type = None" + linesep + linesep
        Lamination_str += "Nrvd = " + str(self.Nrvd) + linesep
        Lamination_str += "Wrvd = " + str(self.Wrvd) + linesep
        Lamination_str += "Kf1 = " + str(self.Kf1) + linesep
        Lamination_str += "is_internal = " + str(self.is_internal) + linesep
        Lamination_str += "Rint = " + str(self.Rint) + linesep
        Lamination_str += "Rext = " + str(self.Rext) + linesep
        Lamination_str += "is_stator = " + str(self.is_stator) + linesep
        if len(self.axial_vent) == 0:
            Lamination_str += "axial_vent = []" + linesep
        for ii in range(len(self.axial_vent)):
            tmp = (
                self.axial_vent[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            Lamination_str += "axial_vent[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.notch) == 0:
            Lamination_str += "notch = []" + linesep
        for ii in range(len(self.notch)):
            tmp = self.notch[ii].__str__().replace(linesep, linesep + "\t") + linesep
            Lamination_str += "notch[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.yoke_notch) == 0:
            Lamination_str += "yoke_notch = []" + linesep
        for ii in range(len(self.yoke_notch)):
            tmp = (
                self.yoke_notch[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            Lamination_str += "yoke_notch[" + str(ii) + "] =" + tmp + linesep + linesep
        if self.bore is not None:
            tmp = self.bore.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Lamination_str += "bore = " + tmp
        else:
            Lamination_str += "bore = None" + linesep + linesep
        return Lamination_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.L1 != self.L1:
            return False
        if other.mat_type != self.mat_type:
            return False
        if other.Nrvd != self.Nrvd:
            return False
        if other.Wrvd != self.Wrvd:
            return False
        if other.Kf1 != self.Kf1:
            return False
        if other.is_internal != self.is_internal:
            return False
        if other.Rint != self.Rint:
            return False
        if other.Rext != self.Rext:
            return False
        if other.is_stator != self.is_stator:
            return False
        if other.axial_vent != self.axial_vent:
            return False
        if other.notch != self.notch:
            return False
        if other.yoke_notch != self.yoke_notch:
            return False
        if other.bore != self.bore:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._L1 != self._L1:
            diff_list.append(name + ".L1")
        if (other.mat_type is None and self.mat_type is not None) or (
            other.mat_type is not None and self.mat_type is None
        ):
            diff_list.append(name + ".mat_type None mismatch")
        elif self.mat_type is not None:
            diff_list.extend(
                self.mat_type.compare(other.mat_type, name=name + ".mat_type")
            )
        if other._Nrvd != self._Nrvd:
            diff_list.append(name + ".Nrvd")
        if other._Wrvd != self._Wrvd:
            diff_list.append(name + ".Wrvd")
        if other._Kf1 != self._Kf1:
            diff_list.append(name + ".Kf1")
        if other._is_internal != self._is_internal:
            diff_list.append(name + ".is_internal")
        if other._Rint != self._Rint:
            diff_list.append(name + ".Rint")
        if other._Rext != self._Rext:
            diff_list.append(name + ".Rext")
        if other._is_stator != self._is_stator:
            diff_list.append(name + ".is_stator")
        if (other.axial_vent is None and self.axial_vent is not None) or (
            other.axial_vent is not None and self.axial_vent is None
        ):
            diff_list.append(name + ".axial_vent None mismatch")
        elif self.axial_vent is None:
            pass
        elif len(other.axial_vent) != len(self.axial_vent):
            diff_list.append("len(" + name + ".axial_vent)")
        else:
            for ii in range(len(other.axial_vent)):
                diff_list.extend(
                    self.axial_vent[ii].compare(
                        other.axial_vent[ii], name=name + ".axial_vent[" + str(ii) + "]"
                    )
                )
        if (other.notch is None and self.notch is not None) or (
            other.notch is not None and self.notch is None
        ):
            diff_list.append(name + ".notch None mismatch")
        elif self.notch is None:
            pass
        elif len(other.notch) != len(self.notch):
            diff_list.append("len(" + name + ".notch)")
        else:
            for ii in range(len(other.notch)):
                diff_list.extend(
                    self.notch[ii].compare(
                        other.notch[ii], name=name + ".notch[" + str(ii) + "]"
                    )
                )
        if (other.yoke_notch is None and self.yoke_notch is not None) or (
            other.yoke_notch is not None and self.yoke_notch is None
        ):
            diff_list.append(name + ".yoke_notch None mismatch")
        elif self.yoke_notch is None:
            pass
        elif len(other.yoke_notch) != len(self.yoke_notch):
            diff_list.append("len(" + name + ".yoke_notch)")
        else:
            for ii in range(len(other.yoke_notch)):
                diff_list.extend(
                    self.yoke_notch[ii].compare(
                        other.yoke_notch[ii], name=name + ".yoke_notch[" + str(ii) + "]"
                    )
                )
        if (other.bore is None and self.bore is not None) or (
            other.bore is not None and self.bore is None
        ):
            diff_list.append(name + ".bore None mismatch")
        elif self.bore is not None:
            diff_list.extend(self.bore.compare(other.bore, name=name + ".bore"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.L1)
        S += getsizeof(self.mat_type)
        S += getsizeof(self.Nrvd)
        S += getsizeof(self.Wrvd)
        S += getsizeof(self.Kf1)
        S += getsizeof(self.is_internal)
        S += getsizeof(self.Rint)
        S += getsizeof(self.Rext)
        S += getsizeof(self.is_stator)
        if self.axial_vent is not None:
            for value in self.axial_vent:
                S += getsizeof(value)
        if self.notch is not None:
            for value in self.notch:
                S += getsizeof(value)
        if self.yoke_notch is not None:
            for value in self.yoke_notch:
                S += getsizeof(value)
        S += getsizeof(self.bore)
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

        Lamination_dict = dict()
        Lamination_dict["L1"] = self.L1
        if self.mat_type is None:
            Lamination_dict["mat_type"] = None
        else:
            Lamination_dict["mat_type"] = self.mat_type.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Lamination_dict["Nrvd"] = self.Nrvd
        Lamination_dict["Wrvd"] = self.Wrvd
        Lamination_dict["Kf1"] = self.Kf1
        Lamination_dict["is_internal"] = self.is_internal
        Lamination_dict["Rint"] = self.Rint
        Lamination_dict["Rext"] = self.Rext
        Lamination_dict["is_stator"] = self.is_stator
        if self.axial_vent is None:
            Lamination_dict["axial_vent"] = None
        else:
            Lamination_dict["axial_vent"] = list()
            for obj in self.axial_vent:
                if obj is not None:
                    Lamination_dict["axial_vent"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    Lamination_dict["axial_vent"].append(None)
        if self.notch is None:
            Lamination_dict["notch"] = None
        else:
            Lamination_dict["notch"] = list()
            for obj in self.notch:
                if obj is not None:
                    Lamination_dict["notch"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    Lamination_dict["notch"].append(None)
        if self.yoke_notch is None:
            Lamination_dict["yoke_notch"] = None
        else:
            Lamination_dict["yoke_notch"] = list()
            for obj in self.yoke_notch:
                if obj is not None:
                    Lamination_dict["yoke_notch"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    Lamination_dict["yoke_notch"].append(None)
        if self.bore is None:
            Lamination_dict["bore"] = None
        else:
            Lamination_dict["bore"] = self.bore.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        Lamination_dict["__class__"] = "Lamination"
        return Lamination_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.L1 = None
        if self.mat_type is not None:
            self.mat_type._set_None()
        self.Nrvd = None
        self.Wrvd = None
        self.Kf1 = None
        self.is_internal = None
        self.Rint = None
        self.Rext = None
        self.is_stator = None
        self.axial_vent = None
        self.notch = None
        self.yoke_notch = None
        if self.bore is not None:
            self.bore._set_None()

    def _get_L1(self):
        """getter of L1"""
        return self._L1

    def _set_L1(self, value):
        """setter of L1"""
        check_var("L1", value, "float", Vmin=0)
        self._L1 = value

    L1 = property(
        fget=_get_L1,
        fset=_set_L1,
        doc=u"""Lamination stack active length [m] without radial ventilation airducts but including insulation layers between lamination sheets

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
        doc=u"""Lamination's material

        :Type: Material
        """,
    )

    def _get_Nrvd(self):
        """getter of Nrvd"""
        return self._Nrvd

    def _set_Nrvd(self, value):
        """setter of Nrvd"""
        check_var("Nrvd", value, "int", Vmin=0)
        self._Nrvd = value

    Nrvd = property(
        fget=_get_Nrvd,
        fset=_set_Nrvd,
        doc=u"""number of radial air ventilation ducts in lamination

        :Type: int
        :min: 0
        """,
    )

    def _get_Wrvd(self):
        """getter of Wrvd"""
        return self._Wrvd

    def _set_Wrvd(self, value):
        """setter of Wrvd"""
        check_var("Wrvd", value, "float", Vmin=0)
        self._Wrvd = value

    Wrvd = property(
        fget=_get_Wrvd,
        fset=_set_Wrvd,
        doc=u"""axial width of ventilation ducts in lamination

        :Type: float
        :min: 0
        """,
    )

    def _get_Kf1(self):
        """getter of Kf1"""
        return self._Kf1

    def _set_Kf1(self, value):
        """setter of Kf1"""
        check_var("Kf1", value, "float", Vmin=0, Vmax=1)
        self._Kf1 = value

    Kf1 = property(
        fget=_get_Kf1,
        fset=_set_Kf1,
        doc=u"""lamination stacking / packing factor

        :Type: float
        :min: 0
        :max: 1
        """,
    )

    def _get_is_internal(self):
        """getter of is_internal"""
        return self._is_internal

    def _set_is_internal(self, value):
        """setter of is_internal"""
        check_var("is_internal", value, "bool")
        self._is_internal = value

    is_internal = property(
        fget=_get_is_internal,
        fset=_set_is_internal,
        doc=u"""1 for internal lamination topology, 0 for external lamination

        :Type: bool
        """,
    )

    def _get_Rint(self):
        """getter of Rint"""
        return self._Rint

    def _set_Rint(self, value):
        """setter of Rint"""
        check_var("Rint", value, "float", Vmin=0)
        self._Rint = value

    Rint = property(
        fget=_get_Rint,
        fset=_set_Rint,
        doc=u"""To fill

        :Type: float
        :min: 0
        """,
    )

    def _get_Rext(self):
        """getter of Rext"""
        return self._Rext

    def _set_Rext(self, value):
        """setter of Rext"""
        check_var("Rext", value, "float", Vmin=0)
        self._Rext = value

    Rext = property(
        fget=_get_Rext,
        fset=_set_Rext,
        doc=u"""To fill

        :Type: float
        :min: 0
        """,
    )

    def _get_is_stator(self):
        """getter of is_stator"""
        return self._is_stator

    def _set_is_stator(self, value):
        """setter of is_stator"""
        check_var("is_stator", value, "bool")
        self._is_stator = value

    is_stator = property(
        fget=_get_is_stator,
        fset=_set_is_stator,
        doc=u"""To fill

        :Type: bool
        """,
    )

    def _get_axial_vent(self):
        """getter of axial_vent"""
        if self._axial_vent is not None:
            for obj in self._axial_vent:
                if obj is not None:
                    obj.parent = self
        return self._axial_vent

    def _set_axial_vent(self, value):
        """setter of axial_vent"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "axial_vent"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("axial_vent", value, "[Hole]")
        self._axial_vent = value

    axial_vent = property(
        fget=_get_axial_vent,
        fset=_set_axial_vent,
        doc=u"""Axial ventilation ducts

        :Type: [Hole]
        """,
    )

    def _get_notch(self):
        """getter of notch"""
        if self._notch is not None:
            for obj in self._notch:
                if obj is not None:
                    obj.parent = self
        return self._notch

    def _set_notch(self, value):
        """setter of notch"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "notch"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("notch", value, "[Notch]")
        self._notch = value

    notch = property(
        fget=_get_notch,
        fset=_set_notch,
        doc=u"""Lamination bore notches

        :Type: [Notch]
        """,
    )

    def _get_yoke_notch(self):
        """getter of yoke_notch"""
        if self._yoke_notch is not None:
            for obj in self._yoke_notch:
                if obj is not None:
                    obj.parent = self
        return self._yoke_notch

    def _set_yoke_notch(self, value):
        """setter of yoke_notch"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "yoke_notch"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("yoke_notch", value, "[Notch]")
        self._yoke_notch = value

    yoke_notch = property(
        fget=_get_yoke_notch,
        fset=_set_yoke_notch,
        doc=u"""Lamination yoke notches

        :Type: [Notch]
        """,
    )

    def _get_bore(self):
        """getter of bore"""
        return self._bore

    def _set_bore(self, value):
        """setter of bore"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "bore")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Bore()
        check_var("bore", value, "Bore")
        self._bore = value

        if self._bore is not None:
            self._bore.parent = self

    bore = property(
        fget=_get_bore,
        fset=_set_bore,
        doc=u"""Bore Shape

        :Type: Bore
        """,
    )
