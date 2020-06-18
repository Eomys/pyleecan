# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/SolutionPoint.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Solution import Solution

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.SolutionPoint.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.SolutionPoint.set_field import set_field
except ImportError as error:
    set_field = error

try:
    from ..Methods.Mesh.SolutionPoint.get_indice import get_indice
except ImportError as error:
    get_indice = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class SolutionPoint(Solution):
    """Define a solution related to the points (or nodes) a Mesh object."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.SolutionPoint.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionPoint method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.SolutionPoint.set_field
    if isinstance(set_field, ImportError):
        set_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionPoint method set_field: " + str(set_field)
                )
            )
        )
    else:
        set_field = set_field
    # cf Methods.Mesh.SolutionPoint.get_indice
    if isinstance(get_indice, ImportError):
        get_indice = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionPoint method get_indice: " + str(get_indice)
                )
            )
        )
    else:
        get_indice = get_indice
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
        self, field=None, indices=None, label=None, init_dict=None, init_str=None
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
            indices = obj.indices
            label = obj.label
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "indices" in list(init_dict.keys()):
                indices = init_dict["indices"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # field can be None, a ndarray or a list
        set_array(self, "field", field)
        # indices can be None, a ndarray or a list
        set_array(self, "indices", indices)
        self.label = label
        # Call Solution init
        super(SolutionPoint, self).__init__()
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SolutionPoint_str = ""
        # Get the properties inherited from Solution
        SolutionPoint_str += super(SolutionPoint, self).__str__()
        SolutionPoint_str += (
            "field = "
            + linesep
            + str(self.field).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SolutionPoint_str += (
            "indices = "
            + linesep
            + str(self.indices).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SolutionPoint_str += 'label = "' + str(self.label) + '"' + linesep
        return SolutionPoint_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Solution
        if not super(SolutionPoint, self).__eq__(other):
            return False
        if not array_equal(other.field, self.field):
            return False
        if not array_equal(other.indices, self.indices):
            return False
        if other.label != self.label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionPoint_dict = super(SolutionPoint, self).as_dict()
        if self.field is None:
            SolutionPoint_dict["field"] = None
        else:
            SolutionPoint_dict["field"] = self.field.tolist()
        if self.indices is None:
            SolutionPoint_dict["indices"] = None
        else:
            SolutionPoint_dict["indices"] = self.indices.tolist()
        SolutionPoint_dict["label"] = self.label
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionPoint_dict["__class__"] = "SolutionPoint"
        return SolutionPoint_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.indices = None
        self.label = None
        # Set to None the properties inherited from Solution
        super(SolutionPoint, self)._set_None()

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

    # Matrix/Vector of the numerical values of the solutions
    # Type : ndarray
    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Matrix/Vector of the numerical values of the solutions""",
    )

    def _get_indices(self):
        """getter of indices"""
        return self._indices

    def _set_indices(self, value):
        """setter of indices"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indices", value, "ndarray")
        self._indices = value

    # Vector of points/nodes indices on which the solution apply
    # Type : ndarray
    indices = property(
        fget=_get_indices,
        fset=_set_indices,
        doc=u"""Vector of points/nodes indices on which the solution apply""",
    )

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    # Label of the Mesh object which is linked to the solution
    # Type : str
    label = property(
        fget=_get_label,
        fset=_set_label,
        doc=u"""Label of the Mesh object which is linked to the solution""",
    )
