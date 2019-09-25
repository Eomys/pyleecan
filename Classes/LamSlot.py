# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Lamination import Lamination

from pyleecan.Methods.Machine.LamSlot.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSlot.check import check
from pyleecan.Methods.Machine.LamSlot.comp_radius_mec import comp_radius_mec
from pyleecan.Methods.Machine.LamSlot.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.LamSlot.get_pole_pair_number import get_pole_pair_number
from pyleecan.Methods.Machine.LamSlot.plot import plot
from pyleecan.Methods.Machine.LamSlot.comp_height_yoke import comp_height_yoke

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.Notch import Notch


class LamSlot(Lamination):
    """Lamination with empty Slot"""

    VERSION = 1

    # cf Methods.Machine.LamSlot.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.LamSlot.check
    check = check
    # cf Methods.Machine.LamSlot.comp_radius_mec
    comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlot.comp_surfaces
    comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlot.get_pole_pair_number
    get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlot.plot
    plot = plot
    # cf Methods.Machine.LamSlot.comp_height_yoke
    comp_height_yoke = comp_height_yoke
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
                    "notch",
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
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
        # Initialisation by argument
        # slot can be None, a Slot object or a dict
        if isinstance(slot, dict):
            # Check that the type is correct (including daughter)
            class_name = slot.get("__class__")
            if class_name not in [
                "Slot",
                "Slot",
                "Slot19",
                "SlotMFlat",
                "SlotMPolar",
                "SlotW10",
                "SlotW11",
                "SlotW12",
                "SlotW13",
                "SlotW14",
                "SlotW15",
                "SlotW16",
                "SlotW21",
                "SlotW22",
                "SlotW23",
                "SlotW24",
                "SlotW25",
                "SlotW26",
                "SlotW27",
                "SlotW28",
                "SlotW29",
                "SlotW60",
                "SlotW61",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.slot = class_obj(init_dict=slot)
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
            notch=notch,
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
