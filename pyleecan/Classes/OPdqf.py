# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/OPdqf.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/OPdqf
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
from .OPdq import OPdq

from numpy import isnan
from ._check import InitUnKnowClassError


class OPdqf(OPdq):
    """Operating Point defined in DQH frame for WRSM"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        If_ref=None,
        Id_ref=None,
        Iq_ref=None,
        Ud_ref=None,
        Uq_ref=None,
        N0=None,
        felec=None,
        Tem_av_ref=None,
        Pem_av_ref=None,
        Pem_av_in=None,
        efficiency=None,
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
            if "If_ref" in list(init_dict.keys()):
                If_ref = init_dict["If_ref"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
            if "Pem_av_in" in list(init_dict.keys()):
                Pem_av_in = init_dict["Pem_av_in"]
            if "efficiency" in list(init_dict.keys()):
                efficiency = init_dict["efficiency"]
        # Set the properties (value check and convertion are done in setter)
        self.If_ref = If_ref
        # Call OPdq init
        super(OPdqf, self).__init__(
            Id_ref=Id_ref,
            Iq_ref=Iq_ref,
            Ud_ref=Ud_ref,
            Uq_ref=Uq_ref,
            N0=N0,
            felec=felec,
            Tem_av_ref=Tem_av_ref,
            Pem_av_ref=Pem_av_ref,
            Pem_av_in=Pem_av_in,
            efficiency=efficiency,
        )
        # The class is frozen (in OPdq init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OPdqf_str = ""
        # Get the properties inherited from OPdq
        OPdqf_str += super(OPdqf, self).__str__()
        OPdqf_str += "If_ref = " + str(self.If_ref) + linesep
        return OPdqf_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OPdq
        if not super(OPdqf, self).__eq__(other):
            return False
        if other.If_ref != self.If_ref:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OPdq
        diff_list.extend(
            super(OPdqf, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._If_ref is not None
            and self._If_ref is not None
            and isnan(other._If_ref)
            and isnan(self._If_ref)
        ):
            pass
        elif other._If_ref != self._If_ref:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._If_ref)
                    + ", other="
                    + str(other._If_ref)
                    + ")"
                )
                diff_list.append(name + ".If_ref" + val_str)
            else:
                diff_list.append(name + ".If_ref")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OPdq
        S += super(OPdqf, self).__sizeof__()
        S += getsizeof(self.If_ref)
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

        # Get the properties inherited from OPdq
        OPdqf_dict = super(OPdqf, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OPdqf_dict["If_ref"] = self.If_ref
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OPdqf_dict["__class__"] = "OPdqf"
        return OPdqf_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        If_ref_val = self.If_ref
        Id_ref_val = self.Id_ref
        Iq_ref_val = self.Iq_ref
        Ud_ref_val = self.Ud_ref
        Uq_ref_val = self.Uq_ref
        N0_val = self.N0
        felec_val = self.felec
        Tem_av_ref_val = self.Tem_av_ref
        Pem_av_ref_val = self.Pem_av_ref
        Pem_av_in_val = self.Pem_av_in
        efficiency_val = self.efficiency
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            If_ref=If_ref_val,
            Id_ref=Id_ref_val,
            Iq_ref=Iq_ref_val,
            Ud_ref=Ud_ref_val,
            Uq_ref=Uq_ref_val,
            N0=N0_val,
            felec=felec_val,
            Tem_av_ref=Tem_av_ref_val,
            Pem_av_ref=Pem_av_ref_val,
            Pem_av_in=Pem_av_in_val,
            efficiency=efficiency_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.If_ref = None
        # Set to None the properties inherited from OPdq
        super(OPdqf, self)._set_None()

    def _get_If_ref(self):
        """getter of If_ref"""
        return self._If_ref

    def _set_If_ref(self, value):
        """setter of If_ref"""
        check_var("If_ref", value, "float")
        self._If_ref = value

    If_ref = property(
        fget=_get_If_ref,
        fset=_set_If_ref,
        doc=u"""DC rotor current

        :Type: float
        """,
    )
