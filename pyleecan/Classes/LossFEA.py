# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Loss/LossFEA.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Loss/LossFEA
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
    from ..Methods.Loss.LossFEA.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Loss.LossFEA.run import run
except ImportError as error:
    run = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LossFEA(Loss):
    """Simplified loss module, with predefined loss models for a quick setup"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Loss.LossFEA.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEA method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Loss.LossFEA.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEA method run: " + str(run))
            )
        )
    else:
        run = run
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        k_ed_enforced=None,
        k_hy_enforced=None,
        k_p_enforced=None,
        type_skin_effect=1,
        type_loss_model_core="Steinmetz",
        is_stacking_factor=True,
        k_ex_enforced=None,
        alpha_B_enforced=None,
        is_calc_windage_loss=False,
        alpha_f_enforced=None,
        is_dynamic=False,
        logger_name="Pyleecan.Loss",
        model_dict=None,
        Tsta=20,
        Trot=20,
        is_get_meshsolution=False,
        is_clean_magmesh=False,
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
            if "k_ed_enforced" in list(init_dict.keys()):
                k_ed_enforced = init_dict["k_ed_enforced"]
            if "k_hy_enforced" in list(init_dict.keys()):
                k_hy_enforced = init_dict["k_hy_enforced"]
            if "k_p_enforced" in list(init_dict.keys()):
                k_p_enforced = init_dict["k_p_enforced"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "type_loss_model_core" in list(init_dict.keys()):
                type_loss_model_core = init_dict["type_loss_model_core"]
            if "is_stacking_factor" in list(init_dict.keys()):
                is_stacking_factor = init_dict["is_stacking_factor"]
            if "k_ex_enforced" in list(init_dict.keys()):
                k_ex_enforced = init_dict["k_ex_enforced"]
            if "alpha_B_enforced" in list(init_dict.keys()):
                alpha_B_enforced = init_dict["alpha_B_enforced"]
            if "is_calc_windage_loss" in list(init_dict.keys()):
                is_calc_windage_loss = init_dict["is_calc_windage_loss"]
            if "alpha_f_enforced" in list(init_dict.keys()):
                alpha_f_enforced = init_dict["alpha_f_enforced"]
            if "is_dynamic" in list(init_dict.keys()):
                is_dynamic = init_dict["is_dynamic"]
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
            if "is_clean_magmesh" in list(init_dict.keys()):
                is_clean_magmesh = init_dict["is_clean_magmesh"]
        # Set the properties (value check and convertion are done in setter)
        self.k_ed_enforced = k_ed_enforced
        self.k_hy_enforced = k_hy_enforced
        self.k_p_enforced = k_p_enforced
        self.type_skin_effect = type_skin_effect
        self.type_loss_model_core = type_loss_model_core
        self.is_stacking_factor = is_stacking_factor
        self.k_ex_enforced = k_ex_enforced
        self.alpha_B_enforced = alpha_B_enforced
        self.is_calc_windage_loss = is_calc_windage_loss
        self.alpha_f_enforced = alpha_f_enforced
        self.is_dynamic = is_dynamic
        # Call Loss init
        super(LossFEA, self).__init__(
            logger_name=logger_name,
            model_dict=model_dict,
            Tsta=Tsta,
            Trot=Trot,
            is_get_meshsolution=is_get_meshsolution,
            is_clean_magmesh=is_clean_magmesh,
        )
        # The class is frozen (in Loss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossFEA_str = ""
        # Get the properties inherited from Loss
        LossFEA_str += super(LossFEA, self).__str__()
        LossFEA_str += "k_ed_enforced = " + str(self.k_ed_enforced) + linesep
        LossFEA_str += "k_hy_enforced = " + str(self.k_hy_enforced) + linesep
        LossFEA_str += "k_p_enforced = " + str(self.k_p_enforced) + linesep
        LossFEA_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        LossFEA_str += (
            'type_loss_model_core = "' + str(self.type_loss_model_core) + '"' + linesep
        )
        LossFEA_str += "is_stacking_factor = " + str(self.is_stacking_factor) + linesep
        LossFEA_str += "k_ex_enforced = " + str(self.k_ex_enforced) + linesep
        LossFEA_str += "alpha_B_enforced = " + str(self.alpha_B_enforced) + linesep
        LossFEA_str += (
            "is_calc_windage_loss = " + str(self.is_calc_windage_loss) + linesep
        )
        LossFEA_str += "alpha_f_enforced = " + str(self.alpha_f_enforced) + linesep
        LossFEA_str += "is_dynamic = " + str(self.is_dynamic) + linesep
        return LossFEA_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(LossFEA, self).__eq__(other):
            return False
        if other.k_ed_enforced != self.k_ed_enforced:
            return False
        if other.k_hy_enforced != self.k_hy_enforced:
            return False
        if other.k_p_enforced != self.k_p_enforced:
            return False
        if other.type_skin_effect != self.type_skin_effect:
            return False
        if other.type_loss_model_core != self.type_loss_model_core:
            return False
        if other.is_stacking_factor != self.is_stacking_factor:
            return False
        if other.k_ex_enforced != self.k_ex_enforced:
            return False
        if other.alpha_B_enforced != self.alpha_B_enforced:
            return False
        if other.is_calc_windage_loss != self.is_calc_windage_loss:
            return False
        if other.alpha_f_enforced != self.alpha_f_enforced:
            return False
        if other.is_dynamic != self.is_dynamic:
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
            super(LossFEA, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._k_ed_enforced is not None
            and self._k_ed_enforced is not None
            and isnan(other._k_ed_enforced)
            and isnan(self._k_ed_enforced)
        ):
            pass
        elif other._k_ed_enforced != self._k_ed_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._k_ed_enforced)
                    + ", other="
                    + str(other._k_ed_enforced)
                    + ")"
                )
                diff_list.append(name + ".k_ed_enforced" + val_str)
            else:
                diff_list.append(name + ".k_ed_enforced")
        if (
            other._k_hy_enforced is not None
            and self._k_hy_enforced is not None
            and isnan(other._k_hy_enforced)
            and isnan(self._k_hy_enforced)
        ):
            pass
        elif other._k_hy_enforced != self._k_hy_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._k_hy_enforced)
                    + ", other="
                    + str(other._k_hy_enforced)
                    + ")"
                )
                diff_list.append(name + ".k_hy_enforced" + val_str)
            else:
                diff_list.append(name + ".k_hy_enforced")
        if (
            other._k_p_enforced is not None
            and self._k_p_enforced is not None
            and isnan(other._k_p_enforced)
            and isnan(self._k_p_enforced)
        ):
            pass
        elif other._k_p_enforced != self._k_p_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._k_p_enforced)
                    + ", other="
                    + str(other._k_p_enforced)
                    + ")"
                )
                diff_list.append(name + ".k_p_enforced" + val_str)
            else:
                diff_list.append(name + ".k_p_enforced")
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
        if other._type_loss_model_core != self._type_loss_model_core:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_loss_model_core)
                    + ", other="
                    + str(other._type_loss_model_core)
                    + ")"
                )
                diff_list.append(name + ".type_loss_model_core" + val_str)
            else:
                diff_list.append(name + ".type_loss_model_core")
        if other._is_stacking_factor != self._is_stacking_factor:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_stacking_factor)
                    + ", other="
                    + str(other._is_stacking_factor)
                    + ")"
                )
                diff_list.append(name + ".is_stacking_factor" + val_str)
            else:
                diff_list.append(name + ".is_stacking_factor")
        if (
            other._k_ex_enforced is not None
            and self._k_ex_enforced is not None
            and isnan(other._k_ex_enforced)
            and isnan(self._k_ex_enforced)
        ):
            pass
        elif other._k_ex_enforced != self._k_ex_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._k_ex_enforced)
                    + ", other="
                    + str(other._k_ex_enforced)
                    + ")"
                )
                diff_list.append(name + ".k_ex_enforced" + val_str)
            else:
                diff_list.append(name + ".k_ex_enforced")
        if (
            other._alpha_B_enforced is not None
            and self._alpha_B_enforced is not None
            and isnan(other._alpha_B_enforced)
            and isnan(self._alpha_B_enforced)
        ):
            pass
        elif other._alpha_B_enforced != self._alpha_B_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._alpha_B_enforced)
                    + ", other="
                    + str(other._alpha_B_enforced)
                    + ")"
                )
                diff_list.append(name + ".alpha_B_enforced" + val_str)
            else:
                diff_list.append(name + ".alpha_B_enforced")
        if other._is_calc_windage_loss != self._is_calc_windage_loss:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_calc_windage_loss)
                    + ", other="
                    + str(other._is_calc_windage_loss)
                    + ")"
                )
                diff_list.append(name + ".is_calc_windage_loss" + val_str)
            else:
                diff_list.append(name + ".is_calc_windage_loss")
        if (
            other._alpha_f_enforced is not None
            and self._alpha_f_enforced is not None
            and isnan(other._alpha_f_enforced)
            and isnan(self._alpha_f_enforced)
        ):
            pass
        elif other._alpha_f_enforced != self._alpha_f_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._alpha_f_enforced)
                    + ", other="
                    + str(other._alpha_f_enforced)
                    + ")"
                )
                diff_list.append(name + ".alpha_f_enforced" + val_str)
            else:
                diff_list.append(name + ".alpha_f_enforced")
        if other._is_dynamic != self._is_dynamic:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_dynamic)
                    + ", other="
                    + str(other._is_dynamic)
                    + ")"
                )
                diff_list.append(name + ".is_dynamic" + val_str)
            else:
                diff_list.append(name + ".is_dynamic")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Loss
        S += super(LossFEA, self).__sizeof__()
        S += getsizeof(self.k_ed_enforced)
        S += getsizeof(self.k_hy_enforced)
        S += getsizeof(self.k_p_enforced)
        S += getsizeof(self.type_skin_effect)
        S += getsizeof(self.type_loss_model_core)
        S += getsizeof(self.is_stacking_factor)
        S += getsizeof(self.k_ex_enforced)
        S += getsizeof(self.alpha_B_enforced)
        S += getsizeof(self.is_calc_windage_loss)
        S += getsizeof(self.alpha_f_enforced)
        S += getsizeof(self.is_dynamic)
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
        LossFEA_dict = super(LossFEA, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LossFEA_dict["k_ed_enforced"] = self.k_ed_enforced
        LossFEA_dict["k_hy_enforced"] = self.k_hy_enforced
        LossFEA_dict["k_p_enforced"] = self.k_p_enforced
        LossFEA_dict["type_skin_effect"] = self.type_skin_effect
        LossFEA_dict["type_loss_model_core"] = self.type_loss_model_core
        LossFEA_dict["is_stacking_factor"] = self.is_stacking_factor
        LossFEA_dict["k_ex_enforced"] = self.k_ex_enforced
        LossFEA_dict["alpha_B_enforced"] = self.alpha_B_enforced
        LossFEA_dict["is_calc_windage_loss"] = self.is_calc_windage_loss
        LossFEA_dict["alpha_f_enforced"] = self.alpha_f_enforced
        LossFEA_dict["is_dynamic"] = self.is_dynamic
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossFEA_dict["__class__"] = "LossFEA"
        return LossFEA_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        k_ed_enforced_val = self.k_ed_enforced
        k_hy_enforced_val = self.k_hy_enforced
        k_p_enforced_val = self.k_p_enforced
        type_skin_effect_val = self.type_skin_effect
        type_loss_model_core_val = self.type_loss_model_core
        is_stacking_factor_val = self.is_stacking_factor
        k_ex_enforced_val = self.k_ex_enforced
        alpha_B_enforced_val = self.alpha_B_enforced
        is_calc_windage_loss_val = self.is_calc_windage_loss
        alpha_f_enforced_val = self.alpha_f_enforced
        is_dynamic_val = self.is_dynamic
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
        is_clean_magmesh_val = self.is_clean_magmesh
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            k_ed_enforced=k_ed_enforced_val,
            k_hy_enforced=k_hy_enforced_val,
            k_p_enforced=k_p_enforced_val,
            type_skin_effect=type_skin_effect_val,
            type_loss_model_core=type_loss_model_core_val,
            is_stacking_factor=is_stacking_factor_val,
            k_ex_enforced=k_ex_enforced_val,
            alpha_B_enforced=alpha_B_enforced_val,
            is_calc_windage_loss=is_calc_windage_loss_val,
            alpha_f_enforced=alpha_f_enforced_val,
            is_dynamic=is_dynamic_val,
            logger_name=logger_name_val,
            model_dict=model_dict_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            is_get_meshsolution=is_get_meshsolution_val,
            is_clean_magmesh=is_clean_magmesh_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_ed_enforced = None
        self.k_hy_enforced = None
        self.k_p_enforced = None
        self.type_skin_effect = None
        self.type_loss_model_core = None
        self.is_stacking_factor = None
        self.k_ex_enforced = None
        self.alpha_B_enforced = None
        self.is_calc_windage_loss = None
        self.alpha_f_enforced = None
        self.is_dynamic = None
        # Set to None the properties inherited from Loss
        super(LossFEA, self)._set_None()

    def _get_k_ed_enforced(self):
        """getter of k_ed_enforced"""
        return self._k_ed_enforced

    def _set_k_ed_enforced(self, value):
        """setter of k_ed_enforced"""
        check_var("k_ed_enforced", value, "float")
        self._k_ed_enforced = value

    k_ed_enforced = property(
        fget=_get_k_ed_enforced,
        fset=_set_k_ed_enforced,
        doc="""User-defined eddy-current loss coefficient to enforce in Bertotti and Steinmetz iron loss model

        :Type: float
        """,
    )

    def _get_k_hy_enforced(self):
        """getter of k_hy_enforced"""
        return self._k_hy_enforced

    def _set_k_hy_enforced(self, value):
        """setter of k_hy_enforced"""
        check_var("k_hy_enforced", value, "float")
        self._k_hy_enforced = value

    k_hy_enforced = property(
        fget=_get_k_hy_enforced,
        fset=_set_k_hy_enforced,
        doc="""User-defined hysteresis loss coefficient to enforce in Bertotti and Steinmetz iron loss model

        :Type: float
        """,
    )

    def _get_k_p_enforced(self):
        """getter of k_p_enforced"""
        return self._k_p_enforced

    def _set_k_p_enforced(self, value):
        """setter of k_p_enforced"""
        check_var("k_p_enforced", value, "float")
        self._k_p_enforced = value

    k_p_enforced = property(
        fget=_get_k_p_enforced,
        fset=_set_k_p_enforced,
        doc="""User-defined proximity loss coefficient to enforce in proximity loss model

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
        doc="""Skin effect for resistance calculation (0 to ignore skin effect, 1 to consider it)

        :Type: int
        """,
    )

    def _get_type_loss_model_core(self):
        """getter of type_loss_model_core"""
        return self._type_loss_model_core

    def _set_type_loss_model_core(self, value):
        """setter of type_loss_model_core"""
        check_var("type_loss_model_core", value, "str")
        self._type_loss_model_core = value

    type_loss_model_core = property(
        fget=_get_type_loss_model_core,
        fset=_set_type_loss_model_core,
        doc="""Loss model for iron cores : "Bertotti" or "Steinmetz"

        :Type: str
        """,
    )

    def _get_is_stacking_factor(self):
        """getter of is_stacking_factor"""
        return self._is_stacking_factor

    def _set_is_stacking_factor(self, value):
        """setter of is_stacking_factor"""
        check_var("is_stacking_factor", value, "bool")
        self._is_stacking_factor = value

    is_stacking_factor = property(
        fget=_get_is_stacking_factor,
        fset=_set_is_stacking_factor,
        doc="""True to consider lamination stacking factor when calculating core losses

        :Type: bool
        """,
    )

    def _get_k_ex_enforced(self):
        """getter of k_ex_enforced"""
        return self._k_ex_enforced

    def _set_k_ex_enforced(self, value):
        """setter of k_ex_enforced"""
        check_var("k_ex_enforced", value, "float")
        self._k_ex_enforced = value

    k_ex_enforced = property(
        fget=_get_k_ex_enforced,
        fset=_set_k_ex_enforced,
        doc="""User-defined hysteresis loss coefficient to enforce in Bertotti iron loss model

        :Type: float
        """,
    )

    def _get_alpha_B_enforced(self):
        """getter of alpha_B_enforced"""
        return self._alpha_B_enforced

    def _set_alpha_B_enforced(self, value):
        """setter of alpha_B_enforced"""
        check_var("alpha_B_enforced", value, "float")
        self._alpha_B_enforced = value

    alpha_B_enforced = property(
        fget=_get_alpha_B_enforced,
        fset=_set_alpha_B_enforced,
        doc="""User-defined hysteresis loss exponent for flux density to enforce for in Bertotti and Steinmetz model

        :Type: float
        """,
    )

    def _get_is_calc_windage_loss(self):
        """getter of is_calc_windage_loss"""
        return self._is_calc_windage_loss

    def _set_is_calc_windage_loss(self, value):
        """setter of is_calc_windage_loss"""
        check_var("is_calc_windage_loss", value, "bool")
        self._is_calc_windage_loss = value

    is_calc_windage_loss = property(
        fget=_get_is_calc_windage_loss,
        fset=_set_is_calc_windage_loss,
        doc="""True to calculate windage losses in the airgap

        :Type: bool
        """,
    )

    def _get_alpha_f_enforced(self):
        """getter of alpha_f_enforced"""
        return self._alpha_f_enforced

    def _set_alpha_f_enforced(self, value):
        """setter of alpha_f_enforced"""
        check_var("alpha_f_enforced", value, "float")
        self._alpha_f_enforced = value

    alpha_f_enforced = property(
        fget=_get_alpha_f_enforced,
        fset=_set_alpha_f_enforced,
        doc="""User-defined hysteresis loss exponent for frequency to enforce for in Steinmetz model

        :Type: float
        """,
    )

    def _get_is_dynamic(self):
        """getter of is_dynamic"""
        return self._is_dynamic

    def _set_is_dynamic(self, value):
        """setter of is_dynamic"""
        check_var("is_dynamic", value, "bool")
        self._is_dynamic = value

    is_dynamic = property(
        fget=_get_is_dynamic,
        fset=_set_is_dynamic,
        doc="""False to calculate average losses in frequency domain, True to calculate dynamic losses over time (not validated yet)

        :Type: bool
        """,
    )
