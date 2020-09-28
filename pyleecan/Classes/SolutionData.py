# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/SolutionData.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/SolutionData
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Solution import Solution

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.SolutionData.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.SolutionData.get_axis import get_axis
except ImportError as error:
    get_axis = error


from ._check import InitUnKnowClassError


class SolutionData(Solution):
    """Define a Solution with SciDataTool objects."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.SolutionData.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionData method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.SolutionData.get_axis
    if isinstance(get_axis, ImportError):
        get_axis = property(
            fget=lambda x: raise_(
                ImportError("Can't use SolutionData method get_axis: " + str(get_axis))
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
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.field = field
        # Call Solution init
        super(SolutionData, self).__init__(
            type_cell=type_cell, label=label, dimension=dimension
        )
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SolutionData_str = ""
        # Get the properties inherited from Solution
        SolutionData_str += super(SolutionData, self).__str__()
        SolutionData_str += "field = " + str(self.field) + linesep + linesep
        return SolutionData_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Solution
        if not super(SolutionData, self).__eq__(other):
            return False
        if other.field != self.field:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionData_dict = super(SolutionData, self).as_dict()
        if self.field is None:
            SolutionData_dict["field"] = None
        else:
            SolutionData_dict["field"] = self.field.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionData_dict["__class__"] = "SolutionData"
        return SolutionData_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        # Set to None the properties inherited from Solution
        super(SolutionData, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "field"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = DataND()
        check_var("field", value, "DataND")
        self._field = value

    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Data object containing the numerical values of a solution. One of the axis must be "Indices", a list of indices. If the solution is a vector, one of the axis must be "Direction", values ['x','y'] for example.

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )
