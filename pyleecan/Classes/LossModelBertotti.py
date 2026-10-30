# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Loss/LossModelBertotti.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Loss/LossModelBertotti
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
from .LossModel import LossModel

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Loss.LossModelBertotti.comp_coeff import comp_coeff
except ImportError as error:
    comp_coeff = error

try:
    from ..Methods.Loss.LossModelBertotti.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error

try:
    from ..Methods.Loss.LossModelBertotti.comp_loss_freq import comp_loss_freq
except ImportError as error:
    comp_loss_freq = error

try:
    from ..Methods.Loss.LossModelBertotti.comp_loss_time import comp_loss_time
except ImportError as error:
    comp_loss_time = error

try:
    from ..Methods.Loss.LossModelBertotti.plot_fitting import plot_fitting
except ImportError as error:
    plot_fitting = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LossModelBertotti(LossModel):
    """Bertotti Loss Model Class"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Loss.LossModelBertotti.comp_coeff
    if isinstance(comp_coeff, ImportError):
        comp_coeff = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_coeff: " + str(comp_coeff)
                )
            )
        )
    else:
        comp_coeff = comp_coeff
    # cf Methods.Loss.LossModelBertotti.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_loss: " + str(comp_loss)
                )
            )
        )
    else:
        comp_loss = comp_loss
    # cf Methods.Loss.LossModelBertotti.comp_loss_freq
    if isinstance(comp_loss_freq, ImportError):
        comp_loss_freq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_loss_freq: "
                    + str(comp_loss_freq)
                )
            )
        )
    else:
        comp_loss_freq = comp_loss_freq
    # cf Methods.Loss.LossModelBertotti.comp_loss_time
    if isinstance(comp_loss_time, ImportError):
        comp_loss_time = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_loss_time: "
                    + str(comp_loss_time)
                )
            )
        )
    else:
        comp_loss_time = comp_loss_time
    # cf Methods.Loss.LossModelBertotti.plot_fitting
    if isinstance(plot_fitting, ImportError):
        plot_fitting = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method plot_fitting: "
                    + str(plot_fitting)
                )
            )
        )
    else:
        plot_fitting = plot_fitting
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        k_hy=None,
        k_ed=None,
        k_ex=None,
        is_stacking_factor=False,
        alpha_B=None,
        name="",
        group="",
        coeff_dict=None,
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
            if "k_hy" in list(init_dict.keys()):
                k_hy = init_dict["k_hy"]
            if "k_ed" in list(init_dict.keys()):
                k_ed = init_dict["k_ed"]
            if "k_ex" in list(init_dict.keys()):
                k_ex = init_dict["k_ex"]
            if "is_stacking_factor" in list(init_dict.keys()):
                is_stacking_factor = init_dict["is_stacking_factor"]
            if "alpha_B" in list(init_dict.keys()):
                alpha_B = init_dict["alpha_B"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.k_hy = k_hy
        self.k_ed = k_ed
        self.k_ex = k_ex
        self.is_stacking_factor = is_stacking_factor
        self.alpha_B = alpha_B
        # Call LossModel init
        super(LossModelBertotti, self).__init__(
            name=name, group=group, coeff_dict=coeff_dict
        )
        # The class is frozen (in LossModel init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossModelBertotti_str = ""
        # Get the properties inherited from LossModel
        LossModelBertotti_str += super(LossModelBertotti, self).__str__()
        LossModelBertotti_str += "k_hy = " + str(self.k_hy) + linesep
        LossModelBertotti_str += "k_ed = " + str(self.k_ed) + linesep
        LossModelBertotti_str += "k_ex = " + str(self.k_ex) + linesep
        LossModelBertotti_str += (
            "is_stacking_factor = " + str(self.is_stacking_factor) + linesep
        )
        LossModelBertotti_str += "alpha_B = " + str(self.alpha_B) + linesep
        return LossModelBertotti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LossModel
        if not super(LossModelBertotti, self).__eq__(other):
            return False
        if other.k_hy != self.k_hy:
            return False
        if other.k_ed != self.k_ed:
            return False
        if other.k_ex != self.k_ex:
            return False
        if other.is_stacking_factor != self.is_stacking_factor:
            return False
        if other.alpha_B != self.alpha_B:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LossModel
        diff_list.extend(
            super(LossModelBertotti, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
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
            other._k_ex is not None
            and self._k_ex is not None
            and isnan(other._k_ex)
            and isnan(self._k_ex)
        ):
            pass
        elif other._k_ex != self._k_ex:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._k_ex) + ", other=" + str(other._k_ex) + ")"
                )
                diff_list.append(name + ".k_ex" + val_str)
            else:
                diff_list.append(name + ".k_ex")
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
            other._alpha_B is not None
            and self._alpha_B is not None
            and isnan(other._alpha_B)
            and isnan(self._alpha_B)
        ):
            pass
        elif other._alpha_B != self._alpha_B:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._alpha_B)
                    + ", other="
                    + str(other._alpha_B)
                    + ")"
                )
                diff_list.append(name + ".alpha_B" + val_str)
            else:
                diff_list.append(name + ".alpha_B")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LossModel
        S += super(LossModelBertotti, self).__sizeof__()
        S += getsizeof(self.k_hy)
        S += getsizeof(self.k_ed)
        S += getsizeof(self.k_ex)
        S += getsizeof(self.is_stacking_factor)
        S += getsizeof(self.alpha_B)
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

        # Get the properties inherited from LossModel
        LossModelBertotti_dict = super(LossModelBertotti, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LossModelBertotti_dict["k_hy"] = self.k_hy
        LossModelBertotti_dict["k_ed"] = self.k_ed
        LossModelBertotti_dict["k_ex"] = self.k_ex
        LossModelBertotti_dict["is_stacking_factor"] = self.is_stacking_factor
        LossModelBertotti_dict["alpha_B"] = self.alpha_B
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossModelBertotti_dict["__class__"] = "LossModelBertotti"
        return LossModelBertotti_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        k_hy_val = self.k_hy
        k_ed_val = self.k_ed
        k_ex_val = self.k_ex
        is_stacking_factor_val = self.is_stacking_factor
        alpha_B_val = self.alpha_B
        name_val = self.name
        group_val = self.group
        if self.coeff_dict is None:
            coeff_dict_val = None
        else:
            coeff_dict_val = self.coeff_dict.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            k_hy=k_hy_val,
            k_ed=k_ed_val,
            k_ex=k_ex_val,
            is_stacking_factor=is_stacking_factor_val,
            alpha_B=alpha_B_val,
            name=name_val,
            group=group_val,
            coeff_dict=coeff_dict_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_hy = None
        self.k_ed = None
        self.k_ex = None
        self.is_stacking_factor = None
        self.alpha_B = None
        # Set to None the properties inherited from LossModel
        super(LossModelBertotti, self)._set_None()

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
        doc="""Hysteresis loss coefficient

        :Type: float
        """,
    )

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
        doc="""Eddy current loss coefficient

        :Type: float
        """,
    )

    def _get_k_ex(self):
        """getter of k_ex"""
        return self._k_ex

    def _set_k_ex(self, value):
        """setter of k_ex"""
        check_var("k_ex", value, "float")
        self._k_ex = value

    k_ex = property(
        fget=_get_k_ex,
        fset=_set_k_ex,
        doc="""Excess loss coefficient

        :Type: float
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

    def _get_alpha_B(self):
        """getter of alpha_B"""
        return self._alpha_B

    def _set_alpha_B(self, value):
        """setter of alpha_B"""
        check_var("alpha_B", value, "float")
        self._alpha_B = value

    alpha_B = property(
        fget=_get_alpha_B,
        fset=_set_alpha_B,
        doc="""Hysteresis loss exponent

        :Type: float
        """,
    )
