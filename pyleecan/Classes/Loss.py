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

    def __init__(self, models=list(), init_dict=None, init_str=None):
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
            models = obj.models
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "models" in list(init_dict.keys()):
                models = init_dict["models"]
        # Initialisation by argument
        self.parent = None
        # models can be None or a list of LossModel object or a list of dict
        if type(models) is list:
            # Check if the list is only composed of LossModel
            if len(models) > 0 and all(isinstance(obj, LossModel) for obj in models):
                # set the list to keep pointer reference
                self.models = models
            else:
                self.models = list()
                for obj in models:
                    if not isinstance(obj, dict):  # Default value
                        self.models.append(obj)
                    elif isinstance(obj, dict):
                        # Check that the type is correct (including daughter)
                        class_name = obj.get("__class__")
                        if class_name not in ["LossModel", "LossModelBertotti"]:
                            raise InitUnKnowClassError(
                                "Unknow class name "
                                + class_name
                                + " in init_dict for models"
                            )
                        # Dynamic import to call the correct constructor
                        module = __import__(
                            "pyleecan.Classes." + class_name, fromlist=[class_name]
                        )
                        class_obj = getattr(module, class_name)
                        self.models.append(class_obj(init_dict=obj))

        elif models is None:
            self.models = list()
        else:
            self.models = models

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        Loss_dict = dict()
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
        for obj in self._models:
            if obj is not None:
                obj.parent = self
        return self._models

    def _set_models(self, value):
        """setter of models"""
        check_var("models", value, "[LossModel]")
        self._models = value

        for obj in self._models:
            if obj is not None:
                obj.parent = self

    models = property(
        fget=_get_models,
        fset=_set_models,
        doc=u"""List of models to compute the machines losses

        :Type: [LossModel]
        """,
    )
