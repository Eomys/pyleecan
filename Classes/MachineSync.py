# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MachineSync.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MachineSync.is_synchronous import is_synchronous
except ImportError as error:
    is_synchronous = error

try:
    from pyleecan.Methods.Machine.MachineSync.comp_initial_angle import (
        comp_initial_angle,
    )
except ImportError as error:
    comp_initial_angle = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class MachineSync(Machine):
    """Abstract class for synchronous machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineSync.is_synchronous
    if isinstance(is_synchronous, ImportError):
        is_synchronous = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineSync method is_synchronous: "
                    + str(is_synchronous)
                )
            )
        )
    else:
        is_synchronous = is_synchronous
    # cf Methods.Machine.MachineSync.comp_initial_angle
    if isinstance(comp_initial_angle, ImportError):
        comp_initial_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineSync method comp_initial_angle: "
                    + str(comp_initial_angle)
                )
            )
        )
    else:
        comp_initial_angle = comp_initial_angle
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
                init_dict,
                ["rotor", "stator", "frame", "shaft", "name", "desc", "type_machine"],
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
        # Initialisation by argument
        # Call Machine init
        super(MachineSync, self).__init__(
            rotor=rotor,
            stator=stator,
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
        )
        # The class is frozen (in Machine init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineSync_str = ""
        # Get the properties inherited from Machine
        MachineSync_str += super(MachineSync, self).__str__() + linesep
        return MachineSync_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Machine
        if not super(MachineSync, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Machine
        MachineSync_dict = super(MachineSync, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineSync_dict["__class__"] = "MachineSync"
        return MachineSync_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Machine
        super(MachineSync, self)._set_None()
