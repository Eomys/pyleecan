# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/SkewModel.csv
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
    from ..Methods.Simulation.SkewModel.comp_dist import comp_dist
except ImportError as error:
    comp_dist = error

try:
    from ..Methods.Simulation.SkewModel.comp_skew import comp_skew
except ImportError as error:
    comp_skew = error

try:
    from ..Methods.Simulation.SkewModel.plot import plot
except ImportError as error:
    plot = error


from ._check import InitUnKnowClassError


class SkewModel(FrozenClass):
    """Class for the skew model"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.SkewModel.comp_dist
    if isinstance(comp_dist, ImportError):
        comp_dist = property(
            fget=lambda x: raise_(
                ImportError("Can't use SkewModel method comp_dist: " + str(comp_dist))
            )
        )
    else:
        comp_dist = comp_dist
    # cf Methods.Simulation.SkewModel.comp_skew
    if isinstance(comp_skew, ImportError):
        comp_skew = property(
            fget=lambda x: raise_(
                ImportError("Can't use SkewModel method comp_skew: " + str(comp_skew))
            )
        )
    else:
        comp_skew = comp_skew
    # cf Methods.Simulation.SkewModel.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use SkewModel method plot: " + str(plot))
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
        type_dist="const",
        Nslices=5,
        z_list=None,
        angle_list_rotor=None,
        angle_list_stator=None,
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
            type_dist = obj.type_dist
            Nslices = obj.Nslices
            z_list = obj.z_list
            angle_list_rotor = obj.angle_list_rotor
            angle_list_stator = obj.angle_list_stator
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "type_dist" in list(init_dict.keys()):
                type_dist = init_dict["type_dist"]
            if "Nslices" in list(init_dict.keys()):
                Nslices = init_dict["Nslices"]
            if "z_list" in list(init_dict.keys()):
                z_list = init_dict["z_list"]
            if "angle_list_rotor" in list(init_dict.keys()):
                angle_list_rotor = init_dict["angle_list_rotor"]
            if "angle_list_stator" in list(init_dict.keys()):
                angle_list_stator = init_dict["angle_list_stator"]
        # Initialisation by argument
        self.parent = None
        self.type_dist = type_dist
        self.Nslices = Nslices
        self.z_list = z_list
        self.angle_list_rotor = angle_list_rotor
        self.angle_list_stator = angle_list_stator

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SkewModel_str = ""
        if self.parent is None:
            SkewModel_str += "parent = None " + linesep
        else:
            SkewModel_str += "parent = " + str(type(self.parent)) + " object" + linesep
        SkewModel_str += 'type_dist = "' + str(self.type_dist) + '"' + linesep
        SkewModel_str += "Nslices = " + str(self.Nslices) + linesep
        SkewModel_str += (
            "z_list = "
            + linesep
            + str(self.z_list).replace(linesep, linesep + "\t")
            + linesep
        )
        SkewModel_str += (
            "angle_list_rotor = "
            + linesep
            + str(self.angle_list_rotor).replace(linesep, linesep + "\t")
            + linesep
        )
        SkewModel_str += (
            "angle_list_stator = "
            + linesep
            + str(self.angle_list_stator).replace(linesep, linesep + "\t")
            + linesep
        )
        return SkewModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_dist != self.type_dist:
            return False
        if other.Nslices != self.Nslices:
            return False
        if other.z_list != self.z_list:
            return False
        if other.angle_list_rotor != self.angle_list_rotor:
            return False
        if other.angle_list_stator != self.angle_list_stator:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        SkewModel_dict = dict()
        SkewModel_dict["type_dist"] = self.type_dist
        SkewModel_dict["Nslices"] = self.Nslices
        SkewModel_dict["z_list"] = self.z_list
        SkewModel_dict["angle_list_rotor"] = self.angle_list_rotor
        SkewModel_dict["angle_list_stator"] = self.angle_list_stator
        # The class name is added to the dict fordeserialisation purpose
        SkewModel_dict["__class__"] = "SkewModel"
        return SkewModel_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_dist = None
        self.Nslices = None
        self.z_list = None
        self.angle_list_rotor = None
        self.angle_list_stator = None

    def _get_type_dist(self):
        """getter of type_dist"""
        return self._type_dist

    def _set_type_dist(self, value):
        """setter of type_dist"""
        check_var("type_dist", value, "str")
        self._type_dist = value

    # Type of slice distribution to use for rotor skew ("uniform", "gauss", "user-defined")
    # Type : str
    type_dist = property(
        fget=_get_type_dist,
        fset=_set_type_dist,
        doc=u"""Type of slice distribution to use for rotor skew ("uniform", "gauss", "user-defined")""",
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

    def _get_z_list(self):
        """getter of z_list"""
        return self._z_list

    def _set_z_list(self, value):
        """setter of z_list"""
        check_var("z_list", value, "list")
        self._z_list = value

    # List of slice positions (for user-defined skew) to be multiplied by lamination length
    # Type : list
    z_list = property(
        fget=_get_z_list,
        fset=_set_z_list,
        doc=u"""List of slice positions (for user-defined skew) to be multiplied by lamination length""",
    )

    def _get_angle_list_rotor(self):
        """getter of angle_list_rotor"""
        return self._angle_list_rotor

    def _set_angle_list_rotor(self, value):
        """setter of angle_list_rotor"""
        check_var("angle_list_rotor", value, "list")
        self._angle_list_rotor = value

    # List of rotor skew angles for user-defined skew (optional)
    # Type : list
    angle_list_rotor = property(
        fget=_get_angle_list_rotor,
        fset=_set_angle_list_rotor,
        doc=u"""List of rotor skew angles for user-defined skew (optional)""",
    )

    def _get_angle_list_stator(self):
        """getter of angle_list_stator"""
        return self._angle_list_stator

    def _set_angle_list_stator(self, value):
        """setter of angle_list_stator"""
        check_var("angle_list_stator", value, "list")
        self._angle_list_stator = value

    # List of stator skew angles for user-defined skew (optional)
    # Type : list
    angle_list_stator = property(
        fget=_get_angle_list_stator,
        fset=_set_angle_list_stator,
        doc=u"""List of stator skew angles for user-defined skew (optional)""",
    )
