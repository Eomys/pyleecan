# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/MagSDM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/MagSDM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Magnetics import Magnetics

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.MagSDM.comp_flux_airgap import comp_flux_airgap
except ImportError as error:
    comp_flux_airgap = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MagSDM(Magnetics):

    VERSION = 1

    # cf Methods.Simulation.MagSDM.comp_flux_airgap
    if isinstance(comp_flux_airgap, ImportError):
        comp_flux_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagSDM method comp_flux_airgap: " + str(comp_flux_airgap)
                )
            )
        )
    else:
        comp_flux_airgap = comp_flux_airgap
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        subdomain_model=None,
        Nharm_coeff=1,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_ventS=False,
        is_remove_ventR=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=False,
        angle_stator_shift=0,
        angle_rotor_shift=0,
        logger_name="Pyleecan.Magnetics",
        Slice_enforced=None,
        Nslices_enforced=None,
        type_distribution_enforced=None,
        is_current_harm=True,
        T_mag=20,
        is_periodicity_rotor=False,
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
            if "subdomain_model" in list(init_dict.keys()):
                subdomain_model = init_dict["subdomain_model"]
            if "Nharm_coeff" in list(init_dict.keys()):
                Nharm_coeff = init_dict["Nharm_coeff"]
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_ventS" in list(init_dict.keys()):
                is_remove_ventS = init_dict["is_remove_ventS"]
            if "is_remove_ventR" in list(init_dict.keys()):
                is_remove_ventR = init_dict["is_remove_ventR"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "angle_stator_shift" in list(init_dict.keys()):
                angle_stator_shift = init_dict["angle_stator_shift"]
            if "angle_rotor_shift" in list(init_dict.keys()):
                angle_rotor_shift = init_dict["angle_rotor_shift"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Slice_enforced" in list(init_dict.keys()):
                Slice_enforced = init_dict["Slice_enforced"]
            if "Nslices_enforced" in list(init_dict.keys()):
                Nslices_enforced = init_dict["Nslices_enforced"]
            if "type_distribution_enforced" in list(init_dict.keys()):
                type_distribution_enforced = init_dict["type_distribution_enforced"]
            if "is_current_harm" in list(init_dict.keys()):
                is_current_harm = init_dict["is_current_harm"]
            if "T_mag" in list(init_dict.keys()):
                T_mag = init_dict["T_mag"]
            if "is_periodicity_rotor" in list(init_dict.keys()):
                is_periodicity_rotor = init_dict["is_periodicity_rotor"]
        # Set the properties (value check and convertion are done in setter)
        self.subdomain_model = subdomain_model
        self.Nharm_coeff = Nharm_coeff
        # Call Magnetics init
        super(MagSDM, self).__init__(
            is_remove_slotS=is_remove_slotS,
            is_remove_slotR=is_remove_slotR,
            is_remove_ventS=is_remove_ventS,
            is_remove_ventR=is_remove_ventR,
            is_mmfs=is_mmfs,
            is_mmfr=is_mmfr,
            type_BH_stator=type_BH_stator,
            type_BH_rotor=type_BH_rotor,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            angle_stator_shift=angle_stator_shift,
            angle_rotor_shift=angle_rotor_shift,
            logger_name=logger_name,
            Slice_enforced=Slice_enforced,
            Nslices_enforced=Nslices_enforced,
            type_distribution_enforced=type_distribution_enforced,
            is_current_harm=is_current_harm,
            T_mag=T_mag,
            is_periodicity_rotor=is_periodicity_rotor,
        )
        # The class is frozen (in Magnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MagSDM_str = ""
        # Get the properties inherited from Magnetics
        MagSDM_str += super(MagSDM, self).__str__()
        if self.subdomain_model is not None:
            tmp = (
                self.subdomain_model.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            MagSDM_str += "subdomain_model = " + tmp
        else:
            MagSDM_str += "subdomain_model = None" + linesep + linesep
        MagSDM_str += "Nharm_coeff = " + str(self.Nharm_coeff) + linesep
        return MagSDM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Magnetics
        if not super(MagSDM, self).__eq__(other):
            return False
        if other.subdomain_model != self.subdomain_model:
            return False
        if other.Nharm_coeff != self.Nharm_coeff:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Magnetics
        diff_list.extend(
            super(MagSDM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.subdomain_model is None and self.subdomain_model is not None) or (
            other.subdomain_model is not None and self.subdomain_model is None
        ):
            diff_list.append(name + ".subdomain_model None mismatch")
        elif self.subdomain_model is not None:
            diff_list.extend(
                self.subdomain_model.compare(
                    other.subdomain_model,
                    name=name + ".subdomain_model",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (
            other._Nharm_coeff is not None
            and self._Nharm_coeff is not None
            and isnan(other._Nharm_coeff)
            and isnan(self._Nharm_coeff)
        ):
            pass
        elif other._Nharm_coeff != self._Nharm_coeff:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nharm_coeff)
                    + ", other="
                    + str(other._Nharm_coeff)
                    + ")"
                )
                diff_list.append(name + ".Nharm_coeff" + val_str)
            else:
                diff_list.append(name + ".Nharm_coeff")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Magnetics
        S += super(MagSDM, self).__sizeof__()
        S += getsizeof(self.subdomain_model)
        S += getsizeof(self.Nharm_coeff)
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

        # Get the properties inherited from Magnetics
        MagSDM_dict = super(MagSDM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.subdomain_model is None:
            MagSDM_dict["subdomain_model"] = None
        else:
            MagSDM_dict["subdomain_model"] = self.subdomain_model.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        MagSDM_dict["Nharm_coeff"] = self.Nharm_coeff
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MagSDM_dict["__class__"] = "MagSDM"
        return MagSDM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.subdomain_model is None:
            subdomain_model_val = None
        else:
            subdomain_model_val = self.subdomain_model.copy()
        Nharm_coeff_val = self.Nharm_coeff
        is_remove_slotS_val = self.is_remove_slotS
        is_remove_slotR_val = self.is_remove_slotR
        is_remove_ventS_val = self.is_remove_ventS
        is_remove_ventR_val = self.is_remove_ventR
        is_mmfs_val = self.is_mmfs
        is_mmfr_val = self.is_mmfr
        type_BH_stator_val = self.type_BH_stator
        type_BH_rotor_val = self.type_BH_rotor
        is_periodicity_t_val = self.is_periodicity_t
        is_periodicity_a_val = self.is_periodicity_a
        angle_stator_shift_val = self.angle_stator_shift
        angle_rotor_shift_val = self.angle_rotor_shift
        logger_name_val = self.logger_name
        if self.Slice_enforced is None:
            Slice_enforced_val = None
        else:
            Slice_enforced_val = self.Slice_enforced.copy()
        Nslices_enforced_val = self.Nslices_enforced
        type_distribution_enforced_val = self.type_distribution_enforced
        is_current_harm_val = self.is_current_harm
        T_mag_val = self.T_mag
        is_periodicity_rotor_val = self.is_periodicity_rotor
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            subdomain_model=subdomain_model_val,
            Nharm_coeff=Nharm_coeff_val,
            is_remove_slotS=is_remove_slotS_val,
            is_remove_slotR=is_remove_slotR_val,
            is_remove_ventS=is_remove_ventS_val,
            is_remove_ventR=is_remove_ventR_val,
            is_mmfs=is_mmfs_val,
            is_mmfr=is_mmfr_val,
            type_BH_stator=type_BH_stator_val,
            type_BH_rotor=type_BH_rotor_val,
            is_periodicity_t=is_periodicity_t_val,
            is_periodicity_a=is_periodicity_a_val,
            angle_stator_shift=angle_stator_shift_val,
            angle_rotor_shift=angle_rotor_shift_val,
            logger_name=logger_name_val,
            Slice_enforced=Slice_enforced_val,
            Nslices_enforced=Nslices_enforced_val,
            type_distribution_enforced=type_distribution_enforced_val,
            is_current_harm=is_current_harm_val,
            T_mag=T_mag_val,
            is_periodicity_rotor=is_periodicity_rotor_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.subdomain_model is not None:
            self.subdomain_model._set_None()
        self.Nharm_coeff = None
        # Set to None the properties inherited from Magnetics
        super(MagSDM, self)._set_None()

    def _get_subdomain_model(self):
        """getter of subdomain_model"""
        return self._subdomain_model

    def _set_subdomain_model(self, value):
        """setter of subdomain_model"""
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
                "pyleecan.Classes", value.get("__class__"), "subdomain_model"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            SubdomainModel = import_class(
                "pyleecan.Classes", "SubdomainModel", "subdomain_model"
            )
            value = SubdomainModel()
        check_var("subdomain_model", value, "SubdomainModel")
        self._subdomain_model = value

        if self._subdomain_model is not None:
            self._subdomain_model.parent = self

    subdomain_model = property(
        fget=_get_subdomain_model,
        fset=_set_subdomain_model,
        doc=u"""The subdomain model object defined to calculate airgap flux density

        :Type: SubdomainModel
        """,
    )

    def _get_Nharm_coeff(self):
        """getter of Nharm_coeff"""
        return self._Nharm_coeff

    def _set_Nharm_coeff(self, value):
        """setter of Nharm_coeff"""
        check_var("Nharm_coeff", value, "float", Vmin=0)
        self._Nharm_coeff = value

    Nharm_coeff = property(
        fget=_get_Nharm_coeff,
        fset=_set_Nharm_coeff,
        doc=u"""Scaling coefficient to calculate more or less harmonics in subdomains

        :Type: float
        :min: 0
        """,
    )
