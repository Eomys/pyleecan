# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LossModel.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LossModel
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
    from ..Methods.Simulation.LossModel.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error


from ._check import InitUnKnowClassError


class LossModel(FrozenClass):
    """Abstract Loss Model Class"""

    VERSION = 1

    # cf Methods.Simulation.LossModel.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossModel method comp_loss: " + str(comp_loss))
            )
        )
    else:
        comp_loss = comp_loss
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, name="", init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            name = obj.name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
        # Initialisation by argument
        self.parent = None
        self.name = name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LossModel_str = ""
        if self.parent is None:
            LossModel_str += "parent = None " + linesep
        else:
            LossModel_str += "parent = " + str(type(self.parent)) + " object" + linesep
        LossModel_str += 'name = "' + str(self.name) + '"' + linesep
        return LossModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        LossModel_dict = dict()
        LossModel_dict["name"] = self.name
        # The class name is added to the dict fordeserialisation purpose
        LossModel_dict["__class__"] = "LossModel"
        return LossModel_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the loss simulation (has to be unique)

        :Type: str
        """,
    )
