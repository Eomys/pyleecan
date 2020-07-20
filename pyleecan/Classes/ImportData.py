# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Import/ImportData.csv
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
        self,
        axes=list(),
        field=None,
        unit="SI",
        name="",
        symbol="",
        is_freq=False,
        init_dict=None,
        init_str=None,
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

        if field == -1:
            field = Import()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            axes = obj.axes
            field = obj.field
            unit = obj.unit
            name = obj.name
            symbol = obj.symbol
            is_freq = obj.is_freq
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
            if "is_freq" in list(init_dict.keys()):
                is_freq = init_dict["is_freq"]
        # Initialisation by argument
        self.parent = None
        # axes can be None or a list of ImportData object
        self.axes = list()
        if type(axes) is list:
            for obj in axes:
                if obj is None:  # Default value
                    self.axes.append(ImportData())
                elif isinstance(obj, dict):
                    self.axes.append(ImportData(init_dict=obj))
                else:
                    self.axes.append(obj)
        elif axes is None:
            self.axes = list()
        else:
            self.axes = axes
        # field can be None, a Import object or a dict
        if isinstance(field, dict):
            # Check that the type is correct (including daughter)
            class_name = field.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for field"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.field = class_obj(init_dict=field)
        elif isinstance(field, str):
            from ..Functions.load import load

            field = load(field)
            # Check that the type is correct (including daughter)
            class_name = field.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for field"
                )
            self.field = field
        else:
            self.field = field
        self.unit = unit
        self.name = name
        self.symbol = symbol
        self.is_freq = is_freq

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
        ImportData_str += "is_freq = " + str(self.is_freq) + linesep
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
        if other.is_freq != self.is_freq:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        ImportData_dict = dict()
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
        ImportData_dict["is_freq"] = self.is_freq
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
        self.is_freq = None

    def _get_axes(self):
        """getter of axes"""
        for obj in self._axes:
            if obj is not None:
                obj.parent = self
        return self._axes

    def _set_axes(self, value):
        """setter of axes"""
        check_var("axes", value, "[ImportData]")
        self._axes = value

        for obj in self._axes:
            if obj is not None:
                obj.parent = self

    # List of axes of the data
    # Type : [ImportData]
    axes = property(fget=_get_axes, fset=_set_axes, doc=u"""List of axes of the data""")

    def _get_field(self):
        """getter of field"""
        return self._field

    def _set_field(self, value):
        """setter of field"""
        check_var("field", value, "Import")
        self._field = value

        if self._field is not None:
            self._field.parent = self

    # Field (Import object)
    # Type : Import
    field = property(fget=_get_field, fset=_set_field, doc=u"""Field (Import object)""")

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    # Unit of the field
    # Type : str
    unit = property(fget=_get_unit, fset=_set_unit, doc=u"""Unit of the field""")

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the field
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the field""")

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    # Symbol of the field
    # Type : str
    symbol = property(
        fget=_get_symbol, fset=_set_symbol, doc=u"""Symbol of the field"""
    )

    def _get_is_freq(self):
        """getter of is_freq"""
        return self._is_freq

    def _set_is_freq(self, value):
        """setter of is_freq"""
        check_var("is_freq", value, "bool")
        self._is_freq = value

    # Field is imported in frequential domain
    # Type : bool
    is_freq = property(
        fget=_get_is_freq,
        fset=_set_is_freq,
        doc=u"""Field is imported in frequential domain""",
    )
