# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Simulation/Force.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Simulation.Force.comp_force import comp_force
except ImportError as error:
    comp_force = error

try:
    from pyleecan.Methods.Simulation.Force.comp_force_nodal import comp_force_nodal
except ImportError as error:
    comp_force_nodal = error


from pyleecan.Classes._check import InitUnKnowClassError


class Force(FrozenClass):
    """Forces module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Force.comp_force
    if isinstance(comp_force, ImportError):
        comp_force = property(
            fget=lambda x: raise_(
                ImportError("Can't use Force method comp_force: " + str(comp_force))
            )
        )
    else:
        comp_force = comp_force
    # cf Methods.Simulation.Force.comp_force_nodal
    if isinstance(comp_force_nodal, ImportError):
        comp_force_nodal = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Force method comp_force_nodal: " + str(comp_force_nodal)
                )
            )
        )
    else:
        comp_force_nodal = comp_force_nodal
    # save method is available in all object
    save = save

    def __init__(self, is_comp_nodal_force=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["is_comp_nodal_force"])
            # Overwrite default value with init_dict content
            if "is_comp_nodal_force" in list(init_dict.keys()):
                is_comp_nodal_force = init_dict["is_comp_nodal_force"]
        # Initialisation by argument
        self.parent = None
        self.is_comp_nodal_force = is_comp_nodal_force

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Force_str = ""
        if self.parent is None:
            Force_str += "parent = None " + linesep
        else:
            Force_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Force_str += "is_comp_nodal_force = " + str(self.is_comp_nodal_force) + linesep
        return Force_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_comp_nodal_force != self.is_comp_nodal_force:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Force_dict = dict()
        Force_dict["is_comp_nodal_force"] = self.is_comp_nodal_force
        # The class name is added to the dict fordeserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_comp_nodal_force = None

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self, "logger_name"):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger("Pyleecan")

    def _get_is_comp_nodal_force(self):
        """getter of is_comp_nodal_force"""
        return self._is_comp_nodal_force

    def _set_is_comp_nodal_force(self, value):
        """setter of is_comp_nodal_force"""
        check_var("is_comp_nodal_force", value, "bool")
        self._is_comp_nodal_force = value

    # 1 to compute lumped tooth forces
    # Type : bool
    is_comp_nodal_force = property(
        fget=_get_is_comp_nodal_force,
        fset=_set_is_comp_nodal_force,
        doc=u"""1 to compute lumped tooth forces""",
    )
