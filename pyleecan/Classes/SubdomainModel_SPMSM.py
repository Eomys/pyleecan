# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/SubdomainModel_SPMSM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/SubdomainModel_SPMSM
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
from .SubdomainModel import SubdomainModel

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.SubdomainModel_SPMSM.set_subdomains import set_subdomains
except ImportError as error:
    set_subdomains = error

try:
    from ..Methods.Simulation.SubdomainModel_SPMSM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.SubdomainModel_SPMSM.store_constants import (
        store_constants,
    )
except ImportError as error:
    store_constants = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class SubdomainModel_SPMSM(SubdomainModel):
    """Subdomain model for Surface Permanent Magnet Synchronous Machine assuming infinite permeability in yokes"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.SubdomainModel_SPMSM.set_subdomains
    if isinstance(set_subdomains, ImportError):
        set_subdomains = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SubdomainModel_SPMSM method set_subdomains: "
                    + str(set_subdomains)
                )
            )
        )
    else:
        set_subdomains = set_subdomains
    # cf Methods.Simulation.SubdomainModel_SPMSM.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SubdomainModel_SPMSM method solve: " + str(solve)
                )
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.SubdomainModel_SPMSM.store_constants
    if isinstance(store_constants, ImportError):
        store_constants = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SubdomainModel_SPMSM method store_constants: "
                    + str(store_constants)
                )
            )
        )
    else:
        store_constants = store_constants
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        stator_slot=None,
        rotor_magnet_surface=None,
        rotor_yoke=None,
        airgap=None,
        per_a=None,
        machine_polar_eq=None,
        is_antiper_a=None,
        mat=None,
        vect=None,
        csts_number=None,
        csts_position=None,
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
            if "stator_slot" in list(init_dict.keys()):
                stator_slot = init_dict["stator_slot"]
            if "rotor_magnet_surface" in list(init_dict.keys()):
                rotor_magnet_surface = init_dict["rotor_magnet_surface"]
            if "rotor_yoke" in list(init_dict.keys()):
                rotor_yoke = init_dict["rotor_yoke"]
            if "airgap" in list(init_dict.keys()):
                airgap = init_dict["airgap"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "machine_polar_eq" in list(init_dict.keys()):
                machine_polar_eq = init_dict["machine_polar_eq"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "mat" in list(init_dict.keys()):
                mat = init_dict["mat"]
            if "vect" in list(init_dict.keys()):
                vect = init_dict["vect"]
            if "csts_number" in list(init_dict.keys()):
                csts_number = init_dict["csts_number"]
            if "csts_position" in list(init_dict.keys()):
                csts_position = init_dict["csts_position"]
        # Set the properties (value check and convertion are done in setter)
        self.stator_slot = stator_slot
        self.rotor_magnet_surface = rotor_magnet_surface
        self.rotor_yoke = rotor_yoke
        # Call SubdomainModel init
        super(SubdomainModel_SPMSM, self).__init__(
            airgap=airgap,
            per_a=per_a,
            machine_polar_eq=machine_polar_eq,
            is_antiper_a=is_antiper_a,
            mat=mat,
            vect=vect,
            csts_number=csts_number,
            csts_position=csts_position,
        )
        # The class is frozen (in SubdomainModel init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SubdomainModel_SPMSM_str = ""
        # Get the properties inherited from SubdomainModel
        SubdomainModel_SPMSM_str += super(SubdomainModel_SPMSM, self).__str__()
        if self.stator_slot is not None:
            tmp = (
                self.stator_slot.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            SubdomainModel_SPMSM_str += "stator_slot = " + tmp
        else:
            SubdomainModel_SPMSM_str += "stator_slot = None" + linesep + linesep
        if self.rotor_magnet_surface is not None:
            tmp = (
                self.rotor_magnet_surface.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            SubdomainModel_SPMSM_str += "rotor_magnet_surface = " + tmp
        else:
            SubdomainModel_SPMSM_str += (
                "rotor_magnet_surface = None" + linesep + linesep
            )
        if self.rotor_yoke is not None:
            tmp = (
                self.rotor_yoke.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            SubdomainModel_SPMSM_str += "rotor_yoke = " + tmp
        else:
            SubdomainModel_SPMSM_str += "rotor_yoke = None" + linesep + linesep
        return SubdomainModel_SPMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SubdomainModel
        if not super(SubdomainModel_SPMSM, self).__eq__(other):
            return False
        if other.stator_slot != self.stator_slot:
            return False
        if other.rotor_magnet_surface != self.rotor_magnet_surface:
            return False
        if other.rotor_yoke != self.rotor_yoke:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from SubdomainModel
        diff_list.extend(
            super(SubdomainModel_SPMSM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.stator_slot is None and self.stator_slot is not None) or (
            other.stator_slot is not None and self.stator_slot is None
        ):
            diff_list.append(name + ".stator_slot None mismatch")
        elif self.stator_slot is not None:
            diff_list.extend(
                self.stator_slot.compare(
                    other.stator_slot,
                    name=name + ".stator_slot",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (
            other.rotor_magnet_surface is None and self.rotor_magnet_surface is not None
        ) or (
            other.rotor_magnet_surface is not None and self.rotor_magnet_surface is None
        ):
            diff_list.append(name + ".rotor_magnet_surface None mismatch")
        elif self.rotor_magnet_surface is not None:
            diff_list.extend(
                self.rotor_magnet_surface.compare(
                    other.rotor_magnet_surface,
                    name=name + ".rotor_magnet_surface",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.rotor_yoke is None and self.rotor_yoke is not None) or (
            other.rotor_yoke is not None and self.rotor_yoke is None
        ):
            diff_list.append(name + ".rotor_yoke None mismatch")
        elif self.rotor_yoke is not None:
            diff_list.extend(
                self.rotor_yoke.compare(
                    other.rotor_yoke,
                    name=name + ".rotor_yoke",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from SubdomainModel
        S += super(SubdomainModel_SPMSM, self).__sizeof__()
        S += getsizeof(self.stator_slot)
        S += getsizeof(self.rotor_magnet_surface)
        S += getsizeof(self.rotor_yoke)
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

        # Get the properties inherited from SubdomainModel
        SubdomainModel_SPMSM_dict = super(SubdomainModel_SPMSM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.stator_slot is None:
            SubdomainModel_SPMSM_dict["stator_slot"] = None
        else:
            SubdomainModel_SPMSM_dict["stator_slot"] = self.stator_slot.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.rotor_magnet_surface is None:
            SubdomainModel_SPMSM_dict["rotor_magnet_surface"] = None
        else:
            SubdomainModel_SPMSM_dict[
                "rotor_magnet_surface"
            ] = self.rotor_magnet_surface.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.rotor_yoke is None:
            SubdomainModel_SPMSM_dict["rotor_yoke"] = None
        else:
            SubdomainModel_SPMSM_dict["rotor_yoke"] = self.rotor_yoke.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SubdomainModel_SPMSM_dict["__class__"] = "SubdomainModel_SPMSM"
        return SubdomainModel_SPMSM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.stator_slot is None:
            stator_slot_val = None
        else:
            stator_slot_val = self.stator_slot.copy()
        if self.rotor_magnet_surface is None:
            rotor_magnet_surface_val = None
        else:
            rotor_magnet_surface_val = self.rotor_magnet_surface.copy()
        if self.rotor_yoke is None:
            rotor_yoke_val = None
        else:
            rotor_yoke_val = self.rotor_yoke.copy()
        if self.airgap is None:
            airgap_val = None
        else:
            airgap_val = self.airgap.copy()
        per_a_val = self.per_a
        if self.machine_polar_eq is None:
            machine_polar_eq_val = None
        else:
            machine_polar_eq_val = self.machine_polar_eq.copy()
        is_antiper_a_val = self.is_antiper_a
        if self.mat is None:
            mat_val = None
        else:
            mat_val = self.mat.copy()
        if self.vect is None:
            vect_val = None
        else:
            vect_val = self.vect.copy()
        if self.csts_number is None:
            csts_number_val = None
        else:
            csts_number_val = self.csts_number.copy()
        if self.csts_position is None:
            csts_position_val = None
        else:
            csts_position_val = self.csts_position.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            stator_slot=stator_slot_val,
            rotor_magnet_surface=rotor_magnet_surface_val,
            rotor_yoke=rotor_yoke_val,
            airgap=airgap_val,
            per_a=per_a_val,
            machine_polar_eq=machine_polar_eq_val,
            is_antiper_a=is_antiper_a_val,
            mat=mat_val,
            vect=vect_val,
            csts_number=csts_number_val,
            csts_position=csts_position_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.stator_slot is not None:
            self.stator_slot._set_None()
        if self.rotor_magnet_surface is not None:
            self.rotor_magnet_surface._set_None()
        if self.rotor_yoke is not None:
            self.rotor_yoke._set_None()
        # Set to None the properties inherited from SubdomainModel
        super(SubdomainModel_SPMSM, self)._set_None()

    def _get_stator_slot(self):
        """getter of stator_slot"""
        return self._stator_slot

    def _set_stator_slot(self, value):
        """setter of stator_slot"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator_slot"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Subdomain_Slot = import_class(
                "pyleecan.Classes", "Subdomain_Slot", "stator_slot"
            )
            value = Subdomain_Slot()
        check_var("stator_slot", value, "Subdomain_Slot")
        self._stator_slot = value

        if self._stator_slot is not None:
            self._stator_slot.parent = self

    stator_slot = property(
        fget=_get_stator_slot,
        fset=_set_stator_slot,
        doc=u"""Subdomain for stator slots

        :Type: Subdomain_Slot
        """,
    )

    def _get_rotor_magnet_surface(self):
        """getter of rotor_magnet_surface"""
        return self._rotor_magnet_surface

    def _set_rotor_magnet_surface(self, value):
        """setter of rotor_magnet_surface"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor_magnet_surface"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Subdomain_MagnetSurface = import_class(
                "pyleecan.Classes", "Subdomain_MagnetSurface", "rotor_magnet_surface"
            )
            value = Subdomain_MagnetSurface()
        check_var("rotor_magnet_surface", value, "Subdomain_MagnetSurface")
        self._rotor_magnet_surface = value

        if self._rotor_magnet_surface is not None:
            self._rotor_magnet_surface.parent = self

    rotor_magnet_surface = property(
        fget=_get_rotor_magnet_surface,
        fset=_set_rotor_magnet_surface,
        doc=u"""Subdomain for surface magnets

        :Type: Subdomain_MagnetSurface
        """,
    )

    def _get_rotor_yoke(self):
        """getter of rotor_yoke"""
        return self._rotor_yoke

    def _set_rotor_yoke(self, value):
        """setter of rotor_yoke"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor_yoke"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Subdomain = import_class("pyleecan.Classes", "Subdomain", "rotor_yoke")
            value = Subdomain()
        check_var("rotor_yoke", value, "Subdomain")
        self._rotor_yoke = value

        if self._rotor_yoke is not None:
            self._rotor_yoke.parent = self

    rotor_yoke = property(
        fget=_get_rotor_yoke,
        fset=_set_rotor_yoke,
        doc=u"""Subdomain for rotor yoke

        :Type: Subdomain
        """,
    )
