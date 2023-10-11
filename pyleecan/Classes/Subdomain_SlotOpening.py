# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain_SlotOpening.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain_SlotOpening
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
    from ..Methods.Simulation.Subdomain_SlotOpening.comp_flux_density import (
        comp_flux_density,
    )
except ImportError as error:
    comp_flux_density = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_SlotOpening(Subdomain):
    """Subdomain class for slots regions"""

    VERSION = 1

    # cf Methods.Simulation.Subdomain_SlotOpening.comp_flux_density
    if isinstance(comp_flux_density, ImportError):
        comp_flux_density = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_SlotOpening method comp_flux_density: "
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
        C=None,
        D=None,
        radius_min=None,
        radius_max=None,
        center_angle=None,
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
            if "C" in list(init_dict.keys()):
                C = init_dict["C"]
            if "D" in list(init_dict.keys()):
                D = init_dict["D"]
            if "radius_min" in list(init_dict.keys()):
                radius_min = init_dict["radius_min"]
            if "radius_max" in list(init_dict.keys()):
                radius_max = init_dict["radius_max"]
            if "center_angle" in list(init_dict.keys()):
                center_angle = init_dict["center_angle"]
            if "angular_width" in list(init_dict.keys()):
                angular_width = init_dict["angular_width"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "periodicity" in list(init_dict.keys()):
                periodicity = init_dict["periodicity"]
        # Set the properties (value check and convertion are done in setter)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # Call Subdomain init
        super(Subdomain_SlotOpening, self).__init__(
            radius_min=radius_min,
            radius_max=radius_max,
            center_angle=center_angle,
            angular_width=angular_width,
            k=k,
            periodicity=periodicity,
        )
        # The class is frozen (in Subdomain init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_SlotOpening_str = ""
        # Get the properties inherited from Subdomain
        Subdomain_SlotOpening_str += super(Subdomain_SlotOpening, self).__str__()
        Subdomain_SlotOpening_str += (
            "A = "
            + linesep
            + str(self.A).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += (
            "B = "
            + linesep
            + str(self.B).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += (
            "C = "
            + linesep
            + str(self.C).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += (
            "D = "
            + linesep
            + str(self.D).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Subdomain_SlotOpening_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain
        if not super(Subdomain_SlotOpening, self).__eq__(other):
            return False
        if not array_equal(other.A, self.A):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.C, self.C):
            return False
        if not array_equal(other.D, self.D):
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
            super(Subdomain_SlotOpening, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if not array_equal(other.A, self.A):
            diff_list.append(name + ".A")
        if not array_equal(other.B, self.B):
            diff_list.append(name + ".B")
        if not array_equal(other.C, self.C):
            diff_list.append(name + ".C")
        if not array_equal(other.D, self.D):
            diff_list.append(name + ".D")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain
        S += super(Subdomain_SlotOpening, self).__sizeof__()
        S += getsizeof(self.A)
        S += getsizeof(self.B)
        S += getsizeof(self.C)
        S += getsizeof(self.D)
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
        Subdomain_SlotOpening_dict = super(Subdomain_SlotOpening, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.A is None:
            Subdomain_SlotOpening_dict["A"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["A"] = self.A.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["A"] = self.A.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["A"] = self.A
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.B is None:
            Subdomain_SlotOpening_dict["B"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["B"] = self.B.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["B"] = self.B.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["B"] = self.B
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.C is None:
            Subdomain_SlotOpening_dict["C"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["C"] = self.C.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["C"] = self.C.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["C"] = self.C
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.D is None:
            Subdomain_SlotOpening_dict["D"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["D"] = self.D.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["D"] = self.D.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["D"] = self.D
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_SlotOpening_dict["__class__"] = "Subdomain_SlotOpening"
        return Subdomain_SlotOpening_dict

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
        if self.C is None:
            C_val = None
        else:
            C_val = self.C.copy()
        if self.D is None:
            D_val = None
        else:
            D_val = self.D.copy()
        radius_min_val = self.radius_min
        radius_max_val = self.radius_max
        center_angle_val = self.center_angle
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
            C=C_val,
            D=D_val,
            radius_min=radius_min_val,
            radius_max=radius_max_val,
            center_angle=center_angle_val,
            angular_width=angular_width_val,
            k=k_val,
            periodicity=periodicity_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.A = None
        self.B = None
        self.C = None
        self.D = None
        # Set to None the properties inherited from Subdomain
        super(Subdomain_SlotOpening, self)._set_None()

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

    def _get_C(self):
        """getter of C"""
        return self._C

    def _set_C(self, value):
        """setter of C"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("C", value, "ndarray")
        self._C = value

    C = property(
        fget=_get_C,
        fset=_set_C,
        doc=u"""Third integration constant function of harmonic number and time

        :Type: ndarray
        """,
    )

    def _get_D(self):
        """getter of D"""
        return self._D

    def _set_D(self, value):
        """setter of D"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("D", value, "ndarray")
        self._D = value

    D = property(
        fget=_get_D,
        fset=_set_D,
        doc=u"""Fourth integration constant function of harmonic number and time

        :Type: ndarray
        """,
    )
