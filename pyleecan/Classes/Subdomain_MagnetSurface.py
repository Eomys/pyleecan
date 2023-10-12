# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain_MagnetSurface.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain_MagnetSurface
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
from .Subdomain_Airgap import Subdomain_Airgap

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.comp_flux_density import (
        comp_flux_density,
    )
except ImportError as error:
    comp_flux_density = error

try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.comp_magnet_solution import (
        comp_magnet_solution,
    )
except ImportError as error:
    comp_magnet_solution = error

try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.comp_magnet_source import (
        comp_magnet_source,
    )
except ImportError as error:
    comp_magnet_source = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_MagnetSurface(Subdomain_Airgap):
    """Subdomain class for surface permanent magnet region"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Subdomain_MagnetSurface.comp_flux_density
    if isinstance(comp_flux_density, ImportError):
        comp_flux_density = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_MagnetSurface method comp_flux_density: "
                    + str(comp_flux_density)
                )
            )
        )
    else:
        comp_flux_density = comp_flux_density
    # cf Methods.Simulation.Subdomain_MagnetSurface.comp_magnet_solution
    if isinstance(comp_magnet_solution, ImportError):
        comp_magnet_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_MagnetSurface method comp_magnet_solution: "
                    + str(comp_magnet_solution)
                )
            )
        )
    else:
        comp_magnet_solution = comp_magnet_solution
    # cf Methods.Simulation.Subdomain_MagnetSurface.comp_magnet_source
    if isinstance(comp_magnet_source, ImportError):
        comp_magnet_source = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_MagnetSurface method comp_magnet_source: "
                    + str(comp_magnet_source)
                )
            )
        )
    else:
        comp_magnet_source = comp_magnet_source
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_magnetization=0,
        A=None,
        B=None,
        C=None,
        D=None,
        radius_min=None,
        radius_max=None,
        angular_width=None,
        k=None,
        periodicity=None,
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
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
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
            if "angular_width" in list(init_dict.keys()):
                angular_width = init_dict["angular_width"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "periodicity" in list(init_dict.keys()):
                periodicity = init_dict["periodicity"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.type_magnetization = type_magnetization
        # Call Subdomain_Airgap init
        super(Subdomain_MagnetSurface, self).__init__(
            A=A,
            B=B,
            C=C,
            D=D,
            radius_min=radius_min,
            radius_max=radius_max,
            angular_width=angular_width,
            k=k,
            periodicity=periodicity,
            permeability_relative=permeability_relative,
        )
        # The class is frozen (in Subdomain_Airgap init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_MagnetSurface_str = ""
        # Get the properties inherited from Subdomain_Airgap
        Subdomain_MagnetSurface_str += super(Subdomain_MagnetSurface, self).__str__()
        Subdomain_MagnetSurface_str += (
            "type_magnetization = " + str(self.type_magnetization) + linesep
        )
        return Subdomain_MagnetSurface_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain_Airgap
        if not super(Subdomain_MagnetSurface, self).__eq__(other):
            return False
        if other.type_magnetization != self.type_magnetization:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Subdomain_Airgap
        diff_list.extend(
            super(Subdomain_MagnetSurface, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._type_magnetization != self._type_magnetization:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_magnetization)
                    + ", other="
                    + str(other._type_magnetization)
                    + ")"
                )
                diff_list.append(name + ".type_magnetization" + val_str)
            else:
                diff_list.append(name + ".type_magnetization")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain_Airgap
        S += super(Subdomain_MagnetSurface, self).__sizeof__()
        S += getsizeof(self.type_magnetization)
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

        # Get the properties inherited from Subdomain_Airgap
        Subdomain_MagnetSurface_dict = super(Subdomain_MagnetSurface, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Subdomain_MagnetSurface_dict["type_magnetization"] = self.type_magnetization
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_MagnetSurface_dict["__class__"] = "Subdomain_MagnetSurface"
        return Subdomain_MagnetSurface_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_magnetization_val = self.type_magnetization
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
        angular_width_val = self.angular_width
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        periodicity_val = self.periodicity
        permeability_relative_val = self.permeability_relative
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            type_magnetization=type_magnetization_val,
            A=A_val,
            B=B_val,
            C=C_val,
            D=D_val,
            radius_min=radius_min_val,
            radius_max=radius_max_val,
            angular_width=angular_width_val,
            k=k_val,
            periodicity=periodicity_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_magnetization = None
        # Set to None the properties inherited from Subdomain_Airgap
        super(Subdomain_MagnetSurface, self)._set_None()

    def _get_type_magnetization(self):
        """getter of type_magnetization"""
        return self._type_magnetization

    def _set_type_magnetization(self, value):
        """setter of type_magnetization"""
        check_var("type_magnetization", value, "int", Vmin=0, Vmax=3)
        self._type_magnetization = value

    type_magnetization = property(
        fget=_get_type_magnetization,
        fset=_set_type_magnetization,
        doc=u"""Magnetization type given by machine properties

        :Type: int
        :min: 0
        :max: 3
        """,
    )
