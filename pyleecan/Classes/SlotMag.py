# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotMag
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Slot import Slot

from ._check import InitUnKnowClassError


class SlotMag(Slot):
    """Slot for inset and surface magnet (abstract)"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, W3=0, Zs=36, init_dict=None, init_str=None):
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
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.W3 = W3
        # Call Slot init
        super(SlotMag, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotMag_str = ""
        # Get the properties inherited from Slot
        SlotMag_str += super(SlotMag, self).__str__()
        SlotMag_str += "W3 = " + str(self.W3) + linesep
        return SlotMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotMag, self).__eq__(other):
            return False
        if other.W3 != self.W3:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Slot
        SlotMag_dict = super(SlotMag, self).as_dict()
        SlotMag_dict["W3"] = self.W3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotMag_dict["__class__"] = "SlotMag"
        return SlotMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W3 = None
        # Set to None the properties inherited from Slot
        super(SlotMag, self)._set_None()

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float")
        self._W3 = value

    W3 = property(
        fget=_get_W3,
        fset=_set_W3,
        doc=u"""Angle between magnet in the slot

        :Type: float
        """,
    )
