# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Subdomain_Airgap.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Subdomain_Airgap
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
    from ..Methods.Simulation.Subdomain_Airgap.comp_flux_density import (
        comp_flux_density,
    )
except ImportError as error:
    comp_flux_density = error

try:
    from ..Methods.Simulation.Subdomain_Airgap.get_constants_number import (
        get_constants_number,
    )
except ImportError as error:
    get_constants_number = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_Airgap(Subdomain):
    """Subdomain class for airgap region"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Subdomain_Airgap.comp_flux_density
    if isinstance(comp_flux_density, ImportError):
        comp_flux_density = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Airgap method comp_flux_density: "
                    + str(comp_flux_density)
                )
            )
        )
    else:
        comp_flux_density = comp_flux_density
    # cf Methods.Simulation.Subdomain_Airgap.get_constants_number
    if isinstance(get_constants_number, ImportError):
        get_constants_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_Airgap method get_constants_number: "
                    + str(get_constants_number)
                )
            )
        )
    else:
        get_constants_number = get_constants_number
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
        Rrbo=None,
        Rsbo=None,
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
            if "C" in list(init_dict.keys()):
                C = init_dict["C"]
            if "D" in list(init_dict.keys()):
                D = init_dict["D"]
            if "Rrbo" in list(init_dict.keys()):
                Rrbo = init_dict["Rrbo"]
            if "Rsbo" in list(init_dict.keys()):
                Rsbo = init_dict["Rsbo"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "number" in list(init_dict.keys()):
                number = init_dict["number"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.Rrbo = Rrbo
        self.Rsbo = Rsbo
        # Call Subdomain init
        super(Subdomain_Airgap, self).__init__(
            k=k, number=number, permeability_relative=permeability_relative
        )
        # The class is frozen (in Subdomain init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_Airgap_str = ""
        # Get the properties inherited from Subdomain
        Subdomain_Airgap_str += super(Subdomain_Airgap, self).__str__()
        Subdomain_Airgap_str += (
            "A = "
            + linesep
            + str(self.A).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Airgap_str += (
            "B = "
            + linesep
            + str(self.B).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Airgap_str += (
            "C = "
            + linesep
            + str(self.C).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Airgap_str += (
            "D = "
            + linesep
            + str(self.D).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_Airgap_str += "Rrbo = " + str(self.Rrbo) + linesep
        Subdomain_Airgap_str += "Rsbo = " + str(self.Rsbo) + linesep
        return Subdomain_Airgap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain
        if not super(Subdomain_Airgap, self).__eq__(other):
            return False
        if not array_equal(other.A, self.A):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.C, self.C):
            return False
        if not array_equal(other.D, self.D):
            return False
        if other.Rrbo != self.Rrbo:
            return False
        if other.Rsbo != self.Rsbo:
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
            super(Subdomain_Airgap, self).compare(
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
        if (
            other._Rrbo is not None
            and self._Rrbo is not None
            and isnan(other._Rrbo)
            and isnan(self._Rrbo)
        ):
            pass
        elif other._Rrbo != self._Rrbo:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Rrbo) + ", other=" + str(other._Rrbo) + ")"
                )
                diff_list.append(name + ".Rrbo" + val_str)
            else:
                diff_list.append(name + ".Rrbo")
        if (
            other._Rsbo is not None
            and self._Rsbo is not None
            and isnan(other._Rsbo)
            and isnan(self._Rsbo)
        ):
            pass
        elif other._Rsbo != self._Rsbo:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Rsbo) + ", other=" + str(other._Rsbo) + ")"
                )
                diff_list.append(name + ".Rsbo" + val_str)
            else:
                diff_list.append(name + ".Rsbo")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain
        S += super(Subdomain_Airgap, self).__sizeof__()
        S += getsizeof(self.A)
        S += getsizeof(self.B)
        S += getsizeof(self.C)
        S += getsizeof(self.D)
        S += getsizeof(self.Rrbo)
        S += getsizeof(self.Rsbo)
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
        Subdomain_Airgap_dict = super(Subdomain_Airgap, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.A is None:
            Subdomain_Airgap_dict["A"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Airgap_dict["A"] = self.A.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Airgap_dict["A"] = self.A.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Airgap_dict["A"] = self.A
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.B is None:
            Subdomain_Airgap_dict["B"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Airgap_dict["B"] = self.B.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Airgap_dict["B"] = self.B.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Airgap_dict["B"] = self.B
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.C is None:
            Subdomain_Airgap_dict["C"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Airgap_dict["C"] = self.C.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Airgap_dict["C"] = self.C.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Airgap_dict["C"] = self.C
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.D is None:
            Subdomain_Airgap_dict["D"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_Airgap_dict["D"] = self.D.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_Airgap_dict["D"] = self.D.copy()
            elif type_handle_ndarray == 2:
                Subdomain_Airgap_dict["D"] = self.D
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_Airgap_dict["Rrbo"] = self.Rrbo
        Subdomain_Airgap_dict["Rsbo"] = self.Rsbo
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_Airgap_dict["__class__"] = "Subdomain_Airgap"
        return Subdomain_Airgap_dict

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
        Rrbo_val = self.Rrbo
        Rsbo_val = self.Rsbo
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
            C=C_val,
            D=D_val,
            Rrbo=Rrbo_val,
            Rsbo=Rsbo_val,
            k=k_val,
            number=number_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.Rrbo = None
        self.Rsbo = None
        # Set to None the properties inherited from Subdomain
        super(Subdomain_Airgap, self)._set_None()

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

    def _get_Rrbo(self):
        """getter of Rrbo"""
        return self._Rrbo

    def _set_Rrbo(self, value):
        """setter of Rrbo"""
        check_var("Rrbo", value, "float")
        self._Rrbo = value

    Rrbo = property(
        fget=_get_Rrbo,
        fset=_set_Rrbo,
        doc=u"""Rotor bore radius

        :Type: float
        """,
    )

    def _get_Rsbo(self):
        """getter of Rsbo"""
        return self._Rsbo

    def _set_Rsbo(self, value):
        """setter of Rsbo"""
        check_var("Rsbo", value, "float")
        self._Rsbo = value

    Rsbo = property(
        fget=_get_Rsbo,
        fset=_set_Rsbo,
        doc=u"""Stator bore radius

        :Type: float
        """,
    )
