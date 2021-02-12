# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class EEC(FrozenClass):
    """Electric module: Equivalent Electrical Circuit abstract class"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert init_dict == {"__class__": "EEC"}
        if init_str is not None:  # Initialisation by str
            assert type(init_str) is str
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_str = ""
        if self.parent is None:
            EEC_str += "parent = None " + linesep
        else:
            EEC_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return EEC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        return S

    def as_dict(self, keep_function=False):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional input parameter 'keep_function' is for internal use only
        and may prevent json serializability.
        """

        EEC_dict = dict()
        # The class name is added to the dict for deserialisation purpose
        EEC_dict["__class__"] = "EEC"
        return EEC_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
        pass
