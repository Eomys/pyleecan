# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/BoreSinePole.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/BoreSinePole
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
from .Bore import Bore

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.BoreSinePole.get_bore_line import get_bore_line
except ImportError as error:
    get_bore_line = error

try:
    from ..Methods.Machine.BoreSinePole.get_pole_shape import get_pole_shape
except ImportError as error:
    get_pole_shape = error

try:
    from ..Methods.Machine.BoreSinePole.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error

try:
    from ..Methods.Machine.BoreSinePole.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error


from numpy import isnan
from ._check import InitUnKnowClassError


class BoreSinePole(Bore):
    """Class for Sine Field Pole Bore shape adapted from 'Muller, Germar, et al. Berechnung Elektrischer Maschinen. Hoboken, NJ, United States, Wiley, 2008.'"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.BoreSinePole.get_bore_line
    if isinstance(get_bore_line, ImportError):
        get_bore_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreSinePole method get_bore_line: " + str(get_bore_line)
                )
            )
        )
    else:
        get_bore_line = get_bore_line
    # cf Methods.Machine.BoreSinePole.get_pole_shape
    if isinstance(get_pole_shape, ImportError):
        get_pole_shape = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreSinePole method get_pole_shape: "
                    + str(get_pole_shape)
                )
            )
        )
    else:
        get_pole_shape = get_pole_shape
    # cf Methods.Machine.BoreSinePole.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreSinePole method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # cf Methods.Machine.BoreSinePole.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreSinePole method plot_schematics: "
                    + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        N=8,
        k=1,
        delta_d=0.001,
        delta_q=None,
        W0=None,
        alpha=0,
        type_merge_slot=1,
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
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "delta_d" in list(init_dict.keys()):
                delta_d = init_dict["delta_d"]
            if "delta_q" in list(init_dict.keys()):
                delta_q = init_dict["delta_q"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
            if "type_merge_slot" in list(init_dict.keys()):
                type_merge_slot = init_dict["type_merge_slot"]
        # Set the properties (value check and convertion are done in setter)
        self.N = N
        self.k = k
        self.delta_d = delta_d
        self.delta_q = delta_q
        self.W0 = W0
        self.alpha = alpha
        # Call Bore init
        super(BoreSinePole, self).__init__(type_merge_slot=type_merge_slot)
        # The class is frozen (in Bore init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        BoreSinePole_str = ""
        # Get the properties inherited from Bore
        BoreSinePole_str += super(BoreSinePole, self).__str__()
        BoreSinePole_str += "N = " + str(self.N) + linesep
        BoreSinePole_str += "k = " + str(self.k) + linesep
        BoreSinePole_str += "delta_d = " + str(self.delta_d) + linesep
        BoreSinePole_str += "delta_q = " + str(self.delta_q) + linesep
        BoreSinePole_str += "W0 = " + str(self.W0) + linesep
        BoreSinePole_str += "alpha = " + str(self.alpha) + linesep
        return BoreSinePole_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Bore
        if not super(BoreSinePole, self).__eq__(other):
            return False
        if other.N != self.N:
            return False
        if other.k != self.k:
            return False
        if other.delta_d != self.delta_d:
            return False
        if other.delta_q != self.delta_q:
            return False
        if other.W0 != self.W0:
            return False
        if other.alpha != self.alpha:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Bore
        diff_list.extend(
            super(BoreSinePole, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._N != self._N:
            if is_add_value:
                val_str = " (self=" + str(self._N) + ", other=" + str(other._N) + ")"
                diff_list.append(name + ".N" + val_str)
            else:
                diff_list.append(name + ".N")
        if (
            other._k is not None
            and self._k is not None
            and isnan(other._k)
            and isnan(self._k)
        ):
            pass
        elif other._k != self._k:
            if is_add_value:
                val_str = " (self=" + str(self._k) + ", other=" + str(other._k) + ")"
                diff_list.append(name + ".k" + val_str)
            else:
                diff_list.append(name + ".k")
        if (
            other._delta_d is not None
            and self._delta_d is not None
            and isnan(other._delta_d)
            and isnan(self._delta_d)
        ):
            pass
        elif other._delta_d != self._delta_d:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._delta_d)
                    + ", other="
                    + str(other._delta_d)
                    + ")"
                )
                diff_list.append(name + ".delta_d" + val_str)
            else:
                diff_list.append(name + ".delta_d")
        if (
            other._delta_q is not None
            and self._delta_q is not None
            and isnan(other._delta_q)
            and isnan(self._delta_q)
        ):
            pass
        elif other._delta_q != self._delta_q:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._delta_q)
                    + ", other="
                    + str(other._delta_q)
                    + ")"
                )
                diff_list.append(name + ".delta_q" + val_str)
            else:
                diff_list.append(name + ".delta_q")
        if (
            other._W0 is not None
            and self._W0 is not None
            and isnan(other._W0)
            and isnan(self._W0)
        ):
            pass
        elif other._W0 != self._W0:
            if is_add_value:
                val_str = " (self=" + str(self._W0) + ", other=" + str(other._W0) + ")"
                diff_list.append(name + ".W0" + val_str)
            else:
                diff_list.append(name + ".W0")
        if (
            other._alpha is not None
            and self._alpha is not None
            and isnan(other._alpha)
            and isnan(self._alpha)
        ):
            pass
        elif other._alpha != self._alpha:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._alpha) + ", other=" + str(other._alpha) + ")"
                )
                diff_list.append(name + ".alpha" + val_str)
            else:
                diff_list.append(name + ".alpha")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Bore
        S += super(BoreSinePole, self).__sizeof__()
        S += getsizeof(self.N)
        S += getsizeof(self.k)
        S += getsizeof(self.delta_d)
        S += getsizeof(self.delta_q)
        S += getsizeof(self.W0)
        S += getsizeof(self.alpha)
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

        # Get the properties inherited from Bore
        BoreSinePole_dict = super(BoreSinePole, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        BoreSinePole_dict["N"] = self.N
        BoreSinePole_dict["k"] = self.k
        BoreSinePole_dict["delta_d"] = self.delta_d
        BoreSinePole_dict["delta_q"] = self.delta_q
        BoreSinePole_dict["W0"] = self.W0
        BoreSinePole_dict["alpha"] = self.alpha
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        BoreSinePole_dict["__class__"] = "BoreSinePole"
        return BoreSinePole_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        N_val = self.N
        k_val = self.k
        delta_d_val = self.delta_d
        delta_q_val = self.delta_q
        W0_val = self.W0
        alpha_val = self.alpha
        type_merge_slot_val = self.type_merge_slot
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            N=N_val,
            k=k_val,
            delta_d=delta_d_val,
            delta_q=delta_q_val,
            W0=W0_val,
            alpha=alpha_val,
            type_merge_slot=type_merge_slot_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N = None
        self.k = None
        self.delta_d = None
        self.delta_q = None
        self.W0 = None
        self.alpha = None
        # Set to None the properties inherited from Bore
        super(BoreSinePole, self)._set_None()

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=0)
        self._N = value

    N = property(
        fget=_get_N,
        fset=_set_N,
        doc=u"""Number of Poles

        :Type: int
        :min: 0
        """,
    )

    def _get_k(self):
        """getter of k"""
        return self._k

    def _set_k(self, value):
        """setter of k"""
        check_var("k", value, "float", Vmin=0)
        self._k = value

    k = property(
        fget=_get_k,
        fset=_set_k,
        doc=u"""pole width modifier

        :Type: float
        :min: 0
        """,
    )

    def _get_delta_d(self):
        """getter of delta_d"""
        return self._delta_d

    def _set_delta_d(self, value):
        """setter of delta_d"""
        check_var("delta_d", value, "float", Vmin=0)
        self._delta_d = value

    delta_d = property(
        fget=_get_delta_d,
        fset=_set_delta_d,
        doc=u"""d-axis air gap width

        :Type: float
        :min: 0
        """,
    )

    def _get_delta_q(self):
        """getter of delta_q"""
        return self._delta_q

    def _set_delta_q(self, value):
        """setter of delta_q"""
        check_var("delta_q", value, "float", Vmin=0)
        self._delta_q = value

    delta_q = property(
        fget=_get_delta_q,
        fset=_set_delta_q,
        doc=u"""q-axis air gap width

        :Type: float
        :min: 0
        """,
    )

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Width of the pole

        :Type: float
        :min: 0
        """,
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float")
        self._alpha = value

    alpha = property(
        fget=_get_alpha,
        fset=_set_alpha,
        doc=u"""Angular offset

        :Type: float
        """,
    )
