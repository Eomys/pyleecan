# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/LamSlotWind.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.LamSlot import LamSlot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.LamSlotWind.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.get_pole_pair_number import (
        get_pole_pair_number,
    )
except ImportError as error:
    get_pole_pair_number = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.get_name_phase import get_name_phase
except ImportError as error:
    get_name_phase = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.plot import plot
except ImportError as error:
    plot = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.plot_winding import plot_winding
except ImportError as error:
    plot_winding = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.comp_fill_factor import comp_fill_factor
except ImportError as error:
    comp_fill_factor = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from pyleecan.Methods.Machine.LamSlotWind.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.Notch import Notch


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
    # cf Methods.Machine.LamSlotWind.get_name_phase
    if isinstance(get_name_phase, ImportError):
        get_name_phase = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotWind method get_name_phase: "
                    + str(get_name_phase)
                )
            )
        )
    else:
        get_name_phase = get_name_phase
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
    # save method is available in all object
    save = save

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
        axial_vent=list(),
        notch=list(),
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if winding == -1:
            winding = Winding()
        if slot == -1:
            slot = Slot()
        if mat_type == -1:
            mat_type = Material()
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
        # Initialisation by argument
        self.Ksfill = Ksfill
        # winding can be None, a Winding object or a dict
        if isinstance(winding, dict):
            # Check that the type is correct (including daughter)
            class_name = winding.get("__class__")
            if class_name not in [
                "Winding",
                "WindingCW1L",
                "WindingCW2LR",
                "WindingCW2LT",
                "WindingDW1L",
                "WindingDW2L",
                "WindingSC",
                "WindingUD",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for winding"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.winding = class_obj(init_dict=winding)
        else:
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
        )
        # The class is frozen (in LamSlot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from LamSlot
        LamSlotWind_dict = super(LamSlotWind, self).as_dict()
        LamSlotWind_dict["Ksfill"] = self.Ksfill
        if self.winding is None:
            LamSlotWind_dict["winding"] = None
        else:
            LamSlotWind_dict["winding"] = self.winding.as_dict()
        # The class name is added to the dict fordeserialisation purpose
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

    # Imposed Slot Fill factor (if None, will be computed according to the winding and the slot)
    # Type : float, min = 0, max = 1
    Ksfill = property(
        fget=_get_Ksfill,
        fset=_set_Ksfill,
        doc=u"""Imposed Slot Fill factor (if None, will be computed according to the winding and the slot)""",
    )

    def _get_winding(self):
        """getter of winding"""
        return self._winding

    def _set_winding(self, value):
        """setter of winding"""
        check_var("winding", value, "Winding")
        self._winding = value

        if self._winding is not None:
            self._winding.parent = self

    # Lamination's Winding
    # Type : Winding
    winding = property(
        fget=_get_winding, fset=_set_winding, doc=u"""Lamination's Winding"""
    )
