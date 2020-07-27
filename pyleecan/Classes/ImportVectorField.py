# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Import/ImportVectorField.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportVectorField.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError
from .ImportData import ImportData


class ImportVectorField(FrozenClass):
    """Abstract class for Data Import/Generation"""

    VERSION = 1

    # cf Methods.Import.ImportVectorField.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportVectorField method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
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
        self, components=dict(), name="", symbol="", init_dict=None, init_str=None
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
            components = obj.components
            name = obj.name
            symbol = obj.symbol
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "components" in list(init_dict.keys()):
                components = init_dict["components"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
        # Initialisation by argument
        self.parent = None
        # components can be None or a dict of ImportData object
        self.components = dict()
        if type(components) is dict:
            for key, obj in components.items():
                if isinstance(obj, dict):
                    self.components[key] = ImportData(init_dict=obj)
                else:
                    self.components[key] = obj
        elif components is None:
            self.components = dict()
        else:
            self.components = components  # Should raise an error
        self.name = name
        self.symbol = symbol

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportVectorField_str = ""
        if self.parent is None:
            ImportVectorField_str += "parent = None " + linesep
        else:
            ImportVectorField_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if len(self.components) == 0:
            ImportVectorField_str += "components = dict()" + linesep
        for key, obj in self.components.items():
            tmp = (
                self.components[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            ImportVectorField_str += (
                "components[" + key + "] =" + tmp + linesep + linesep
            )
        ImportVectorField_str += 'name = "' + str(self.name) + '"' + linesep
        ImportVectorField_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        return ImportVectorField_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.components != self.components:
            return False
        if other.name != self.name:
            return False
        if other.symbol != self.symbol:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        ImportVectorField_dict = dict()
        ImportVectorField_dict["components"] = dict()
        for key, obj in self.components.items():
            ImportVectorField_dict["components"][key] = obj.as_dict()
        ImportVectorField_dict["name"] = self.name
        ImportVectorField_dict["symbol"] = self.symbol
        # The class name is added to the dict fordeserialisation purpose
        ImportVectorField_dict["__class__"] = "ImportVectorField"
        return ImportVectorField_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for key, obj in self.components.items():
            obj._set_None()
        self.name = None
        self.symbol = None

    def _get_components(self):
        """getter of components"""
        for key, obj in self._components.items():
            if obj is not None:
                obj.parent = self
        return self._components

    def _set_components(self, value):
        """setter of components"""
        check_var("components", value, "{ImportData}")
        self._components = value

    # Dict of components (e.g. {"radial": ImportData})
    # Type : {ImportData}
    components = property(
        fget=_get_components,
        fset=_set_components,
        doc=u"""Dict of components (e.g. {"radial": ImportData})""",
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the vector field
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the vector field""")

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    # Symbol of the vector field
    # Type : str
    symbol = property(
        fget=_get_symbol, fset=_set_symbol, doc=u"""Symbol of the vector field"""
    )
