# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.MachineSync import MachineSync

from pyleecan.Methods.Machine.MachineSIPMSM.check import check
from pyleecan.Methods.Machine.MachineSIPMSM.get_machine_type import get_machine_type

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft



class MachineSIPMSM(MachineSync):
    """Inset and Surface Permanent Magnet Synchronous Machine"""

    VERSION = 1

    # cf Methods.Machine.MachineSIPMSM.check
    check = check
    # cf Methods.Machine.MachineSIPMSM.get_machine_type
    get_machine_type = get_machine_type
    # save method is available in all object
    save = save

    def __init__(self, rotor=-1, stator=-1, frame=-1, shaft=-1, name="default_machine", desc="", init_dict=None):
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
            check_init_dict(init_dict, ["rotor", "stator", "frame", "shaft", "name", "desc"])
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
        # Call MachineSync init
        super(MachineSIPMSM, self).__init__(rotor=rotor, stator=stator, frame=frame, shaft=shaft, name=name, desc=desc)
        # The class is frozen (in MachineSync init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineSIPMSM_str = ""
        # Get the properties inherited from MachineSync
        MachineSIPMSM_str += super(MachineSIPMSM, self).__str__() + linesep
        return MachineSIPMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineSync
        if not super(MachineSIPMSM, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MachineSync
        MachineSIPMSM_dict = super(MachineSIPMSM, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineSIPMSM_dict["__class__"] = "MachineSIPMSM"
        return MachineSIPMSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from MachineSync
        super(MachineSIPMSM, self)._set_None()


