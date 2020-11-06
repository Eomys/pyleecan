# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Structural.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Structural
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Structural.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Structural.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error


from ._check import InitUnKnowClassError


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
    # cf Methods.Simulation.Structural.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Structural method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, structural=0, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "structural" in list(init_dict.keys()):
                structural = init_dict["structural"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.structural = structural

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Structural_str = ""
        if self.parent is None:
            Structural_str += "parent = None " + linesep
        else:
            Structural_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Structural_str += "structural = " + str(self.structural) + linesep
        return Structural_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.structural != self.structural:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Structural_dict = dict()
        Structural_dict["structural"] = self.structural
        # The class name is added to the dict for deserialisation purpose
        Structural_dict["__class__"] = "Structural"
        return Structural_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.structural = None

    def _get_structural(self):
        """getter of structural"""
        return self._structural

    def _set_structural(self, value):
        """setter of structural"""
        check_var("structural", value, "int")
        self._structural = value

    structural = property(
        fget=_get_structural,
        fset=_set_structural,
        doc=u"""Structural module

        :Type: int
        """,
    )
