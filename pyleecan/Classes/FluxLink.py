# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/FluxLink.csv
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
    from ..Methods.Simulation.FluxLink.comp_fluxlinkage import comp_fluxlinkage
except ImportError as error:
    comp_fluxlinkage = error


from ._check import InitUnKnowClassError


class FluxLink(FrozenClass):
    """Electric module: Flux Linkage"""

    VERSION = 1

    # cf Methods.Simulation.FluxLink.comp_fluxlinkage
    if isinstance(comp_fluxlinkage, ImportError):
        comp_fluxlinkage = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FluxLink method comp_fluxlinkage: "
                    + str(comp_fluxlinkage)
                )
            )
        )
    else:
        comp_fluxlinkage = comp_fluxlinkage
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, a=0, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "a" in list(init_dict.keys()):
                a = init_dict["a"]
        # Initialisation by argument
        self.parent = None
        self.a = a

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        FluxLink_str = ""
        if self.parent is None:
            FluxLink_str += "parent = None " + linesep
        else:
            FluxLink_str += "parent = " + str(type(self.parent)) + " object" + linesep
        FluxLink_str += "a = " + str(self.a) + linesep
        return FluxLink_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.a != self.a:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        FluxLink_dict = dict()
        FluxLink_dict["a"] = self.a
        # The class name is added to the dict fordeserialisation purpose
        FluxLink_dict["__class__"] = "FluxLink"
        return FluxLink_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.a = None

    def _get_a(self):
        """getter of a"""
        return self._a

    def _set_a(self, value):
        """setter of a"""
        check_var("a", value, "int")
        self._a = value

    # a
    # Type : int
    a = property(fget=_get_a, fset=_set_a, doc=u"""a""")
