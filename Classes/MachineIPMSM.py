# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MachineIPMSM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MachineSync import MachineSync

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MachineIPMSM.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Machine.MachineIPMSM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class MachineIPMSM(MachineSync):
    """Interior Permanent Magnet Synchronous Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineIPMSM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineIPMSM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineIPMSM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineIPMSM method get_machine_type: "
                    + str(get_machine_type)
                )
            )
        )
    else:
        get_machine_type = get_machine_type
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
        type_machine=1,
        logger_name="Pyleecan.Machine",
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
            rotor = LamHole()
        if stator == -1:
            stator = LamSlotWind()
        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "rotor",
                    "stator",
                    "frame",
                    "shaft",
                    "name",
                    "desc",
                    "type_machine",
                    "logger_name",
                ],
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
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        # rotor can be None, a LamHole object or a dict
        if isinstance(rotor, dict):
            self.rotor = LamHole(init_dict=rotor)
        else:
            self.rotor = rotor
        # stator can be None, a LamSlotWind object or a dict
        if isinstance(stator, dict):
            # Check that the type is correct (including daughter)
            class_name = stator.get("__class__")
            if class_name not in ["LamSlotWind", "LamSquirrelCage"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for stator"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.stator = class_obj(init_dict=stator)
        else:
            self.stator = stator
        # Call MachineSync init
        super(MachineIPMSM, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in MachineSync init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineIPMSM_str = ""
        # Get the properties inherited from MachineSync
        MachineIPMSM_str += super(MachineIPMSM, self).__str__()
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineIPMSM_str += "rotor = " + tmp
        else:
            MachineIPMSM_str += "rotor = None" + linesep + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineIPMSM_str += "stator = " + tmp
        else:
            MachineIPMSM_str += "stator = None" + linesep + linesep
        return MachineIPMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineSync
        if not super(MachineIPMSM, self).__eq__(other):
            return False
        if other.rotor != self.rotor:
            return False
        if other.stator != self.stator:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MachineSync
        MachineIPMSM_dict = super(MachineIPMSM, self).as_dict()
        if self.rotor is None:
            MachineIPMSM_dict["rotor"] = None
        else:
            MachineIPMSM_dict["rotor"] = self.rotor.as_dict()
        if self.stator is None:
            MachineIPMSM_dict["stator"] = None
        else:
            MachineIPMSM_dict["stator"] = self.stator.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineIPMSM_dict["__class__"] = "MachineIPMSM"
        return MachineIPMSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        # Set to None the properties inherited from MachineSync
        super(MachineIPMSM, self)._set_None()

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self, "logger_name"):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger("Pyleecan")

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        check_var("rotor", value, "LamHole")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    # Machine's Rotor
    # Type : LamHole
    rotor = property(fget=_get_rotor, fset=_set_rotor, doc=u"""Machine's Rotor""")

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        check_var("stator", value, "LamSlotWind")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    # Machine's Stator
    # Type : LamSlotWind
    stator = property(fget=_get_stator, fset=_set_stator, doc=u"""Machine's Stator""")
