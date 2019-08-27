# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.ImportMatrix import ImportMatrix

from pyleecan.Methods.Import.ImportFemmMesh.get_data import get_data

from pyleecan.Classes.check import InitUnKnowClassError


class ImportFemmMesh(ImportMatrix):
    """Import a mesh from a .dat file"""

    VERSION = 1

    # cf Methods.Import.ImportFemmMesh.get_data
    get_data = get_data
    # save method is available in all object
    save = save

    def __init__(self, project_path="", is_transpose=False, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["project_path", "is_transpose"])
            # Overwrite default value with init_dict content
            if "project_path" in list(init_dict.keys()):
                project_path = init_dict["project_path"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        self.project_path = project_path
        # Call ImportMatrix init
        super(ImportFemmMesh, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportFemmMesh_str = ""
        # Get the properties inherited from ImportMatrix
        ImportFemmMesh_str += super(ImportFemmMesh, self).__str__() + linesep
        ImportFemmMesh_str += 'project_path = "' + str(self.project_path) + '"'
        return ImportFemmMesh_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportFemmMesh, self).__eq__(other):
            return False
        if other.project_path != self.project_path:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportFemmMesh_dict = super(ImportFemmMesh, self).as_dict()
        ImportFemmMesh_dict["project_path"] = self.project_path
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportFemmMesh_dict["__class__"] = "ImportFemmMesh"
        return ImportFemmMesh_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.project_path = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportFemmMesh, self)._set_None()

    def _get_project_path(self):
        """getter of project_path"""
        return self._project_path

    def _set_project_path(self, value):
        """setter of project_path"""
        check_var("project_path", value, "str")
        self._project_path = value

    # Path of the files to load
    # Type : str
    project_path = property(fget=_get_project_path, fset=_set_project_path,
                            doc=u"""Path of the files to load""")
