# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.LamSlot import LamSlot

from pyleecan.Methods.Machine.LamSlotWind.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSlotWind.check import check
from pyleecan.Methods.Machine.LamSlotWind.comp_masses import comp_masses
from pyleecan.Methods.Machine.LamSlotWind.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.LamSlotWind.comp_volumes import comp_volumes
from pyleecan.Methods.Machine.LamSlotWind.get_pole_pair_number import (
    get_pole_pair_number,
)
from pyleecan.Methods.Machine.LamSlotWind.plot import plot
from pyleecan.Methods.Machine.LamSlotWind.plot_winding import plot_winding

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.HoleMag import HoleMag
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


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
    # cf Methods.Machine.LamSlotWind.plot
    plot = plot
    # cf Methods.Machine.LamSlotWind.plot_winding
    plot_winding = plot_winding

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
        # Initialisation by argument
        self.Ksfill = Ksfill
        # winding can be None, a Winding object or a dict
        if isinstance(winding, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "WindingCW1L": WindingCW1L,
                "WindingCW2LR": WindingCW2LR,
                "WindingCW2LT": WindingCW2LT,
                "WindingDW1L": WindingDW1L,
                "WindingDW2L": WindingDW2L,
                "WindingSC": WindingSC,
                "WindingUD": WindingUD,
                "Winding": Winding,
            }
            obj_class = winding.get("__class__")
            if obj_class is None:
                self.winding = Winding(init_dict=winding)
            elif obj_class in list(load_dict.keys()):
                self.winding = load_dict[obj_class](init_dict=winding)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for winding")
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
