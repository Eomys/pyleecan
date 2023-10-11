# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain_SlotWinding.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain_SlotWinding
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
from .Subdomain_Slot import Subdomain_Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Subdomain_SlotWinding.comp_current_solution import (
        comp_current_solution,
    )
except ImportError as error:
    comp_current_solution = error

try:
    from ..Methods.Simulation.Subdomain_SlotWinding.comp_current_source import (
        comp_current_source,
    )
except ImportError as error:
    comp_current_source = error

try:
    from ..Methods.Simulation.Subdomain_SlotWinding.comp_flux_density import (
        comp_flux_density,
    )
except ImportError as error:
    comp_flux_density = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_SlotWinding(Subdomain_Slot):
    """Subdomain class for slots regions with windings"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Subdomain_SlotWinding.comp_current_solution
    if isinstance(comp_current_solution, ImportError):
        comp_current_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_SlotWinding method comp_current_solution: "
                    + str(comp_current_solution)
                )
            )
        )
    else:
        comp_current_solution = comp_current_solution
    # cf Methods.Simulation.Subdomain_SlotWinding.comp_current_source
    if isinstance(comp_current_source, ImportError):
        comp_current_source = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_SlotWinding method comp_current_source: "
                    + str(comp_current_source)
                )
            )
        )
    else:
        comp_current_source = comp_current_source
    # cf Methods.Simulation.Subdomain_SlotWinding.comp_flux_density
    if isinstance(comp_flux_density, ImportError):
        comp_flux_density = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_SlotWinding method comp_flux_density: "
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
        Ji=None,
        Jik=None,
        A=None,
        B=None,
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
            if "Ji" in list(init_dict.keys()):
                Ji = init_dict["Ji"]
            if "Jik" in list(init_dict.keys()):
                Jik = init_dict["Jik"]
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
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
        self.Ji = Ji
        self.Jik = Jik
        # Call Subdomain_Slot init
        super(Subdomain_SlotWinding, self).__init__(
            A=A,
            B=B,
            radius_min=radius_min,
            radius_max=radius_max,
            center_angle=center_angle,
            angular_width=angular_width,
            k=k,
            periodicity=periodicity,
        )
        # The class is frozen (in Subdomain_Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_SlotWinding_str = ""
        # Get the properties inherited from Subdomain_Slot
        Subdomain_SlotWinding_str += super(Subdomain_SlotWinding, self).__str__()
        Subdomain_SlotWinding_str += (
            "Ji = "
            + linesep
            + str(self.Ji).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotWinding_str += (
            "Jik = "
            + linesep
            + str(self.Jik).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Subdomain_SlotWinding_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain_Slot
        if not super(Subdomain_SlotWinding, self).__eq__(other):
            return False
        if not array_equal(other.Ji, self.Ji):
            return False
        if not array_equal(other.Jik, self.Jik):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Subdomain_Slot
        diff_list.extend(
            super(Subdomain_SlotWinding, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if not array_equal(other.Ji, self.Ji):
            diff_list.append(name + ".Ji")
        if not array_equal(other.Jik, self.Jik):
            diff_list.append(name + ".Jik")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain_Slot
        S += super(Subdomain_SlotWinding, self).__sizeof__()
        S += getsizeof(self.Ji)
        S += getsizeof(self.Jik)
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

        # Get the properties inherited from Subdomain_Slot
        Subdomain_SlotWinding_dict = super(Subdomain_SlotWinding, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.Ji is None:
            Subdomain_SlotWinding_dict["Ji"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotWinding_dict["Ji"] = self.Ji.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotWinding_dict["Ji"] = self.Ji.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotWinding_dict["Ji"] = self.Ji
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Jik is None:
            Subdomain_SlotWinding_dict["Jik"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotWinding_dict["Jik"] = self.Jik.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotWinding_dict["Jik"] = self.Jik.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotWinding_dict["Jik"] = self.Jik
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_SlotWinding_dict["__class__"] = "Subdomain_SlotWinding"
        return Subdomain_SlotWinding_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.Ji is None:
            Ji_val = None
        else:
            Ji_val = self.Ji.copy()
        if self.Jik is None:
            Jik_val = None
        else:
            Jik_val = self.Jik.copy()
        if self.A is None:
            A_val = None
        else:
            A_val = self.A.copy()
        if self.B is None:
            B_val = None
        else:
            B_val = self.B.copy()
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
            Ji=Ji_val,
            Jik=Jik_val,
            A=A_val,
            B=B_val,
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

        self.Ji = None
        self.Jik = None
        # Set to None the properties inherited from Subdomain_Slot
        super(Subdomain_SlotWinding, self)._set_None()

    def _get_Ji(self):
        """getter of Ji"""
        return self._Ji

    def _set_Ji(self, value):
        """setter of Ji"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ji", value, "ndarray")
        self._Ji = value

    Ji = property(
        fget=_get_Ji,
        fset=_set_Ji,
        doc=u"""Average current density in slots

        :Type: ndarray
        """,
    )

    def _get_Jik(self):
        """getter of Jik"""
        return self._Jik

    def _set_Jik(self, value):
        """setter of Jik"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Jik", value, "ndarray")
        self._Jik = value

    Jik = property(
        fget=_get_Jik,
        fset=_set_Jik,
        doc=u"""Current density space harmonics in slots for concentrated double layer windings

        :Type: ndarray
        """,
    )
