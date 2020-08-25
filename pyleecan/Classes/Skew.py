# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Skew.csv
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
    from ..Methods.Simulation.Skew.comp_angle import comp_angle
except ImportError as error:
    comp_angle = error

try:
    from ..Methods.Simulation.Skew.plot import plot
except ImportError as error:
    plot = error


from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class Skew(FrozenClass):
    """Class for the skew (rotor or stator)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Skew.comp_angle
    if isinstance(comp_angle, ImportError):
        comp_angle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Skew method comp_angle: " + str(comp_angle))
            )
        )
    else:
        comp_angle = comp_angle
    # cf Methods.Simulation.Skew.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Skew method plot: " + str(plot))
            )
        )
    else:
        plot = plot
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
        Nslices=10,
        rate=0,
        Nsegm=None,
        curve=None,
        angle_list=None,
        index_list=None,
        is_stator=True,
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
            Nslices = obj.Nslices
            rate = obj.rate
            Nsegm = obj.Nsegm
            curve = obj.curve
            angle_list = obj.angle_list
            index_list = obj.index_list
            is_stator = obj.is_stator
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "type" in list(init_dict.keys()):
                type = init_dict["type"]
            if "Nslices" in list(init_dict.keys()):
                Nslices = init_dict["Nslices"]
            if "rate" in list(init_dict.keys()):
                rate = init_dict["rate"]
            if "Nsegm" in list(init_dict.keys()):
                Nsegm = init_dict["Nsegm"]
            if "curve" in list(init_dict.keys()):
                curve = init_dict["curve"]
            if "angle_list" in list(init_dict.keys()):
                angle_list = init_dict["angle_list"]
            if "index_list" in list(init_dict.keys()):
                index_list = init_dict["index_list"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
        # Initialisation by argument
        self.parent = None
        self.type = type
        self.Nslices = Nslices
        self.rate = rate
        self.Nsegm = Nsegm
        self.curve = curve
        self.angle_list = angle_list
        self.index_list = index_list
        self.is_stator = is_stator

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
        Skew_str += "Nslices = " + str(self.Nslices) + linesep
        Skew_str += "rate = " + str(self.rate) + linesep
        Skew_str += "Nsegm = " + str(self.Nsegm) + linesep
        if self._curve[1] is None:
            Skew_str += "curve = " + str(self._curve[1])
        else:
            Skew_str += "curve = " + linesep + str(self._curve[1]) + linesep + linesep
        Skew_str += (
            "angle_list = "
            + linesep
            + str(self.angle_list).replace(linesep, linesep + "\t")
            + linesep
        )
        Skew_str += (
            "index_list = "
            + linesep
            + str(self.index_list).replace(linesep, linesep + "\t")
            + linesep
        )
        Skew_str += "is_stator = " + str(self.is_stator) + linesep
        return Skew_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type != self.type:
            return False
        if other.Nslices != self.Nslices:
            return False
        if other.rate != self.rate:
            return False
        if other.Nsegm != self.Nsegm:
            return False
        if other.curve != self.curve:
            return False
        if other.angle_list != self.angle_list:
            return False
        if other.index_list != self.index_list:
            return False
        if other.is_stator != self.is_stator:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Skew_dict = dict()
        Skew_dict["type"] = self.type
        Skew_dict["Nslices"] = self.Nslices
        Skew_dict["rate"] = self.rate
        Skew_dict["Nsegm"] = self.Nsegm
        if self.curve is None:
            Skew_dict["curve"] = None
        else:
            Skew_dict["curve"] = [
                dumps(self._curve[0]).decode("ISO-8859-2"),
                self._curve[1],
            ]
        Skew_dict["angle_list"] = self.angle_list
        Skew_dict["index_list"] = self.index_list
        Skew_dict["is_stator"] = self.is_stator
        # The class name is added to the dict fordeserialisation purpose
        Skew_dict["__class__"] = "Skew"
        return Skew_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type = None
        self.Nslices = None
        self.rate = None
        self.Nsegm = None
        self.curve = None
        self.angle_list = None
        self.index_list = None
        self.is_stator = None

    def _get_type(self):
        """getter of type"""
        return self._type

    def _set_type(self, value):
        """setter of type"""
        check_var("type", value, "str")
        self._type = value

    # Type of skew ("linear", "step", "vshape", "user-defined")
    # Type : str
    type = property(
        fget=_get_type,
        fset=_set_type,
        doc=u"""Type of skew ("linear", "step", "vshape", "user-defined")""",
    )

    def _get_Nslices(self):
        """getter of Nslices"""
        return self._Nslices

    def _set_Nslices(self, value):
        """setter of Nslices"""
        check_var("Nslices", value, "int")
        self._Nslices = value

    # Number of slices
    # Type : int
    Nslices = property(
        fget=_get_Nslices, fset=_set_Nslices, doc=u"""Number of slices"""
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

    def _get_Nsegm(self):
        """getter of Nsegm"""
        return self._Nsegm

    def _set_Nsegm(self, value):
        """setter of Nsegm"""
        check_var("Nsegm", value, "int")
        self._Nsegm = value

    # Number of segments for step skew
    # Type : int
    Nsegm = property(
        fget=_get_Nsegm, fset=_set_Nsegm, doc=u"""Number of segments for step skew"""
    )

    def _get_curve(self):
        """getter of curve"""
        return self._curve[0]

    def _set_curve(self, value):
        """setter of curve"""
        try:
            check_var("curve", value, "list")
        except CheckTypeError:
            check_var("curve", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._curve = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._curve = [None, None]
        elif callable(value):
            self._curve = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Curve for user-defined skew
    # Type : function
    curve = property(
        fget=_get_curve, fset=_set_curve, doc=u"""Curve for user-defined skew"""
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

    def _get_index_list(self):
        """getter of index_list"""
        return self._index_list

    def _set_index_list(self, value):
        """setter of index_list"""
        check_var("index_list", value, "list")
        self._index_list = value

    # List of indices to avoid redundant computations
    # Type : list
    index_list = property(
        fget=_get_index_list,
        fset=_set_index_list,
        doc=u"""List of indices to avoid redundant computations""",
    )

    def _get_is_stator(self):
        """getter of is_stator"""
        return self._is_stator

    def _set_is_stator(self, value):
        """setter of is_stator"""
        check_var("is_stator", value, "bool")
        self._is_stator = value

    # Is the skew defined for a stator
    # Type : bool
    is_stator = property(
        fget=_get_is_stator,
        fset=_set_is_stator,
        doc=u"""Is the skew defined for a stator""",
    )
