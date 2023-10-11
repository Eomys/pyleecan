# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain_Slot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain_Slot
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
from .Subdomain import Subdomain

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Subdomain_Slot.comp_flux_density import comp_flux_density
except ImportError as error:
    comp_flux_density = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_Slot(Subdomain):
    """Subdomain class for slots regions"""

    VERSION = 1

    # cf Methods.Simulation.Subdomain_Slot.comp_flux_density
    if isinstance(comp_flux_density, ImportError):
        comp_flux_density = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method comp_flux_density: "
                    + str(comp_flux_density)
                )
            )
        )
    else:
        comp_flux_density = comp_flux_density
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        A=None,
        B=None,
        center_angle=None,
        radius_min=None,
        radius_max=None,
        angular_width=None,
        k=None,
        periodicity=None,
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
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "center_angle" in list(init_dict.keys()):
                center_angle = init_dict["center_angle"]
            if "radius_min" in list(init_dict.keys()):
                radius_min = init_dict["radius_min"]
            if "radius_max" in list(init_dict.keys()):
                radius_max = init_dict["radius_max"]
            if "angular_width" in list(init_dict.keys()):
                angular_width = init_dict["angular_width"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "periodicity" in list(init_dict.keys()):
                periodicity = init_dict["periodicity"]
        # Set the properties (value check and convertion are done in setter)
        self.A = A
        self.B = B
        self.center_angle = center_angle
        # Call Subdomain init
        super(Subdomain_Slot, self).__init__(
            radius_min=radius_min,
            radius_max=radius_max,
            angular_width=angular_width,
            k=k,
            periodicity=periodicity,
        )
        # The class is frozen (in Subdomain init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_Slot_str = ""
        # Get the properties inherited from Subdomain
        Subdomain_Slot_str += super(Subdomain_Slot, self).__str__()
        Subdomain_Slot_str += (
            "A = "
            + linesep
            + str(self.A).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Slot_str += (
            "B = "
            + linesep
            + str(self.B).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Slot_str += (
            "center_angle = "
            + linesep
            + str(self.center_angle).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Subdomain_Slot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain
        if not super(Subdomain_Slot, self).__eq__(other):
            return False
        if not array_equal(other.A, self.A):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.center_angle, self.center_angle):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Subdomain
        diff_list.extend(
            super(Subdomain_Slot, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if not array_equal(other.A, self.A):
            diff_list.append(name + ".A")
        if not array_equal(other.B, self.B):
            diff_list.append(name + ".B")
        if not array_equal(other.center_angle, self.center_angle):
            diff_list.append(name + ".center_angle")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain
        S += super(Subdomain_Slot, self).__sizeof__()
        S += getsizeof(self.A)
        S += getsizeof(self.B)
        S += getsizeof(self.center_angle)
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

        # Get the properties inherited from Subdomain
        Subdomain_Slot_dict = super(Subdomain_Slot, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.A is None:
            Subdomain_Slot_dict["A"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Slot_dict["A"] = self.A.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Slot_dict["A"] = self.A.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Slot_dict["A"] = self.A
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.B is None:
            Subdomain_Slot_dict["B"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Slot_dict["B"] = self.B.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Slot_dict["B"] = self.B.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Slot_dict["B"] = self.B
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.center_angle is None:
            Subdomain_Slot_dict["center_angle"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Slot_dict["center_angle"] = self.center_angle.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Slot_dict["center_angle"] = self.center_angle.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Slot_dict["center_angle"] = self.center_angle
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_Slot_dict["__class__"] = "Subdomain_Slot"
        return Subdomain_Slot_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.A is None:
            A_val = None
        else:
            A_val = self.A.copy()
        if self.B is None:
            B_val = None
        else:
            B_val = self.B.copy()
        if self.center_angle is None:
            center_angle_val = None
        else:
            center_angle_val = self.center_angle.copy()
        radius_min_val = self.radius_min
        radius_max_val = self.radius_max
        angular_width_val = self.angular_width
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        periodicity_val = self.periodicity
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            A=A_val,
            B=B_val,
            center_angle=center_angle_val,
            radius_min=radius_min_val,
            radius_max=radius_max_val,
            angular_width=angular_width_val,
            k=k_val,
            periodicity=periodicity_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.A = None
        self.B = None
        self.center_angle = None
        # Set to None the properties inherited from Subdomain
        super(Subdomain_Slot, self)._set_None()

    def _get_A(self):
        """getter of A"""
        return self._A

    def _set_A(self, value):
        """setter of A"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("A", value, "ndarray")
        self._A = value

    A = property(
        fget=_get_A,
        fset=_set_A,
        doc=u"""First integration constant function of harmonic number and time

        :Type: ndarray
        """,
    )

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("B", value, "ndarray")
        self._B = value

    B = property(
        fget=_get_B,
        fset=_set_B,
        doc=u"""Second integration constant function of harmonic number and time

        :Type: ndarray
        """,
    )

    def _get_center_angle(self):
        """getter of center_angle"""
        return self._center_angle

    def _set_center_angle(self, value):
        """setter of center_angle"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("center_angle", value, "ndarray")
        self._center_angle = value

    center_angle = property(
        fget=_get_center_angle,
        fset=_set_center_angle,
        doc=u"""Angle value at subdomain center

        :Type: ndarray
        """,
    )
