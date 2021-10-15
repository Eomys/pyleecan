# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportGenMatrixSin.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportGenMatrixSin
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportGenMatrixSin.get_data import get_data
except ImportError as error:
    get_data = error

try:
    from ..Methods.Import.ImportGenMatrixSin.init_vector import init_vector
except ImportError as error:
    init_vector = error


from ._check import InitUnKnowClassError
from .ImportGenVectSin import ImportGenVectSin


class ImportGenMatrixSin(ImportMatrix):
    """To generate a Sinus matrix"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Import.ImportGenMatrixSin.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenMatrixSin method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # cf Methods.Import.ImportGenMatrixSin.init_vector
    if isinstance(init_vector, ImportError):
        init_vector = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenMatrixSin method init_vector: "
                    + str(init_vector)
                )
            )
        )
    else:
        init_vector = init_vector
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, sin_list=-1, is_transpose=False, init_dict=None, init_str=None):
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
            if "sin_list" in list(init_dict.keys()):
                sin_list = init_dict["sin_list"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.sin_list = sin_list
        # Call ImportMatrix init
        super(ImportGenMatrixSin, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportGenMatrixSin_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenMatrixSin_str += super(ImportGenMatrixSin, self).__str__()
        if len(self.sin_list) == 0:
            ImportGenMatrixSin_str += "sin_list = []" + linesep
        for ii in range(len(self.sin_list)):
            tmp = self.sin_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            ImportGenMatrixSin_str += (
                "sin_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return ImportGenMatrixSin_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenMatrixSin, self).__eq__(other):
            return False
        if other.sin_list != self.sin_list:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ImportMatrix
        diff_list.extend(super(ImportGenMatrixSin, self).compare(other, name=name))
        if (other.sin_list is None and self.sin_list is not None) or (
            other.sin_list is not None and self.sin_list is None
        ):
            diff_list.append(name + ".sin_list None mismatch")
        elif self.sin_list is None:
            pass
        elif len(other.sin_list) != len(self.sin_list):
            diff_list.append("len(" + name + ".sin_list)")
        else:
            for ii in range(len(other.sin_list)):
                diff_list.extend(
                    self.sin_list[ii].compare(
                        other.sin_list[ii], name=name + ".sin_list[" + str(ii) + "]"
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportGenMatrixSin, self).__sizeof__()
        if self.sin_list is not None:
            for value in self.sin_list:
                S += getsizeof(value)
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

        # Get the properties inherited from ImportMatrix
        ImportGenMatrixSin_dict = super(ImportGenMatrixSin, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.sin_list is None:
            ImportGenMatrixSin_dict["sin_list"] = None
        else:
            ImportGenMatrixSin_dict["sin_list"] = list()
            for obj in self.sin_list:
                if obj is not None:
                    ImportGenMatrixSin_dict["sin_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    ImportGenMatrixSin_dict["sin_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportGenMatrixSin_dict["__class__"] = "ImportGenMatrixSin"
        return ImportGenMatrixSin_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.sin_list = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenMatrixSin, self)._set_None()

    def _get_sin_list(self):
        """getter of sin_list"""
        if self._sin_list is not None:
            for obj in self._sin_list:
                if obj is not None:
                    obj.parent = self
        return self._sin_list

    def _set_sin_list(self, value):
        """setter of sin_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "sin_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("sin_list", value, "[ImportGenVectSin]")
        self._sin_list = value

    sin_list = property(
        fget=_get_sin_list,
        fset=_set_sin_list,
        doc=u"""List of sinus vector to generate the matrix lines

        :Type: [ImportGenVectSin]
        """,
    )
