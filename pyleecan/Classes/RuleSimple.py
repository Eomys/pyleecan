# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/RuleSimple.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/RuleSimple
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
    from ..Methods.Converter.RuleSimple.convert_to_P import convert_to_P
except ImportError as error:
    convert_to_P = error

try:
    from ..Methods.Converter.RuleSimple.convert_to_other import convert_to_other
except ImportError as error:
    convert_to_other = error


from numpy import isnan
from ._check import InitUnKnowClassError


class RuleSimple(Rule):
    """simple rules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.RuleSimple.convert_to_P
    if isinstance(convert_to_P, ImportError):
        convert_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleSimple method convert_to_P: " + str(convert_to_P)
                )
            )
        )
    else:
        convert_to_P = convert_to_P
    # cf Methods.Converter.RuleSimple.convert_to_other
    if isinstance(convert_to_other, ImportError):
        convert_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleSimple method convert_to_other: "
                    + str(convert_to_other)
                )
            )
        )
    else:
        convert_to_other = convert_to_other
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        other_key_list=None,
        P_obj_path=None,
        scaling_to_P=1,
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
            if "other_key_list" in list(init_dict.keys()):
                other_key_list = init_dict["other_key_list"]
            if "P_obj_path" in list(init_dict.keys()):
                P_obj_path = init_dict["P_obj_path"]
            if "scaling_to_P" in list(init_dict.keys()):
                scaling_to_P = init_dict["scaling_to_P"]
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
            if "unit_type" in list(init_dict.keys()):
                unit_type = init_dict["unit_type"]
        # Set the properties (value check and convertion are done in setter)
        self.other_key_list = other_key_list
        self.P_obj_path = P_obj_path
        self.scaling_to_P = scaling_to_P
        self.file_name = file_name
        # Call Rule init
        super(RuleSimple, self).__init__(unit_type=unit_type)
        # The class is frozen (in Rule init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RuleSimple_str = ""
        # Get the properties inherited from Rule
        RuleSimple_str += super(RuleSimple, self).__str__()
        RuleSimple_str += (
            "other_key_list = "
            + linesep
            + str(self.other_key_list).replace(linesep, linesep + "\t")
            + linesep
        )
        RuleSimple_str += 'P_obj_path = "' + str(self.P_obj_path) + '"' + linesep
        RuleSimple_str += "scaling_to_P = " + str(self.scaling_to_P) + linesep
        RuleSimple_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        return RuleSimple_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Rule
        if not super(RuleSimple, self).__eq__(other):
            return False
        if other.other_key_list != self.other_key_list:
            return False
        if other.P_obj_path != self.P_obj_path:
            return False
        if other.scaling_to_P != self.scaling_to_P:
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
            super(RuleSimple, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._other_key_list != self._other_key_list:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._other_key_list)
                    + ", other="
                    + str(other._other_key_list)
                    + ")"
                )
                diff_list.append(name + ".other_key_list" + val_str)
            else:
                diff_list.append(name + ".other_key_list")
        if other._P_obj_path != self._P_obj_path:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._P_obj_path)
                    + ", other="
                    + str(other._P_obj_path)
                    + ")"
                )
                diff_list.append(name + ".P_obj_path" + val_str)
            else:
                diff_list.append(name + ".P_obj_path")
        if (
            other._scaling_to_P is not None
            and self._scaling_to_P is not None
            and isnan(other._scaling_to_P)
            and isnan(self._scaling_to_P)
        ):
            pass
        elif other._scaling_to_P != self._scaling_to_P:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._scaling_to_P)
                    + ", other="
                    + str(other._scaling_to_P)
                    + ")"
                )
                diff_list.append(name + ".scaling_to_P" + val_str)
            else:
                diff_list.append(name + ".scaling_to_P")
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
        S += super(RuleSimple, self).__sizeof__()
        if self.other_key_list is not None:
            for value in self.other_key_list:
                S += getsizeof(value)
        S += getsizeof(self.P_obj_path)
        S += getsizeof(self.scaling_to_P)
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
        RuleSimple_dict = super(RuleSimple, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        RuleSimple_dict["other_key_list"] = (
            self.other_key_list.copy() if self.other_key_list is not None else None
        )
        RuleSimple_dict["P_obj_path"] = self.P_obj_path
        RuleSimple_dict["scaling_to_P"] = self.scaling_to_P
        RuleSimple_dict["file_name"] = self.file_name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        RuleSimple_dict["__class__"] = "RuleSimple"
        return RuleSimple_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.other_key_list is None:
            other_key_list_val = None
        else:
            other_key_list_val = self.other_key_list.copy()
        P_obj_path_val = self.P_obj_path
        scaling_to_P_val = self.scaling_to_P
        file_name_val = self.file_name
        unit_type_val = self.unit_type
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            other_key_list=other_key_list_val,
            P_obj_path=P_obj_path_val,
            scaling_to_P=scaling_to_P_val,
            file_name=file_name_val,
            unit_type=unit_type_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.other_key_list = None
        self.P_obj_path = None
        self.scaling_to_P = None
        self.file_name = None
        # Set to None the properties inherited from Rule
        super(RuleSimple, self)._set_None()

    def _get_other_key_list(self):
        """getter of other_key_list"""
        return self._other_key_list

    def _set_other_key_list(self, value):
        """setter of other_key_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("other_key_list", value, "list")
        self._other_key_list = value

    other_key_list = property(
        fget=_get_other_key_list,
        fset=_set_other_key_list,
        doc=u"""parameter 

        :Type: list
        """,
    )

    def _get_P_obj_path(self):
        """getter of P_obj_path"""
        return self._P_obj_path

    def _set_P_obj_path(self, value):
        """setter of P_obj_path"""
        check_var("P_obj_path", value, "str")
        self._P_obj_path = value

    P_obj_path = property(
        fget=_get_P_obj_path,
        fset=_set_P_obj_path,
        doc=u"""path pyleecan parameter in object machine 

        :Type: str
        """,
    )

    def _get_scaling_to_P(self):
        """getter of scaling_to_P"""
        return self._scaling_to_P

    def _set_scaling_to_P(self, value):
        """setter of scaling_to_P"""
        check_var("scaling_to_P", value, "float")
        self._scaling_to_P = value

    scaling_to_P = property(
        fget=_get_scaling_to_P,
        fset=_set_scaling_to_P,
        doc=u"""conversion paramter to pyleecan

        :Type: float
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
