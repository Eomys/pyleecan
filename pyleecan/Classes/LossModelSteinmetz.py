# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LossModelSteinmetz.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LossModelSteinmetz
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
    from ..Methods.Simulation.LossModelSteinmetz.comp_coeff import comp_coeff
except ImportError as error:
    comp_coeff = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LossModelSteinmetz(LossModel):
    """Steinmetz Loss Model Class"""

    VERSION = 1

    # cf Methods.Simulation.LossModelSteinmetz.comp_coeff
    if isinstance(comp_coeff, ImportError):
        comp_coeff = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelSteinmetz method comp_coeff: " + str(comp_coeff)
                )
            )
        )
    else:
        comp_coeff = comp_coeff
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        k_hy=None,
        k_ed=None,
        alpha_f=None,
        alpha_B=None,
        name="",
        is_show_fig=False,
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
            if "alpha_f" in list(init_dict.keys()):
                alpha_f = init_dict["alpha_f"]
            if "alpha_B" in list(init_dict.keys()):
                alpha_B = init_dict["alpha_B"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "is_show_fig" in list(init_dict.keys()):
                is_show_fig = init_dict["is_show_fig"]
        # Set the properties (value check and convertion are done in setter)
        self.k_hy = k_hy
        self.k_ed = k_ed
        self.alpha_f = alpha_f
        self.alpha_B = alpha_B
        # Call LossModel init
        super(LossModelSteinmetz, self).__init__(name=name, is_show_fig=is_show_fig)
        # The class is frozen (in LossModel init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossModelSteinmetz_str = ""
        # Get the properties inherited from LossModel
        LossModelSteinmetz_str += super(LossModelSteinmetz, self).__str__()
        LossModelSteinmetz_str += "k_hy = " + str(self.k_hy) + linesep
        LossModelSteinmetz_str += "k_ed = " + str(self.k_ed) + linesep
        LossModelSteinmetz_str += "alpha_f = " + str(self.alpha_f) + linesep
        LossModelSteinmetz_str += "alpha_B = " + str(self.alpha_B) + linesep
        return LossModelSteinmetz_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LossModel
        if not super(LossModelSteinmetz, self).__eq__(other):
            return False
        if other.k_hy != self.k_hy:
            return False
        if other.k_ed != self.k_ed:
            return False
        if other.alpha_f != self.alpha_f:
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
            super(LossModelSteinmetz, self).compare(
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
            other._alpha_f is not None
            and self._alpha_f is not None
            and isnan(other._alpha_f)
            and isnan(self._alpha_f)
        ):
            pass
        elif other._alpha_f != self._alpha_f:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._alpha_f)
                    + ", other="
                    + str(other._alpha_f)
                    + ")"
                )
                diff_list.append(name + ".alpha_f" + val_str)
            else:
                diff_list.append(name + ".alpha_f")
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
        S += super(LossModelSteinmetz, self).__sizeof__()
        S += getsizeof(self.k_hy)
        S += getsizeof(self.k_ed)
        S += getsizeof(self.alpha_f)
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
        LossModelSteinmetz_dict = super(LossModelSteinmetz, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LossModelSteinmetz_dict["k_hy"] = self.k_hy
        LossModelSteinmetz_dict["k_ed"] = self.k_ed
        LossModelSteinmetz_dict["alpha_f"] = self.alpha_f
        LossModelSteinmetz_dict["alpha_B"] = self.alpha_B
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossModelSteinmetz_dict["__class__"] = "LossModelSteinmetz"
        return LossModelSteinmetz_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        k_hy_val = self.k_hy
        k_ed_val = self.k_ed
        alpha_f_val = self.alpha_f
        alpha_B_val = self.alpha_B
        name_val = self.name
        is_show_fig_val = self.is_show_fig
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            k_hy=k_hy_val,
            k_ed=k_ed_val,
            alpha_f=alpha_f_val,
            alpha_B=alpha_B_val,
            name=name_val,
            is_show_fig=is_show_fig_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_hy = None
        self.k_ed = None
        self.alpha_f = None
        self.alpha_B = None
        # Set to None the properties inherited from LossModel
        super(LossModelSteinmetz, self)._set_None()

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
        doc=u"""Hysteresis loss coefficient

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
        doc=u"""Eddy current loss coefficient

        :Type: float
        """,
    )

    def _get_alpha_f(self):
        """getter of alpha_f"""
        return self._alpha_f

    def _set_alpha_f(self, value):
        """setter of alpha_f"""
        check_var("alpha_f", value, "float")
        self._alpha_f = value

    alpha_f = property(
        fget=_get_alpha_f,
        fset=_set_alpha_f,
        doc=u"""Hysteresis loss power coefficient for the frequency

        :Type: float
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
        doc=u"""Hysteresis loss power coefficient for the flux density magnitude

        :Type: float
        """,
    )
