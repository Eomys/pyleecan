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
from .Subdomain_Slot import Subdomain_Slot

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


class Subdomain_SlotOpening(Subdomain_Slot):
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
        C=None,
        D=None,
        E=None,
        F=None,
        opening_width=None,
        v=None,
        Ropening=None,
        A=None,
        B=None,
        center_angle=None,
        slot_width=None,
        Ji=None,
        Jik=None,
        Ryoke=None,
        Rbore=None,
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
            if "C" in list(init_dict.keys()):
                C = init_dict["C"]
            if "D" in list(init_dict.keys()):
                D = init_dict["D"]
            if "E" in list(init_dict.keys()):
                E = init_dict["E"]
            if "F" in list(init_dict.keys()):
                F = init_dict["F"]
            if "opening_width" in list(init_dict.keys()):
                opening_width = init_dict["opening_width"]
            if "v" in list(init_dict.keys()):
                v = init_dict["v"]
            if "Ropening" in list(init_dict.keys()):
                Ropening = init_dict["Ropening"]
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
            if "k" in list(init_dict.keys()):
                k = init_dict["k"]
            if "number" in list(init_dict.keys()):
                number = init_dict["number"]
            if "permeability_relative" in list(init_dict.keys()):
                permeability_relative = init_dict["permeability_relative"]
        # Set the properties (value check and convertion are done in setter)
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.opening_width = opening_width
        self.v = v
        self.Ropening = Ropening
        # Call Subdomain_Slot init
        super(Subdomain_SlotOpening, self).__init__(
            A=A,
            B=B,
            center_angle=center_angle,
            slot_width=slot_width,
            Ji=Ji,
            Jik=Jik,
            Ryoke=Ryoke,
            Rbore=Rbore,
            k=k,
            number=number,
            permeability_relative=permeability_relative,
        )
        # The class is frozen (in Subdomain_Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Subdomain_SlotOpening_str = ""
        # Get the properties inherited from Subdomain_Slot
        Subdomain_SlotOpening_str += super(Subdomain_SlotOpening, self).__str__()
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
        Subdomain_SlotOpening_str += (
            "E = "
            + linesep
            + str(self.E).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += (
            "F = "
            + linesep
            + str(self.F).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += (
            "opening_width = " + str(self.opening_width) + linesep
        )
        Subdomain_SlotOpening_str += (
            "v = "
            + linesep
            + str(self.v).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Subdomain_SlotOpening_str += "Ropening = " + str(self.Ropening) + linesep
        return Subdomain_SlotOpening_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Subdomain_Slot
        if not super(Subdomain_SlotOpening, self).__eq__(other):
            return False
        if not array_equal(other.C, self.C):
            return False
        if not array_equal(other.D, self.D):
            return False
        if not array_equal(other.E, self.E):
            return False
        if not array_equal(other.F, self.F):
            return False
        if other.opening_width != self.opening_width:
            return False
        if not array_equal(other.v, self.v):
            return False
        if other.Ropening != self.Ropening:
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
            super(Subdomain_SlotOpening, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if not array_equal(other.C, self.C):
            diff_list.append(name + ".C")
        if not array_equal(other.D, self.D):
            diff_list.append(name + ".D")
        if not array_equal(other.E, self.E):
            diff_list.append(name + ".E")
        if not array_equal(other.F, self.F):
            diff_list.append(name + ".F")
        if (
            other._opening_width is not None
            and self._opening_width is not None
            and isnan(other._opening_width)
            and isnan(self._opening_width)
        ):
            pass
        elif other._opening_width != self._opening_width:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._opening_width)
                    + ", other="
                    + str(other._opening_width)
                    + ")"
                )
                diff_list.append(name + ".opening_width" + val_str)
            else:
                diff_list.append(name + ".opening_width")
        if not array_equal(other.v, self.v):
            diff_list.append(name + ".v")
        if (
            other._Ropening is not None
            and self._Ropening is not None
            and isnan(other._Ropening)
            and isnan(self._Ropening)
        ):
            pass
        elif other._Ropening != self._Ropening:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Ropening)
                    + ", other="
                    + str(other._Ropening)
                    + ")"
                )
                diff_list.append(name + ".Ropening" + val_str)
            else:
                diff_list.append(name + ".Ropening")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Subdomain_Slot
        S += super(Subdomain_SlotOpening, self).__sizeof__()
        S += getsizeof(self.C)
        S += getsizeof(self.D)
        S += getsizeof(self.E)
        S += getsizeof(self.F)
        S += getsizeof(self.opening_width)
        S += getsizeof(self.v)
        S += getsizeof(self.Ropening)
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
        Subdomain_SlotOpening_dict = super(Subdomain_SlotOpening, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
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
        if self.E is None:
            Subdomain_SlotOpening_dict["E"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["E"] = self.E.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["E"] = self.E.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["E"] = self.E
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.F is None:
            Subdomain_SlotOpening_dict["F"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["F"] = self.F.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["F"] = self.F.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["F"] = self.F
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_SlotOpening_dict["opening_width"] = self.opening_width
        if self.v is None:
            Subdomain_SlotOpening_dict["v"] = None
        else:
            if type_handle_ndarray == 0:
                Subdomain_SlotOpening_dict["v"] = self.v.tolist()
            elif type_handle_ndarray == 1:
                Subdomain_SlotOpening_dict["v"] = self.v.copy()
            elif type_handle_ndarray == 2:
                Subdomain_SlotOpening_dict["v"] = self.v
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Subdomain_SlotOpening_dict["Ropening"] = self.Ropening
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Subdomain_SlotOpening_dict["__class__"] = "Subdomain_SlotOpening"
        return Subdomain_SlotOpening_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.C is None:
            C_val = None
        else:
            C_val = self.C.copy()
        if self.D is None:
            D_val = None
        else:
            D_val = self.D.copy()
        if self.E is None:
            E_val = None
        else:
            E_val = self.E.copy()
        if self.F is None:
            F_val = None
        else:
            F_val = self.F.copy()
        opening_width_val = self.opening_width
        if self.v is None:
            v_val = None
        else:
            v_val = self.v.copy()
        Ropening_val = self.Ropening
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
        if self.k is None:
            k_val = None
        else:
            k_val = self.k.copy()
        number_val = self.number
        permeability_relative_val = self.permeability_relative
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            C=C_val,
            D=D_val,
            E=E_val,
            F=F_val,
            opening_width=opening_width_val,
            v=v_val,
            Ropening=Ropening_val,
            A=A_val,
            B=B_val,
            center_angle=center_angle_val,
            slot_width=slot_width_val,
            Ji=Ji_val,
            Jik=Jik_val,
            Ryoke=Ryoke_val,
            Rbore=Rbore_val,
            k=k_val,
            number=number_val,
            permeability_relative=permeability_relative_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.C = None
        self.D = None
        self.E = None
        self.F = None
        self.opening_width = None
        self.v = None
        self.Ropening = None
        # Set to None the properties inherited from Subdomain_Slot
        super(Subdomain_SlotOpening, self)._set_None()

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
        doc=u"""First integration constant function of harmonic number and time in slot opening subdomain

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
        doc=u"""Second integration constant function of harmonic number and time in slot opening subdomain

        :Type: ndarray
        """,
    )

    def _get_E(self):
        """getter of E"""
        return self._E

    def _set_E(self, value):
        """setter of E"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("E", value, "ndarray")
        self._E = value

    E = property(
        fget=_get_E,
        fset=_set_E,
        doc=u"""Third integration constant function of harmonic number and time in slot opening subdomain

        :Type: ndarray
        """,
    )

    def _get_F(self):
        """getter of F"""
        return self._F

    def _set_F(self, value):
        """setter of F"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("F", value, "ndarray")
        self._F = value

    F = property(
        fget=_get_F,
        fset=_set_F,
        doc=u"""Fourth integration constant function of harmonic number and time in slot opening subdomain

        :Type: ndarray
        """,
    )

    def _get_opening_width(self):
        """getter of opening_width"""
        return self._opening_width

    def _set_opening_width(self, value):
        """setter of opening_width"""
        check_var("opening_width", value, "float", Vmin=0)
        self._opening_width = value

    opening_width = property(
        fget=_get_opening_width,
        fset=_set_opening_width,
        doc=u"""Angular width of slot opening

        :Type: float
        :min: 0
        """,
    )

    def _get_v(self):
        """getter of v"""
        return self._v

    def _set_v(self, value):
        """setter of v"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("v", value, "ndarray")
        self._v = value

    v = property(
        fget=_get_v,
        fset=_set_v,
        doc=u"""Harmonic vector for slot opening

        :Type: ndarray
        """,
    )

    def _get_Ropening(self):
        """getter of Ropening"""
        return self._Ropening

    def _set_Ropening(self, value):
        """setter of Ropening"""
        check_var("Ropening", value, "float", Vmin=0)
        self._Ropening = value

    Ropening = property(
        fget=_get_Ropening,
        fset=_set_Ropening,
        doc=u"""Radius of slot opening / slot interface

        :Type: float
        :min: 0
        """,
    )
