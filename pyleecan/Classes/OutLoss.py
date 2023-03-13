# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLoss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLoss
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
    from ..Methods.Output.OutLoss.get_loss_density_ag import get_loss_density_ag
except ImportError as error:
    get_loss_density_ag = error

try:
    from ..Methods.Output.OutLoss.get_loss_overall import get_loss_overall
except ImportError as error:
    get_loss_overall = error

try:
    from ..Methods.Output.OutLoss.get_power_dict import get_power_dict
except ImportError as error:
    get_power_dict = error

try:
    from ..Methods.Output.OutLoss.plot_losses import plot_losses
except ImportError as error:
    plot_losses = error

try:
    from ..Methods.Output.OutLoss.__getitem__ import __getitem__
except ImportError as error:
    __getitem__ = error

try:
    from ..Methods.Output.OutLoss.__len__ import __len__
except ImportError as error:
    __len__ = error


from numpy import isnan
from ._check import InitUnKnowClassError


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLoss.get_loss_density_ag
    if isinstance(get_loss_density_ag, ImportError):
        get_loss_density_ag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_density_ag: "
                    + str(get_loss_density_ag)
                )
            )
        )
    else:
        get_loss_density_ag = get_loss_density_ag
    # cf Methods.Output.OutLoss.get_loss_overall
    if isinstance(get_loss_overall, ImportError):
        get_loss_overall = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_overall: "
                    + str(get_loss_overall)
                )
            )
        )
    else:
        get_loss_overall = get_loss_overall
    # cf Methods.Output.OutLoss.get_power_dict
    if isinstance(get_power_dict, ImportError):
        get_power_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_power_dict: " + str(get_power_dict)
                )
            )
        )
    else:
        get_power_dict = get_power_dict
    # cf Methods.Output.OutLoss.plot_losses
    if isinstance(plot_losses, ImportError):
        plot_losses = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method plot_losses: " + str(plot_losses))
            )
        )
    else:
        plot_losses = plot_losses
    # cf Methods.Output.OutLoss.__getitem__
    if isinstance(__getitem__, ImportError):
        __getitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method __getitem__: " + str(__getitem__))
            )
        )
    else:
        __getitem__ = __getitem__
    # cf Methods.Output.OutLoss.__len__
    if isinstance(__len__, ImportError):
        __len__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method __len__: " + str(__len__))
            )
        )
    else:
        __len__ = __len__
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        axes_dict=None,
        loss_dict=-1,
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
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "loss_dict" in list(init_dict.keys()):
                loss_dict = init_dict["loss_dict"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.axes_dict = axes_dict
        self.loss_dict = loss_dict
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLoss_str = ""
        if self.parent is None:
            OutLoss_str += "parent = None " + linesep
        else:
            OutLoss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutLoss_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        if len(self.loss_dict) == 0:
            OutLoss_str += "loss_dict = dict()" + linesep
        for key, obj in self.loss_dict.items():
            tmp = (
                self.loss_dict[key].__str__().replace(linesep, linesep + "\t") + linesep
            )
            OutLoss_str += "loss_dict[" + key + "] =" + tmp + linesep + linesep
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.loss_dict != self.loss_dict:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key],
                        name=name + ".axes_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.loss_dict is None and self.loss_dict is not None) or (
            other.loss_dict is not None and self.loss_dict is None
        ):
            diff_list.append(name + ".loss_dict None mismatch")
        elif self.loss_dict is None:
            pass
        elif len(other.loss_dict) != len(self.loss_dict):
            diff_list.append("len(" + name + "loss_dict)")
        else:
            for key in self.loss_dict:
                diff_list.extend(
                    self.loss_dict[key].compare(
                        other.loss_dict[key],
                        name=name + ".loss_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
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
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.loss_dict is not None:
            for key, value in self.loss_dict.items():
                S += getsizeof(value) + getsizeof(key)
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

        OutLoss_dict = dict()
        if self.axes_dict is None:
            OutLoss_dict["axes_dict"] = None
        else:
            OutLoss_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutLoss_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutLoss_dict["axes_dict"][key] = None
        if self.loss_dict is None:
            OutLoss_dict["loss_dict"] = None
        else:
            OutLoss_dict["loss_dict"] = dict()
            for key, obj in self.loss_dict.items():
                if obj is not None:
                    OutLoss_dict["loss_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutLoss_dict["loss_dict"][key] = None
        OutLoss_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.axes_dict is None:
            axes_dict_val = None
        else:
            axes_dict_val = dict()
            for key, obj in self.axes_dict.items():
                axes_dict_val[key] = obj.copy()
        if self.loss_dict is None:
            loss_dict_val = None
        else:
            loss_dict_val = dict()
            for key, obj in self.loss_dict.items():
                loss_dict_val[key] = obj.copy()
        logger_name_val = self.logger_name
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            axes_dict=axes_dict_val,
            loss_dict=loss_dict_val,
            logger_name=logger_name_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.axes_dict = None
        self.loss_dict = None
        self.logger_name = None

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
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
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc=u"""Dict containing axes data used for Magnetics

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_loss_dict(self):
        """getter of loss_dict"""
        if self._loss_dict is not None:
            for key, obj in self._loss_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._loss_dict

    def _set_loss_dict(self, value):
        """setter of loss_dict"""
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
                        "pyleecan.Classes", obj.get("__class__"), "loss_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("loss_dict", value, "{OutLossModel}")
        self._loss_dict = value

    loss_dict = property(
        fget=_get_loss_dict,
        fset=_set_loss_dict,
        doc=u"""Dict containing OutLossModel obects for each type of loss

        :Type: {OutLossModel}
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
