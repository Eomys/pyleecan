# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/Rules_complex.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/Rules_complex
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
from .Rules import Rules

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.Rules_complex.add_rules_complex import add_rules_complex
except ImportError as error:
    add_rules_complex = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Rules_complex(Rules):
    """complex rules"""

    VERSION = 1

    # cf Methods.Converter.Rules_complex.add_rules_complex
    if isinstance(add_rules_complex, ImportError):
        add_rules_complex = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_complex method add_rules_complex: "
                    + str(add_rules_complex)
                )
            )
        )
    else:
        add_rules_complex = add_rules_complex
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, complex=None, init_dict=None, init_str=None):
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
            if "complex" in list(init_dict.keys()):
                complex = init_dict["complex"]
        # Set the properties (value check and convertion are done in setter)
        self.complex = complex
        # Call Rules init
        super(Rules_complex, self).__init__()
        # The class is frozen (in Rules init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Rules_complex_str = ""
        # Get the properties inherited from Rules
        Rules_complex_str += super(Rules_complex, self).__str__()
        Rules_complex_str += 'complex = "' + str(self.complex) + '"' + linesep
        return Rules_complex_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Rules
        if not super(Rules_complex, self).__eq__(other):
            return False
        if other.complex != self.complex:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Rules
        diff_list.extend(
            super(Rules_complex, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._complex != self._complex:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._complex)
                    + ", other="
                    + str(other._complex)
                    + ")"
                )
                diff_list.append(name + ".complex" + val_str)
            else:
                diff_list.append(name + ".complex")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Rules
        S += super(Rules_complex, self).__sizeof__()
        S += getsizeof(self.complex)
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

        # Get the properties inherited from Rules
        Rules_complex_dict = super(Rules_complex, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Rules_complex_dict["complex"] = self.complex
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Rules_complex_dict["__class__"] = "Rules_complex"
        return Rules_complex_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        complex_val = self.complex
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(complex=complex_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.complex = None
        # Set to None the properties inherited from Rules
        super(Rules_complex, self)._set_None()

    def _get_complex(self):
        """getter of complex"""
        return self._complex

    def _set_complex(self, value):
        """setter of complex"""
        check_var("complex", value, "str")
        self._complex = value

    complex = property(
        fget=_get_complex,
        fset=_set_complex,
        doc=u"""fonction name to convert 

        :Type: str
        """,
    )
