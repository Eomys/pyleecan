# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleMag
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleMag.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error


from ._check import InitUnKnowClassError
from .Material import Material


class HoleMag(Hole):
    """Hole with magnets for lamination (abstract)"""

    VERSION = 1

    # cf Methods.Slot.HoleMag.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleMag method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Zh=36, mat_void=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_void == -1:
            mat_void = Material()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            Zh = obj.Zh
            mat_void = obj.mat_void
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        # Call Hole init
        super(HoleMag, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleMag_str = ""
        # Get the properties inherited from Hole
        HoleMag_str += super(HoleMag, self).__str__()
        return HoleMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(HoleMag, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Hole
        HoleMag_dict = super(HoleMag, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleMag_dict["__class__"] = "HoleMag"
        return HoleMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Hole
        super(HoleMag, self)._set_None()
