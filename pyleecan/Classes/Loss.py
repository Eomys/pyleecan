# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Loss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Loss
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
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
from .LossModel import LossModel


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
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, models=-1, init_dict=None, init_str=None):
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
            if "models" in list(init_dict.keys()):
                models = init_dict["models"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.models = models

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Loss_str = ""
        if self.parent is None:
            Loss_str += "parent = None " + linesep
        else:
            Loss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if len(self.models) == 0:
            Loss_str += "models = []" + linesep
        for ii in range(len(self.models)):
            tmp = self.models[ii].__str__().replace(linesep, linesep + "\t") + linesep
            Loss_str += "models[" + str(ii) + "] =" + tmp + linesep + linesep
        return Loss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.models != self.models:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Loss_dict = dict()
        if self.models is None:
            Loss_dict["models"] = None
        else:
            Loss_dict["models"] = list()
            for obj in self.models:
                Loss_dict["models"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        Loss_dict["__class__"] = "Loss"
        return Loss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.models:
            obj._set_None()

    def _get_models(self):
        """getter of models"""
        if self._models is not None:
            for obj in self._models:
                if obj is not None:
                    obj.parent = self
        return self._models

    def _set_models(self, value):
        """setter of models"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "models"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("models", value, "[LossModel]")
        self._models = value

    models = property(
        fget=_get_models,
        fset=_set_models,
        doc=u"""List of models to compute the machines losses

        :Type: [LossModel]
        """,
    )
