# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Loss/LossModel.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Loss/LossModel
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

from numpy import isnan
from ._check import InitUnKnowClassError


class LossModel(FrozenClass):
    """Abstract Loss Model Class"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        group="",
        is_show_fig=False,
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
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "is_show_fig" in list(init_dict.keys()):
                is_show_fig = init_dict["is_show_fig"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.group = group
        self.is_show_fig = is_show_fig
        self.coeff_dict = coeff_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossModel_str = ""
        if self.parent is None:
            LossModel_str += "parent = None " + linesep
        else:
            LossModel_str += "parent = " + str(type(self.parent)) + " object" + linesep
        LossModel_str += 'name = "' + str(self.name) + '"' + linesep
        LossModel_str += 'group = "' + str(self.group) + '"' + linesep
        LossModel_str += "is_show_fig = " + str(self.is_show_fig) + linesep
        LossModel_str += "coeff_dict = " + str(self.coeff_dict) + linesep
        return LossModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.group != self.group:
            return False
        if other.is_show_fig != self.is_show_fig:
            return False
        if other.coeff_dict != self.coeff_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        if other._group != self._group:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._group) + ", other=" + str(other._group) + ")"
                )
                diff_list.append(name + ".group" + val_str)
            else:
                diff_list.append(name + ".group")
        if other._is_show_fig != self._is_show_fig:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_show_fig)
                    + ", other="
                    + str(other._is_show_fig)
                    + ")"
                )
                diff_list.append(name + ".is_show_fig" + val_str)
            else:
                diff_list.append(name + ".is_show_fig")
        if other._coeff_dict != self._coeff_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._coeff_dict)
                    + ", other="
                    + str(other._coeff_dict)
                    + ")"
                )
                diff_list.append(name + ".coeff_dict" + val_str)
            else:
                diff_list.append(name + ".coeff_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.group)
        S += getsizeof(self.is_show_fig)
        if self.coeff_dict is not None:
            for key, value in self.coeff_dict.items():
                S += getsizeof(value) + getsizeof(key)
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

        LossModel_dict = dict()
        LossModel_dict["name"] = self.name
        LossModel_dict["group"] = self.group
        LossModel_dict["is_show_fig"] = self.is_show_fig
        LossModel_dict["coeff_dict"] = (
            self.coeff_dict.copy() if self.coeff_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        LossModel_dict["__class__"] = "LossModel"
        return LossModel_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        name_val = self.name
        group_val = self.group
        is_show_fig_val = self.is_show_fig
        if self.coeff_dict is None:
            coeff_dict_val = None
        else:
            coeff_dict_val = self.coeff_dict.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            name=name_val,
            group=group_val,
            is_show_fig=is_show_fig_val,
            coeff_dict=coeff_dict_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.group = None
        self.is_show_fig = None
        self.coeff_dict = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the loss simulation (has to be unique)

        :Type: str
        """,
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        check_var("group", value, "str")
        self._group = value

    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Group in which the loss will be computed

        :Type: str
        """,
    )

    def _get_is_show_fig(self):
        """getter of is_show_fig"""
        return self._is_show_fig

    def _set_is_show_fig(self, value):
        """setter of is_show_fig"""
        check_var("is_show_fig", value, "bool")
        self._is_show_fig = value

    is_show_fig = property(
        fget=_get_is_show_fig,
        fset=_set_is_show_fig,
        doc=u"""True to show the plot of the curve fitting

        :Type: bool
        """,
    )

    def _get_coeff_dict(self):
        """getter of coeff_dict"""
        return self._coeff_dict

    def _set_coeff_dict(self, value):
        """setter of coeff_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("coeff_dict", value, "dict")
        self._coeff_dict = value

    coeff_dict = property(
        fget=_get_coeff_dict,
        fset=_set_coeff_dict,
        doc=u"""dict of coefficients to compute losses with respect to frequency

        :Type: dict
        """,
    )
