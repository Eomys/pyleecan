# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/SliceModel.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/SliceModel
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.SliceModel.get_distribution import get_distribution
except ImportError as error:
    get_distribution = error

try:
    from ..Methods.Simulation.SliceModel.get_data import get_data
except ImportError as error:
    get_data = error

try:
    from ..Methods.Simulation.SliceModel.plot import plot
except ImportError as error:
    plot = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class SliceModel(FrozenClass):
    """Class to hande slices in magnetics model"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.SliceModel.get_distribution
    if isinstance(get_distribution, ImportError):
        get_distribution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SliceModel method get_distribution: "
                    + str(get_distribution)
                )
            )
        )
    else:
        get_distribution = get_distribution
    # cf Methods.Simulation.SliceModel.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use SliceModel method get_data: " + str(get_data))
            )
        )
    else:
        get_data = get_data
    # cf Methods.Simulation.SliceModel.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use SliceModel method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_distribution=None,
        Nslices=5,
        z_list=None,
        angle_rotor=None,
        angle_stator=None,
        L=None,
        is_step=None,
        is_skew=None,
        init_dict=None,
        init_str=None,
    ):
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
            if "type_distribution" in list(init_dict.keys()):
                type_distribution = init_dict["type_distribution"]
            if "Nslices" in list(init_dict.keys()):
                Nslices = init_dict["Nslices"]
            if "z_list" in list(init_dict.keys()):
                z_list = init_dict["z_list"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "angle_stator" in list(init_dict.keys()):
                angle_stator = init_dict["angle_stator"]
            if "L" in list(init_dict.keys()):
                L = init_dict["L"]
            if "is_step" in list(init_dict.keys()):
                is_step = init_dict["is_step"]
            if "is_skew" in list(init_dict.keys()):
                is_skew = init_dict["is_skew"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.type_distribution = type_distribution
        self.Nslices = Nslices
        self.z_list = z_list
        self.angle_rotor = angle_rotor
        self.angle_stator = angle_stator
        self.L = L
        self.is_step = is_step
        self.is_skew = is_skew

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SliceModel_str = ""
        if self.parent is None:
            SliceModel_str += "parent = None " + linesep
        else:
            SliceModel_str += "parent = " + str(type(self.parent)) + " object" + linesep
        SliceModel_str += (
            'type_distribution = "' + str(self.type_distribution) + '"' + linesep
        )
        SliceModel_str += "Nslices = " + str(self.Nslices) + linesep
        SliceModel_str += (
            "z_list = "
            + linesep
            + str(self.z_list).replace(linesep, linesep + "\t")
            + linesep
        )
        SliceModel_str += (
            "angle_rotor = "
            + linesep
            + str(self.angle_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SliceModel_str += (
            "angle_stator = "
            + linesep
            + str(self.angle_stator).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        SliceModel_str += "L = " + str(self.L) + linesep
        SliceModel_str += "is_step = " + str(self.is_step) + linesep
        SliceModel_str += "is_skew = " + str(self.is_skew) + linesep
        return SliceModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_distribution != self.type_distribution:
            return False
        if other.Nslices != self.Nslices:
            return False
        if other.z_list != self.z_list:
            return False
        if not array_equal(other.angle_rotor, self.angle_rotor):
            return False
        if not array_equal(other.angle_stator, self.angle_stator):
            return False
        if other.L != self.L:
            return False
        if other.is_step != self.is_step:
            return False
        if other.is_skew != self.is_skew:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._type_distribution != self._type_distribution:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_distribution)
                    + ", other="
                    + str(other._type_distribution)
                    + ")"
                )
                diff_list.append(name + ".type_distribution" + val_str)
            else:
                diff_list.append(name + ".type_distribution")
        if other._Nslices != self._Nslices:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nslices)
                    + ", other="
                    + str(other._Nslices)
                    + ")"
                )
                diff_list.append(name + ".Nslices" + val_str)
            else:
                diff_list.append(name + ".Nslices")
        if other._z_list != self._z_list:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._z_list)
                    + ", other="
                    + str(other._z_list)
                    + ")"
                )
                diff_list.append(name + ".z_list" + val_str)
            else:
                diff_list.append(name + ".z_list")
        if not array_equal(other.angle_rotor, self.angle_rotor):
            diff_list.append(name + ".angle_rotor")
        if not array_equal(other.angle_stator, self.angle_stator):
            diff_list.append(name + ".angle_stator")
        if (
            other._L is not None
            and self._L is not None
            and isnan(other._L)
            and isnan(self._L)
        ):
            pass
        elif other._L != self._L:
            if is_add_value:
                val_str = " (self=" + str(self._L) + ", other=" + str(other._L) + ")"
                diff_list.append(name + ".L" + val_str)
            else:
                diff_list.append(name + ".L")
        if other._is_step != self._is_step:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_step)
                    + ", other="
                    + str(other._is_step)
                    + ")"
                )
                diff_list.append(name + ".is_step" + val_str)
            else:
                diff_list.append(name + ".is_step")
        if other._is_skew != self._is_skew:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_skew)
                    + ", other="
                    + str(other._is_skew)
                    + ")"
                )
                diff_list.append(name + ".is_skew" + val_str)
            else:
                diff_list.append(name + ".is_skew")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.type_distribution)
        S += getsizeof(self.Nslices)
        if self.z_list is not None:
            for value in self.z_list:
                S += getsizeof(value)
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.angle_stator)
        S += getsizeof(self.L)
        S += getsizeof(self.is_step)
        S += getsizeof(self.is_skew)
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

        SliceModel_dict = dict()
        SliceModel_dict["type_distribution"] = self.type_distribution
        SliceModel_dict["Nslices"] = self.Nslices
        SliceModel_dict["z_list"] = (
            self.z_list.copy() if self.z_list is not None else None
        )
        if self.angle_rotor is None:
            SliceModel_dict["angle_rotor"] = None
        else:
            if type_handle_ndarray == 0:
                SliceModel_dict["angle_rotor"] = self.angle_rotor.tolist()
            elif type_handle_ndarray == 1:
                SliceModel_dict["angle_rotor"] = self.angle_rotor.copy()
            elif type_handle_ndarray == 2:
                SliceModel_dict["angle_rotor"] = self.angle_rotor
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.angle_stator is None:
            SliceModel_dict["angle_stator"] = None
        else:
            if type_handle_ndarray == 0:
                SliceModel_dict["angle_stator"] = self.angle_stator.tolist()
            elif type_handle_ndarray == 1:
                SliceModel_dict["angle_stator"] = self.angle_stator.copy()
            elif type_handle_ndarray == 2:
                SliceModel_dict["angle_stator"] = self.angle_stator
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        SliceModel_dict["L"] = self.L
        SliceModel_dict["is_step"] = self.is_step
        SliceModel_dict["is_skew"] = self.is_skew
        # The class name is added to the dict for deserialisation purpose
        SliceModel_dict["__class__"] = "SliceModel"
        return SliceModel_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_distribution_val = self.type_distribution
        Nslices_val = self.Nslices
        if self.z_list is None:
            z_list_val = None
        else:
            z_list_val = self.z_list.copy()
        if self.angle_rotor is None:
            angle_rotor_val = None
        else:
            angle_rotor_val = self.angle_rotor.copy()
        if self.angle_stator is None:
            angle_stator_val = None
        else:
            angle_stator_val = self.angle_stator.copy()
        L_val = self.L
        is_step_val = self.is_step
        is_skew_val = self.is_skew
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            type_distribution=type_distribution_val,
            Nslices=Nslices_val,
            z_list=z_list_val,
            angle_rotor=angle_rotor_val,
            angle_stator=angle_stator_val,
            L=L_val,
            is_step=is_step_val,
            is_skew=is_skew_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_distribution = None
        self.Nslices = None
        self.z_list = None
        self.angle_rotor = None
        self.angle_stator = None
        self.L = None
        self.is_step = None
        self.is_skew = None

    def _get_type_distribution(self):
        """getter of type_distribution"""
        return self._type_distribution

    def _set_type_distribution(self, value):
        """setter of type_distribution"""
        check_var("type_distribution", value, "str")
        self._type_distribution = value

    type_distribution = property(
        fget=_get_type_distribution,
        fset=_set_type_distribution,
        doc=u"""Type of slice distribution to use for rotor skew if linear and continuous ("uniform", "gauss", "user-defined")

        :Type: str
        """,
    )

    def _get_Nslices(self):
        """getter of Nslices"""
        return self._Nslices

    def _set_Nslices(self, value):
        """setter of Nslices"""
        check_var("Nslices", value, "int")
        self._Nslices = value

    Nslices = property(
        fget=_get_Nslices,
        fset=_set_Nslices,
        doc=u"""Number of slices

        :Type: int
        """,
    )

    def _get_z_list(self):
        """getter of z_list"""
        return self._z_list

    def _set_z_list(self, value):
        """setter of z_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("z_list", value, "list")
        self._z_list = value

    z_list = property(
        fget=_get_z_list,
        fset=_set_z_list,
        doc=u"""List of slice positions

        :Type: list
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_rotor", value, "ndarray")
        self._angle_rotor = value

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Array of rotor skew angles in case of skew

        :Type: ndarray
        """,
    )

    def _get_angle_stator(self):
        """getter of angle_stator"""
        return self._angle_stator

    def _set_angle_stator(self, value):
        """setter of angle_stator"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_stator", value, "ndarray")
        self._angle_stator = value

    angle_stator = property(
        fget=_get_angle_stator,
        fset=_set_angle_stator,
        doc=u"""Array of stator skew angles in case of skew

        :Type: ndarray
        """,
    )

    def _get_L(self):
        """getter of L"""
        return self._L

    def _set_L(self, value):
        """setter of L"""
        check_var("L", value, "float")
        self._L = value

    L = property(
        fget=_get_L,
        fset=_set_L,
        doc=u"""Machine length (mean of rotor/stator lengths)

        :Type: float
        """,
    )

    def _get_is_step(self):
        """getter of is_step"""
        return self._is_step

    def _set_is_step(self, value):
        """setter of is_step"""
        check_var("is_step", value, "bool")
        self._is_step = value

    is_step = property(
        fget=_get_is_step,
        fset=_set_is_step,
        doc=u"""True to define slices as steps

        :Type: bool
        """,
    )

    def _get_is_skew(self):
        """getter of is_skew"""
        return self._is_skew

    def _set_is_skew(self, value):
        """setter of is_skew"""
        check_var("is_skew", value, "bool")
        self._is_skew = value

    is_skew = property(
        fget=_get_is_skew,
        fset=_set_is_skew,
        doc=u"""True if slices account for skew

        :Type: bool
        """,
    )
