# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamH.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamH
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
from .Lamination import Lamination

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamH.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamH.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.LamH.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamH.comp_radius_mid_yoke import comp_radius_mid_yoke
except ImportError as error:
    comp_radius_mid_yoke = error

try:
    from ..Methods.Machine.LamH.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamH.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamH.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamH.get_Zs import get_Zs
except ImportError as error:
    get_Zs = error

try:
    from ..Methods.Machine.LamH.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Machine.LamH.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamH.set_pole_pair_number import set_pole_pair_number
except ImportError as error:
    set_pole_pair_number = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LamH(Lamination):
    """Lamination with Hole (Abstract class)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamH.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method comp_angle_d_axis: " + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamH.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method comp_height_yoke: " + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamH.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamH method comp_masses: " + str(comp_masses))
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamH.comp_radius_mid_yoke
    if isinstance(comp_radius_mid_yoke, ImportError):
        comp_radius_mid_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method comp_radius_mid_yoke: "
                    + str(comp_radius_mid_yoke)
                )
            )
        )
    else:
        comp_radius_mid_yoke = comp_radius_mid_yoke
    # cf Methods.Machine.LamH.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamH.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamH method comp_volumes: " + str(comp_volumes))
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamH.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamH.get_Zs
    if isinstance(get_Zs, ImportError):
        get_Zs = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamH method get_Zs: " + str(get_Zs))
            )
        )
    else:
        get_Zs = get_Zs
    # cf Methods.Machine.LamH.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamH method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Machine.LamH.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamH method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamH.set_pole_pair_number
    if isinstance(set_pole_pair_number, ImportError):
        set_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamH method set_pole_pair_number: "
                    + str(set_pole_pair_number)
                )
            )
        )
    else:
        set_pole_pair_number = set_pole_pair_number
    # generic save method is available in all object
    save = save
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
        # Call Lamination init
        super(LamH, self).__init__(
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
        # The class is frozen (in Lamination init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamH_str = ""
        # Get the properties inherited from Lamination
        LamH_str += super(LamH, self).__str__()
        return LamH_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Lamination
        if not super(LamH, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Lamination
        diff_list.extend(
            super(LamH, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Lamination
        S += super(LamH, self).__sizeof__()
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

        # Get the properties inherited from Lamination
        LamH_dict = super(LamH, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamH_dict["__class__"] = "LamH"
        return LamH_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
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

        # Set to None the properties inherited from Lamination
        super(LamH, self)._set_None()
