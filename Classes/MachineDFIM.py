# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MachineDFIM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MachineAsync import MachineAsync

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MachineDFIM.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Machine.MachineDFIM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class MachineDFIM(MachineAsync):
    """Doubly Fed Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineDFIM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineDFIM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineDFIM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineDFIM method get_machine_type: "
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
        # Call MachineAsync init
        super(MachineDFIM, self).__init__(
            rotor=rotor,
            stator=stator,
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
        )
        # The class is frozen (in MachineAsync init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineDFIM_str = ""
        # Get the properties inherited from MachineAsync
        MachineDFIM_str += super(MachineDFIM, self).__str__() + linesep
        return MachineDFIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineAsync
        if not super(MachineDFIM, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MachineAsync
        MachineDFIM_dict = super(MachineDFIM, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineDFIM_dict["__class__"] = "MachineDFIM"
        return MachineDFIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from MachineAsync
        super(MachineDFIM, self)._set_None()
