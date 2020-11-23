# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMagFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMagFEMM
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .OutInternal import OutInternal

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutMagFEMM.clean import clean
except ImportError as error:
    clean = error


from ._check import InitUnKnowClassError


class OutMagFEMM(OutInternal):
    """Class to store outputs related to MagFEMM magnetic model"""

    VERSION = 1

    # cf Methods.Output.OutMagFEMM.clean
    if isinstance(clean, ImportError):
        clean = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMagFEMM method clean: " + str(clean))
            )
        )
    else:
        clean = clean
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, FEMM_dict=None, init_dict=None, init_str=None):
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
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.FEMM_dict = FEMM_dict
        # Call OutInternal init
        super(OutMagFEMM, self).__init__()
        # The class is frozen (in OutInternal init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutMagFEMM_str = ""
        # Get the properties inherited from OutInternal
        OutMagFEMM_str += super(OutMagFEMM, self).__str__()
        OutMagFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        return OutMagFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutInternal
        if not super(OutMagFEMM, self).__eq__(other):
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from OutInternal
        OutMagFEMM_dict = super(OutMagFEMM, self).as_dict()
        OutMagFEMM_dict["FEMM_dict"] = (
            self.FEMM_dict.copy() if self.FEMM_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutMagFEMM_dict["__class__"] = "OutMagFEMM"
        return OutMagFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEMM_dict = None
        # Set to None the properties inherited from OutInternal
        super(OutMagFEMM, self)._set_None()

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    FEMM_dict = property(
        fget=_get_FEMM_dict,
        fset=_set_FEMM_dict,
        doc=u"""Dictionnary containing the main FEMM parameters

        :Type: dict
        """,
    )
