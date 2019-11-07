# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Import import Import

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Import.ImportMatlab.get_data import get_data
except ImportError as error:
    get_data = error


from pyleecan.Classes.check import InitUnKnowClassError


class ImportMatlab(Import):
    """Import the data from a mat file"""

    VERSION = 1

    # cf Methods.Import.ImportMatlab.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportMatlab method get_data: " + str(get_data))
            )
        )
    else:
        get_data = get_data
    # save method is available in all object
    save = save

    def __init__(self, file_path="", var_name="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["file_path", "var_name"])
            # Overwrite default value with init_dict content
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
            if "var_name" in list(init_dict.keys()):
                var_name = init_dict["var_name"]
        # Initialisation by argument
        self.file_path = file_path
        self.var_name = var_name
        # Call Import init
        super(ImportMatlab, self).__init__()
        # The class is frozen (in Import init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportMatlab_str = ""
        # Get the properties inherited from Import
        ImportMatlab_str += super(ImportMatlab, self).__str__() + linesep
        ImportMatlab_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        ImportMatlab_str += 'var_name = "' + str(self.var_name) + '"'
        return ImportMatlab_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Import
        if not super(ImportMatlab, self).__eq__(other):
            return False
        if other.file_path != self.file_path:
            return False
        if other.var_name != self.var_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Import
        ImportMatlab_dict = super(ImportMatlab, self).as_dict()
        ImportMatlab_dict["file_path"] = self.file_path
        ImportMatlab_dict["var_name"] = self.var_name
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportMatlab_dict["__class__"] = "ImportMatlab"
        return ImportMatlab_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        self.var_name = None
        # Set to None the properties inherited from Import
        super(ImportMatlab, self)._set_None()

    def _get_file_path(self):
        """getter of file_path"""
        return self._file_path

    def _set_file_path(self, value):
        """setter of file_path"""
        check_var("file_path", value, "str")
        self._file_path = value

    # Path of the file to load
    # Type : str
    file_path = property(
        fget=_get_file_path, fset=_set_file_path, doc=u"""Path of the file to load"""
    )

    def _get_var_name(self):
        """getter of var_name"""
        return self._var_name

    def _set_var_name(self, value):
        """setter of var_name"""
        check_var("var_name", value, "str")
        self._var_name = value

    # Name of the variable to load
    # Type : str
    var_name = property(
        fget=_get_var_name, fset=_set_var_name, doc=u"""Name of the variable to load"""
    )
