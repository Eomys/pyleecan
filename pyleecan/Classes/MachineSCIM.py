# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/MachineSCIM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .MachineDFIM import MachineDFIM

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineSCIM.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.MachineSCIM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error


from ._check import InitUnKnowClassError
from .LamSlotWind import LamSlotWind
from .Frame import Frame
from .Shaft import Shaft


class MachineSCIM(MachineDFIM):
    """Squirrel Cage Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineSCIM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineSCIM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineSCIM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineSCIM method get_machine_type: "
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
        # Call MachineDFIM init
        super(MachineSCIM, self).__init__(
            rotor=rotor,
            stator=stator,
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in MachineDFIM init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineSCIM_str = ""
        # Get the properties inherited from MachineDFIM
        MachineSCIM_str += super(MachineSCIM, self).__str__()
        return MachineSCIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineDFIM
        if not super(MachineSCIM, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MachineDFIM
        MachineSCIM_dict = super(MachineSCIM, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineSCIM_dict["__class__"] = "MachineSCIM"
        return MachineSCIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from MachineDFIM
        super(MachineSCIM, self)._set_None()
