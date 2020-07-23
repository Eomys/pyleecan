# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/MachineWRSM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .MachineSync import MachineSync

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineWRSM.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.MachineWRSM.get_lam_list import get_lam_list
except ImportError as error:
    get_lam_list = error

try:
    from ..Methods.Machine.MachineWRSM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error


from ._check import InitUnKnowClassError
from .LamSlotWind import LamSlotWind
from .Frame import Frame
from .Shaft import Shaft


class MachineWRSM(MachineSync):
    """Wound Rotor Synchronous Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineWRSM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineWRSM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineWRSM.get_lam_list
    if isinstance(get_lam_list, ImportError):
        get_lam_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineWRSM method get_lam_list: " + str(get_lam_list)
                )
            )
        )
    else:
        get_lam_list = get_lam_list
    # cf Methods.Machine.MachineWRSM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineWRSM method get_machine_type: "
                    + str(get_machine_type)
                )
            )
        )
    else:
        get_machine_type = get_machine_type
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

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
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if rotor == -1:
            rotor = LamSlotWind()
        if stator == -1:
            stator = LamSlotWind()
        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            rotor = obj.rotor
            stator = obj.stator
            frame = obj.frame
            shaft = obj.shaft
            name = obj.name
            desc = obj.desc
            type_machine = obj.type_machine
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
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
        # rotor can be None, a LamSlotWind object or a dict
        if isinstance(rotor, dict):
            # Check that the type is correct (including daughter)
            class_name = rotor.get("__class__")
            if class_name not in ["LamSlotWind", "LamSquirrelCage"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for rotor"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.rotor = class_obj(init_dict=rotor)
        elif isinstance(rotor, str):
            from ..Functions.load import load

            rotor = load(rotor)
            # Check that the type is correct (including daughter)
            class_name = rotor.__class__.__name__
            if class_name not in ["LamSlotWind", "LamSquirrelCage"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for rotor"
                )
            self.rotor = rotor
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
        elif isinstance(stator, str):
            from ..Functions.load import load

            stator = load(stator)
            # Check that the type is correct (including daughter)
            class_name = stator.__class__.__name__
            if class_name not in ["LamSlotWind", "LamSquirrelCage"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for stator"
                )
            self.stator = stator
        else:
            self.stator = stator
        # Call MachineSync init
        super(MachineWRSM, self).__init__(
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

        MachineWRSM_str = ""
        # Get the properties inherited from MachineSync
        MachineWRSM_str += super(MachineWRSM, self).__str__()
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineWRSM_str += "rotor = " + tmp
        else:
            MachineWRSM_str += "rotor = None" + linesep + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineWRSM_str += "stator = " + tmp
        else:
            MachineWRSM_str += "stator = None" + linesep + linesep
        return MachineWRSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineSync
        if not super(MachineWRSM, self).__eq__(other):
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
        MachineWRSM_dict = super(MachineWRSM, self).as_dict()
        if self.rotor is None:
            MachineWRSM_dict["rotor"] = None
        else:
            MachineWRSM_dict["rotor"] = self.rotor.as_dict()
        if self.stator is None:
            MachineWRSM_dict["stator"] = None
        else:
            MachineWRSM_dict["stator"] = self.stator.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineWRSM_dict["__class__"] = "MachineWRSM"
        return MachineWRSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        # Set to None the properties inherited from MachineSync
        super(MachineWRSM, self)._set_None()

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        check_var("rotor", value, "LamSlotWind")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    # Machine's Rotor
    # Type : LamSlotWind
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
