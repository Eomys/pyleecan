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
from .Subdomain import Subdomain

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.comp_flux_density import (
        comp_flux_density,
    )
except ImportError as error:
    comp_flux_density = error

try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.comp_interface_airgap import (
        comp_interface_airgap,
    )
except ImportError as error:
    comp_interface_airgap = error

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

try:
    from ..Methods.Simulation.Subdomain_MagnetSurface.get_constants_number import (
        get_constants_number,
    )
except ImportError as error:
    get_constants_number = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Subdomain_MagnetSurface(Subdomain):
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
    # cf Methods.Simulation.Subdomain_MagnetSurface.comp_interface_airgap
    if isinstance(comp_interface_airgap, ImportError):
        comp_interface_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_MagnetSurface method comp_interface_airgap: "
                    + str(comp_interface_airgap)
                )
            )
        )
    else:
        comp_interface_airgap = comp_interface_airgap
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
    # cf Methods.Simulation.Subdomain_MagnetSurface.get_constants_number
    if isinstance(get_constants_number, ImportError):
        get_constants_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Subdomain_MagnetSurface method get_constants_number: "
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
        type_magnetization=0,
        magnet_width=None,
        Ryoke=None,
        A=None,
        B=None,
        C=None,
        D=None,
        Rbore=None,
        Mrn=None,
        Mtn=None,
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
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
            if "magnet_width" in list(init_dict.keys()):
                magnet_width = init_dict["magnet_width"]
            if "Ryoke" in list(init_dict.keys()):
                Ryoke = init_dict["Ryoke"]
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "C" in list(init_dict.keys()):
                C = init_dict["C"]
            if "D" in list(init_dict.keys()):
                D = init_dict["D"]
            if "Rbore" in list(init_dict.keys()):
                Rbore = init_dict["Rbore"]
            if "Mrn" in list(init_dict.keys()):
                Mrn = init_dict["Mrn"]
            if "Mtn" in list(init_dict.keys()):
                Mtn = init_dict["Mtn"]
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "number" in list(init_dict.keys()):
                number = init_dict["number"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.type_magnetization = type_magnetization
        self.magnet_width = magnet_width
        self.Ryoke = Ryoke
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.Rbore = Rbore
        self.Mrn = Mrn
        self.Mtn = Mtn
        # Call Subdomain init
        super(Subdomain_MagnetSurface, self).__init__(
            k=k, number=number, permeability_relative=permeability_relative
        )
        # The class is frozen (in Subdomain init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_MagnetSurface_str = ""
        # Get the properties inherited from Subdomain
        Subdomain_MagnetSurface_str += super(Subdomain_MagnetSurface, self).__str__()
        Subdomain_MagnetSurface_str += (
            "type_magnetization = " + str(self.type_magnetization) + linesep
        )
        Subdomain_MagnetSurface_str += (
            "magnet_width = " + str(self.magnet_width) + linesep
        )
        Subdomain_MagnetSurface_str += "Ryoke = " + str(self.Ryoke) + linesep
        Subdomain_MagnetSurface_str += (
            "A = "
            + linesep
            + str(self.A).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_MagnetSurface_str += (
            "B = "
            + linesep
            + str(self.B).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_MagnetSurface_str += (
            "C = "
            + linesep
            + str(self.C).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_MagnetSurface_str += (
            "D = "
            + linesep
            + str(self.D).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_MagnetSurface_str += "Rbore = " + str(self.Rbore) + linesep
        Subdomain_MagnetSurface_str += (
            "Mrn = "
            + linesep
            + str(self.Mrn).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_MagnetSurface_str += (
            "Mtn = "
            + linesep
            + str(self.Mtn).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Subdomain_MagnetSurface_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain
        if not super(Subdomain_MagnetSurface, self).__eq__(other):
            return False
        if other.type_magnetization != self.type_magnetization:
            return False
        if other.magnet_width != self.magnet_width:
            return False
        if other.Ryoke != self.Ryoke:
            return False
        if not array_equal(other.A, self.A):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.C, self.C):
            return False
        if not array_equal(other.D, self.D):
            return False
        if other.Rbore != self.Rbore:
            return False
        if not array_equal(other.Mrn, self.Mrn):
            return False
        if not array_equal(other.Mtn, self.Mtn):
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
        if (
            other._magnet_width is not None
            and self._magnet_width is not None
            and isnan(other._magnet_width)
            and isnan(self._magnet_width)
        ):
            pass
        elif other._magnet_width != self._magnet_width:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._magnet_width)
                    + ", other="
                    + str(other._magnet_width)
                    + ")"
                )
                diff_list.append(name + ".magnet_width" + val_str)
            else:
                diff_list.append(name + ".magnet_width")
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
        if not array_equal(other.A, self.A):
            diff_list.append(name + ".A")
        if not array_equal(other.B, self.B):
            diff_list.append(name + ".B")
        if not array_equal(other.C, self.C):
            diff_list.append(name + ".C")
        if not array_equal(other.D, self.D):
            diff_list.append(name + ".D")
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
        if not array_equal(other.Mrn, self.Mrn):
            diff_list.append(name + ".Mrn")
        if not array_equal(other.Mtn, self.Mtn):
            diff_list.append(name + ".Mtn")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain
        S += super(Subdomain_MagnetSurface, self).__sizeof__()
        S += getsizeof(self.type_magnetization)
        S += getsizeof(self.magnet_width)
        S += getsizeof(self.Ryoke)
        S += getsizeof(self.A)
        S += getsizeof(self.B)
        S += getsizeof(self.C)
        S += getsizeof(self.D)
        S += getsizeof(self.Rbore)
        S += getsizeof(self.Mrn)
        S += getsizeof(self.Mtn)
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
        Subdomain_MagnetSurface_dict = super(Subdomain_MagnetSurface, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Subdomain_MagnetSurface_dict["type_magnetization"] = self.type_magnetization
        Subdomain_MagnetSurface_dict["magnet_width"] = self.magnet_width
        Subdomain_MagnetSurface_dict["Ryoke"] = self.Ryoke
        if self.A is None:
            Subdomain_MagnetSurface_dict["A"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["A"] = self.A.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["A"] = self.A.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["A"] = self.A
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.B is None:
            Subdomain_MagnetSurface_dict["B"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["B"] = self.B.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["B"] = self.B.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["B"] = self.B
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.C is None:
            Subdomain_MagnetSurface_dict["C"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["C"] = self.C.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["C"] = self.C.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["C"] = self.C
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.D is None:
            Subdomain_MagnetSurface_dict["D"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["D"] = self.D.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["D"] = self.D.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["D"] = self.D
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_MagnetSurface_dict["Rbore"] = self.Rbore
        if self.Mrn is None:
            Subdomain_MagnetSurface_dict["Mrn"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["Mrn"] = self.Mrn.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["Mrn"] = self.Mrn.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["Mrn"] = self.Mrn
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Mtn is None:
            Subdomain_MagnetSurface_dict["Mtn"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_MagnetSurface_dict["Mtn"] = self.Mtn.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_MagnetSurface_dict["Mtn"] = self.Mtn.copy()
            elif type_handle_ndarray == 2:
                Subdomain_MagnetSurface_dict["Mtn"] = self.Mtn
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_MagnetSurface_dict["__class__"] = "Subdomain_MagnetSurface"
        return Subdomain_MagnetSurface_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_magnetization_val = self.type_magnetization
        magnet_width_val = self.magnet_width
        Ryoke_val = self.Ryoke
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
        Rbore_val = self.Rbore
        if self.Mrn is None:
            Mrn_val = None
        else:
            Mrn_val = self.Mrn.copy()
        if self.Mtn is None:
            Mtn_val = None
        else:
            Mtn_val = self.Mtn.copy()
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        number_val = self.number
        permeability_relative_val = self.permeability_relative
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            type_magnetization=type_magnetization_val,
            magnet_width=magnet_width_val,
            Ryoke=Ryoke_val,
            A=A_val,
            B=B_val,
            C=C_val,
            D=D_val,
            Rbore=Rbore_val,
            Mrn=Mrn_val,
            Mtn=Mtn_val,
            k=k_val,
            number=number_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_magnetization = None
        self.magnet_width = None
        self.Ryoke = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.Rbore = None
        self.Mrn = None
        self.Mtn = None
        # Set to None the properties inherited from Subdomain
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

    def _get_magnet_width(self):
        """getter of magnet_width"""
        return self._magnet_width

    def _set_magnet_width(self, value):
        """setter of magnet_width"""
        check_var("magnet_width", value, "float", Vmin=0)
        self._magnet_width = value

    magnet_width = property(
        fget=_get_magnet_width,
        fset=_set_magnet_width,
        doc=u"""Angular width of a magnet

        :Type: float
        :min: 0
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
        doc=u"""Radius at magnet / yoke interface

        :Type: float
        :min: 0
        """,
    )

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
        doc=u"""Radius at magnet / airgap interface

        :Type: float
        :min: 0
        """,
    )

    def _get_Mrn(self):
        """getter of Mrn"""
        return self._Mrn

    def _set_Mrn(self, value):
        """setter of Mrn"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Mrn", value, "ndarray")
        self._Mrn = value

    Mrn = property(
        fget=_get_Mrn,
        fset=_set_Mrn,
        doc=u"""Fourier series of radial magnetization

        :Type: ndarray
        """,
    )

    def _get_Mtn(self):
        """getter of Mtn"""
        return self._Mtn

    def _set_Mtn(self, value):
        """setter of Mtn"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Mtn", value, "ndarray")
        self._Mtn = value

    Mtn = property(
        fget=_get_Mtn,
        fset=_set_Mtn,
        doc=u"""Fourier series of circumferential magnetization

        :Type: ndarray
        """,
    )
