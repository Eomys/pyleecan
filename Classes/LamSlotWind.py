# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.LamSlot import LamSlot

from pyleecan.Methods.Machine.LamSlotWind.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSlotWind.check import check
from pyleecan.Methods.Machine.LamSlotWind.comp_masses import comp_masses
from pyleecan.Methods.Machine.LamSlotWind.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.LamSlotWind.comp_volumes import comp_volumes
from pyleecan.Methods.Machine.LamSlotWind.get_pole_pair_number import (
    get_pole_pair_number,
)
from pyleecan.Methods.Machine.LamSlotWind.get_name_phase import get_name_phase
from pyleecan.Methods.Machine.LamSlotWind.plot import plot
from pyleecan.Methods.Machine.LamSlotWind.plot_winding import plot_winding
from pyleecan.Methods.Machine.LamSlotWind.comp_fill_factor import comp_fill_factor
from pyleecan.Methods.Machine.LamSlotWind.comp_output_geo import comp_output_geo
from pyleecan.Methods.Machine.LamSlotWind.get_polar_eq import get_polar_eq

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.Notch import Notch


class LamSlotWind(LamSlot):
    """Lamination with Slot filled with winding"""

    VERSION = 1

    # cf Methods.Machine.LamSlotWind.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.LamSlotWind.check
    check = check
    # cf Methods.Machine.LamSlotWind.comp_masses
    comp_masses = comp_masses
    # cf Methods.Machine.LamSlotWind.comp_surfaces
    comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotWind.comp_volumes
    comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotWind.get_pole_pair_number
    get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlotWind.get_name_phase
    get_name_phase = get_name_phase
    # cf Methods.Machine.LamSlotWind.plot
    plot = plot
    # cf Methods.Machine.LamSlotWind.plot_winding
    plot_winding = plot_winding
    # cf Methods.Machine.LamSlotWind.comp_fill_factor
    comp_fill_factor = comp_fill_factor
    # cf Methods.Machine.LamSlotWind.comp_output_geo
    comp_output_geo = comp_output_geo
    # cf Methods.Machine.LamSlotWind.get_polar_eq
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
            check_init_dict(
                init_dict,
                [
                    "Ksfill",
                    "winding",
                    "slot",
                    "L1",
                    "mat_type",
                    "Nrvd",
                    "Wrvd",
                    "Kf1",
                    "is_internal",
                    "Rint",
                    "Rext",
                    "is_stator",
                    "axial_vent",
                    "notch",
                ],
            )
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
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
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
        LamSlotWind_str += super(LamSlotWind, self).__str__() + linesep
        LamSlotWind_str += "Ksfill = " + str(self.Ksfill) + linesep
        LamSlotWind_str += "winding = " + str(self.winding.as_dict())
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
