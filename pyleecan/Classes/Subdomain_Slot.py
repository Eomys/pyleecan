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
    from ..Methods.Simulation.Subdomain_Slot.add_constants_numbers import (
        add_constants_numbers,
    )
except ImportError as error:
    add_constants_numbers = error

try:
    from ..Methods.Simulation.Subdomain_Slot.comp_current_solution import (
        comp_current_solution,
    )
except ImportError as error:
    comp_current_solution = error

try:
    from ..Methods.Simulation.Subdomain_Slot.comp_current_source import (
        comp_current_source,
    )
except ImportError as error:
    comp_current_source = error

try:
    from ..Methods.Simulation.Subdomain_Slot.comp_flux_density import comp_flux_density
except ImportError as error:
    comp_flux_density = error

try:
    from ..Methods.Simulation.Subdomain_Slot.comp_interface_airgap import (
        comp_interface_airgap,
    )
except ImportError as error:
    comp_interface_airgap = error

try:
    from ..Methods.Simulation.Subdomain_Slot.comp_Phi_wind import comp_Phi_wind
except ImportError as error:
    comp_Phi_wind = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_Slot(Subdomain):
    """Subdomain class for slots regions without openings and with windings"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Subdomain_Slot.add_constants_numbers
    if isinstance(add_constants_numbers, ImportError):
        add_constants_numbers = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method add_constants_numbers: "
                    + str(add_constants_numbers)
                )
            )
        )
    else:
        add_constants_numbers = add_constants_numbers
    # cf Methods.Simulation.Subdomain_Slot.comp_current_solution
    if isinstance(comp_current_solution, ImportError):
        comp_current_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method comp_current_solution: "
                    + str(comp_current_solution)
                )
            )
        )
    else:
        comp_current_solution = comp_current_solution
    # cf Methods.Simulation.Subdomain_Slot.comp_current_source
    if isinstance(comp_current_source, ImportError):
        comp_current_source = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method comp_current_source: "
                    + str(comp_current_source)
                )
            )
        )
    else:
        comp_current_source = comp_current_source
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
    # cf Methods.Simulation.Subdomain_Slot.comp_interface_airgap
    if isinstance(comp_interface_airgap, ImportError):
        comp_interface_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method comp_interface_airgap: "
                    + str(comp_interface_airgap)
                )
            )
        )
    else:
        comp_interface_airgap = comp_interface_airgap
    # cf Methods.Simulation.Subdomain_Slot.comp_Phi_wind
    if isinstance(comp_Phi_wind, ImportError):
        comp_Phi_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Slot method comp_Phi_wind: "
                    + str(comp_Phi_wind)
                )
            )
        )
    else:
        comp_Phi_wind = comp_Phi_wind
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        A=None,
        B=None,
        center_angle=None,
        slot_width=None,
        Ji=None,
        Jik=None,
        Ryoke=None,
        Rbore=None,
        number_per_a=None,
        k=None,
        number=None,
        permeability_relative=1,
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
            if "slot_width" in list(init_dict.keys()):
                slot_width = init_dict["slot_width"]
            if "Ji" in list(init_dict.keys()):
                Ji = init_dict["Ji"]
            if "Jik" in list(init_dict.keys()):
                Jik = init_dict["Jik"]
            if "Ryoke" in list(init_dict.keys()):
                Ryoke = init_dict["Ryoke"]
            if "Rbore" in list(init_dict.keys()):
                Rbore = init_dict["Rbore"]
            if "number_per_a" in list(init_dict.keys()):
                number_per_a = init_dict["number_per_a"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "number" in list(init_dict.keys()):
                number = init_dict["number"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.A = A
        self.B = B
        self.center_angle = center_angle
        self.slot_width = slot_width
        self.Ji = Ji
        self.Jik = Jik
        self.Ryoke = Ryoke
        self.Rbore = Rbore
        self.number_per_a = number_per_a
        # Call Subdomain init
        super(Subdomain_Slot, self).__init__(
            k=k, number=number, permeability_relative=permeability_relative
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
        Subdomain_Slot_str += "slot_width = " + str(self.slot_width) + linesep
        Subdomain_Slot_str += (
            "Ji = "
            + linesep
            + str(self.Ji).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Slot_str += (
            "Jik = "
            + linesep
            + str(self.Jik).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Slot_str += "Ryoke = " + str(self.Ryoke) + linesep
        Subdomain_Slot_str += "Rbore = " + str(self.Rbore) + linesep
        Subdomain_Slot_str += "number_per_a = " + str(self.number_per_a) + linesep
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
        if other.slot_width != self.slot_width:
            return False
        if not array_equal(other.Ji, self.Ji):
            return False
        if not array_equal(other.Jik, self.Jik):
            return False
        if other.Ryoke != self.Ryoke:
            return False
        if other.Rbore != self.Rbore:
            return False
        if other.number_per_a != self.number_per_a:
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
        if (
            other._slot_width is not None
            and self._slot_width is not None
            and isnan(other._slot_width)
            and isnan(self._slot_width)
        ):
            pass
        elif other._slot_width != self._slot_width:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._slot_width)
                    + ", other="
                    + str(other._slot_width)
                    + ")"
                )
                diff_list.append(name + ".slot_width" + val_str)
            else:
                diff_list.append(name + ".slot_width")
        if not array_equal(other.Ji, self.Ji):
            diff_list.append(name + ".Ji")
        if not array_equal(other.Jik, self.Jik):
            diff_list.append(name + ".Jik")
        if (
            other._Ryoke is not None
            and self._Ryoke is not None
            and isnan(other._Ryoke)
            and isnan(self._Ryoke)
        ):
            pass
        elif other._Ryoke != self._Ryoke:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Ryoke) + ", other=" + str(other._Ryoke) + ")"
                )
                diff_list.append(name + ".Ryoke" + val_str)
            else:
                diff_list.append(name + ".Ryoke")
        if (
            other._Rbore is not None
            and self._Rbore is not None
            and isnan(other._Rbore)
            and isnan(self._Rbore)
        ):
            pass
        elif other._Rbore != self._Rbore:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Rbore) + ", other=" + str(other._Rbore) + ")"
                )
                diff_list.append(name + ".Rbore" + val_str)
            else:
                diff_list.append(name + ".Rbore")
        if other._number_per_a != self._number_per_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._number_per_a)
                    + ", other="
                    + str(other._number_per_a)
                    + ")"
                )
                diff_list.append(name + ".number_per_a" + val_str)
            else:
                diff_list.append(name + ".number_per_a")
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
        S += getsizeof(self.slot_width)
        S += getsizeof(self.Ji)
        S += getsizeof(self.Jik)
        S += getsizeof(self.Ryoke)
        S += getsizeof(self.Rbore)
        S += getsizeof(self.number_per_a)
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
        Subdomain_Slot_dict["slot_width"] = self.slot_width
        if self.Ji is None:
            Subdomain_Slot_dict["Ji"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Slot_dict["Ji"] = self.Ji.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Slot_dict["Ji"] = self.Ji.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Slot_dict["Ji"] = self.Ji
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Jik is None:
            Subdomain_Slot_dict["Jik"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Slot_dict["Jik"] = self.Jik.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Slot_dict["Jik"] = self.Jik.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Slot_dict["Jik"] = self.Jik
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_Slot_dict["Ryoke"] = self.Ryoke
        Subdomain_Slot_dict["Rbore"] = self.Rbore
        Subdomain_Slot_dict["number_per_a"] = self.number_per_a
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
        slot_width_val = self.slot_width
        if self.Ji is None:
            Ji_val = None
        else:
            Ji_val = self.Ji.copy()
        if self.Jik is None:
            Jik_val = None
        else:
            Jik_val = self.Jik.copy()
        Ryoke_val = self.Ryoke
        Rbore_val = self.Rbore
        number_per_a_val = self.number_per_a
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        number_val = self.number
        permeability_relative_val = self.permeability_relative
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            A=A_val,
            B=B_val,
            center_angle=center_angle_val,
            slot_width=slot_width_val,
            Ji=Ji_val,
            Jik=Jik_val,
            Ryoke=Ryoke_val,
            Rbore=Rbore_val,
            number_per_a=number_per_a_val,
            k=k_val,
            number=number_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.A = None
        self.B = None
        self.center_angle = None
        self.slot_width = None
        self.Ji = None
        self.Jik = None
        self.Ryoke = None
        self.Rbore = None
        self.number_per_a = None
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
        doc=u"""Angle value at slot center

        :Type: ndarray
        """,
    )

    def _get_slot_width(self):
        """getter of slot_width"""
        return self._slot_width

    def _set_slot_width(self, value):
        """setter of slot_width"""
        check_var("slot_width", value, "float", Vmin=0)
        self._slot_width = value

    slot_width = property(
        fget=_get_slot_width,
        fset=_set_slot_width,
        doc=u"""Angular width of slot

        :Type: float
        :min: 0
        """,
    )

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

    def _get_Ryoke(self):
        """getter of Ryoke"""
        return self._Ryoke

    def _set_Ryoke(self, value):
        """setter of Ryoke"""
        check_var("Ryoke", value, "float", Vmin=0)
        self._Ryoke = value

    Ryoke = property(
        fget=_get_Ryoke,
        fset=_set_Ryoke,
        doc=u"""Radius at slot / yoke interface

        :Type: float
        :min: 0
        """,
    )

    def _get_Rbore(self):
        """getter of Rbore"""
        return self._Rbore

    def _set_Rbore(self, value):
        """setter of Rbore"""
        check_var("Rbore", value, "float", Vmin=0)
        self._Rbore = value

    Rbore = property(
        fget=_get_Rbore,
        fset=_set_Rbore,
        doc=u"""Radius at slot / airgap interface

        :Type: float
        :min: 0
        """,
    )

    def _get_number_per_a(self):
        """getter of number_per_a"""
        return self._number_per_a

    def _set_number_per_a(self, value):
        """setter of number_per_a"""
        check_var("number_per_a", value, "int", Vmin=1)
        self._number_per_a = value

    number_per_a = property(
        fget=_get_number_per_a,
        fset=_set_number_per_a,
        doc=u"""Number of subdomains accounting for spatial (anti-)periodicity

        :Type: int
        :min: 1
        """,
    )
