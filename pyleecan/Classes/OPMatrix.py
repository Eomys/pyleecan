# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/OPMatrix.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/OPMatrix
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
    from ..Methods.Simulation.OPMatrix.get_N_OP import get_N_OP
except ImportError as error:
    get_N_OP = error

try:
    from ..Methods.Simulation.OPMatrix.get_OP import get_OP
except ImportError as error:
    get_OP = error

try:
    from ..Methods.Simulation.OPMatrix.get_OP_list import get_OP_list
except ImportError as error:
    get_OP_list = error

try:
    from ..Methods.Simulation.OPMatrix.get_OP_array import get_OP_array
except ImportError as error:
    get_OP_array = error

try:
    from ..Methods.Simulation.OPMatrix.set_OP_array import set_OP_array
except ImportError as error:
    set_OP_array = error

try:
    from ..Methods.Simulation.OPMatrix.has_Pem import has_Pem
except ImportError as error:
    has_Pem = error

try:
    from ..Methods.Simulation.OPMatrix.has_Tem import has_Tem
except ImportError as error:
    has_Tem = error

try:
    from ..Methods.Simulation.OPMatrix.has_slip import has_slip
except ImportError as error:
    has_slip = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class OPMatrix(FrozenClass):
    """Define the Operating Point of a variable speed simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.OPMatrix.get_N_OP
    if isinstance(get_N_OP, ImportError):
        get_N_OP = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPMatrix method get_N_OP: " + str(get_N_OP))
            )
        )
    else:
        get_N_OP = get_N_OP
    # cf Methods.Simulation.OPMatrix.get_OP
    if isinstance(get_OP, ImportError):
        get_OP = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPMatrix method get_OP: " + str(get_OP))
            )
        )
    else:
        get_OP = get_OP
    # cf Methods.Simulation.OPMatrix.get_OP_list
    if isinstance(get_OP_list, ImportError):
        get_OP_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OPMatrix method get_OP_list: " + str(get_OP_list)
                )
            )
        )
    else:
        get_OP_list = get_OP_list
    # cf Methods.Simulation.OPMatrix.get_OP_array
    if isinstance(get_OP_array, ImportError):
        get_OP_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OPMatrix method get_OP_array: " + str(get_OP_array)
                )
            )
        )
    else:
        get_OP_array = get_OP_array
    # cf Methods.Simulation.OPMatrix.set_OP_array
    if isinstance(set_OP_array, ImportError):
        set_OP_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OPMatrix method set_OP_array: " + str(set_OP_array)
                )
            )
        )
    else:
        set_OP_array = set_OP_array
    # cf Methods.Simulation.OPMatrix.has_Pem
    if isinstance(has_Pem, ImportError):
        has_Pem = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPMatrix method has_Pem: " + str(has_Pem))
            )
        )
    else:
        has_Pem = has_Pem
    # cf Methods.Simulation.OPMatrix.has_Tem
    if isinstance(has_Tem, ImportError):
        has_Tem = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPMatrix method has_Tem: " + str(has_Tem))
            )
        )
    else:
        has_Tem = has_Tem
    # cf Methods.Simulation.OPMatrix.has_slip
    if isinstance(has_slip, ImportError):
        has_slip = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPMatrix method has_slip: " + str(has_slip))
            )
        )
    else:
        has_slip = has_slip
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        N0=None,
        Id_ref=None,
        Iq_ref=None,
        Ud_ref=None,
        Uq_ref=None,
        Tem_av_ref=None,
        Pem_av_ref=None,
        slip_ref=None,
        is_output_power=True,
        If_ref=None,
        col_names=None,
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
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
            if "slip_ref" in list(init_dict.keys()):
                slip_ref = init_dict["slip_ref"]
            if "is_output_power" in list(init_dict.keys()):
                is_output_power = init_dict["is_output_power"]
            if "If_ref" in list(init_dict.keys()):
                If_ref = init_dict["If_ref"]
            if "col_names" in list(init_dict.keys()):
                col_names = init_dict["col_names"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.N0 = N0
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        self.Ud_ref = Ud_ref
        self.Uq_ref = Uq_ref
        self.Tem_av_ref = Tem_av_ref
        self.Pem_av_ref = Pem_av_ref
        self.slip_ref = slip_ref
        self.is_output_power = is_output_power
        self.If_ref = If_ref
        self.col_names = col_names

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OPMatrix_str = ""
        if self.parent is None:
            OPMatrix_str += "parent = None " + linesep
        else:
            OPMatrix_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OPMatrix_str += (
            "N0 = "
            + linesep
            + str(self.N0).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Id_ref = "
            + linesep
            + str(self.Id_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Iq_ref = "
            + linesep
            + str(self.Iq_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Ud_ref = "
            + linesep
            + str(self.Ud_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Uq_ref = "
            + linesep
            + str(self.Uq_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Tem_av_ref = "
            + linesep
            + str(self.Tem_av_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "Pem_av_ref = "
            + linesep
            + str(self.Pem_av_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "slip_ref = "
            + linesep
            + str(self.slip_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += "is_output_power = " + str(self.is_output_power) + linesep
        OPMatrix_str += (
            "If_ref = "
            + linesep
            + str(self.If_ref).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OPMatrix_str += (
            "col_names = "
            + linesep
            + str(self.col_names).replace(linesep, linesep + "\t")
            + linesep
        )
        return OPMatrix_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.N0, self.N0):
            return False
        if not array_equal(other.Id_ref, self.Id_ref):
            return False
        if not array_equal(other.Iq_ref, self.Iq_ref):
            return False
        if not array_equal(other.Ud_ref, self.Ud_ref):
            return False
        if not array_equal(other.Uq_ref, self.Uq_ref):
            return False
        if not array_equal(other.Tem_av_ref, self.Tem_av_ref):
            return False
        if not array_equal(other.Pem_av_ref, self.Pem_av_ref):
            return False
        if not array_equal(other.slip_ref, self.slip_ref):
            return False
        if other.is_output_power != self.is_output_power:
            return False
        if not array_equal(other.If_ref, self.If_ref):
            return False
        if other.col_names != self.col_names:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if not array_equal(other.N0, self.N0):
            diff_list.append(name + ".N0")
        if not array_equal(other.Id_ref, self.Id_ref):
            diff_list.append(name + ".Id_ref")
        if not array_equal(other.Iq_ref, self.Iq_ref):
            diff_list.append(name + ".Iq_ref")
        if not array_equal(other.Ud_ref, self.Ud_ref):
            diff_list.append(name + ".Ud_ref")
        if not array_equal(other.Uq_ref, self.Uq_ref):
            diff_list.append(name + ".Uq_ref")
        if not array_equal(other.Tem_av_ref, self.Tem_av_ref):
            diff_list.append(name + ".Tem_av_ref")
        if not array_equal(other.Pem_av_ref, self.Pem_av_ref):
            diff_list.append(name + ".Pem_av_ref")
        if not array_equal(other.slip_ref, self.slip_ref):
            diff_list.append(name + ".slip_ref")
        if other._is_output_power != self._is_output_power:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_output_power)
                    + ", other="
                    + str(other._is_output_power)
                    + ")"
                )
                diff_list.append(name + ".is_output_power" + val_str)
            else:
                diff_list.append(name + ".is_output_power")
        if not array_equal(other.If_ref, self.If_ref):
            diff_list.append(name + ".If_ref")
        if other._col_names != self._col_names:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._col_names)
                    + ", other="
                    + str(other._col_names)
                    + ")"
                )
                diff_list.append(name + ".col_names" + val_str)
            else:
                diff_list.append(name + ".col_names")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.N0)
        S += getsizeof(self.Id_ref)
        S += getsizeof(self.Iq_ref)
        S += getsizeof(self.Ud_ref)
        S += getsizeof(self.Uq_ref)
        S += getsizeof(self.Tem_av_ref)
        S += getsizeof(self.Pem_av_ref)
        S += getsizeof(self.slip_ref)
        S += getsizeof(self.is_output_power)
        S += getsizeof(self.If_ref)
        if self.col_names is not None:
            for value in self.col_names:
                S += getsizeof(value)
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

        OPMatrix_dict = dict()
        if self.N0 is None:
            OPMatrix_dict["N0"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["N0"] = self.N0.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["N0"] = self.N0.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["N0"] = self.N0
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Id_ref is None:
            OPMatrix_dict["Id_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Id_ref"] = self.Id_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Id_ref"] = self.Id_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Id_ref"] = self.Id_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Iq_ref is None:
            OPMatrix_dict["Iq_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Iq_ref"] = self.Iq_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Iq_ref"] = self.Iq_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Iq_ref"] = self.Iq_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Ud_ref is None:
            OPMatrix_dict["Ud_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Ud_ref"] = self.Ud_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Ud_ref"] = self.Ud_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Ud_ref"] = self.Ud_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Uq_ref is None:
            OPMatrix_dict["Uq_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Uq_ref"] = self.Uq_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Uq_ref"] = self.Uq_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Uq_ref"] = self.Uq_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Tem_av_ref is None:
            OPMatrix_dict["Tem_av_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Tem_av_ref"] = self.Tem_av_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Tem_av_ref"] = self.Tem_av_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Tem_av_ref"] = self.Tem_av_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Pem_av_ref is None:
            OPMatrix_dict["Pem_av_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["Pem_av_ref"] = self.Pem_av_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["Pem_av_ref"] = self.Pem_av_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["Pem_av_ref"] = self.Pem_av_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.slip_ref is None:
            OPMatrix_dict["slip_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["slip_ref"] = self.slip_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["slip_ref"] = self.slip_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["slip_ref"] = self.slip_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OPMatrix_dict["is_output_power"] = self.is_output_power
        if self.If_ref is None:
            OPMatrix_dict["If_ref"] = None
        else:
            if type_handle_ndarray == 0:
                OPMatrix_dict["If_ref"] = self.If_ref.tolist()
            elif type_handle_ndarray == 1:
                OPMatrix_dict["If_ref"] = self.If_ref.copy()
            elif type_handle_ndarray == 2:
                OPMatrix_dict["If_ref"] = self.If_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OPMatrix_dict["col_names"] = (
            self.col_names.copy() if self.col_names is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        OPMatrix_dict["__class__"] = "OPMatrix"
        return OPMatrix_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.N0 is None:
            N0_val = None
        else:
            N0_val = self.N0.copy()
        if self.Id_ref is None:
            Id_ref_val = None
        else:
            Id_ref_val = self.Id_ref.copy()
        if self.Iq_ref is None:
            Iq_ref_val = None
        else:
            Iq_ref_val = self.Iq_ref.copy()
        if self.Ud_ref is None:
            Ud_ref_val = None
        else:
            Ud_ref_val = self.Ud_ref.copy()
        if self.Uq_ref is None:
            Uq_ref_val = None
        else:
            Uq_ref_val = self.Uq_ref.copy()
        if self.Tem_av_ref is None:
            Tem_av_ref_val = None
        else:
            Tem_av_ref_val = self.Tem_av_ref.copy()
        if self.Pem_av_ref is None:
            Pem_av_ref_val = None
        else:
            Pem_av_ref_val = self.Pem_av_ref.copy()
        if self.slip_ref is None:
            slip_ref_val = None
        else:
            slip_ref_val = self.slip_ref.copy()
        is_output_power_val = self.is_output_power
        if self.If_ref is None:
            If_ref_val = None
        else:
            If_ref_val = self.If_ref.copy()
        if self.col_names is None:
            col_names_val = None
        else:
            col_names_val = self.col_names.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            N0=N0_val,
            Id_ref=Id_ref_val,
            Iq_ref=Iq_ref_val,
            Ud_ref=Ud_ref_val,
            Uq_ref=Uq_ref_val,
            Tem_av_ref=Tem_av_ref_val,
            Pem_av_ref=Pem_av_ref_val,
            slip_ref=slip_ref_val,
            is_output_power=is_output_power_val,
            If_ref=If_ref_val,
            col_names=col_names_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N0 = None
        self.Id_ref = None
        self.Iq_ref = None
        self.Ud_ref = None
        self.Uq_ref = None
        self.Tem_av_ref = None
        self.Pem_av_ref = None
        self.slip_ref = None
        self.is_output_power = None
        self.If_ref = None
        self.col_names = None

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("N0", value, "ndarray")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: ndarray
        """,
    )

    def _get_Id_ref(self):
        """getter of Id_ref"""
        return self._Id_ref

    def _set_Id_ref(self, value):
        """setter of Id_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Id_ref", value, "ndarray")
        self._Id_ref = value

    Id_ref = property(
        fget=_get_Id_ref,
        fset=_set_Id_ref,
        doc=u"""d-axis current rms value

        :Type: ndarray
        """,
    )

    def _get_Iq_ref(self):
        """getter of Iq_ref"""
        return self._Iq_ref

    def _set_Iq_ref(self, value):
        """setter of Iq_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Iq_ref", value, "ndarray")
        self._Iq_ref = value

    Iq_ref = property(
        fget=_get_Iq_ref,
        fset=_set_Iq_ref,
        doc=u"""q-axis current rms value

        :Type: ndarray
        """,
    )

    def _get_Ud_ref(self):
        """getter of Ud_ref"""
        return self._Ud_ref

    def _set_Ud_ref(self, value):
        """setter of Ud_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ud_ref", value, "ndarray")
        self._Ud_ref = value

    Ud_ref = property(
        fget=_get_Ud_ref,
        fset=_set_Ud_ref,
        doc=u"""d-axis voltage rms value

        :Type: ndarray
        """,
    )

    def _get_Uq_ref(self):
        """getter of Uq_ref"""
        return self._Uq_ref

    def _set_Uq_ref(self, value):
        """setter of Uq_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Uq_ref", value, "ndarray")
        self._Uq_ref = value

    Uq_ref = property(
        fget=_get_Uq_ref,
        fset=_set_Uq_ref,
        doc=u"""q-axis voltage rms value

        :Type: ndarray
        """,
    )

    def _get_Tem_av_ref(self):
        """getter of Tem_av_ref"""
        return self._Tem_av_ref

    def _set_Tem_av_ref(self, value):
        """setter of Tem_av_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Tem_av_ref", value, "ndarray")
        self._Tem_av_ref = value

    Tem_av_ref = property(
        fget=_get_Tem_av_ref,
        fset=_set_Tem_av_ref,
        doc=u"""Output average electromagnetic torque

        :Type: ndarray
        """,
    )

    def _get_Pem_av_ref(self):
        """getter of Pem_av_ref"""
        return self._Pem_av_ref

    def _set_Pem_av_ref(self, value):
        """setter of Pem_av_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pem_av_ref", value, "ndarray")
        self._Pem_av_ref = value

    Pem_av_ref = property(
        fget=_get_Pem_av_ref,
        fset=_set_Pem_av_ref,
        doc=u"""Output/Input average Electromagnetic Power

        :Type: ndarray
        """,
    )

    def _get_slip_ref(self):
        """getter of slip_ref"""
        return self._slip_ref

    def _set_slip_ref(self, value):
        """setter of slip_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("slip_ref", value, "ndarray")
        self._slip_ref = value

    slip_ref = property(
        fget=_get_slip_ref,
        fset=_set_slip_ref,
        doc=u"""Rotor mechanical slip

        :Type: ndarray
        """,
    )

    def _get_is_output_power(self):
        """getter of is_output_power"""
        return self._is_output_power

    def _set_is_output_power(self, value):
        """setter of is_output_power"""
        check_var("is_output_power", value, "bool")
        self._is_output_power = value

    is_output_power = property(
        fget=_get_is_output_power,
        fset=_set_is_output_power,
        doc=u"""True if power given in OP_matrix is the output power, False if it is the input power

        :Type: bool
        """,
    )

    def _get_If_ref(self):
        """getter of If_ref"""
        return self._If_ref

    def _set_If_ref(self, value):
        """setter of If_ref"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("If_ref", value, "ndarray")
        self._If_ref = value

    If_ref = property(
        fget=_get_If_ref,
        fset=_set_If_ref,
        doc=u"""DC rotor current

        :Type: ndarray
        """,
    )

    def _get_col_names(self):
        """getter of col_names"""
        return self._col_names

    def _set_col_names(self, value):
        """setter of col_names"""
        if type(value) is int and value == -1:
            value = list()
        check_var("col_names", value, "list")
        self._col_names = value

    col_names = property(
        fget=_get_col_names,
        fset=_set_col_names,
        doc=u"""Name of the columns from set_OP_matrix

        :Type: list
        """,
    )
