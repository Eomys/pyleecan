# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/SolutionCell.csv
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
    from ..Methods.Mesh.SolutionCell.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.SolutionCell.set_field import set_field
except ImportError as error:
    set_field = error

try:
    from ..Methods.Mesh.SolutionCell.get_tag import get_tag
except ImportError as error:
    get_tag = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class SolutionCell(Solution):
    """Define a solution related to the cells of a Mesh object."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.SolutionCell.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionCell method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.SolutionCell.set_field
    if isinstance(set_field, ImportError):
        set_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionCell method set_field: " + str(set_field)
                )
            )
        )
    else:
        set_field = set_field
    # cf Methods.Mesh.SolutionCell.get_tag
    if isinstance(get_tag, ImportError):
        get_tag = property(
            fget=lambda x: raise_(
                ImportError("Can't use SolutionCell method get_tag: " + str(get_tag))
            )
        )
    else:
        get_tag = get_tag
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, field=None, tag=None, label=None, init_dict=None, init_str=None):
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
            tag = obj.tag
            label = obj.label
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "tag" in list(init_dict.keys()):
                tag = init_dict["tag"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.field = field
        # tag can be None, a ndarray or a list
        set_array(self, "tag", tag)
        self.label = label
        # Call Solution init
        super(SolutionCell, self).__init__()
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SolutionCell_str = ""
        # Get the properties inherited from Solution
        SolutionCell_str += super(SolutionCell, self).__str__()
        SolutionCell_str += (
            "field = "
            + linesep
            + str(self.field).replace(linesep, linesep + "\t")
            + linesep
        )
        SolutionCell_str += (
            "tag = "
            + linesep
            + str(self.tag).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SolutionCell_str += 'label = "' + str(self.label) + '"' + linesep
        return SolutionCell_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Solution
        if not super(SolutionCell, self).__eq__(other):
            return False
        if other.field != self.field:
            return False
        if not array_equal(other.tag, self.tag):
            return False
        if other.label != self.label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionCell_dict = super(SolutionCell, self).as_dict()
        SolutionCell_dict["field"] = self.field
        if self.tag is None:
            SolutionCell_dict["tag"] = None
        else:
            SolutionCell_dict["tag"] = self.tag.tolist()
        SolutionCell_dict["label"] = self.label
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionCell_dict["__class__"] = "SolutionCell"
        return SolutionCell_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.field = None
        self.tag = None
        self.label = None
        # Set to None the properties inherited from Solution
        super(SolutionCell, self)._set_None()

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        check_var("field", value, "list")
        self._field = value

    # List of vector of the numerical values of the solutions
    # Type : list
    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""List of vector of the numerical values of the solutions""",
    )

    def _get_tag(self):
        """getter of tag"""
        return self._tag

    def _set_tag(self, value):
        """setter of tag"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("tag", value, "ndarray")
        self._tag = value

    # Vector of cell tags on which the solution apply
    # Type : ndarray
    tag = property(
        fget=_get_tag,
        fset=_set_tag,
        doc=u"""Vector of cell tags on which the solution apply""",
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
