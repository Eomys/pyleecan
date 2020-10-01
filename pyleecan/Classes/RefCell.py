# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/RefCell.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/RefCell
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
    from ..Methods.Mesh.RefCell.interpolation import interpolation
except ImportError as error:
    interpolation = error


from ._check import InitUnKnowClassError


class RefCell(FrozenClass):
    """Store shape functions definition in the reference element"""

    VERSION = 1

    # cf Methods.Mesh.RefCell.interpolation
    if isinstance(interpolation, ImportError):
        interpolation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefCell method interpolation: " + str(interpolation)
                )
            )
        )
    else:
        interpolation = interpolation
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, epsilon=0.05, init_dict = None, init_str = None):
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
            if "epsilon" in list(init_dict.keys()):
                epsilon = init_dict["epsilon"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.epsilon = epsilon

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RefCell_str = ""
        if self.parent is None:
            RefCell_str += "parent = None " + linesep
        else:
            RefCell_str += "parent = " + str(type(self.parent)) + " object" + linesep
        RefCell_str += "epsilon = " + str(self.epsilon) + linesep
        return RefCell_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.epsilon != self.epsilon:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        RefCell_dict = dict()
        RefCell_dict["epsilon"] = self.epsilon
        # The class name is added to the dict fordeserialisation purpose
        RefCell_dict["__class__"] = "RefCell"
        return RefCell_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.epsilon = None

    def _get_epsilon(self):
        """getter of epsilon"""
        return self._epsilon

    def _set_epsilon(self, value):
        """setter of epsilon"""
        check_var("epsilon", value, "float", Vmin=0.00E+00)
        self._epsilon = value

    epsilon = property(
        fget=_get_epsilon,
        fset=_set_epsilon,
        doc=u"""Precision criterion

        :Type: float
        :min: 0.00E+00
        """,
    )
