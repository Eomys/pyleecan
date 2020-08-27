# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/Skew.csv
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
    from ..Methods.Machine.Skew.comp_angle import comp_angle
except ImportError as error:
    comp_angle = error

try:
    from ..Methods.Machine.Skew.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.Skew.get_angle_unique import get_angle_unique
except ImportError as error:
    get_angle_unique = error

try:
    from ..Methods.Machine.Skew.get_ind_unique import get_ind_unique
except ImportError as error:
    get_ind_unique = error


from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class Skew(FrozenClass):
    """Class for the skew (rotor or stator)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Skew.comp_angle
    if isinstance(comp_angle, ImportError):
        comp_angle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Skew method comp_angle: " + str(comp_angle))
            )
        )
    else:
        comp_angle = comp_angle
    # cf Methods.Machine.Skew.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Skew method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.Skew.get_angle_unique
    if isinstance(get_angle_unique, ImportError):
        get_angle_unique = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Skew method get_angle_unique: " + str(get_angle_unique)
                )
            )
        )
    else:
        get_angle_unique = get_angle_unique
    # cf Methods.Machine.Skew.get_ind_unique
    if isinstance(get_ind_unique, ImportError):
        get_ind_unique = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Skew method get_ind_unique: " + str(get_ind_unique)
                )
            )
        )
    else:
        get_ind_unique = get_ind_unique
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
        type=None,
        rate=0,
        is_step=True,
        function=None,
        angle_list=None,
        z_list=None,
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

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            type = obj.type
            rate = obj.rate
            is_step = obj.is_step
            function = obj.function
            angle_list = obj.angle_list
            z_list = obj.z_list
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "type" in list(init_dict.keys()):
                type = init_dict["type"]
            if "rate" in list(init_dict.keys()):
                rate = init_dict["rate"]
            if "is_step" in list(init_dict.keys()):
                is_step = init_dict["is_step"]
            if "function" in list(init_dict.keys()):
                function = init_dict["function"]
            if "angle_list" in list(init_dict.keys()):
                angle_list = init_dict["angle_list"]
            if "z_list" in list(init_dict.keys()):
                z_list = init_dict["z_list"]
        # Initialisation by argument
        self.parent = None
        self.type = type
        self.rate = rate
        self.is_step = is_step
        self.function = function
        self.angle_list = angle_list
        self.z_list = z_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Skew_str = ""
        if self.parent is None:
            Skew_str += "parent = None " + linesep
        else:
            Skew_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Skew_str += 'type = "' + str(self.type) + '"' + linesep
        Skew_str += "rate = " + str(self.rate) + linesep
        Skew_str += "is_step = " + str(self.is_step) + linesep
        if self._function[1] is None:
            Skew_str += "function = " + str(self._function[1])
        else:
            Skew_str += (
                "function = " + linesep + str(self._function[1]) + linesep + linesep
            )
        Skew_str += (
            "angle_list = "
            + linesep
            + str(self.angle_list).replace(linesep, linesep + "\t")
            + linesep
        )
        Skew_str += (
            "z_list = "
            + linesep
            + str(self.z_list).replace(linesep, linesep + "\t")
            + linesep
        )
        return Skew_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type != self.type:
            return False
        if other.rate != self.rate:
            return False
        if other.is_step != self.is_step:
            return False
        if other.function != self.function:
            return False
        if other.angle_list != self.angle_list:
            return False
        if other.z_list != self.z_list:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Skew_dict = dict()
        Skew_dict["type"] = self.type
        Skew_dict["rate"] = self.rate
        Skew_dict["is_step"] = self.is_step
        if self.function is None:
            Skew_dict["function"] = None
        else:
            Skew_dict["function"] = [
                dumps(self._function[0]).decode("ISO-8859-2"),
                self._function[1],
            ]
        Skew_dict["angle_list"] = self.angle_list
        Skew_dict["z_list"] = self.z_list
        # The class name is added to the dict fordeserialisation purpose
        Skew_dict["__class__"] = "Skew"
        return Skew_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type = None
        self.rate = None
        self.is_step = None
        self.function = None
        self.angle_list = None
        self.z_list = None

    def _get_type(self):
        """getter of type"""
        return self._type

    def _set_type(self, value):
        """setter of type"""
        check_var("type", value, "str")
        self._type = value

    # Type of skew ("linear", "vshape", "function", "user-defined")
    # Type : str
    type = property(
        fget=_get_type,
        fset=_set_type,
        doc=u"""Type of skew ("linear", "vshape", "function", "user-defined")""",
    )

    def _get_rate(self):
        """getter of rate"""
        return self._rate

    def _set_rate(self, value):
        """setter of rate"""
        check_var("rate", value, "float")
        self._rate = value

    # Skew rate
    # Type : float
    rate = property(fget=_get_rate, fset=_set_rate, doc=u"""Skew rate""")

    def _get_is_step(self):
        """getter of is_step"""
        return self._is_step

    def _set_is_step(self, value):
        """setter of is_step"""
        check_var("is_step", value, "bool")
        self._is_step = value

    # Skew is defined as steps
    # Type : bool
    is_step = property(
        fget=_get_is_step, fset=_set_is_step, doc=u"""Skew is defined as steps"""
    )

    def _get_function(self):
        """getter of function"""
        return self._function[0]

    def _set_function(self, value):
        """setter of function"""
        try:
            check_var("function", value, "list")
        except CheckTypeError:
            check_var("function", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._function = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._function = [None, None]
        elif callable(value):
            self._function = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Function for function skew
    # Type : function
    function = property(
        fget=_get_function, fset=_set_function, doc=u"""Function for function skew"""
    )

    def _get_angle_list(self):
        """getter of angle_list"""
        return self._angle_list

    def _set_angle_list(self, value):
        """setter of angle_list"""
        check_var("angle_list", value, "list")
        self._angle_list = value

    # List of skew angles
    # Type : list
    angle_list = property(
        fget=_get_angle_list, fset=_set_angle_list, doc=u"""List of skew angles"""
    )

    def _get_z_list(self):
        """getter of z_list"""
        return self._z_list

    def _set_z_list(self, value):
        """setter of z_list"""
        check_var("z_list", value, "list")
        self._z_list = value

    # List of slice positions
    # Type : list
    z_list = property(
        fget=_get_z_list, fset=_set_z_list, doc=u"""List of slice positions"""
    )
