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

try:
    from ..Methods.Simulation.Loss.add_model import add_model
except ImportError as error:
    add_model = error

try:
    from ..Methods.Simulation.Loss.remove_model import remove_model
except ImportError as error:
    remove_model = error


from ._check import InitUnKnowClassError
from .LossModel import LossModel


class Loss(FrozenClass):
    """Losses module object that containt the loss models. See method add_model for implementation details."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Loss.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(ImportError("Can't use Loss method run: " + str(run)))
        )
    else:
        run = run
    # cf Methods.Simulation.Loss.add_model
    if isinstance(add_model, ImportError):
        add_model = property(
            fget=lambda x: raise_(
                ImportError("Can't use Loss method add_model: " + str(add_model))
            )
        )
    else:
        add_model = add_model
    # cf Methods.Simulation.Loss.remove_model
    if isinstance(remove_model, ImportError):
        remove_model = property(
            fget=lambda x: raise_(
                ImportError("Can't use Loss method remove_model: " + str(remove_model))
            )
        )
    else:
        remove_model = remove_model
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        model_index=-1,
        model_list=-1,
        logger_name="Pyleecan.Loss",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "model_index" in list(init_dict.keys()):
                model_index = init_dict["model_index"]
            if "model_list" in list(init_dict.keys()):
                model_list = init_dict["model_list"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.model_index = model_index
        self.model_list = model_list
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Loss_str = ""
        if self.parent is None:
            Loss_str += "parent = None " + linesep
        else:
            Loss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Loss_str += "model_index = " + str(self.model_index) + linesep
        if len(self.model_list) == 0:
            Loss_str += "model_list = []" + linesep
        for ii in range(len(self.model_list)):
            tmp = (
                self.model_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            Loss_str += "model_list[" + str(ii) + "] =" + tmp + linesep + linesep
        Loss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return Loss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.model_index != self.model_index:
            return False
        if other.model_list != self.model_list:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._model_index != self._model_index:
            diff_list.append(name + ".model_index")
        if (other.model_list is None and self.model_list is not None) or (
            other.model_list is not None and self.model_list is None
        ):
            diff_list.append(name + ".model_list None mismatch")
        elif self.model_list is None:
            pass
        elif len(other.model_list) != len(self.model_list):
            diff_list.append("len(" + name + ".model_list)")
        else:
            for ii in range(len(other.model_list)):
                diff_list.extend(
                    self.model_list[ii].compare(
                        other.model_list[ii], name=name + ".model_list[" + str(ii) + "]"
                    )
                )
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.model_index is not None:
            for key, value in self.model_index.items():
                S += getsizeof(value) + getsizeof(key)
        if self.model_list is not None:
            for value in self.model_list:
                S += getsizeof(value)
        S += getsizeof(self.logger_name)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        Loss_dict = dict()
        Loss_dict["model_index"] = (
            self.model_index.copy() if self.model_index is not None else None
        )
        if self.model_list is None:
            Loss_dict["model_list"] = None
        else:
            Loss_dict["model_list"] = list()
            for obj in self.model_list:
                if obj is not None:
                    Loss_dict["model_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    Loss_dict["model_list"].append(None)
        Loss_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        Loss_dict["__class__"] = "Loss"
        return Loss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.model_index = None
        self.model_list = None
        self.logger_name = None

    def _get_model_index(self):
        """getter of model_index"""
        return self._model_index

    def _set_model_index(self, value):
        """setter of model_index"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("model_index", value, "dict")
        self._model_index = value

    model_index = property(
        fget=_get_model_index,
        fset=_set_model_index,
        doc=u"""Internal dict to strore model index

        :Type: dict
        """,
    )

    def _get_model_list(self):
        """getter of model_list"""
        if self._model_list is not None:
            for obj in self._model_list:
                if obj is not None:
                    obj.parent = self
        return self._model_list

    def _set_model_list(self, value):
        """setter of model_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "model_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("model_list", value, "[LossModel]")
        self._model_list = value

    model_list = property(
        fget=_get_model_list,
        fset=_set_model_list,
        doc=u"""Internal list of loss models

        :Type: [LossModel]
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )
