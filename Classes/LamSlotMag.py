# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.LamSlot import LamSlot

from pyleecan.Methods.Machine.LamSlotMag.build_geometry import build_geometry
from pyleecan.Methods.Machine.LamSlotMag.check import check
from pyleecan.Methods.Machine.LamSlotMag.comp_masses import comp_masses
from pyleecan.Methods.Machine.LamSlotMag.comp_radius_mec import comp_radius_mec
from pyleecan.Methods.Machine.LamSlotMag.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.LamSlotMag.comp_volumes import comp_volumes
from pyleecan.Methods.Machine.LamSlotMag.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.Notch import Notch


class LamSlotMag(LamSlot):
    """Lamination with Slot for Magnets"""

    VERSION = 1

    # cf Methods.Machine.LamSlotMag.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMag.check
    check = check
    # cf Methods.Machine.LamSlotMag.comp_masses
    comp_masses = comp_masses
    # cf Methods.Machine.LamSlotMag.comp_radius_mec
    comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlotMag.comp_surfaces
    comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotMag.comp_volumes
    comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotMag.plot
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
        )
        # The class is frozen (in LamSlot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamSlotMag_str = ""
        # Get the properties inherited from LamSlot
        LamSlotMag_str += super(LamSlotMag, self).__str__() + linesep
        return LamSlotMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlot
        if not super(LamSlotMag, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from LamSlot
        LamSlotMag_dict = super(LamSlotMag, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSlotMag_dict["__class__"] = "LamSlotMag"
        return LamSlotMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from LamSlot
        super(LamSlotMag, self)._set_None()
