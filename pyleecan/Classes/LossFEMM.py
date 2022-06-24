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
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
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


from numpy import isnan
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
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Ce=None,
        Ch=None,
        Cp=None,
        type_skin_effect=1,
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
            if "Ce" in list(init_dict.keys()):
                Ce = init_dict["Ce"]
            if "Ch" in list(init_dict.keys()):
                Ch = init_dict["Ch"]
            if "Cp" in list(init_dict.keys()):
                Cp = init_dict["Cp"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
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
        self.Ce = Ce
        self.Ch = Ch
        self.Cp = Cp
        self.type_skin_effect = type_skin_effect
        # Call Loss init
        super(LossFEMM, self).__init__(
            logger_name=logger_name,
            model_dict=model_dict,
            Tsta=Tsta,
            Trot=Trot,
            is_get_meshsolution=is_get_meshsolution,
        )
        # The class is frozen (in Loss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossFEMM_str = ""
        # Get the properties inherited from Loss
        LossFEMM_str += super(LossFEMM, self).__str__()
        LossFEMM_str += "Ce = " + str(self.Ce) + linesep
        LossFEMM_str += "Ch = " + str(self.Ch) + linesep
        LossFEMM_str += "Cp = " + str(self.Cp) + linesep
        LossFEMM_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        return LossFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(LossFEMM, self).__eq__(other):
            return False
        if other.Ce != self.Ce:
            return False
        if other.Ch != self.Ch:
            return False
        if other.Cp != self.Cp:
            return False
        if other.type_skin_effect != self.type_skin_effect:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Loss
        diff_list.extend(
            super(LossFEMM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Ce is not None
            and self._Ce is not None
            and isnan(other._Ce)
            and isnan(self._Ce)
        ):
            pass
        elif other._Ce != self._Ce:
            if is_add_value:
                val_str = " (self=" + str(self._Ce) + ", other=" + str(other._Ce) + ")"
                diff_list.append(name + ".Ce" + val_str)
            else:
                diff_list.append(name + ".Ce")
        if (
            other._Ch is not None
            and self._Ch is not None
            and isnan(other._Ch)
            and isnan(self._Ch)
        ):
            pass
        elif other._Ch != self._Ch:
            if is_add_value:
                val_str = " (self=" + str(self._Ch) + ", other=" + str(other._Ch) + ")"
                diff_list.append(name + ".Ch" + val_str)
            else:
                diff_list.append(name + ".Ch")
        if (
            other._Cp is not None
            and self._Cp is not None
            and isnan(other._Cp)
            and isnan(self._Cp)
        ):
            pass
        elif other._Cp != self._Cp:
            if is_add_value:
                val_str = " (self=" + str(self._Cp) + ", other=" + str(other._Cp) + ")"
                diff_list.append(name + ".Cp" + val_str)
            else:
                diff_list.append(name + ".Cp")
        if other._type_skin_effect != self._type_skin_effect:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_skin_effect)
                    + ", other="
                    + str(other._type_skin_effect)
                    + ")"
                )
                diff_list.append(name + ".type_skin_effect" + val_str)
            else:
                diff_list.append(name + ".type_skin_effect")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Loss
        S += super(LossFEMM, self).__sizeof__()
        S += getsizeof(self.Ce)
        S += getsizeof(self.Ch)
        S += getsizeof(self.Cp)
        S += getsizeof(self.type_skin_effect)
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
        LossFEMM_dict["Ce"] = self.Ce
        LossFEMM_dict["Ch"] = self.Ch
        LossFEMM_dict["Cp"] = self.Cp
        LossFEMM_dict["type_skin_effect"] = self.type_skin_effect
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossFEMM_dict["__class__"] = "LossFEMM"
        return LossFEMM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        is_get_meshsolution_val = self.is_get_meshsolution
        Tsta_val = self.Tsta
        Trot_val = self.Trot
        type_skin_effect_val = self.type_skin_effect
        Cp_val = self.Cp
        if self.model_index is None:
            model_index_val = None
        else:
            model_index_val = self.model_index.copy()
        if self.model_list is None:
            model_list_val = None
        else:
            model_list_val = list()
            for obj in self.model_list:
                model_list_val.append(obj.copy())
        logger_name_val = self.logger_name
        if self.model_dict is None:
            model_dict_val = None
        else:
            model_dict_val = dict()
            for key, obj in self.model_dict.items():
                model_dict_val[key] = obj.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            is_get_meshsolution=is_get_meshsolution_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            type_skin_effect=type_skin_effect_val,
            Cp=Cp_val,
            model_index=model_index_val,
            model_list=model_list_val,
            logger_name=logger_name_val,
            model_dict=model_dict_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Ce = None
        self.Ch = None
        self.Cp = None
        self.type_skin_effect = None
        # Set to None the properties inherited from Loss
        super(LossFEMM, self)._set_None()

    def _get_Ce(self):
        """getter of Ce"""
        return self._Ce

    def _set_Ce(self, value):
        """setter of Ce"""
        check_var("Ce", value, "float")
        self._Ce = value

    Ce = property(
        fget=_get_Ce,
        fset=_set_Ce,
        doc=u"""eddy current loss coefficients [W/(m3*T2*Hz2)]

        :Type: float
        """,
    )

    def _get_Ch(self):
        """getter of Ch"""
        return self._Ch

    def _set_Ch(self, value):
        """setter of Ch"""
        check_var("Ch", value, "float")
        self._Ch = value

    Ch = property(
        fget=_get_Ch,
        fset=_set_Ch,
        doc=u"""hysteresis loss coefficients [W/(m3*T2*Hz)]

        :Type: float
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
        doc=u"""proximity loss coefficients [W/(m3*T2*Hz2)]

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
        doc=u"""Skin effect for resistance calculation [-]

        :Type: int
        """,
    )
