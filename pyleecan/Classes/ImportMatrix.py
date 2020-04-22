# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Import/ImportMatrix.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Import import Import

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportMatrix.edit_matrix import edit_matrix
except ImportError as error:
    edit_matrix = error


from ._check import InitUnKnowClassError


class ImportMatrix(Import):
    """Abstract class to Import/Generate 1D or D matrix"""

    VERSION = 1

    # cf Methods.Import.ImportMatrix.edit_matrix
    if isinstance(edit_matrix, ImportError):
        edit_matrix = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportMatrix method edit_matrix: " + str(edit_matrix)
                )
            )
        )
    else:
        edit_matrix = edit_matrix
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, is_transpose=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        self.is_transpose = is_transpose
        # Call Import init
        super(ImportMatrix, self).__init__()
        # The class is frozen (in Import init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportMatrix_str = ""
        # Get the properties inherited from Import
        ImportMatrix_str += super(ImportMatrix, self).__str__()
        ImportMatrix_str += "is_transpose = " + str(self.is_transpose) + linesep
        return ImportMatrix_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Import
        if not super(ImportMatrix, self).__eq__(other):
            return False
        if other.is_transpose != self.is_transpose:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Import
        ImportMatrix_dict = super(ImportMatrix, self).as_dict()
        ImportMatrix_dict["is_transpose"] = self.is_transpose
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportMatrix_dict["__class__"] = "ImportMatrix"
        return ImportMatrix_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_transpose = None
        # Set to None the properties inherited from Import
        super(ImportMatrix, self)._set_None()

    def _get_is_transpose(self):
        """getter of is_transpose"""
        return self._is_transpose

    def _set_is_transpose(self, value):
        """setter of is_transpose"""
        check_var("is_transpose", value, "bool")
        self._is_transpose = value

    # 1 to transpose the Imported/Generated matrix
    # Type : bool
    is_transpose = property(
        fget=_get_is_transpose,
        fset=_set_is_transpose,
        doc=u"""1 to transpose the Imported/Generated matrix""",
    )
