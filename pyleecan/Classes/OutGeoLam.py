# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutGeoLam.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutGeoLam
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from numpy import array, array_equal
from ._check import InitUnKnowClassError


class OutGeoLam(FrozenClass):
    """Gather the geometrical and the global outputs of a lamination"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name_phase=None,
        BH_curve=None,
        Ksfill=None,
        S_slot=None,
        S_slot_wind=None,
        S_wind_act=None,
        sym=None,
        is_asym_wind=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            name_phase = obj.name_phase
            BH_curve = obj.BH_curve
            Ksfill = obj.Ksfill
            S_slot = obj.S_slot
            S_slot_wind = obj.S_slot_wind
            S_wind_act = obj.S_wind_act
            sym = obj.sym
            is_asym_wind = obj.is_asym_wind
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name_phase" in list(init_dict.keys()):
                name_phase = init_dict["name_phase"]
            if "BH_curve" in list(init_dict.keys()):
                BH_curve = init_dict["BH_curve"]
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "S_slot" in list(init_dict.keys()):
                S_slot = init_dict["S_slot"]
            if "S_slot_wind" in list(init_dict.keys()):
                S_slot_wind = init_dict["S_slot_wind"]
            if "S_wind_act" in list(init_dict.keys()):
                S_wind_act = init_dict["S_wind_act"]
            if "sym" in list(init_dict.keys()):
                sym = init_dict["sym"]
            if "is_asym_wind" in list(init_dict.keys()):
                is_asym_wind = init_dict["is_asym_wind"]
        # Initialisation by argument
        self.parent = None
        if name_phase == -1:
            name_phase = []
        self.name_phase = name_phase
        # BH_curve can be None, a ndarray or a list
        set_array(self, "BH_curve", BH_curve)
        self.Ksfill = Ksfill
        self.S_slot = S_slot
        self.S_slot_wind = S_slot_wind
        self.S_wind_act = S_wind_act
        self.sym = sym
        self.is_asym_wind = is_asym_wind

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutGeoLam_str = ""
        if self.parent is None:
            OutGeoLam_str += "parent = None " + linesep
        else:
            OutGeoLam_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutGeoLam_str += (
            "name_phase = "
            + linesep
            + str(self.name_phase).replace(linesep, linesep + "\t")
            + linesep
        )
        OutGeoLam_str += (
            "BH_curve = "
            + linesep
            + str(self.BH_curve).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutGeoLam_str += "Ksfill = " + str(self.Ksfill) + linesep
        OutGeoLam_str += "S_slot = " + str(self.S_slot) + linesep
        OutGeoLam_str += "S_slot_wind = " + str(self.S_slot_wind) + linesep
        OutGeoLam_str += "S_wind_act = " + str(self.S_wind_act) + linesep
        OutGeoLam_str += "sym = " + str(self.sym) + linesep
        OutGeoLam_str += "is_asym_wind = " + str(self.is_asym_wind) + linesep
        return OutGeoLam_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name_phase != self.name_phase:
            return False
        if not array_equal(other.BH_curve, self.BH_curve):
            return False
        if other.Ksfill != self.Ksfill:
            return False
        if other.S_slot != self.S_slot:
            return False
        if other.S_slot_wind != self.S_slot_wind:
            return False
        if other.S_wind_act != self.S_wind_act:
            return False
        if other.sym != self.sym:
            return False
        if other.is_asym_wind != self.is_asym_wind:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutGeoLam_dict = dict()
        OutGeoLam_dict["name_phase"] = self.name_phase
        if self.BH_curve is None:
            OutGeoLam_dict["BH_curve"] = None
        else:
            OutGeoLam_dict["BH_curve"] = self.BH_curve.tolist()
        OutGeoLam_dict["Ksfill"] = self.Ksfill
        OutGeoLam_dict["S_slot"] = self.S_slot
        OutGeoLam_dict["S_slot_wind"] = self.S_slot_wind
        OutGeoLam_dict["S_wind_act"] = self.S_wind_act
        OutGeoLam_dict["sym"] = self.sym
        OutGeoLam_dict["is_asym_wind"] = self.is_asym_wind
        # The class name is added to the dict fordeserialisation purpose
        OutGeoLam_dict["__class__"] = "OutGeoLam"
        return OutGeoLam_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name_phase = None
        self.BH_curve = None
        self.Ksfill = None
        self.S_slot = None
        self.S_slot_wind = None
        self.S_wind_act = None
        self.sym = None
        self.is_asym_wind = None

    def _get_name_phase(self):
        """getter of name_phase"""
        return self._name_phase

    def _set_name_phase(self, value):
        """setter of name_phase"""
        check_var("name_phase", value, "list")
        self._name_phase = value

    name_phase = property(
        fget=_get_name_phase,
        fset=_set_name_phase,
        doc=u"""Name of the phases of the winding (if any)

        :Type: list
        """,
    )

    def _get_BH_curve(self):
        """getter of BH_curve"""
        return self._BH_curve

    def _set_BH_curve(self, value):
        """setter of BH_curve"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("BH_curve", value, "ndarray")
        self._BH_curve = value

    BH_curve = property(
        fget=_get_BH_curve,
        fset=_set_BH_curve,
        doc=u"""B(H) curve (two columns matrix, H and B(H))

        :Type: ndarray
        """,
    )

    def _get_Ksfill(self):
        """getter of Ksfill"""
        return self._Ksfill

    def _set_Ksfill(self, value):
        """setter of Ksfill"""
        check_var("Ksfill", value, "float")
        self._Ksfill = value

    Ksfill = property(
        fget=_get_Ksfill,
        fset=_set_Ksfill,
        doc=u"""Slot fill factor

        :Type: float
        """,
    )

    def _get_S_slot(self):
        """getter of S_slot"""
        return self._S_slot

    def _set_S_slot(self, value):
        """setter of S_slot"""
        check_var("S_slot", value, "float")
        self._S_slot = value

    S_slot = property(
        fget=_get_S_slot,
        fset=_set_S_slot,
        doc=u"""Slot surface

        :Type: float
        """,
    )

    def _get_S_slot_wind(self):
        """getter of S_slot_wind"""
        return self._S_slot_wind

    def _set_S_slot_wind(self, value):
        """setter of S_slot_wind"""
        check_var("S_slot_wind", value, "float")
        self._S_slot_wind = value

    S_slot_wind = property(
        fget=_get_S_slot_wind,
        fset=_set_S_slot_wind,
        doc=u"""Slot winding surface

        :Type: float
        """,
    )

    def _get_S_wind_act(self):
        """getter of S_wind_act"""
        return self._S_wind_act

    def _set_S_wind_act(self, value):
        """setter of S_wind_act"""
        check_var("S_wind_act", value, "float")
        self._S_wind_act = value

    S_wind_act = property(
        fget=_get_S_wind_act,
        fset=_set_S_wind_act,
        doc=u"""Conductor active surface

        :Type: float
        """,
    )

    def _get_sym(self):
        """getter of sym"""
        return self._sym

    def _set_sym(self, value):
        """setter of sym"""
        check_var("sym", value, "int")
        self._sym = value

    sym = property(
        fget=_get_sym,
        fset=_set_sym,
        doc=u"""Symmetry factor of the lamination (1=full machine; 2 = half;...)

        :Type: int
        """,
    )

    def _get_is_asym_wind(self):
        """getter of is_asym_wind"""
        return self._is_asym_wind

    def _set_is_asym_wind(self, value):
        """setter of is_asym_wind"""
        check_var("is_asym_wind", value, "bool")
        self._is_asym_wind = value

    is_asym_wind = property(
        fget=_get_is_asym_wind,
        fset=_set_is_asym_wind,
        doc=u"""True if the winding has a asymmetry

        :Type: bool
        """,
    )
