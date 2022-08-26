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


from numpy import isnan
from ._check import InitUnKnowClassError


class LossFEMM(Loss):
    """Simplified loss module, with predefined loss models for a quick setup"""

    VERSION = 1

    # cf Methods.Simulation.LossFEMM.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method run: " + str(run))
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
        k_ed=None,
        k_hy=None,
        h_p=None,
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
            if "k_ed" in list(init_dict.keys()):
                k_ed = init_dict["k_ed"]
            if "k_hy" in list(init_dict.keys()):
                k_hy = init_dict["k_hy"]
            if "h_p" in list(init_dict.keys()):
                h_p = init_dict["h_p"]
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
        self.k_ed = k_ed
        self.k_hy = k_hy
        self.h_p = h_p
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
        LossFEMM_str += "k_ed = " + str(self.k_ed) + linesep
        LossFEMM_str += "k_hy = " + str(self.k_hy) + linesep
        LossFEMM_str += "h_p = " + str(self.h_p) + linesep
        LossFEMM_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        return LossFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(LossFEMM, self).__eq__(other):
            return False
        if other.k_ed != self.k_ed:
            return False
        if other.k_hy != self.k_hy:
            return False
        if other.h_p != self.h_p:
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
            other._k_ed is not None
            and self._k_ed is not None
            and isnan(other._k_ed)
            and isnan(self._k_ed)
        ):
            pass
        elif other._k_ed != self._k_ed:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._k_ed) + ", other=" + str(other._k_ed) + ")"
                )
                diff_list.append(name + ".k_ed" + val_str)
            else:
                diff_list.append(name + ".k_ed")
        if (
            other._k_hy is not None
            and self._k_hy is not None
            and isnan(other._k_hy)
            and isnan(self._k_hy)
        ):
            pass
        elif other._k_hy != self._k_hy:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._k_hy) + ", other=" + str(other._k_hy) + ")"
                )
                diff_list.append(name + ".k_hy" + val_str)
            else:
                diff_list.append(name + ".k_hy")
        if (
            other._h_p is not None
            and self._h_p is not None
            and isnan(other._h_p)
            and isnan(self._h_p)
        ):
            pass
        elif other._h_p != self._h_p:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._h_p) + ", other=" + str(other._h_p) + ")"
                )
                diff_list.append(name + ".h_p" + val_str)
            else:
                diff_list.append(name + ".h_p")
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
        S += getsizeof(self.k_ed)
        S += getsizeof(self.k_hy)
        S += getsizeof(self.h_p)
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
        LossFEMM_dict["k_ed"] = self.k_ed
        LossFEMM_dict["k_hy"] = self.k_hy
        LossFEMM_dict["h_p"] = self.h_p
        LossFEMM_dict["type_skin_effect"] = self.type_skin_effect
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossFEMM_dict["__class__"] = "LossFEMM"
        return LossFEMM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        k_ed_val = self.k_ed
        k_hy_val = self.k_hy
        h_p_val = self.h_p
        type_skin_effect_val = self.type_skin_effect
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
            k_ed=k_ed_val,
            k_hy=k_hy_val,
            h_p=h_p_val,
            type_skin_effect=type_skin_effect_val,
            logger_name=logger_name_val,
            model_dict=model_dict_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            is_get_meshsolution=is_get_meshsolution_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_ed = None
        self.k_hy = None
        self.h_p = None
        self.type_skin_effect = None
        # Set to None the properties inherited from Loss
        super(LossFEMM, self)._set_None()

    def _get_k_ed(self):
        """getter of k_ed"""
        return self._k_ed

    def _set_k_ed(self, value):
        """setter of k_ed"""
        check_var("k_ed", value, "float")
        self._k_ed = value

    k_ed = property(
        fget=_get_k_ed,
        fset=_set_k_ed,
        doc=u"""eddy current loss coefficients [W/(m3*T2*Hz2)]

        :Type: float
        """,
    )

    def _get_k_hy(self):
        """getter of k_hy"""
        return self._k_hy

    def _set_k_hy(self, value):
        """setter of k_hy"""
        check_var("k_hy", value, "float")
        self._k_hy = value

    k_hy = property(
        fget=_get_k_hy,
        fset=_set_k_hy,
        doc=u"""hysteresis loss coefficients [W/(m3*T2*Hz)]

        :Type: float
        """,
    )

    def _get_h_p(self):
        """getter of h_p"""
        return self._h_p

    def _set_h_p(self, value):
        """setter of h_p"""
        check_var("h_p", value, "float")
        self._h_p = value

    h_p = property(
        fget=_get_h_p,
        fset=_set_h_p,
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
