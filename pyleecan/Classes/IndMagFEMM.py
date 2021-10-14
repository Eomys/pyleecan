# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/IndMagFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/IndMagFEMM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .IndMag import IndMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.IndMagFEMM.comp_inductance import comp_inductance
except ImportError as error:
    comp_inductance = error

try:
    from ..Methods.Simulation.IndMagFEMM.solve_FEMM import solve_FEMM
except ImportError as error:
    solve_FEMM = error


from ._check import InitUnKnowClassError


class IndMagFEMM(IndMag):
    """Electric module: Magnetic Inductance with FEMM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.IndMagFEMM.comp_inductance
    if isinstance(comp_inductance, ImportError):
        comp_inductance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use IndMagFEMM method comp_inductance: "
                    + str(comp_inductance)
                )
            )
        )
    else:
        comp_inductance = comp_inductance
    # cf Methods.Simulation.IndMagFEMM.solve_FEMM
    if isinstance(solve_FEMM, ImportError):
        solve_FEMM = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use IndMagFEMM method solve_FEMM: " + str(solve_FEMM)
                )
            )
        )
    else:
        solve_FEMM = solve_FEMM
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        FEMM_dict=-1,
        type_calc_leakage=0,
        is_sliding_band=True,
        is_periodicity_a=False,
        Nt_tot=5,
        Kgeo_fineness=0.5,
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
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "type_calc_leakage" in list(init_dict.keys()):
                type_calc_leakage = init_dict["type_calc_leakage"]
            if "is_sliding_band" in list(init_dict.keys()):
                is_sliding_band = init_dict["is_sliding_band"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Kgeo_fineness" in list(init_dict.keys()):
                Kgeo_fineness = init_dict["Kgeo_fineness"]
        # Set the properties (value check and convertion are done in setter)
        self.FEMM_dict = FEMM_dict
        self.type_calc_leakage = type_calc_leakage
        self.is_sliding_band = is_sliding_band
        self.is_periodicity_a = is_periodicity_a
        self.Nt_tot = Nt_tot
        self.Kgeo_fineness = Kgeo_fineness
        # Call IndMag init
        super(IndMagFEMM, self).__init__()
        # The class is frozen (in IndMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        IndMagFEMM_str = ""
        # Get the properties inherited from IndMag
        IndMagFEMM_str += super(IndMagFEMM, self).__str__()
        IndMagFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        IndMagFEMM_str += "type_calc_leakage = " + str(self.type_calc_leakage) + linesep
        IndMagFEMM_str += "is_sliding_band = " + str(self.is_sliding_band) + linesep
        IndMagFEMM_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        IndMagFEMM_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        IndMagFEMM_str += "Kgeo_fineness = " + str(self.Kgeo_fineness) + linesep
        return IndMagFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from IndMag
        if not super(IndMagFEMM, self).__eq__(other):
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.type_calc_leakage != self.type_calc_leakage:
            return False
        if other.is_sliding_band != self.is_sliding_band:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Kgeo_fineness != self.Kgeo_fineness:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from IndMag
        diff_list.extend(super(IndMagFEMM, self).compare(other, name=name))
        if other._FEMM_dict != self._FEMM_dict:
            diff_list.append(name + ".FEMM_dict")
        if other._type_calc_leakage != self._type_calc_leakage:
            diff_list.append(name + ".type_calc_leakage")
        if other._is_sliding_band != self._is_sliding_band:
            diff_list.append(name + ".is_sliding_band")
        if other._is_periodicity_a != self._is_periodicity_a:
            diff_list.append(name + ".is_periodicity_a")
        if other._Nt_tot != self._Nt_tot:
            diff_list.append(name + ".Nt_tot")
        if other._Kgeo_fineness != self._Kgeo_fineness:
            diff_list.append(name + ".Kgeo_fineness")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from IndMag
        S += super(IndMagFEMM, self).__sizeof__()
        if self.FEMM_dict is not None:
            for key, value in self.FEMM_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.type_calc_leakage)
        S += getsizeof(self.is_sliding_band)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.Nt_tot)
        S += getsizeof(self.Kgeo_fineness)
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

        # Get the properties inherited from IndMag
        IndMagFEMM_dict = super(IndMagFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        IndMagFEMM_dict["FEMM_dict"] = (
            self.FEMM_dict.copy() if self.FEMM_dict is not None else None
        )
        IndMagFEMM_dict["type_calc_leakage"] = self.type_calc_leakage
        IndMagFEMM_dict["is_sliding_band"] = self.is_sliding_band
        IndMagFEMM_dict["is_periodicity_a"] = self.is_periodicity_a
        IndMagFEMM_dict["Nt_tot"] = self.Nt_tot
        IndMagFEMM_dict["Kgeo_fineness"] = self.Kgeo_fineness
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        IndMagFEMM_dict["__class__"] = "IndMagFEMM"
        return IndMagFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEMM_dict = None
        self.type_calc_leakage = None
        self.is_sliding_band = None
        self.is_periodicity_a = None
        self.Nt_tot = None
        self.Kgeo_fineness = None
        # Set to None the properties inherited from IndMag
        super(IndMagFEMM, self)._set_None()

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    FEMM_dict = property(
        fget=_get_FEMM_dict,
        fset=_set_FEMM_dict,
        doc=u"""To enforce user-defined values for FEMM main parameters 

        :Type: dict
        """,
    )

    def _get_type_calc_leakage(self):
        """getter of type_calc_leakage"""
        return self._type_calc_leakage

    def _set_type_calc_leakage(self, value):
        """setter of type_calc_leakage"""
        check_var("type_calc_leakage", value, "int", Vmin=0, Vmax=1)
        self._type_calc_leakage = value

    type_calc_leakage = property(
        fget=_get_type_calc_leakage,
        fset=_set_type_calc_leakage,
        doc=u"""0 no leakage calculation /  1 calculation using single slot 

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_is_sliding_band(self):
        """getter of is_sliding_band"""
        return self._is_sliding_band

    def _set_is_sliding_band(self, value):
        """setter of is_sliding_band"""
        check_var("is_sliding_band", value, "bool")
        self._is_sliding_band = value

    is_sliding_band = property(
        fget=_get_is_sliding_band,
        fset=_set_is_sliding_band,
        doc=u"""0 to desactivate the sliding band

        :Type: bool
        """,
    )

    def _get_is_periodicity_a(self):
        """getter of is_periodicity_a"""
        return self._is_periodicity_a

    def _set_is_periodicity_a(self, value):
        """setter of is_periodicity_a"""
        check_var("is_periodicity_a", value, "bool")
        self._is_periodicity_a = value

    is_periodicity_a = property(
        fget=_get_is_periodicity_a,
        fset=_set_is_periodicity_a,
        doc=u"""True to take into account the spatial periodicity of the machine

        :Type: bool
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Number of time steps for the FEMM simulation

        :Type: int
        """,
    )

    def _get_Kgeo_fineness(self):
        """getter of Kgeo_fineness"""
        return self._Kgeo_fineness

    def _set_Kgeo_fineness(self, value):
        """setter of Kgeo_fineness"""
        check_var("Kgeo_fineness", value, "float")
        self._Kgeo_fineness = value

    Kgeo_fineness = property(
        fget=_get_Kgeo_fineness,
        fset=_set_Kgeo_fineness,
        doc=u"""global coefficient to adjust geometry fineness in FEMM (0.5 : default , > 1 : finner , < 1 : less fine)

        :Type: float
        """,
    )
