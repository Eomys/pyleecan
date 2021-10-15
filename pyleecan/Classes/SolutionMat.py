# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/SolutionMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/SolutionMat
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Solution import Solution

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.SolutionMat.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.SolutionMat.get_axes_list import get_axes_list
except ImportError as error:
    get_axes_list = error

try:
    from ..Methods.Mesh.SolutionMat.get_solution import get_solution
except ImportError as error:
    get_solution = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class SolutionMat(Solution):
    """Define a Solution with ndarray object."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.SolutionMat.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError("Can't use SolutionMat method get_field: " + str(get_field))
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.SolutionMat.get_axes_list
    if isinstance(get_axes_list, ImportError):
        get_axes_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionMat method get_axes_list: " + str(get_axes_list)
                )
            )
        )
    else:
        get_axes_list = get_axes_list
    # cf Methods.Mesh.SolutionMat.get_solution
    if isinstance(get_solution, ImportError):
        get_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionMat method get_solution: " + str(get_solution)
                )
            )
        )
    else:
        get_solution = get_solution
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        field=None,
        indice=None,
        axis_name=None,
        axis_size=None,
        type_cell="triangle",
        label=None,
        dimension=2,
        unit="",
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
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
            if "axis_name" in list(init_dict.keys()):
                axis_name = init_dict["axis_name"]
            if "axis_size" in list(init_dict.keys()):
                axis_size = init_dict["axis_size"]
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
        # Set the properties (value check and convertion are done in setter)
        self.field = field
        self.indice = indice
        self.axis_name = axis_name
        self.axis_size = axis_size
        # Call Solution init
        super(SolutionMat, self).__init__(
            type_cell=type_cell, label=label, dimension=dimension, unit=unit
        )
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SolutionMat_str = ""
        # Get the properties inherited from Solution
        SolutionMat_str += super(SolutionMat, self).__str__()
        SolutionMat_str += (
            "field = "
            + linesep
            + str(self.field).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SolutionMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SolutionMat_str += (
            "axis_name = "
            + linesep
            + str(self.axis_name).replace(linesep, linesep + "\t")
            + linesep
        )
        SolutionMat_str += (
            "axis_size = "
            + linesep
            + str(self.axis_size).replace(linesep, linesep + "\t")
            + linesep
        )
        return SolutionMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Solution
        if not super(SolutionMat, self).__eq__(other):
            return False
        if not array_equal(other.field, self.field):
            return False
        if not array_equal(other.indice, self.indice):
            return False
        if other.axis_name != self.axis_name:
            return False
        if other.axis_size != self.axis_size:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Solution
        diff_list.extend(super(SolutionMat, self).compare(other, name=name))
        if not array_equal(other.field, self.field):
            diff_list.append(name + ".field")
        if not array_equal(other.indice, self.indice):
            diff_list.append(name + ".indice")
        if other._axis_name != self._axis_name:
            diff_list.append(name + ".axis_name")
        if other._axis_size != self._axis_size:
            diff_list.append(name + ".axis_size")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Solution
        S += super(SolutionMat, self).__sizeof__()
        S += getsizeof(self.field)
        S += getsizeof(self.indice)
        if self.axis_name is not None:
            for value in self.axis_name:
                S += getsizeof(value)
        if self.axis_size is not None:
            for value in self.axis_size:
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

        # Get the properties inherited from Solution
        SolutionMat_dict = super(SolutionMat, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.field is None:
            SolutionMat_dict["field"] = None
        else:
            if type_handle_ndarray == 0:
                SolutionMat_dict["field"] = self.field.tolist()
            elif type_handle_ndarray == 1:
                SolutionMat_dict["field"] = self.field.copy()
            elif type_handle_ndarray == 2:
                SolutionMat_dict["field"] = self.field
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.indice is None:
            SolutionMat_dict["indice"] = None
        else:
            if type_handle_ndarray == 0:
                SolutionMat_dict["indice"] = self.indice.tolist()
            elif type_handle_ndarray == 1:
                SolutionMat_dict["indice"] = self.indice.copy()
            elif type_handle_ndarray == 2:
                SolutionMat_dict["indice"] = self.indice
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        SolutionMat_dict["axis_name"] = (
            self.axis_name.copy() if self.axis_name is not None else None
        )
        SolutionMat_dict["axis_size"] = (
            self.axis_size.copy() if self.axis_size is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SolutionMat_dict["__class__"] = "SolutionMat"
        return SolutionMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.indice = None
        self.axis_name = None
        self.axis_size = None
        # Set to None the properties inherited from Solution
        super(SolutionMat, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("field", value, "ndarray")
        self._field = value

    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Matrix/Vector of the numerical values of the solutions.

        :Type: ndarray
        """,
    )

    def _get_indice(self):
        """getter of indice"""
        return self._indice

    def _set_indice(self, value):
        """setter of indice"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indice", value, "ndarray")
        self._indice = value

    indice = property(
        fget=_get_indice,
        fset=_set_indice,
        doc=u"""Indices of loaded cells. Set to None if all cells are loaded

        :Type: ndarray
        """,
    )

    def _get_axis_name(self):
        """getter of axis_name"""
        return self._axis_name

    def _set_axis_name(self, value):
        """setter of axis_name"""
        if type(value) is int and value == -1:
            value = list()
        check_var("axis_name", value, "list")
        self._axis_name = value

    axis_name = property(
        fget=_get_axis_name,
        fset=_set_axis_name,
        doc=u"""List of axis names (e.g. "time", "direction")

        :Type: list
        """,
    )

    def _get_axis_size(self):
        """getter of axis_size"""
        return self._axis_size

    def _set_axis_size(self, value):
        """setter of axis_size"""
        if type(value) is int and value == -1:
            value = list()
        check_var("axis_size", value, "list")
        self._axis_size = value

    axis_size = property(
        fget=_get_axis_size,
        fset=_set_axis_size,
        doc=u"""List of axis sizes

        :Type: list
        """,
    )
