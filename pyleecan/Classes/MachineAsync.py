# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/MachineAsync.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineAsync.is_synchronous import is_synchronous
except ImportError as error:
    is_synchronous = error


from ._check import InitUnKnowClassError
from .Frame import Frame
from .Shaft import Shaft


class MachineAsync(Machine):
    """Abstract class for asynchronous machines"""

    VERSION = 1

    # cf Methods.Machine.MachineAsync.is_synchronous
    if isinstance(is_synchronous, ImportError):
        is_synchronous = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineAsync method is_synchronous: "
                    + str(is_synchronous)
                )
            )
        )
    else:
        is_synchronous = is_synchronous
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object
        - __init__ (init_str = s) s must be a string
        s is the file path to load """

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
            frame = obj.frame
            shaft = obj.shaft
            name = obj.name
            desc = obj.desc
            type_machine = obj.type_machine
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
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
        # Call Machine init
        super(MachineAsync, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in Machine init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineAsync_str = ""
        # Get the properties inherited from Machine
        MachineAsync_str += super(MachineAsync, self).__str__()
        return MachineAsync_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Machine
        if not super(MachineAsync, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Machine
        MachineAsync_dict = super(MachineAsync, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineAsync_dict["__class__"] = "MachineAsync"
        return MachineAsync_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Machine
        super(MachineAsync, self)._set_None()
