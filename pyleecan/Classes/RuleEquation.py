# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/RuleEquation.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/RuleEquation
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
from .Rule import Rule

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.RuleEquation.convert_to_P import convert_to_P
except ImportError as error:
    convert_to_P = error

try:
    from ..Methods.Converter.RuleEquation.convert_to_other import convert_to_other
except ImportError as error:
    convert_to_other = error

try:
    from ..Methods.Converter.RuleEquation.solve_equation import solve_equation
except ImportError as error:
    solve_equation = error


from numpy import isnan
from ._check import InitUnKnowClassError


class RuleEquation(Rule):
    """simple rules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.RuleEquation.convert_to_P
    if isinstance(convert_to_P, ImportError):
        convert_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleEquation method convert_to_P: " + str(convert_to_P)
                )
            )
        )
    else:
        convert_to_P = convert_to_P
    # cf Methods.Converter.RuleEquation.convert_to_other
    if isinstance(convert_to_other, ImportError):
        convert_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleEquation method convert_to_other: "
                    + str(convert_to_other)
                )
            )
        )
    else:
        convert_to_other = convert_to_other
    # cf Methods.Converter.RuleEquation.solve_equation
    if isinstance(solve_equation, ImportError):
        solve_equation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleEquation method solve_equation: "
                    + str(solve_equation)
                )
            )
        )
    else:
        solve_equation = solve_equation
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        param=None,
        equation=None,
        file_name=None,
        unit_type="m",
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
            if "param" in list(init_dict.keys()):
                param = init_dict["param"]
            if "equation" in list(init_dict.keys()):
                equation = init_dict["equation"]
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
            if "unit_type" in list(init_dict.keys()):
                unit_type = init_dict["unit_type"]
        # Set the properties (value check and convertion are done in setter)
        self.param = param
        self.equation = equation
        self.file_name = file_name
        # Call Rule init
        super(RuleEquation, self).__init__(unit_type=unit_type)
        # The class is frozen (in Rule init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RuleEquation_str = ""
        # Get the properties inherited from Rule
        RuleEquation_str += super(RuleEquation, self).__str__()
        RuleEquation_str += (
            "param = "
            + linesep
            + str(self.param).replace(linesep, linesep + "\t")
            + linesep
        )
        RuleEquation_str += 'equation = "' + str(self.equation) + '"' + linesep
        RuleEquation_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        return RuleEquation_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Rule
        if not super(RuleEquation, self).__eq__(other):
            return False
        if other.param != self.param:
            return False
        if other.equation != self.equation:
            return False
        if other.file_name != self.file_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Rule
        diff_list.extend(
            super(RuleEquation, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._param != self._param:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._param) + ", other=" + str(other._param) + ")"
                )
                diff_list.append(name + ".param" + val_str)
            else:
                diff_list.append(name + ".param")
        if other._equation != self._equation:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._equation)
                    + ", other="
                    + str(other._equation)
                    + ")"
                )
                diff_list.append(name + ".equation" + val_str)
            else:
                diff_list.append(name + ".equation")
        if other._file_name != self._file_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._file_name)
                    + ", other="
                    + str(other._file_name)
                    + ")"
                )
                diff_list.append(name + ".file_name" + val_str)
            else:
                diff_list.append(name + ".file_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Rule
        S += super(RuleEquation, self).__sizeof__()
        if self.param is not None:
            for value in self.param:
                S += getsizeof(value)
        S += getsizeof(self.equation)
        S += getsizeof(self.file_name)
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

        # Get the properties inherited from Rule
        RuleEquation_dict = super(RuleEquation, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        RuleEquation_dict["param"] = (
            self.param.copy() if self.param is not None else None
        )
        RuleEquation_dict["equation"] = self.equation
        RuleEquation_dict["file_name"] = self.file_name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        RuleEquation_dict["__class__"] = "RuleEquation"
        return RuleEquation_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.param is None:
            param_val = None
        else:
            param_val = self.param.copy()
        equation_val = self.equation
        file_name_val = self.file_name
        unit_type_val = self.unit_type
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            param=param_val,
            equation=equation_val,
            file_name=file_name_val,
            unit_type=unit_type_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.param = None
        self.equation = None
        self.file_name = None
        # Set to None the properties inherited from Rule
        super(RuleEquation, self)._set_None()

    def _get_param(self):
        """getter of param"""
        return self._param

    def _set_param(self, value):
        """setter of param"""
        if type(value) is int and value == -1:
            value = list()
        check_var("param", value, "list")
        self._param = value

    param = property(
        fget=_get_param,
        fset=_set_param,
        doc=u"""dict all parameters

        :Type: list
        """,
    )

    def _get_equation(self):
        """getter of equation"""
        return self._equation

    def _set_equation(self, value):
        """setter of equation"""
        check_var("equation", value, "str")
        self._equation = value

    equation = property(
        fget=_get_equation,
        fset=_set_equation,
        doc=u"""conversion paramter to pyleecan (Y are always on other side

        :Type: str
        """,
    )

    def _get_file_name(self):
        """getter of file_name"""
        return self._file_name

    def _set_file_name(self, value):
        """setter of file_name"""
        check_var("file_name", value, "str")
        self._file_name = value

    file_name = property(
        fget=_get_file_name,
        fset=_set_file_name,
        doc=u"""use just to debug, give name of file

        :Type: str
        """,
    )
