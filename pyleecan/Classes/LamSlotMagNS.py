# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotMagNS.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotMagNS
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .LamSlotM import LamSlotM

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotMagNS.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotMagNS.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlotMagNS.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSlotMagNS.comp_periodicity_geo import comp_periodicity_geo
except ImportError as error:
    comp_periodicity_geo = error

try:
    from ..Methods.Machine.LamSlotMagNS.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error

try:
    from ..Methods.Machine.LamSlotMagNS.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlotMagNS.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamSlotMagNS.get_all_mag_obj import get_all_mag_obj
except ImportError as error:
    get_all_mag_obj = error

try:
    from ..Methods.Machine.LamSlotMagNS.get_magnet_by_label import get_magnet_by_label
except ImportError as error:
    get_magnet_by_label = error

try:
    from ..Methods.Machine.LamSlotMagNS.get_slot_desc_list import get_slot_desc_list
except ImportError as error:
    get_slot_desc_list = error

try:
    from ..Methods.Machine.LamSlotMagNS.set_Lmag import set_Lmag
except ImportError as error:
    set_Lmag = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class LamSlotMagNS(LamSlotM):
    """Lamination with Slot for Magnets with uneven north/south"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotMagNS.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMagNS.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMagNS method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlotMagNS.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSlotMagNS.comp_periodicity_geo
    if isinstance(comp_periodicity_geo, ImportError):
        comp_periodicity_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method comp_periodicity_geo: "
                    + str(comp_periodicity_geo)
                )
            )
        )
    else:
        comp_periodicity_geo = comp_periodicity_geo
    # cf Methods.Machine.LamSlotMagNS.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # cf Methods.Machine.LamSlotMagNS.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotMagNS.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotMagNS.get_all_mag_obj
    if isinstance(get_all_mag_obj, ImportError):
        get_all_mag_obj = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method get_all_mag_obj: "
                    + str(get_all_mag_obj)
                )
            )
        )
    else:
        get_all_mag_obj = get_all_mag_obj
    # cf Methods.Machine.LamSlotMagNS.get_magnet_by_label
    if isinstance(get_magnet_by_label, ImportError):
        get_magnet_by_label = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method get_magnet_by_label: "
                    + str(get_magnet_by_label)
                )
            )
        )
    else:
        get_magnet_by_label = get_magnet_by_label
    # cf Methods.Machine.LamSlotMagNS.get_slot_desc_list
    if isinstance(get_slot_desc_list, ImportError):
        get_slot_desc_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMagNS method get_slot_desc_list: "
                    + str(get_slot_desc_list)
                )
            )
        )
    else:
        get_slot_desc_list = get_slot_desc_list
    # cf Methods.Machine.LamSlotMagNS.set_Lmag
    if isinstance(set_Lmag, ImportError):
        set_Lmag = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMagNS method set_Lmag: " + str(set_Lmag))
            )
        )
    else:
        set_Lmag = set_Lmag
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        magnet_north=-1,
        magnet_south=-1,
        slot_south=-1,
        mur_lin_matrix=None,
        Brm20_matrix=None,
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
            if "magnet_north" in list(init_dict.keys()):
                magnet_north = init_dict["magnet_north"]
            if "magnet_south" in list(init_dict.keys()):
                magnet_south = init_dict["magnet_south"]
            if "slot_south" in list(init_dict.keys()):
                slot_south = init_dict["slot_south"]
            if "mur_lin_matrix" in list(init_dict.keys()):
                mur_lin_matrix = init_dict["mur_lin_matrix"]
            if "Brm20_matrix" in list(init_dict.keys()):
                Brm20_matrix = init_dict["Brm20_matrix"]
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
        self.magnet_north = magnet_north
        self.magnet_south = magnet_south
        self.slot_south = slot_south
        # Call LamSlotM init
        super(LamSlotMagNS, self).__init__(
            mur_lin_matrix=mur_lin_matrix,
            Brm20_matrix=Brm20_matrix,
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
        # The class is frozen (in LamSlotM init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSlotMagNS_str = ""
        # Get the properties inherited from LamSlotM
        LamSlotMagNS_str += super(LamSlotMagNS, self).__str__()
        if self.magnet_north is not None:
            tmp = (
                self.magnet_north.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            LamSlotMagNS_str += "magnet_north = " + tmp
        else:
            LamSlotMagNS_str += "magnet_north = None" + linesep + linesep
        if self.magnet_south is not None:
            tmp = (
                self.magnet_south.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            LamSlotMagNS_str += "magnet_south = " + tmp
        else:
            LamSlotMagNS_str += "magnet_south = None" + linesep + linesep
        if self.slot_south is not None:
            tmp = (
                self.slot_south.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            LamSlotMagNS_str += "slot_south = " + tmp
        else:
            LamSlotMagNS_str += "slot_south = None" + linesep + linesep
        return LamSlotMagNS_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotM
        if not super(LamSlotMagNS, self).__eq__(other):
            return False
        if other.magnet_north != self.magnet_north:
            return False
        if other.magnet_south != self.magnet_south:
            return False
        if other.slot_south != self.slot_south:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamSlotM
        diff_list.extend(
            super(LamSlotMagNS, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.magnet_north is None and self.magnet_north is not None) or (
            other.magnet_north is not None and self.magnet_north is None
        ):
            diff_list.append(name + ".magnet_north None mismatch")
        elif self.magnet_north is not None:
            diff_list.extend(
                self.magnet_north.compare(
                    other.magnet_north,
                    name=name + ".magnet_north",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.magnet_south is None and self.magnet_south is not None) or (
            other.magnet_south is not None and self.magnet_south is None
        ):
            diff_list.append(name + ".magnet_south None mismatch")
        elif self.magnet_south is not None:
            diff_list.extend(
                self.magnet_south.compare(
                    other.magnet_south,
                    name=name + ".magnet_south",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.slot_south is None and self.slot_south is not None) or (
            other.slot_south is not None and self.slot_south is None
        ):
            diff_list.append(name + ".slot_south None mismatch")
        elif self.slot_south is not None:
            diff_list.extend(
                self.slot_south.compare(
                    other.slot_south,
                    name=name + ".slot_south",
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

        # Get size of the properties inherited from LamSlotM
        S += super(LamSlotMagNS, self).__sizeof__()
        S += getsizeof(self.magnet_north)
        S += getsizeof(self.magnet_south)
        S += getsizeof(self.slot_south)
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

        # Get the properties inherited from LamSlotM
        LamSlotMagNS_dict = super(LamSlotMagNS, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.magnet_north is None:
            LamSlotMagNS_dict["magnet_north"] = None
        else:
            LamSlotMagNS_dict["magnet_north"] = self.magnet_north.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.magnet_south is None:
            LamSlotMagNS_dict["magnet_south"] = None
        else:
            LamSlotMagNS_dict["magnet_south"] = self.magnet_south.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.slot_south is None:
            LamSlotMagNS_dict["slot_south"] = None
        else:
            LamSlotMagNS_dict["slot_south"] = self.slot_south.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSlotMagNS_dict["__class__"] = "LamSlotMagNS"
        return LamSlotMagNS_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.magnet_north is None:
            magnet_north_val = None
        else:
            magnet_north_val = self.magnet_north.copy()
        if self.magnet_south is None:
            magnet_south_val = None
        else:
            magnet_south_val = self.magnet_south.copy()
        if self.slot_south is None:
            slot_south_val = None
        else:
            slot_south_val = self.slot_south.copy()
        if self.mur_lin_matrix is None:
            mur_lin_matrix_val = None
        else:
            mur_lin_matrix_val = self.mur_lin_matrix.copy()
        if self.Brm20_matrix is None:
            Brm20_matrix_val = None
        else:
            Brm20_matrix_val = self.Brm20_matrix.copy()
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
            magnet_north=magnet_north_val,
            magnet_south=magnet_south_val,
            slot_south=slot_south_val,
            mur_lin_matrix=mur_lin_matrix_val,
            Brm20_matrix=Brm20_matrix_val,
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

        if self.magnet_north is not None:
            self.magnet_north._set_None()
        if self.magnet_south is not None:
            self.magnet_south._set_None()
        if self.slot_south is not None:
            self.slot_south._set_None()
        # Set to None the properties inherited from LamSlotM
        super(LamSlotMagNS, self)._set_None()

    def _get_magnet_north(self):
        """getter of magnet_north"""
        return self._magnet_north

    def _set_magnet_north(self, value):
        """setter of magnet_north"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_north"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_north")
            value = Magnet()
        check_var("magnet_north", value, "Magnet")
        self._magnet_north = value

        if self._magnet_north is not None:
            self._magnet_north.parent = self

    magnet_north = property(
        fget=_get_magnet_north,
        fset=_set_magnet_north,
        doc="""North Magnet of the lamination

        :Type: Magnet
        """,
    )

    def _get_magnet_south(self):
        """getter of magnet_south"""
        return self._magnet_south

    def _set_magnet_south(self, value):
        """setter of magnet_south"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_south"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_south")
            value = Magnet()
        check_var("magnet_south", value, "Magnet")
        self._magnet_south = value

        if self._magnet_south is not None:
            self._magnet_south.parent = self

    magnet_south = property(
        fget=_get_magnet_south,
        fset=_set_magnet_south,
        doc="""South Magnet of the lamination

        :Type: Magnet
        """,
    )

    def _get_slot_south(self):
        """getter of slot_south"""
        return self._slot_south

    def _set_slot_south(self, value):
        """setter of slot_south"""
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
                "pyleecan.Classes", value.get("__class__"), "slot_south"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Slot = import_class("pyleecan.Classes", "Slot", "slot_south")
            value = Slot()
        check_var("slot_south", value, "Slot")
        self._slot_south = value

        if self._slot_south is not None:
            self._slot_south.parent = self

    slot_south = property(
        fget=_get_slot_south,
        fset=_set_slot_south,
        doc="""South slot of the lamination

        :Type: Slot
        """,
    )
