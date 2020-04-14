# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Import/ImportGenMatrixSin.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.get_logger import get_logger
from pyleecan.Functions.save import save
from pyleecan.Classes.ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Import.ImportGenMatrixSin.get_data import get_data
except ImportError as error:
    get_data = error

try:
    from pyleecan.Methods.Import.ImportGenMatrixSin.init_vector import init_vector
except ImportError as error:
    init_vector = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin


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
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, sin_list=list(), is_transpose=False, init_dict=None):
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
            if "sin_list" in list(init_dict.keys()):
                sin_list = init_dict["sin_list"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        # sin_list can be None or a list of ImportGenVectSin object
        self.sin_list = list()
        if type(sin_list) is list:
            for obj in sin_list:
                if obj is None:  # Default value
                    self.sin_list.append(ImportGenVectSin())
                elif isinstance(obj, dict):
                    self.sin_list.append(ImportGenVectSin(init_dict=obj))
                else:
                    self.sin_list.append(obj)
        elif sin_list is None:
            self.sin_list = list()
        else:
            self.sin_list = sin_list
        # Call ImportMatrix init
        super(ImportGenMatrixSin, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportGenMatrixSin_dict = super(ImportGenMatrixSin, self).as_dict()
        ImportGenMatrixSin_dict["sin_list"] = list()
        for obj in self.sin_list:
            ImportGenMatrixSin_dict["sin_list"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportGenMatrixSin_dict["__class__"] = "ImportGenMatrixSin"
        return ImportGenMatrixSin_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.sin_list:
            obj._set_None()
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenMatrixSin, self)._set_None()

    def _get_sin_list(self):
        """getter of sin_list"""
        for obj in self._sin_list:
            if obj is not None:
                obj.parent = self
        return self._sin_list

    def _set_sin_list(self, value):
        """setter of sin_list"""
        check_var("sin_list", value, "[ImportGenVectSin]")
        self._sin_list = value

        for obj in self._sin_list:
            if obj is not None:
                obj.parent = self

    # List of sinus vector to generate the matrix lines
    # Type : [ImportGenVectSin]
    sin_list = property(
        fget=_get_sin_list,
        fset=_set_sin_list,
        doc=u"""List of sinus vector to generate the matrix lines""",
    )
