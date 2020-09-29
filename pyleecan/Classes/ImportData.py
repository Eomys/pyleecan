# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportData.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportData
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportData.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError
from .Import import Import


class ImportData(FrozenClass):
    """Abstract class for Data Import/Generation"""

    VERSION = 1

    # cf Methods.Import.ImportData.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportData method get_data: " + str(get_data))
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        axes=-1,
        field=None,
        unit="SI",
        name="",
        symbol="",
        normalizations=-1,
        symmetries=-1,
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
            if "axes" in list(init_dict.keys()):
                axes = init_dict["axes"]
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "normalizations" in list(init_dict.keys()):
                normalizations = init_dict["normalizations"]
            if "symmetries" in list(init_dict.keys()):
                symmetries = init_dict["symmetries"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.axes = axes
        self.field = field
        self.unit = unit
        self.name = name
        self.symbol = symbol
        self.normalizations = normalizations
        self.symmetries = symmetries

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportData_str = ""
        if self.parent is None:
            ImportData_str += "parent = None " + linesep
        else:
            ImportData_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if len(self.axes) == 0:
            ImportData_str += "axes = []" + linesep
        for ii in range(len(self.axes)):
            tmp = self.axes[ii].__str__().replace(linesep, linesep + "\t") + linesep
            ImportData_str += "axes[" + str(ii) + "] =" + tmp + linesep + linesep
        if self.field is not None:
            tmp = self.field.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            ImportData_str += "field = " + tmp
        else:
            ImportData_str += "field = None" + linesep + linesep
        ImportData_str += 'unit = "' + str(self.unit) + '"' + linesep
        ImportData_str += 'name = "' + str(self.name) + '"' + linesep
        ImportData_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        ImportData_str += "normalizations = " + str(self.normalizations) + linesep
        ImportData_str += "symmetries = " + str(self.symmetries) + linesep
        return ImportData_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.axes != self.axes:
            return False
        if other.field != self.field:
            return False
        if other.unit != self.unit:
            return False
        if other.name != self.name:
            return False
        if other.symbol != self.symbol:
            return False
        if other.normalizations != self.normalizations:
            return False
        if other.symmetries != self.symmetries:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        ImportData_dict = dict()
        if self.axes is None:
            ImportData_dict["axes"] = None
        else:
            ImportData_dict["axes"] = list()
            for obj in self.axes:
                ImportData_dict["axes"].append(obj.as_dict())
        if self.field is None:
            ImportData_dict["field"] = None
        else:
            ImportData_dict["field"] = self.field.as_dict()
        ImportData_dict["unit"] = self.unit
        ImportData_dict["name"] = self.name
        ImportData_dict["symbol"] = self.symbol
        ImportData_dict["normalizations"] = self.normalizations
        ImportData_dict["symmetries"] = self.symmetries
        # The class name is added to the dict fordeserialisation purpose
        ImportData_dict["__class__"] = "ImportData"
        return ImportData_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.axes:
            obj._set_None()
        if self.field is not None:
            self.field._set_None()
        self.unit = None
        self.name = None
        self.symbol = None
        self.normalizations = None
        self.symmetries = None

    def _get_axes(self):
        """getter of axes"""
        if self._axes is not None:
            for obj in self._axes:
                if obj is not None:
                    obj.parent = self
        return self._axes

    def _set_axes(self, value):
        """setter of axes"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "axes"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("axes", value, "[ImportData]")
        self._axes = value

    axes = property(
        fget=_get_axes,
        fset=_set_axes,
        doc=u"""List of axes of the data

        :Type: [ImportData]
        """,
    )

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "field"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Import()
        check_var("field", value, "Import")
        self._field = value

        if self._field is not None:
            self._field.parent = self

    field = property(
        fget=_get_field,
        fset=_set_field,
        doc=u"""Field (Import object)

        :Type: Import
        """,
    )

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc=u"""Unit of the field

        :Type: str
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the field

        :Type: str
        """,
    )

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    symbol = property(
        fget=_get_symbol,
        fset=_set_symbol,
        doc=u"""Symbol of the field

        :Type: str
        """,
    )

    def _get_normalizations(self):
        """getter of normalizations"""
        return self._normalizations

    def _set_normalizations(self, value):
        """setter of normalizations"""
        if value is -1:
            value = dict()
        check_var("normalizations", value, "dict")
        self._normalizations = value

    normalizations = property(
        fget=_get_normalizations,
        fset=_set_normalizations,
        doc=u"""Dict of normalizations

        :Type: dict
        """,
    )

    def _get_symmetries(self):
        """getter of symmetries"""
        return self._symmetries

    def _set_symmetries(self, value):
        """setter of symmetries"""
        if value is -1:
            value = dict()
        check_var("symmetries", value, "dict")
        self._symmetries = value

    symmetries = property(
        fget=_get_symmetries,
        fset=_set_symmetries,
        doc=u"""Dict of symmetries

        :Type: dict
        """,
    )
