# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Subdomain.comp_polynoms import comp_polynoms
except ImportError as error:
    comp_polynoms = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain(FrozenClass):
    """Abstract class for all subdomains"""

    VERSION = 1

    # cf Methods.Simulation.Subdomain.comp_polynoms
    if isinstance(comp_polynoms, ImportError):
        comp_polynoms = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain method comp_polynoms: " + str(comp_polynoms)
                )
            )
        )
    else:
        comp_polynoms = comp_polynoms
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        radius_min=None,
        radius_max=None,
        k=None,
        number=None,
        permeability_relative=1,
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
            if "radius_min" in list(init_dict.keys()):
                radius_min = init_dict["radius_min"]
            if "radius_max" in list(init_dict.keys()):
                radius_max = init_dict["radius_max"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "number" in list(init_dict.keys()):
                number = init_dict["number"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.radius_min = radius_min
        self.radius_max = radius_max
        self.k = k
        self.number = number
        self.permeability_relative = permeability_relative

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_str = ""
        if self.parent is None:
            Subdomain_str += "parent = None " + linesep
        else:
            Subdomain_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Subdomain_str += "radius_min = " + str(self.radius_min) + linesep
        Subdomain_str += "radius_max = " + str(self.radius_max) + linesep
        Subdomain_str += (
            "k = "
            + linesep
            + str(self.k).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_str += "number = " + str(self.number) + linesep
        Subdomain_str += (
            "permeability_relative = " + str(self.permeability_relative) + linesep
        )
        return Subdomain_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.radius_min != self.radius_min:
            return False
        if other.radius_max != self.radius_max:
            return False
        if not array_equal(other.k, self.k):
            return False
        if other.number != self.number:
            return False
        if other.permeability_relative != self.permeability_relative:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (
            other._radius_min is not None
            and self._radius_min is not None
            and isnan(other._radius_min)
            and isnan(self._radius_min)
        ):
            pass
        elif other._radius_min != self._radius_min:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._radius_min)
                    + ", other="
                    + str(other._radius_min)
                    + ")"
                )
                diff_list.append(name + ".radius_min" + val_str)
            else:
                diff_list.append(name + ".radius_min")
        if (
            other._radius_max is not None
            and self._radius_max is not None
            and isnan(other._radius_max)
            and isnan(self._radius_max)
        ):
            pass
        elif other._radius_max != self._radius_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._radius_max)
                    + ", other="
                    + str(other._radius_max)
                    + ")"
                )
                diff_list.append(name + ".radius_max" + val_str)
            else:
                diff_list.append(name + ".radius_max")
        if not array_equal(other.k, self.k):
            diff_list.append(name + ".k")
        if other._number != self._number:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._number)
                    + ", other="
                    + str(other._number)
                    + ")"
                )
                diff_list.append(name + ".number" + val_str)
            else:
                diff_list.append(name + ".number")
        if (
            other._permeability_relative is not None
            and self._permeability_relative is not None
            and isnan(other._permeability_relative)
            and isnan(self._permeability_relative)
        ):
            pass
        elif other._permeability_relative != self._permeability_relative:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._permeability_relative)
                    + ", other="
                    + str(other._permeability_relative)
                    + ")"
                )
                diff_list.append(name + ".permeability_relative" + val_str)
            else:
                diff_list.append(name + ".permeability_relative")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.radius_min)
        S += getsizeof(self.radius_max)
        S += getsizeof(self.k)
        S += getsizeof(self.number)
        S += getsizeof(self.permeability_relative)
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

        Subdomain_dict = dict()
        Subdomain_dict["radius_min"] = self.radius_min
        Subdomain_dict["radius_max"] = self.radius_max
        if self.k is None:
            Subdomain_dict["k"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_dict["k"] = self.k.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_dict["k"] = self.k.copy()
            elif type_handle_ndarray == 2:
                Subdomain_dict["k"] = self.k
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_dict["number"] = self.number
        Subdomain_dict["permeability_relative"] = self.permeability_relative
        # The class name is added to the dict for deserialisation purpose
        Subdomain_dict["__class__"] = "Subdomain"
        return Subdomain_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        radius_min_val = self.radius_min
        radius_max_val = self.radius_max
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        number_val = self.number
        permeability_relative_val = self.permeability_relative
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            radius_min=radius_min_val,
            radius_max=radius_max_val,
            k=k_val,
            number=number_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.radius_min = None
        self.radius_max = None
        self.k = None
        self.number = None
        self.permeability_relative = None

    def _get_radius_min(self):
        """getter of radius_min"""
        return self._radius_min

    def _set_radius_min(self, value):
        """setter of radius_min"""
        check_var("radius_min", value, "float", Vmin=0)
        self._radius_min = value

    radius_min = property(
        fget=_get_radius_min,
        fset=_set_radius_min,
        doc=u"""Minimum radius of subdomain

        :Type: float
        :min: 0
        """,
    )

    def _get_radius_max(self):
        """getter of radius_max"""
        return self._radius_max

    def _set_radius_max(self, value):
        """setter of radius_max"""
        check_var("radius_max", value, "float", Vmin=0)
        self._radius_max = value

    radius_max = property(
        fget=_get_radius_max,
        fset=_set_radius_max,
        doc=u"""Maximum radius of subdomain

        :Type: float
        :min: 0
        """,
    )

    def _get_k(self):
        """getter of k"""
        return self._k

    def _set_k(self, value):
        """setter of k"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("k", value, "ndarray", Vmin=0)
        self._k = value

    k = property(
        fget=_get_k,
        fset=_set_k,
        doc=u"""Array of harmonic numbers 

        :Type: ndarray
        :min: 0
        """,
    )

    def _get_number(self):
        """getter of number"""
        return self._number

    def _set_number(self, value):
        """setter of number"""
        check_var("number", value, "int", Vmin=0)
        self._number = value

    number = property(
        fget=_get_number,
        fset=_set_number,
        doc=u"""Number of identical subdomains in model

        :Type: int
        :min: 0
        """,
    )

    def _get_permeability_relative(self):
        """getter of permeability_relative"""
        return self._permeability_relative

    def _set_permeability_relative(self, value):
        """setter of permeability_relative"""
        check_var("permeability_relative", value, "float", Vmin=1)
        self._permeability_relative = value

    permeability_relative = property(
        fget=_get_permeability_relative,
        fset=_set_permeability_relative,
        doc=u"""Relative permeability of subdomain

        :Type: float
        :min: 1
        """,
    )
