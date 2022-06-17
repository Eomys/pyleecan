# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamHoleNS.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamHoleNS
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
from .LamH import LamH

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamHoleNS._plot_arrow_mag import _plot_arrow_mag
except ImportError as error:
    _plot_arrow_mag = error

try:
    from ..Methods.Machine.LamHoleNS.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamHoleNS.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamHoleNS.comp_periodicity_geo import comp_periodicity_geo
except ImportError as error:
    comp_periodicity_geo = error

try:
    from ..Methods.Machine.LamHoleNS.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error

try:
    from ..Methods.Machine.LamHoleNS.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamHoleNS.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamHoleNS.get_hole_list import get_hole_list
except ImportError as error:
    get_hole_list = error

try:
    from ..Methods.Machine.LamHoleNS.get_magnet_number import get_magnet_number
except ImportError as error:
    get_magnet_number = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LamHoleNS(LamH):
    """Lamination with Hole with or without magnet or winding with different hole for North/South pole"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamHoleNS._plot_arrow_mag
    if isinstance(_plot_arrow_mag, ImportError):
        _plot_arrow_mag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method _plot_arrow_mag: "
                    + str(_plot_arrow_mag)
                )
            )
        )
    else:
        _plot_arrow_mag = _plot_arrow_mag
    # cf Methods.Machine.LamHoleNS.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamHoleNS.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamHoleNS.comp_periodicity_geo
    if isinstance(comp_periodicity_geo, ImportError):
        comp_periodicity_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method comp_periodicity_geo: "
                    + str(comp_periodicity_geo)
                )
            )
        )
    else:
        comp_periodicity_geo = comp_periodicity_geo
    # cf Methods.Machine.LamHoleNS.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # cf Methods.Machine.LamHoleNS.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamHoleNS.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamHoleNS.get_hole_list
    if isinstance(get_hole_list, ImportError):
        get_hole_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method get_hole_list: " + str(get_hole_list)
                )
            )
        )
    else:
        get_hole_list = get_hole_list
    # cf Methods.Machine.LamHoleNS.get_magnet_number
    if isinstance(get_magnet_number, ImportError):
        get_magnet_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHoleNS method get_magnet_number: "
                    + str(get_magnet_number)
                )
            )
        )
    else:
        get_magnet_number = get_magnet_number
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        hole_north=-1,
        hole_south=-1,
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
            if "hole_north" in list(init_dict.keys()):
                hole_north = init_dict["hole_north"]
            if "hole_south" in list(init_dict.keys()):
                hole_south = init_dict["hole_south"]
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
        self.hole_north = hole_north
        self.hole_south = hole_south
        # Call LamH init
        super(LamHoleNS, self).__init__(
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
        # The class is frozen (in LamH init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamHoleNS_str = ""
        # Get the properties inherited from LamH
        LamHoleNS_str += super(LamHoleNS, self).__str__()
        if len(self.hole_north) == 0:
            LamHoleNS_str += "hole_north = []" + linesep
        for ii in range(len(self.hole_north)):
            tmp = (
                self.hole_north[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            LamHoleNS_str += "hole_north[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.hole_south) == 0:
            LamHoleNS_str += "hole_south = []" + linesep
        for ii in range(len(self.hole_south)):
            tmp = (
                self.hole_south[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            LamHoleNS_str += "hole_south[" + str(ii) + "] =" + tmp + linesep + linesep
        return LamHoleNS_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamH
        if not super(LamHoleNS, self).__eq__(other):
            return False
        if other.hole_north != self.hole_north:
            return False
        if other.hole_south != self.hole_south:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamH
        diff_list.extend(
            super(LamHoleNS, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.hole_north is None and self.hole_north is not None) or (
            other.hole_north is not None and self.hole_north is None
        ):
            diff_list.append(name + ".hole_north None mismatch")
        elif self.hole_north is None:
            pass
        elif len(other.hole_north) != len(self.hole_north):
            diff_list.append("len(" + name + ".hole_north)")
        else:
            for ii in range(len(other.hole_north)):
                diff_list.extend(
                    self.hole_north[ii].compare(
                        other.hole_north[ii],
                        name=name + ".hole_north[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.hole_south is None and self.hole_south is not None) or (
            other.hole_south is not None and self.hole_south is None
        ):
            diff_list.append(name + ".hole_south None mismatch")
        elif self.hole_south is None:
            pass
        elif len(other.hole_south) != len(self.hole_south):
            diff_list.append("len(" + name + ".hole_south)")
        else:
            for ii in range(len(other.hole_south)):
                diff_list.extend(
                    self.hole_south[ii].compare(
                        other.hole_south[ii],
                        name=name + ".hole_south[" + str(ii) + "]",
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

        # Get size of the properties inherited from LamH
        S += super(LamHoleNS, self).__sizeof__()
        if self.hole_north is not None:
            for value in self.hole_north:
                S += getsizeof(value)
        if self.hole_south is not None:
            for value in self.hole_south:
                S += getsizeof(value)
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

        # Get the properties inherited from LamH
        LamHoleNS_dict = super(LamHoleNS, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.hole_north is None:
            LamHoleNS_dict["hole_north"] = None
        else:
            LamHoleNS_dict["hole_north"] = list()
            for obj in self.hole_north:
                if obj is not None:
                    LamHoleNS_dict["hole_north"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LamHoleNS_dict["hole_north"].append(None)
        if self.hole_south is None:
            LamHoleNS_dict["hole_south"] = None
        else:
            LamHoleNS_dict["hole_south"] = list()
            for obj in self.hole_south:
                if obj is not None:
                    LamHoleNS_dict["hole_south"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LamHoleNS_dict["hole_south"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamHoleNS_dict["__class__"] = "LamHoleNS"
        return LamHoleNS_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.hole_north is None:
            hole_north_val = None
        else:
            hole_north_val = list()
            for obj in self.hole_north:
                hole_north_val.append(obj.copy())
        if self.hole_south is None:
            hole_south_val = None
        else:
            hole_south_val = list()
            for obj in self.hole_south:
                hole_south_val.append(obj.copy())
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
            hole_north=hole_north_val,
            hole_south=hole_south_val,
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

        self.hole_north = None
        self.hole_south = None
        # Set to None the properties inherited from LamH
        super(LamHoleNS, self)._set_None()

    def _get_hole_north(self):
        """getter of hole_north"""
        if self._hole_north is not None:
            for obj in self._hole_north:
                if obj is not None:
                    obj.parent = self
        return self._hole_north

    def _set_hole_north(self, value):
        """setter of hole_north"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "hole_north"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("hole_north", value, "[Hole]")
        self._hole_north = value

    hole_north = property(
        fget=_get_hole_north,
        fset=_set_hole_north,
        doc=u"""lamination Holes for North pole

        :Type: [Hole]
        """,
    )

    def _get_hole_south(self):
        """getter of hole_south"""
        if self._hole_south is not None:
            for obj in self._hole_south:
                if obj is not None:
                    obj.parent = self
        return self._hole_south

    def _set_hole_south(self, value):
        """setter of hole_south"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "hole_south"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("hole_south", value, "[Hole]")
        self._hole_south = value

    hole_south = property(
        fget=_get_hole_south,
        fset=_set_hole_south,
        doc=u"""lamination Holes for South pole

        :Type: [Hole]
        """,
    )
