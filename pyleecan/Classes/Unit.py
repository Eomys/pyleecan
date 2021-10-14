# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/GUI_Option/Unit.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/GUI_Option/Unit
"""

from os import linesep
from sys import getsizeof
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
    from ..Methods.GUI_Option.Unit.get_m import get_m
except ImportError as error:
    get_m = error

try:
    from ..Methods.GUI_Option.Unit.get_m2 import get_m2
except ImportError as error:
    get_m2 = error

try:
    from ..Methods.GUI_Option.Unit.get_m_name import get_m_name
except ImportError as error:
    get_m_name = error

try:
    from ..Methods.GUI_Option.Unit.get_m2_name import get_m2_name
except ImportError as error:
    get_m2_name = error

try:
    from ..Methods.GUI_Option.Unit.set_m import set_m
except ImportError as error:
    set_m = error

try:
    from ..Methods.GUI_Option.Unit.set_m2 import set_m2
except ImportError as error:
    set_m2 = error


from ._check import InitUnKnowClassError


class Unit(FrozenClass):

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.GUI_Option.Unit.get_m
    if isinstance(get_m, ImportError):
        get_m = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method get_m: " + str(get_m))
            )
        )
    else:
        get_m = get_m
    # cf Methods.GUI_Option.Unit.get_m2
    if isinstance(get_m2, ImportError):
        get_m2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method get_m2: " + str(get_m2))
            )
        )
    else:
        get_m2 = get_m2
    # cf Methods.GUI_Option.Unit.get_m_name
    if isinstance(get_m_name, ImportError):
        get_m_name = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method get_m_name: " + str(get_m_name))
            )
        )
    else:
        get_m_name = get_m_name
    # cf Methods.GUI_Option.Unit.get_m2_name
    if isinstance(get_m2_name, ImportError):
        get_m2_name = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method get_m2_name: " + str(get_m2_name))
            )
        )
    else:
        get_m2_name = get_m2_name
    # cf Methods.GUI_Option.Unit.set_m
    if isinstance(set_m, ImportError):
        set_m = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method set_m: " + str(set_m))
            )
        )
    else:
        set_m = set_m
    # cf Methods.GUI_Option.Unit.set_m2
    if isinstance(set_m2, ImportError):
        set_m2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use Unit method set_m2: " + str(set_m2))
            )
        )
    else:
        set_m2 = set_m2
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, unit_m=0, unit_rad=0, unit_m2=0, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "unit_m" in list(init_dict.keys()):
                unit_m = init_dict["unit_m"]
            if "unit_rad" in list(init_dict.keys()):
                unit_rad = init_dict["unit_rad"]
            if "unit_m2" in list(init_dict.keys()):
                unit_m2 = init_dict["unit_m2"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.unit_m = unit_m
        self.unit_rad = unit_rad
        self.unit_m2 = unit_m2

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Unit_str = ""
        if self.parent is None:
            Unit_str += "parent = None " + linesep
        else:
            Unit_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Unit_str += "unit_m = " + str(self.unit_m) + linesep
        Unit_str += "unit_rad = " + str(self.unit_rad) + linesep
        Unit_str += "unit_m2 = " + str(self.unit_m2) + linesep
        return Unit_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.unit_m != self.unit_m:
            return False
        if other.unit_rad != self.unit_rad:
            return False
        if other.unit_m2 != self.unit_m2:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._unit_m != self._unit_m:
            diff_list.append(name + ".unit_m")
        if other._unit_rad != self._unit_rad:
            diff_list.append(name + ".unit_rad")
        if other._unit_m2 != self._unit_m2:
            diff_list.append(name + ".unit_m2")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.unit_m)
        S += getsizeof(self.unit_rad)
        S += getsizeof(self.unit_m2)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        Unit_dict = dict()
        Unit_dict["unit_m"] = self.unit_m
        Unit_dict["unit_rad"] = self.unit_rad
        Unit_dict["unit_m2"] = self.unit_m2
        # The class name is added to the dict for deserialisation purpose
        Unit_dict["__class__"] = "Unit"
        return Unit_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.unit_m = None
        self.unit_rad = None
        self.unit_m2 = None

    def _get_unit_m(self):
        """getter of unit_m"""
        return self._unit_m

    def _set_unit_m(self, value):
        """setter of unit_m"""
        check_var("unit_m", value, "int", Vmin=0, Vmax=1)
        self._unit_m = value

    unit_m = property(
        fget=_get_unit_m,
        fset=_set_unit_m,
        doc=u"""0: use m, 1: use mm

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_unit_rad(self):
        """getter of unit_rad"""
        return self._unit_rad

    def _set_unit_rad(self, value):
        """setter of unit_rad"""
        check_var("unit_rad", value, "int", Vmin=0, Vmax=1)
        self._unit_rad = value

    unit_rad = property(
        fget=_get_unit_rad,
        fset=_set_unit_rad,
        doc=u"""0: use rad, 1: use deg

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_unit_m2(self):
        """getter of unit_m2"""
        return self._unit_m2

    def _set_unit_m2(self, value):
        """setter of unit_m2"""
        check_var("unit_m2", value, "int", Vmin=0, Vmax=1)
        self._unit_m2 = value

    unit_m2 = property(
        fget=_get_unit_m2,
        fset=_set_unit_m2,
        doc=u"""0: use m^2, 1: use mm^2

        :Type: int
        :min: 0
        :max: 1
        """,
    )
