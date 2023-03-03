# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Loss/Loss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Loss/Loss
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Loss.Loss.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Loss.Loss.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Loss.Loss.comp_all_losses import comp_all_losses
except ImportError as error:
    comp_all_losses = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Loss(FrozenClass):
    """Loss module object that contain the loss models."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Loss.Loss.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(ImportError("Can't use Loss method run: " + str(run)))
        )
    else:
        run = run
    # cf Methods.Loss.Loss.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Loss method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Loss.Loss.comp_all_losses
    if isinstance(comp_all_losses, ImportError):
        comp_all_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Loss method comp_all_losses: " + str(comp_all_losses)
                )
            )
        )
    else:
        comp_all_losses = comp_all_losses
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        logger_name="Pyleecan.Loss",
        model_dict=None,
        Tsta=20,
        Trot=20,
        is_get_meshsolution=False,
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
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "model_dict" in list(init_dict.keys()):
                model_dict = init_dict["model_dict"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "is_get_meshsolution" in list(init_dict.keys()):
                is_get_meshsolution = init_dict["is_get_meshsolution"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.logger_name = logger_name
        self.model_dict = model_dict
        self.Tsta = Tsta
        self.Trot = Trot
        self.is_get_meshsolution = is_get_meshsolution

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Loss_str = ""
        if self.parent is None:
            Loss_str += "parent = None " + linesep
        else:
            Loss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Loss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if len(self.model_dict) == 0:
            Loss_str += "model_dict = dict()" + linesep
        for key, obj in self.model_dict.items():
            tmp = (
                self.model_dict[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            Loss_str += "model_dict[" + key + "] =" + tmp + linesep + linesep
        Loss_str += "Tsta = " + str(self.Tsta) + linesep
        Loss_str += "Trot = " + str(self.Trot) + linesep
        Loss_str += "is_get_meshsolution = " + str(self.is_get_meshsolution) + linesep
        return Loss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.model_dict != self.model_dict:
            return False
        if other.Tsta != self.Tsta:
            return False
        if other.Trot != self.Trot:
            return False
        if other.is_get_meshsolution != self.is_get_meshsolution:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._logger_name != self._logger_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._logger_name)
                    + ", other="
                    + str(other._logger_name)
                    + ")"
                )
                diff_list.append(name + ".logger_name" + val_str)
            else:
                diff_list.append(name + ".logger_name")
        if (other.model_dict is None and self.model_dict is not None) or (
            other.model_dict is not None and self.model_dict is None
        ):
            diff_list.append(name + ".model_dict None mismatch")
        elif self.model_dict is None:
            pass
        elif len(other.model_dict) != len(self.model_dict):
            diff_list.append("len(" + name + "model_dict)")
        else:
            for key in self.model_dict:
                diff_list.extend(
                    self.model_dict[key].compare(
                        other.model_dict[key],
                        name=name + ".model_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (
            other._Tsta is not None
            and self._Tsta is not None
            and isnan(other._Tsta)
            and isnan(self._Tsta)
        ):
            pass
        elif other._Tsta != self._Tsta:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Tsta) + ", other=" + str(other._Tsta) + ")"
                )
                diff_list.append(name + ".Tsta" + val_str)
            else:
                diff_list.append(name + ".Tsta")
        if (
            other._Trot is not None
            and self._Trot is not None
            and isnan(other._Trot)
            and isnan(self._Trot)
        ):
            pass
        elif other._Trot != self._Trot:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Trot) + ", other=" + str(other._Trot) + ")"
                )
                diff_list.append(name + ".Trot" + val_str)
            else:
                diff_list.append(name + ".Trot")
        if other._is_get_meshsolution != self._is_get_meshsolution:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_get_meshsolution)
                    + ", other="
                    + str(other._is_get_meshsolution)
                    + ")"
                )
                diff_list.append(name + ".is_get_meshsolution" + val_str)
            else:
                diff_list.append(name + ".is_get_meshsolution")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.logger_name)
        if self.model_dict is not None:
            for key, value in self.model_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Tsta)
        S += getsizeof(self.Trot)
        S += getsizeof(self.is_get_meshsolution)
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
        Loss_dict["logger_name"] = self.logger_name
        if self.model_dict is None:
            Loss_dict["model_dict"] = None
        else:
            Loss_dict["model_dict"] = dict()
            for key, obj in self.model_dict.items():
                if obj is not None:
                    Loss_dict["model_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    Loss_dict["model_dict"][key] = None
        Loss_dict["Tsta"] = self.Tsta
        Loss_dict["Trot"] = self.Trot
        Loss_dict["is_get_meshsolution"] = self.is_get_meshsolution
        # The class name is added to the dict for deserialisation purpose
        Loss_dict["__class__"] = "Loss"
        return Loss_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        logger_name_val = self.logger_name
        if self.model_dict is None:
            model_dict_val = None
        else:
            model_dict_val = dict()
            for key, obj in self.model_dict.items():
                model_dict_val[key] = obj.copy()
        Tsta_val = self.Tsta
        Trot_val = self.Trot
        is_get_meshsolution_val = self.is_get_meshsolution
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            logger_name=logger_name_val,
            model_dict=model_dict_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            is_get_meshsolution=is_get_meshsolution_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.logger_name = None
        self.model_dict = None
        self.Tsta = None
        self.Trot = None
        self.is_get_meshsolution = None

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

    def _get_model_dict(self):
        """getter of model_dict"""
        if self._model_dict is not None:
            for key, obj in self._model_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._model_dict

    def _set_model_dict(self, value):
        """setter of model_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "model_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("model_dict", value, "{LossModel}")
        self._model_dict = value

    model_dict = property(
        fget=_get_model_dict,
        fset=_set_model_dict,
        doc=u"""Dict of loss model whose key is a lamination and value is the associated loss model (alternative to model_index/model_list)

        :Type: {LossModel}
        """,
    )

    def _get_Tsta(self):
        """getter of Tsta"""
        return self._Tsta

    def _set_Tsta(self, value):
        """setter of Tsta"""
        check_var("Tsta", value, "float")
        self._Tsta = value

    Tsta = property(
        fget=_get_Tsta,
        fset=_set_Tsta,
        doc=u"""Average stator temperature for Electrical calculation

        :Type: float
        """,
    )

    def _get_Trot(self):
        """getter of Trot"""
        return self._Trot

    def _set_Trot(self, value):
        """setter of Trot"""
        check_var("Trot", value, "float")
        self._Trot = value

    Trot = property(
        fget=_get_Trot,
        fset=_set_Trot,
        doc=u"""Average rotor temperature for Electrical calculation

        :Type: float
        """,
    )

    def _get_is_get_meshsolution(self):
        """getter of is_get_meshsolution"""
        return self._is_get_meshsolution

    def _set_is_get_meshsolution(self, value):
        """setter of is_get_meshsolution"""
        check_var("is_get_meshsolution", value, "bool")
        self._is_get_meshsolution = value

    is_get_meshsolution = property(
        fget=_get_is_get_meshsolution,
        fset=_set_is_get_meshsolution,
        doc=u"""True to save loss density map as meshsolution

        :Type: bool
        """,
    )
