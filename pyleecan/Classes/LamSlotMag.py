# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotMag
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
    from ..Methods.Machine.LamSlotMag.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotMag.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlotMag.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSlotMag.comp_radius_mec import comp_radius_mec
except ImportError as error:
    comp_radius_mec = error

try:
    from ..Methods.Machine.LamSlotMag.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlotMag.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamSlotMag.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlotMag.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSlotMag.comp_periodicity import comp_periodicity
except ImportError as error:
    comp_periodicity = error


from ._check import InitUnKnowClassError
from .Magnet import Magnet
from .Slot import Slot
from .Material import Material
from .Hole import Hole
from .Notch import Notch
from .Bore import Bore


class LamSlotMag(LamSlot):
    """Lamination with Slot for Magnets"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotMag.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMag.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMag method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlotMag.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSlotMag.comp_radius_mec
    if isinstance(comp_radius_mec, ImportError):
        comp_radius_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_radius_mec: "
                    + str(comp_radius_mec)
                )
            )
        )
    else:
        comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlotMag.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotMag.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotMag.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMag method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlotMag.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSlotMag.comp_periodicity
    if isinstance(comp_periodicity, ImportError):
        comp_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_periodicity: "
                    + str(comp_periodicity)
                )
            )
        )
    else:
        comp_periodicity = comp_periodicity
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        magnet=-1,
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
            if "magnet" in list(init_dict.keys()):
                magnet = init_dict["magnet"]
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
        self.magnet = magnet
        # Call LamSlot init
        super(LamSlotMag, self).__init__(
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

        LamSlotMag_str = ""
        # Get the properties inherited from LamSlot
        LamSlotMag_str += super(LamSlotMag, self).__str__()
        if self.magnet is not None:
            tmp = self.magnet.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSlotMag_str += "magnet = " + tmp
        else:
            LamSlotMag_str += "magnet = None" + linesep + linesep
        return LamSlotMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlot
        if not super(LamSlotMag, self).__eq__(other):
            return False
        if other.magnet != self.magnet:
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
        diff_list.extend(super(LamSlotMag, self).compare(other, name=name))
        if (other.magnet is None and self.magnet is not None) or (
            other.magnet is not None and self.magnet is None
        ):
            diff_list.append(name + ".magnet None mismatch")
        elif self.magnet is not None:
            diff_list.extend(self.magnet.compare(other.magnet, name=name + ".magnet"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlot
        S += super(LamSlotMag, self).__sizeof__()
        S += getsizeof(self.magnet)
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
        LamSlotMag_dict = super(LamSlotMag, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.magnet is None:
            LamSlotMag_dict["magnet"] = None
        else:
            LamSlotMag_dict["magnet"] = self.magnet.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSlotMag_dict["__class__"] = "LamSlotMag"
        return LamSlotMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.magnet is not None:
            self.magnet._set_None()
        # Set to None the properties inherited from LamSlot
        super(LamSlotMag, self)._set_None()

    def _get_magnet(self):
        """getter of magnet"""
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "magnet"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Magnet()
        check_var("magnet", value, "Magnet")
        self._magnet = value

        if self._magnet is not None:
            self._magnet.parent = self

    magnet = property(
        fget=_get_magnet,
        fset=_set_magnet,
        doc=u"""Magnet of the lamination

        :Type: Magnet
        """,
    )
