# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Structural.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Structural.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Structural.comp_time_angle import comp_time_angle
except ImportError as error:
    comp_time_angle = error


from ._check import InitUnKnowClassError
from .Force import Force


class Structural(FrozenClass):
    """Structural module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Structural.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Structural method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Structural.comp_time_angle
    if isinstance(comp_time_angle, ImportError):
        comp_time_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Structural method comp_time_angle: "
                    + str(comp_time_angle)
                )
            )
        )
    else:
        comp_time_angle = comp_time_angle
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, force=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if force == -1:
            force = Force()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            force = obj.force
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "force" in list(init_dict.keys()):
                force = init_dict["force"]
        # Initialisation by argument
        self.parent = None
        # force can be None, a Force object or a dict
        if isinstance(force, dict):
            # Check that the type is correct (including daughter)
            class_name = force.get("__class__")
            if class_name not in ["Force", "ForceMT"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for force"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.force = class_obj(init_dict=force)
        elif isinstance(force, str):
            from ..Functions.load import load

            force = load(force)
            # Check that the type is correct (including daughter)
            class_name = force.__class__.__name__
            if class_name not in ["Force", "ForceMT"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for force"
                )
            self.force = force
        else:
            self.force = force

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Structural_str = ""
        if self.parent is None:
            Structural_str += "parent = None " + linesep
        else:
            Structural_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.force is not None:
            tmp = self.force.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Structural_str += "force = " + tmp
        else:
            Structural_str += "force = None" + linesep + linesep
        return Structural_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.force != self.force:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Structural_dict = dict()
        if self.force is None:
            Structural_dict["force"] = None
        else:
            Structural_dict["force"] = self.force.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Structural_dict["__class__"] = "Structural"
        return Structural_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.force is not None:
            self.force._set_None()

    def _get_force(self):
        """getter of force"""
        return self._force

    def _set_force(self, value):
        """setter of force"""
        check_var("force", value, "Force")
        self._force = value

        if self._force is not None:
            self._force.parent = self

    # Force module
    # Type : Force
    force = property(fget=_get_force, fset=_set_force, doc=u"""Force module""")
