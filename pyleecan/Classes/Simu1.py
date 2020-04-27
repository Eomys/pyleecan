# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Simu1.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Simulation import Simulation

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Simu1.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .Magnetics import Magnetics
from .Structural import Structural
from .Machine import Machine
from .Input import Input


class Simu1(Simulation):
    """Five sequential weak coupling multi physics simulation"""

    VERSION = 1

    # cf Methods.Simulation.Simu1.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Simu1 method run: " + str(run))
            )
        )
    else:
        run = run
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mag=-1,
        struct=-1,
        name="",
        desc="",
        machine=-1,
        input=-1,
        logger_name="Pyleecan.Simulation",
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

        if mag == -1:
            mag = Magnetics()
        if struct == -1:
            struct = Structural()
        if machine == -1:
            machine = Machine()
        if input == -1:
            input = Input()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            mag = obj.mag
            struct = obj.struct
            name = obj.name
            desc = obj.desc
            machine = obj.machine
            input = obj.input
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "mag" in list(init_dict.keys()):
                mag = init_dict["mag"]
            if "struct" in list(init_dict.keys()):
                struct = init_dict["struct"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        # mag can be None, a Magnetics object or a dict
        if isinstance(mag, dict):
            # Check that the type is correct (including daughter)
            class_name = mag.get("__class__")
            if class_name not in ["Magnetics", "MagFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for mag"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.mag = class_obj(init_dict=mag)
        else:
            self.mag = mag
        # struct can be None, a Structural object or a dict
        if isinstance(struct, dict):
            self.struct = Structural(init_dict=struct)
        else:
            self.struct = struct
        # Call Simulation init
        super(Simu1, self).__init__(
            name=name, desc=desc, machine=machine, input=input, logger_name=logger_name
        )
        # The class is frozen (in Simulation init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Simu1_str = ""
        # Get the properties inherited from Simulation
        Simu1_str += super(Simu1, self).__str__()
        if self.mag is not None:
            tmp = self.mag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "mag = " + tmp
        else:
            Simu1_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            tmp = self.struct.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "struct = " + tmp
        else:
            Simu1_str += "struct = None" + linesep + linesep
        return Simu1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Simulation
        if not super(Simu1, self).__eq__(other):
            return False
        if other.mag != self.mag:
            return False
        if other.struct != self.struct:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Simulation
        Simu1_dict = super(Simu1, self).as_dict()
        if self.mag is None:
            Simu1_dict["mag"] = None
        else:
            Simu1_dict["mag"] = self.mag.as_dict()
        if self.struct is None:
            Simu1_dict["struct"] = None
        else:
            Simu1_dict["struct"] = self.struct.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Simu1_dict["__class__"] = "Simu1"
        return Simu1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.mag is not None:
            self.mag._set_None()
        if self.struct is not None:
            self.struct._set_None()
        # Set to None the properties inherited from Simulation
        super(Simu1, self)._set_None()

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        check_var("mag", value, "Magnetics")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    # Magnetic module
    # Type : Magnetics
    mag = property(fget=_get_mag, fset=_set_mag, doc=u"""Magnetic module""")

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        check_var("struct", value, "Structural")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    # Structural module
    # Type : Structural
    struct = property(fget=_get_struct, fset=_set_struct, doc=u"""Structural module""")
