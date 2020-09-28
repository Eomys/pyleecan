# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/SolutionMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/SolutionMat
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
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
    from ..Methods.Mesh.SolutionMat.get_axis import get_axis
except ImportError as error:
    get_axis = error


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
    # cf Methods.Mesh.SolutionMat.get_axis
    if isinstance(get_axis, ImportError):
        get_axis = property(
            fget=lambda x: raise_(
                ImportError("Can't use SolutionMat method get_axis: " + str(get_axis))
            )
        )
    else:
        get_axis = get_axis
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        field=None,
        indice=None,
        axis=None,
        type_cell="triangle",
        label=None,
        dimension=2,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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
            if "axis" in list(init_dict.keys()):
                axis = init_dict["axis"]
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.field = field
        self.indice = indice
        self.axis = axis
        # Call Solution init
        super(SolutionMat, self).__init__(
            type_cell=type_cell, label=label, dimension=dimension
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
        SolutionMat_str += "axis = " + str(self.axis) + linesep
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
        if other.axis != self.axis:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionMat_dict = super(SolutionMat, self).as_dict()
        if self.field is None:
            SolutionMat_dict["field"] = None
        else:
            SolutionMat_dict["field"] = self.field.tolist()
        if self.indice is None:
            SolutionMat_dict["indice"] = None
        else:
            SolutionMat_dict["indice"] = self.indice.tolist()
        SolutionMat_dict["axis"] = self.axis
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionMat_dict["__class__"] = "SolutionMat"
        return SolutionMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.indice = None
        self.axis = None
        # Set to None the properties inherited from Solution
        super(SolutionMat, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        if value is -1:
            value = list()
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
        if value is -1:
            value = list()
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

    def _get_axis(self):
        """getter of axis"""
        return self._axis

    def _set_axis(self, value):
        """setter of axis"""
        if value is -1:
            value = dict()
        check_var("axis", value, "dict")
        self._axis = value

    axis = property(
        fget=_get_axis,
        fset=_set_axis,
        doc=u"""Dict of axis names storing axis sizes (e.g. time, direction )

        :Type: dict
        """,
    )
