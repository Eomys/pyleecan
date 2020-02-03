# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Import/ImportMatrixVal.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Import.ImportMatrixVal.get_data import get_data
except ImportError as error:
    get_data = error


from numpy import array, array_equal
from pyleecan.Classes._check import InitUnKnowClassError


class ImportMatrixVal(ImportMatrix):
    """Import directly the value from the object"""

    VERSION = 1

    # cf Methods.Import.ImportMatrixVal.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportMatrixVal method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # save method is available in all object
    save = save

    def __init__(self, value=None, is_transpose=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["value", "is_transpose"])
            # Overwrite default value with init_dict content
            if "value" in list(init_dict.keys()):
                value = init_dict["value"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        # value can be None, a ndarray or a list
        set_array(self, "value", value)
        # Call ImportMatrix init
        super(ImportMatrixVal, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportMatrixVal_str = ""
        # Get the properties inherited from ImportMatrix
        ImportMatrixVal_str += super(ImportMatrixVal, self).__str__() + linesep
        ImportMatrixVal_str += "value = " + linesep + str(self.value)
        return ImportMatrixVal_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportMatrixVal, self).__eq__(other):
            return False
        if not array_equal(other.value, self.value):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportMatrixVal_dict = super(ImportMatrixVal, self).as_dict()
        if self.value is None:
            ImportMatrixVal_dict["value"] = None
        else:
            ImportMatrixVal_dict["value"] = self.value.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportMatrixVal_dict["__class__"] = "ImportMatrixVal"
        return ImportMatrixVal_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.value = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportMatrixVal, self)._set_None()

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("value", value, "ndarray")
        self._value = value

    # The matrix to return
    # Type : ndarray
    value = property(fget=_get_value, fset=_set_value, doc=u"""The matrix to return""")
