# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Machine.Machine.build_geometry import build_geometry
from pyleecan.Methods.Machine.Machine.check import check
from pyleecan.Methods.Machine.Machine.comp_masses import comp_masses
from pyleecan.Methods.Machine.Machine.comp_width_airgap_mag import comp_width_airgap_mag
from pyleecan.Methods.Machine.Machine.comp_width_airgap_mec import comp_width_airgap_mec
from pyleecan.Methods.Machine.Machine.get_lamination import get_lamination
from pyleecan.Methods.Machine.Machine.comp_Rgap_mec import comp_Rgap_mec
from pyleecan.Methods.Machine.Machine.plot import plot
from pyleecan.Methods.Machine.Machine.comp_output_geo import comp_output_geo
from pyleecan.Methods.Machine.Machine.comp_length_airgap_active import (
    comp_length_airgap_active,
)
from pyleecan.Methods.Machine.Machine.get_surface_airgap import get_surface_airgap
from pyleecan.Methods.Machine.Machine.comp_sym import comp_sym

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class Machine(FrozenClass):

    VERSION = 1

    # cf Methods.Machine.Machine.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.Machine.check
    check = check
    # cf Methods.Machine.Machine.comp_masses
    comp_masses = comp_masses
    # cf Methods.Machine.Machine.comp_width_airgap_mag
    comp_width_airgap_mag = comp_width_airgap_mag
    # cf Methods.Machine.Machine.comp_width_airgap_mec
    comp_width_airgap_mec = comp_width_airgap_mec
    # cf Methods.Machine.Machine.get_lamination
    get_lamination = get_lamination
    # cf Methods.Machine.Machine.comp_Rgap_mec
    comp_Rgap_mec = comp_Rgap_mec
    # cf Methods.Machine.Machine.plot
    plot = plot
    # cf Methods.Machine.Machine.comp_output_geo
    comp_output_geo = comp_output_geo
    # cf Methods.Machine.Machine.comp_length_airgap_active
    comp_length_airgap_active = comp_length_airgap_active
    # cf Methods.Machine.Machine.get_surface_airgap
    get_surface_airgap = get_surface_airgap
    # cf Methods.Machine.Machine.comp_sym
    comp_sym = comp_sym
    # save method is available in all object
    save = save

    def __init__(
        self,
        rotor=-1,
        stator=-1,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if rotor == -1:
            rotor = Lamination()
        if stator == -1:
            stator = Lamination()
        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict, ["rotor", "stator", "frame", "shaft", "name", "desc"]
            )
            # Overwrite default value with init_dict content
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
        # Initialisation by argument
        self.parent = None
        # rotor can be None, a Lamination object or a dict
        if isinstance(rotor, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "LamHole": LamHole,
                "LamSlot": LamSlot,
                "LamSlotWind": LamSlotWind,
                "LamSlotMag": LamSlotMag,
                "LamSquirrelCage": LamSquirrelCage,
                "Lamination": Lamination,
            }
            obj_class = rotor.get("__class__")
            if obj_class is None:
                self.rotor = Lamination(init_dict=rotor)
            elif obj_class in list(load_dict.keys()):
                self.rotor = load_dict[obj_class](init_dict=rotor)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for rotor")
        else:
            self.rotor = rotor
        # stator can be None, a Lamination object or a dict
        if isinstance(stator, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "LamHole": LamHole,
                "LamSlot": LamSlot,
                "LamSlotWind": LamSlotWind,
                "LamSlotMag": LamSlotMag,
                "LamSquirrelCage": LamSquirrelCage,
                "Lamination": Lamination,
            }
            obj_class = stator.get("__class__")
            if obj_class is None:
                self.stator = Lamination(init_dict=stator)
            elif obj_class in list(load_dict.keys()):
                self.stator = load_dict[obj_class](init_dict=stator)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for stator")
        else:
            self.stator = stator
        # frame can be None, a Frame object or a dict
        if isinstance(frame, dict):
            self.frame = Frame(init_dict=frame)
        else:
            self.frame = frame
        # shaft can be None, a Shaft object or a dict
        if isinstance(shaft, dict):
            self.shaft = Shaft(init_dict=shaft)
        else:
            self.shaft = shaft
        self.name = name
        self.desc = desc

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Machine_str = ""
        if self.parent is None:
            Machine_str += "parent = None " + linesep
        else:
            Machine_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Machine_str += "rotor = " + str(self.rotor.as_dict()) + linesep + linesep
        Machine_str += "stator = " + str(self.stator.as_dict()) + linesep + linesep
        Machine_str += "frame = " + str(self.frame.as_dict()) + linesep + linesep
        Machine_str += "shaft = " + str(self.shaft.as_dict()) + linesep + linesep
        Machine_str += 'name = "' + str(self.name) + '"' + linesep
        Machine_str += 'desc = "' + str(self.desc) + '"'
        return Machine_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rotor != self.rotor:
            return False
        if other.stator != self.stator:
            return False
        if other.frame != self.frame:
            return False
        if other.shaft != self.shaft:
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Machine_dict = dict()
        if self.rotor is None:
            Machine_dict["rotor"] = None
        else:
            Machine_dict["rotor"] = self.rotor.as_dict()
        if self.stator is None:
            Machine_dict["stator"] = None
        else:
            Machine_dict["stator"] = self.stator.as_dict()
        if self.frame is None:
            Machine_dict["frame"] = None
        else:
            Machine_dict["frame"] = self.frame.as_dict()
        if self.shaft is None:
            Machine_dict["shaft"] = None
        else:
            Machine_dict["shaft"] = self.shaft.as_dict()
        Machine_dict["name"] = self.name
        Machine_dict["desc"] = self.desc
        # The class name is added to the dict fordeserialisation purpose
        Machine_dict["__class__"] = "Machine"
        return Machine_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        if self.frame is not None:
            self.frame._set_None()
        if self.shaft is not None:
            self.shaft._set_None()
        self.name = None
        self.desc = None

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        check_var("rotor", value, "Lamination")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    # Machine's Rotor
    # Type : Lamination
    rotor = property(fget=_get_rotor, fset=_set_rotor, doc=u"""Machine's Rotor""")

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        check_var("stator", value, "Lamination")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    # Machine's Stator
    # Type : Lamination
    stator = property(fget=_get_stator, fset=_set_stator, doc=u"""Machine's Stator""")

    def _get_frame(self):
        """getter of frame"""
        return self._frame

    def _set_frame(self, value):
        """setter of frame"""
        check_var("frame", value, "Frame")
        self._frame = value

        if self._frame is not None:
            self._frame.parent = self

    # Machine's Frame
    # Type : Frame
    frame = property(fget=_get_frame, fset=_set_frame, doc=u"""Machine's Frame""")

    def _get_shaft(self):
        """getter of shaft"""
        return self._shaft

    def _set_shaft(self, value):
        """setter of shaft"""
        check_var("shaft", value, "Shaft")
        self._shaft = value

        if self._shaft is not None:
            self._shaft.parent = self

    # Machine's Shaft
    # Type : Shaft
    shaft = property(fget=_get_shaft, fset=_set_shaft, doc=u"""Machine's Shaft""")

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the machine
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the machine""")

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    # Machine description
    # Type : str
    desc = property(fget=_get_desc, fset=_set_desc, doc=u"""Machine description""")
