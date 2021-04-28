# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSquirrelCageMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSquirrelCageMag
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
from .LamSlotWind import LamSlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSquirrelCageMag.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_length_ring import comp_length_ring
except ImportError as error:
    comp_length_ring = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_number_phase_eq import (
        comp_number_phase_eq,
    )
except ImportError as error:
    comp_number_phase_eq = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_periodicity import comp_periodicity
except ImportError as error:
    comp_periodicity = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_surface_ring import comp_surface_ring
except ImportError as error:
    comp_surface_ring = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_resistance_wind import (
        comp_resistance_wind,
    )
except ImportError as error:
    comp_resistance_wind = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.get_pole_pair_number import (
        get_pole_pair_number,
    )
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.comp_radius_mid_yoke import (
        comp_radius_mid_yoke,
    )
except ImportError as error:
    comp_radius_mid_yoke = error

try:
    from ..Methods.Machine.LamSquirrelCageMag.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error


from ._check import InitUnKnowClassError
from .Material import Material
from .Hole import Hole
from .Bore import Bore
from .Winding import Winding
from .Slot import Slot
from .Notch import Notch


class LamSquirrelCageMag(LamSlotWind):
    """Rotor lamination for LSPM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSquirrelCageMag.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSquirrelCageMag.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCageMag method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSquirrelCageMag.comp_length_ring
    if isinstance(comp_length_ring, ImportError):
        comp_length_ring = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_length_ring: "
                    + str(comp_length_ring)
                )
            )
        )
    else:
        comp_length_ring = comp_length_ring
    # cf Methods.Machine.LamSquirrelCageMag.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCageMag method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSquirrelCageMag.comp_number_phase_eq
    if isinstance(comp_number_phase_eq, ImportError):
        comp_number_phase_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_number_phase_eq: "
                    + str(comp_number_phase_eq)
                )
            )
        )
    else:
        comp_number_phase_eq = comp_number_phase_eq
    # cf Methods.Machine.LamSquirrelCageMag.comp_periodicity
    if isinstance(comp_periodicity, ImportError):
        comp_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_periodicity: "
                    + str(comp_periodicity)
                )
            )
        )
    else:
        comp_periodicity = comp_periodicity
    # cf Methods.Machine.LamSquirrelCageMag.comp_surface_ring
    if isinstance(comp_surface_ring, ImportError):
        comp_surface_ring = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_surface_ring: "
                    + str(comp_surface_ring)
                )
            )
        )
    else:
        comp_surface_ring = comp_surface_ring
    # cf Methods.Machine.LamSquirrelCageMag.comp_resistance_wind
    if isinstance(comp_resistance_wind, ImportError):
        comp_resistance_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_resistance_wind: "
                    + str(comp_resistance_wind)
                )
            )
        )
    else:
        comp_resistance_wind = comp_resistance_wind
    # cf Methods.Machine.LamSquirrelCageMag.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_height_yoke: "
                    + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamSquirrelCageMag.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_masses: "
                    + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSquirrelCageMag.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_surfaces: "
                    + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSquirrelCageMag.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_volumes: "
                    + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamSquirrelCageMag.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSquirrelCageMag.comp_radius_mid_yoke
    if isinstance(comp_radius_mid_yoke, ImportError):
        comp_radius_mid_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method comp_radius_mid_yoke: "
                    + str(comp_radius_mid_yoke)
                )
            )
        )
    else:
        comp_radius_mid_yoke = comp_radius_mid_yoke
    # cf Methods.Machine.LamSquirrelCageMag.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCageMag method has_magnet: " + str(has_magnet)
                )
            )
        )
    else:
        has_magnet = has_magnet
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Hscr=0.03,
        Lscr=0.015,
        ring_mat=-1,
        hole=-1,
        bore=None,
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
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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
            if "hole" in list(init_dict.keys()):
                hole = init_dict["hole"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
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
        # Set the properties (value check and convertion are done in setter)
        self.Hscr = Hscr
        self.Lscr = Lscr
        self.ring_mat = ring_mat
        self.hole = hole
        self.bore = bore
        # Call LamSlotWind init
        super(LamSquirrelCageMag, self).__init__(
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
        )
        # The class is frozen (in LamSlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSquirrelCageMag_str = ""
        # Get the properties inherited from LamSlotWind
        LamSquirrelCageMag_str += super(LamSquirrelCageMag, self).__str__()
        LamSquirrelCageMag_str += "Hscr = " + str(self.Hscr) + linesep
        LamSquirrelCageMag_str += "Lscr = " + str(self.Lscr) + linesep
        if self.ring_mat is not None:
            tmp = self.ring_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSquirrelCageMag_str += "ring_mat = " + tmp
        else:
            LamSquirrelCageMag_str += "ring_mat = None" + linesep + linesep
        if len(self.hole) == 0:
            LamSquirrelCageMag_str += "hole = []" + linesep
        for ii in range(len(self.hole)):
            tmp = self.hole[ii].__str__().replace(linesep, linesep + "\t") + linesep
            LamSquirrelCageMag_str += (
                "hole[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        if self.bore is not None:
            tmp = self.bore.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSquirrelCageMag_str += "bore = " + tmp
        else:
            LamSquirrelCageMag_str += "bore = None" + linesep + linesep
        return LamSquirrelCageMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotWind
        if not super(LamSquirrelCageMag, self).__eq__(other):
            return False
        if other.Hscr != self.Hscr:
            return False
        if other.Lscr != self.Lscr:
            return False
        if other.ring_mat != self.ring_mat:
            return False
        if other.hole != self.hole:
            return False
        if other.bore != self.bore:
            return False
        return True

    def compare(self, other, name="self"):
        """Compare two objects and return list of differences"""

        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamSlotWind
        diff_list.extend(super(LamSquirrelCageMag, self).compare(other, name=name))
        if other._Hscr != self._Hscr:
            diff_list.append(name + ".Hscr")
        if other._Lscr != self._Lscr:
            diff_list.append(name + ".Lscr")
        if (other.ring_mat is None and self.ring_mat is not None) or (
            other.ring_mat is not None and self.ring_mat is None
        ):
            diff_list.append(name + ".ring_mat None mismatch")
        elif self.ring_mat is not None:
            diff_list.extend(
                self.ring_mat.compare(other.ring_mat, name=name + ".ring_mat")
            )
        if (other.hole is None and self.hole is not None) or (
            other.hole is not None and self.hole is None
        ):
            diff_list.append(name + ".hole None mismatch")
        elif self.hole is None:
            pass
        elif len(other.hole) != len(self.hole):
            diff_list.append("len(" + name + ".hole)")
        else:
            for ii in range(len(other.hole)):
                diff_list.extend(
                    self.hole[ii].compare(
                        other.hole[ii], name=name + ".hole[" + str(ii) + "]"
                    )
                )
        if (other.bore is None and self.bore is not None) or (
            other.bore is not None and self.bore is None
        ):
            diff_list.append(name + ".bore None mismatch")
        elif self.bore is not None:
            diff_list.extend(self.bore.compare(other.bore, name=name + ".bore"))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlotWind
        S += super(LamSquirrelCageMag, self).__sizeof__()
        S += getsizeof(self.Hscr)
        S += getsizeof(self.Lscr)
        S += getsizeof(self.ring_mat)
        if self.hole is not None:
            for value in self.hole:
                S += getsizeof(value)
        S += getsizeof(self.bore)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from LamSlotWind
        LamSquirrelCageMag_dict = super(LamSquirrelCageMag, self).as_dict(**kwargs)
        LamSquirrelCageMag_dict["Hscr"] = self.Hscr
        LamSquirrelCageMag_dict["Lscr"] = self.Lscr
        if self.ring_mat is None:
            LamSquirrelCageMag_dict["ring_mat"] = None
        else:
            LamSquirrelCageMag_dict["ring_mat"] = self.ring_mat.as_dict(**kwargs)
        if self.hole is None:
            LamSquirrelCageMag_dict["hole"] = None
        else:
            LamSquirrelCageMag_dict["hole"] = list()
            for obj in self.hole:
                if obj is not None:
                    LamSquirrelCageMag_dict["hole"].append(obj.as_dict(**kwargs))
                else:
                    LamSquirrelCageMag_dict["hole"].append(None)
        if self.bore is None:
            LamSquirrelCageMag_dict["bore"] = None
        else:
            LamSquirrelCageMag_dict["bore"] = self.bore.as_dict(**kwargs)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSquirrelCageMag_dict["__class__"] = "LamSquirrelCageMag"
        return LamSquirrelCageMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hscr = None
        self.Lscr = None
        if self.ring_mat is not None:
            self.ring_mat._set_None()
        self.hole = None
        if self.bore is not None:
            self.bore._set_None()
        # Set to None the properties inherited from LamSlotWind
        super(LamSquirrelCageMag, self)._set_None()

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
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "ring_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
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

    def _get_hole(self):
        """getter of hole"""
        if self._hole is not None:
            for obj in self._hole:
                if obj is not None:
                    obj.parent = self
        return self._hole

    def _set_hole(self, value):
        """setter of hole"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "hole"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("hole", value, "[Hole]")
        self._hole = value

    hole = property(
        fget=_get_hole,
        fset=_set_hole,
        doc=u"""lamination Hole

        :Type: [Hole]
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
