# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/SolutionData.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Solution import Solution

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.SolutionData.get_field import get_field
except ImportError as error:
    get_field = error


from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from SciDataTool.Classes.DataND import DataND
except ImportError:
    DataND = ImportError
from ._check import InitUnKnowClassError


class SolutionData(Solution):
    """Define a Solution with SciDataTool objects."""

    VERSION = 1

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
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, field=None, type_cell="triangle", init_dict=None, init_str=None):
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
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
        # Initialisation by argument
        # Check if the type DataND has been imported with success
        if isinstance(DataND, ImportError):
            raise ImportError("Unknown type DataND please install SciDataTool")
        self.field = field
        self.type_cell = type_cell
        # Call Solution init
        super(SolutionData, self).__init__()
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SolutionData_str = ""
        # Get the properties inherited from Solution
        SolutionData_str += super(SolutionData, self).__str__()
        SolutionData_str += "field = " + str(self.field) + linesep + linesep
        SolutionData_str += 'type_cell = "' + str(self.type_cell) + '"' + linesep
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
        if other.type_cell != self.type_cell:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionData_dict = super(SolutionData, self).as_dict()
        if self.field is None:
            SolutionData_dict["field"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            SolutionData_dict["field"] = {
                "__class__": str(type(self._field)),
                "__repr__": str(self._field.__repr__()),
                "serialized": dumps(self._field).decode("ISO-8859-2"),
            }
        SolutionData_dict["type_cell"] = self.type_cell
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionData_dict["__class__"] = "SolutionData"
        return SolutionData_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.type_cell = None
        # Set to None the properties inherited from Solution
        super(SolutionData, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        try:  # Check the type
            check_var("field", value, "dict")
        except CheckTypeError:
            check_var("field", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._field = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._field = value

    # Data object containing the numerical values of a solution. One of the axis must be "Indices", a list of indices. If the solution is a vector, one of the axis must be "Direction", values ['x','y'] for example.
    # Type : SciDataTool.Classes.DataND.DataND
    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Data object containing the numerical values of a solution. One of the axis must be "Indices", a list of indices. If the solution is a vector, one of the axis must be "Direction", values ['x','y'] for example.""",
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
