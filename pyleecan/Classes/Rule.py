# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/Rule.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/Rule
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.Rule.set_P import set_P
except ImportError as error:
    set_P = error

try:
    from ..Methods.Converter.Rule.get_P import get_P
except ImportError as error:
    get_P = error

try:
    from ..Methods.Converter.Rule.set_other import set_other
except ImportError as error:
    set_other = error

try:
    from ..Methods.Converter.Rule.get_other import get_other
except ImportError as error:
    get_other = error

try:
    from ..Methods.Converter.Rule.get_name import get_name
except ImportError as error:
    get_name = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Rule(FrozenClass):
    """abstract class for rules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.Rule.set_P
    if isinstance(set_P, ImportError):
        set_P = property(
            fget=lambda x: raise_(
                ImportError("Can't use Rule method set_P: " + str(set_P))
            )
        )
    else:
        set_P = set_P
    # cf Methods.Converter.Rule.get_P
    if isinstance(get_P, ImportError):
        get_P = property(
            fget=lambda x: raise_(
                ImportError("Can't use Rule method get_P: " + str(get_P))
            )
        )
    else:
        get_P = get_P
    # cf Methods.Converter.Rule.set_other
    if isinstance(set_other, ImportError):
        set_other = property(
            fget=lambda x: raise_(
                ImportError("Can't use Rule method set_other: " + str(set_other))
            )
        )
    else:
        set_other = set_other
    # cf Methods.Converter.Rule.get_other
    if isinstance(get_other, ImportError):
        get_other = property(
            fget=lambda x: raise_(
                ImportError("Can't use Rule method get_other: " + str(get_other))
            )
        )
    else:
        get_other = get_other
    # cf Methods.Converter.Rule.get_name
    if isinstance(get_name, ImportError):
        get_name = property(
            fget=lambda x: raise_(
                ImportError("Can't use Rule method get_name: " + str(get_name))
            )
        )
    else:
        get_name = get_name
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, unit_type="m", init_dict=None, init_str=None):
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
            if "unit_type" in list(init_dict.keys()):
                unit_type = init_dict["unit_type"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.unit_type = unit_type

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Rule_str = ""
        if self.parent is None:
            Rule_str += "parent = None " + linesep
        else:
            Rule_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Rule_str += 'unit_type = "' + str(self.unit_type) + '"' + linesep
        return Rule_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.unit_type != self.unit_type:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._unit_type != self._unit_type:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._unit_type)
                    + ", other="
                    + str(other._unit_type)
                    + ")"
                )
                diff_list.append(name + ".unit_type" + val_str)
            else:
                diff_list.append(name + ".unit_type")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.unit_type)
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

        Rule_dict = dict()
        Rule_dict["unit_type"] = self.unit_type
        # The class name is added to the dict for deserialisation purpose
        Rule_dict["__class__"] = "Rule"
        return Rule_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        unit_type_val = self.unit_type
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(unit_type=unit_type_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.unit_type = None

    def _get_unit_type(self):
        """getter of unit_type"""
        return self._unit_type

    def _set_unit_type(self, value):
        """setter of unit_type"""
        check_var("unit_type", value, "str")
        self._unit_type = value

    unit_type = property(
        fget=_get_unit_type,
        fset=_set_unit_type,
        doc="""unit

        :Type: str
        """,
    )
