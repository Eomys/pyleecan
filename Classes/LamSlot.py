# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Lamination import Lamination

from pyleecan.Methods.Machine.LamSlot.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSlot.check import check
from pyleecan.Methods.Machine.LamSlot.comp_height_yoke import comp_height_yoke
from pyleecan.Methods.Machine.LamSlot.comp_radius_mec import comp_radius_mec
from pyleecan.Methods.Machine.LamSlot.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.LamSlot.get_pole_pair_number import get_pole_pair_number
from pyleecan.Methods.Machine.LamSlot.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
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


class LamSlot(Lamination):
    """Lamination with empty Slot"""

    VERSION = 1

    # cf Methods.Machine.LamSlot.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.LamSlot.check
    check = check
    # cf Methods.Machine.LamSlot.comp_height_yoke
    comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamSlot.comp_radius_mec
    comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlot.comp_surfaces
    comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlot.get_pole_pair_number
    get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlot.plot
    plot = plot
    # save method is available in all object
    save = save

    def __init__(
        self,
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

        if slot == -1:
            slot = Slot()
        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
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
        # slot can be None, a Slot object or a dict
        if isinstance(slot, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "SlotMFlat": SlotMFlat,
                "SlotMPolar": SlotMPolar,
                "SlotW10": SlotW10,
                "SlotW11": SlotW11,
                "SlotW12": SlotW12,
                "SlotW13": SlotW13,
                "SlotW14": SlotW14,
                "SlotW15": SlotW15,
                "SlotW16": SlotW16,
                "SlotW21": SlotW21,
                "SlotW22": SlotW22,
                "SlotW23": SlotW23,
                "SlotW24": SlotW24,
                "SlotW25": SlotW25,
                "SlotW26": SlotW26,
                "SlotW27": SlotW27,
                "SlotW28": SlotW28,
                "SlotW29": SlotW29,
                "SlotW60": SlotW60,
                "SlotW61": SlotW61,
                "Slot": Slot,
            }
            obj_class = slot.get("__class__")
            if obj_class is None:
                self.slot = Slot(init_dict=slot)
            elif obj_class in list(load_dict.keys()):
                self.slot = load_dict[obj_class](init_dict=slot)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for slot")
        else:
            self.slot = slot
        # Call Lamination init
        super(LamSlot, self).__init__(
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
        # The class is frozen (in Lamination init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamSlot_str = ""
        # Get the properties inherited from Lamination
        LamSlot_str += super(LamSlot, self).__str__() + linesep
        LamSlot_str += "slot = " + str(self.slot.as_dict())
        return LamSlot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Lamination
        if not super(LamSlot, self).__eq__(other):
            return False
        if other.slot != self.slot:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Lamination
        LamSlot_dict = super(LamSlot, self).as_dict()
        if self.slot is None:
            LamSlot_dict["slot"] = None
        else:
            LamSlot_dict["slot"] = self.slot.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSlot_dict["__class__"] = "LamSlot"
        return LamSlot_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.slot is not None:
            self.slot._set_None()
        # Set to None the properties inherited from Lamination
        super(LamSlot, self)._set_None()

    def _get_slot(self):
        """getter of slot"""
        return self._slot

    def _set_slot(self, value):
        """setter of slot"""
        check_var("slot", value, "Slot")
        self._slot = value

        if self._slot is not None:
            self._slot.parent = self

    # lamination Slot
    # Type : Slot
    slot = property(fget=_get_slot, fset=_set_slot, doc=u"""lamination Slot""")
