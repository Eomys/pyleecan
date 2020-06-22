# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/SolutionMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Solution import Solution

from numpy import array, array_equal
from ._check import InitUnKnowClassError


class SolutionMat(Solution):
    """Define a Solution with ndarray object."""

    VERSION = 1

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
        type_cell="triangle",
        label=None,
        indice=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            field = obj.field
            type_cell = obj.type_cell
            label = obj.label
            indice = obj.indice
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
        # Initialisation by argument
        # field can be None, a ndarray or a list
        set_array(self, "field", field)
        self.type_cell = type_cell
        self.label = label
        # indice can be None, a ndarray or a list
        set_array(self, "indice", indice)
        # Call Solution init
        super(SolutionMat, self).__init__()
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
        SolutionMat_str += 'type_cell = "' + str(self.type_cell) + '"' + linesep
        SolutionMat_str += 'label = "' + str(self.label) + '"' + linesep
        SolutionMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
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
        if other.type_cell != self.type_cell:
            return False
        if other.label != self.label:
            return False
        if not array_equal(other.indice, self.indice):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionMat_dict = super(SolutionMat, self).as_dict()
        if self.field is None:
            SolutionMat_dict["field"] = None
        else:
            SolutionMat_dict["field"] = self.field.tolist()
        SolutionMat_dict["type_cell"] = self.type_cell
        SolutionMat_dict["label"] = self.label
        if self.indice is None:
            SolutionMat_dict["indice"] = None
        else:
            SolutionMat_dict["indice"] = self.indice.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionMat_dict["__class__"] = "SolutionMat"
        return SolutionMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.type_cell = None
        self.label = None
        self.indice = None
        # Set to None the properties inherited from Solution
        super(SolutionMat, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("field", value, "ndarray")
        self._field = value

    # Matrix/Vector of the numerical values of the solutions.
    # Type : ndarray
    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Matrix/Vector of the numerical values of the solutions.""",
    )

    def _get_type_cell(self):
        """getter of type_cell"""
        return self._type_cell

    def _set_type_cell(self, value):
        """setter of type_cell"""
        check_var("type_cell", value, "str")
        self._type_cell = value

    # Type of cell (Point, Segment2, Triangle3, etc.)
    # Type : str
    type_cell = property(
        fget=_get_type_cell,
        fset=_set_type_cell,
        doc=u"""Type of cell (Point, Segment2, Triangle3, etc.)""",
    )

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    # Label to identify the solution
    # Type : str
    label = property(
        fget=_get_label, fset=_set_label, doc=u"""Label to identify the solution"""
    )

    def _get_indice(self):
        """getter of indice"""
        return self._indice

    def _set_indice(self, value):
        """setter of indice"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indice", value, "ndarray")
        self._indice = value

    # Indices of loaded cells. Set to None if all cells are loaded
    # Type : ndarray
    indice = property(
        fget=_get_indice,
        fset=_set_indice,
        doc=u"""Indices of loaded cells. Set to None if all cells are loaded""",
    )
