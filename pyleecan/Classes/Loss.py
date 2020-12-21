# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Loss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Loss
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Loss.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError


class Loss(FrozenClass):
    """Losses module object that containt the loss models"""

    VERSION = 1

    # cf Methods.Simulation.Loss.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(ImportError("Can't use Loss method run: " + str(run)))
        )
    else:
        run = run
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, iron=-1, winding=-1, magnet=-1, init_dict=None, init_str=None):
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
            if "iron" in list(init_dict.keys()):
                iron = init_dict["iron"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "magnet" in list(init_dict.keys()):
                magnet = init_dict["magnet"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.iron = iron
        self.winding = winding
        self.magnet = magnet

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Loss_str = ""
        if self.parent is None:
            Loss_str += "parent = None " + linesep
        else:
            Loss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Loss_str += "iron = " + str(self.iron) + linesep
        Loss_str += "winding = " + str(self.winding) + linesep
        Loss_str += "magnet = " + str(self.magnet) + linesep
        return Loss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.iron != self.iron:
            return False
        if other.winding != self.winding:
            return False
        if other.magnet != self.magnet:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.iron is not None:
            for key, value in self.iron.items():
                S += getsizeof(value) + getsizeof(key)
        if self.winding is not None:
            for key, value in self.winding.items():
                S += getsizeof(value) + getsizeof(key)
        if self.magnet is not None:
            for key, value in self.magnet.items():
                S += getsizeof(value) + getsizeof(key)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Loss_dict = dict()
        Loss_dict["iron"] = self.iron.copy() if self.iron is not None else None
        Loss_dict["winding"] = self.winding.copy() if self.winding is not None else None
        Loss_dict["magnet"] = self.magnet.copy() if self.magnet is not None else None
        # The class name is added to the dict for deserialisation purpose
        Loss_dict["__class__"] = "Loss"
        return Loss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.iron = None
        self.winding = None
        self.magnet = None

    def _get_iron(self):
        """getter of iron"""
        return self._iron

    def _set_iron(self, value):
        """setter of iron"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("iron", value, "dict")
        self._iron = value

    iron = property(
        fget=_get_iron,
        fset=_set_iron,
        doc=u"""Dict of the iron loss model (key is the lamination name)

        :Type: dict
        """,
    )

    def _get_winding(self):
        """getter of winding"""
        return self._winding

    def _set_winding(self, value):
        """setter of winding"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("winding", value, "dict")
        self._winding = value

    winding = property(
        fget=_get_winding,
        fset=_set_winding,
        doc=u"""Dict of the winding loss model (key is the lamination name)

        :Type: dict
        """,
    )

    def _get_magnet(self):
        """getter of magnet"""
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("magnet", value, "dict")
        self._magnet = value

    magnet = property(
        fget=_get_magnet,
        fset=_set_magnet,
        doc=u"""Dict of the magnet loss model (key is the lamination name)

        :Type: dict
        """,
    )
