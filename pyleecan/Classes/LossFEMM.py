# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LossFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LossFEMM
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
from .Loss import Loss

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LossFEMM.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.LossFEMM.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_core import (
        comp_loss_density_core,
    )
except ImportError as error:
    comp_loss_density_core = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_joule import (
        comp_loss_density_joule,
    )
except ImportError as error:
    comp_loss_density_joule = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_magnet import (
        comp_loss_density_magnet,
    )
except ImportError as error:
    comp_loss_density_magnet = error


from ._check import InitUnKnowClassError


class LossFEMM(Loss):
    """Loss module dedicated to FEMM developed in https://www.femm.info/wiki/SPMLoss"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.LossFEMM.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.LossFEMM.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Simulation.LossFEMM.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method comp_loss: " + str(comp_loss))
            )
        )
    else:
        comp_loss = comp_loss
    # cf Methods.Simulation.LossFEMM.comp_loss_density_core
    if isinstance(comp_loss_density_core, ImportError):
        comp_loss_density_core = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_core: "
                    + str(comp_loss_density_core)
                )
            )
        )
    else:
        comp_loss_density_core = comp_loss_density_core
    # cf Methods.Simulation.LossFEMM.comp_loss_density_joule
    if isinstance(comp_loss_density_joule, ImportError):
        comp_loss_density_joule = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_joule: "
                    + str(comp_loss_density_joule)
                )
            )
        )
    else:
        comp_loss_density_joule = comp_loss_density_joule
    # cf Methods.Simulation.LossFEMM.comp_loss_density_magnet
    if isinstance(comp_loss_density_magnet, ImportError):
        comp_loss_density_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_magnet: "
                    + str(comp_loss_density_magnet)
                )
            )
        )
    else:
        comp_loss_density_magnet = comp_loss_density_magnet
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_get_meshsolution=False,
        Tsta=20,
        Trot=20,
        type_skin_effect=1,
        Loss_model_dict=None,
        Cp=None,
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
            if "is_get_meshsolution" in list(init_dict.keys()):
                is_get_meshsolution = init_dict["is_get_meshsolution"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "Loss_model_dict" in list(init_dict.keys()):
                Loss_model_dict = init_dict["Loss_model_dict"]
            if "Cp" in list(init_dict.keys()):
                Cp = init_dict["Cp"]
            if "model_index" in list(init_dict.keys()):
                model_index = init_dict["model_index"]
            if "model_list" in list(init_dict.keys()):
                model_list = init_dict["model_list"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.is_get_meshsolution = is_get_meshsolution
        self.Tsta = Tsta
        self.Trot = Trot
        self.type_skin_effect = type_skin_effect
        self.Loss_model_dict = Loss_model_dict
        self.Cp = Cp
        # Call Loss init
        super(LossFEMM, self).__init__(
            model_index=model_index, model_list=model_list, logger_name=logger_name
        )
        # The class is frozen (in Loss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossFEMM_str = ""
        # Get the properties inherited from Loss
        LossFEMM_str += super(LossFEMM, self).__str__()
        LossFEMM_str += (
            "is_get_meshsolution = " + str(self.is_get_meshsolution) + linesep
        )
        LossFEMM_str += "Tsta = " + str(self.Tsta) + linesep
        LossFEMM_str += "Trot = " + str(self.Trot) + linesep
        LossFEMM_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        if len(self.Loss_model_dict) == 0:
            LossFEMM_str += "Loss_model_dict = dict()" + linesep
        for key, obj in self.Loss_model_dict.items():
            tmp = (
                self.Loss_model_dict[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            LossFEMM_str += "Loss_model_dict[" + key + "] =" + tmp + linesep + linesep
        LossFEMM_str += "Cp = " + str(self.Cp) + linesep
        return LossFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(LossFEMM, self).__eq__(other):
            return False
        if other.is_get_meshsolution != self.is_get_meshsolution:
            return False
        if other.Tsta != self.Tsta:
            return False
        if other.Trot != self.Trot:
            return False
        if other.type_skin_effect != self.type_skin_effect:
            return False
        if other.Loss_model_dict != self.Loss_model_dict:
            return False
        if other.Cp != self.Cp:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Loss
        diff_list.extend(super(LossFEMM, self).compare(other, name=name))
        if other._is_get_meshsolution != self._is_get_meshsolution:
            diff_list.append(name + ".is_get_meshsolution")
        if other._Tsta != self._Tsta:
            diff_list.append(name + ".Tsta")
        if other._Trot != self._Trot:
            diff_list.append(name + ".Trot")
        if other._type_skin_effect != self._type_skin_effect:
            diff_list.append(name + ".type_skin_effect")
        if (other.Loss_model_dict is None and self.Loss_model_dict is not None) or (
            other.Loss_model_dict is not None and self.Loss_model_dict is None
        ):
            diff_list.append(name + ".Loss_model_dict None mismatch")
        elif self.Loss_model_dict is None:
            pass
        elif len(other.Loss_model_dict) != len(self.Loss_model_dict):
            diff_list.append("len(" + name + "Loss_model_dict)")
        else:
            for key in self.Loss_model_dict:
                diff_list.extend(
                    self.Loss_model_dict[key].compare(
                        other.Loss_model_dict[key], name=name + ".Loss_model_dict"
                    )
                )
        if other._Cp != self._Cp:
            diff_list.append(name + ".Cp")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Loss
        S += super(LossFEMM, self).__sizeof__()
        S += getsizeof(self.is_get_meshsolution)
        S += getsizeof(self.Tsta)
        S += getsizeof(self.Trot)
        S += getsizeof(self.type_skin_effect)
        if self.Loss_model_dict is not None:
            for key, value in self.Loss_model_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Cp)
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

        # Get the properties inherited from Loss
        LossFEMM_dict = super(LossFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LossFEMM_dict["is_get_meshsolution"] = self.is_get_meshsolution
        LossFEMM_dict["Tsta"] = self.Tsta
        LossFEMM_dict["Trot"] = self.Trot
        LossFEMM_dict["type_skin_effect"] = self.type_skin_effect
        if self.Loss_model_dict is None:
            LossFEMM_dict["Loss_model_dict"] = None
        else:
            LossFEMM_dict["Loss_model_dict"] = dict()
            for key, obj in self.Loss_model_dict.items():
                if obj is not None:
                    LossFEMM_dict["Loss_model_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    LossFEMM_dict["Loss_model_dict"][key] = None
        LossFEMM_dict["Cp"] = self.Cp
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossFEMM_dict["__class__"] = "LossFEMM"
        return LossFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_get_meshsolution = None
        self.Tsta = None
        self.Trot = None
        self.type_skin_effect = None
        self.Loss_model_dict = None
        self.Cp = None
        # Set to None the properties inherited from Loss
        super(LossFEMM, self)._set_None()

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

    def _get_type_skin_effect(self):
        """getter of type_skin_effect"""
        return self._type_skin_effect

    def _set_type_skin_effect(self, value):
        """setter of type_skin_effect"""
        check_var("type_skin_effect", value, "int")
        self._type_skin_effect = value

    type_skin_effect = property(
        fget=_get_type_skin_effect,
        fset=_set_type_skin_effect,
        doc=u"""Skin effect for resistance calculation

        :Type: int
        """,
    )

    def _get_Loss_model_dict(self):
        """getter of Loss_model_dict"""
        if self._Loss_model_dict is not None:
            for key, obj in self._Loss_model_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._Loss_model_dict

    def _set_Loss_model_dict(self, value):
        """setter of Loss_model_dict"""
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
                        "pyleecan.Classes", obj.get("__class__"), "Loss_model_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("Loss_model_dict", value, "{LossModel}")
        self._Loss_model_dict = value

    Loss_model_dict = property(
        fget=_get_Loss_model_dict,
        fset=_set_Loss_model_dict,
        doc=u"""Dict of loss model whose key is a lamination and value is the associated loss model

        :Type: {LossModel}
        """,
    )

    def _get_Cp(self):
        """getter of Cp"""
        return self._Cp

    def _set_Cp(self, value):
        """setter of Cp"""
        check_var("Cp", value, "float")
        self._Cp = value

    Cp = property(
        fget=_get_Cp,
        fset=_set_Cp,
        doc=u"""proximity loss coefficients

        :Type: float
        """,
    )
