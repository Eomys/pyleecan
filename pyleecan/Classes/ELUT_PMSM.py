# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ELUT_PMSM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ELUT_PMSM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .ELUT import ELUT

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ELUT_PMSM.get_param_dict import get_param_dict
except ImportError as error:
    get_param_dict = error

try:
    from ..Methods.Simulation.ELUT_PMSM.get_Lq import get_Lq
except ImportError as error:
    get_Lq = error

try:
    from ..Methods.Simulation.ELUT_PMSM.get_bemf import get_bemf
except ImportError as error:
    get_bemf = error

try:
    from ..Methods.Simulation.ELUT_PMSM.get_Ld import get_Ld
except ImportError as error:
    get_Ld = error

try:
    from ..Methods.Simulation.ELUT_PMSM.get_Lmd import get_Lmd
except ImportError as error:
    get_Lmd = error

try:
    from ..Methods.Simulation.ELUT_PMSM.get_Lmq import get_Lmq
except ImportError as error:
    get_Lmq = error

try:
    from ..Methods.Simulation.ELUT_PMSM.comp_Ldqh_from_Phidqh import (
        comp_Ldqh_from_Phidqh,
    )
except ImportError as error:
    comp_Ldqh_from_Phidqh = error

try:
    from ..Methods.Simulation.ELUT_PMSM.comp_Phidqh_from_Phiwind import (
        comp_Phidqh_from_Phiwind,
    )
except ImportError as error:
    comp_Phidqh_from_Phiwind = error

try:
    from ..Methods.Simulation.ELUT_PMSM.import_from_data import import_from_data
except ImportError as error:
    import_from_data = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ELUT_PMSM(ELUT):
    """ELUT class for PMSM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ELUT_PMSM.get_param_dict
    if isinstance(get_param_dict, ImportError):
        get_param_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_PMSM method get_param_dict: " + str(get_param_dict)
                )
            )
        )
    else:
        get_param_dict = get_param_dict
    # cf Methods.Simulation.ELUT_PMSM.get_Lq
    if isinstance(get_Lq, ImportError):
        get_Lq = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_PMSM method get_Lq: " + str(get_Lq))
            )
        )
    else:
        get_Lq = get_Lq
    # cf Methods.Simulation.ELUT_PMSM.get_bemf
    if isinstance(get_bemf, ImportError):
        get_bemf = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_PMSM method get_bemf: " + str(get_bemf))
            )
        )
    else:
        get_bemf = get_bemf
    # cf Methods.Simulation.ELUT_PMSM.get_Ld
    if isinstance(get_Ld, ImportError):
        get_Ld = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_PMSM method get_Ld: " + str(get_Ld))
            )
        )
    else:
        get_Ld = get_Ld
    # cf Methods.Simulation.ELUT_PMSM.get_Lmd
    if isinstance(get_Lmd, ImportError):
        get_Lmd = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_PMSM method get_Lmd: " + str(get_Lmd))
            )
        )
    else:
        get_Lmd = get_Lmd
    # cf Methods.Simulation.ELUT_PMSM.get_Lmq
    if isinstance(get_Lmq, ImportError):
        get_Lmq = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_PMSM method get_Lmq: " + str(get_Lmq))
            )
        )
    else:
        get_Lmq = get_Lmq
    # cf Methods.Simulation.ELUT_PMSM.comp_Ldqh_from_Phidqh
    if isinstance(comp_Ldqh_from_Phidqh, ImportError):
        comp_Ldqh_from_Phidqh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_PMSM method comp_Ldqh_from_Phidqh: "
                    + str(comp_Ldqh_from_Phidqh)
                )
            )
        )
    else:
        comp_Ldqh_from_Phidqh = comp_Ldqh_from_Phidqh
    # cf Methods.Simulation.ELUT_PMSM.comp_Phidqh_from_Phiwind
    if isinstance(comp_Phidqh_from_Phiwind, ImportError):
        comp_Phidqh_from_Phiwind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_PMSM method comp_Phidqh_from_Phiwind: "
                    + str(comp_Phidqh_from_Phiwind)
                )
            )
        )
    else:
        comp_Phidqh_from_Phiwind = comp_Phidqh_from_Phiwind
    # cf Methods.Simulation.ELUT_PMSM.import_from_data
    if isinstance(import_from_data, ImportError):
        import_from_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_PMSM method import_from_data: "
                    + str(import_from_data)
                )
            )
        )
    else:
        import_from_data = import_from_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Phi_dqh=None,
        I_dqh=None,
        Tmag_ref=20,
        E0=None,
        E_dqh=None,
        orders_dqh=None,
        R1=None,
        L1=None,
        T1_ref=20,
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
            if "Phi_dqh" in list(init_dict.keys()):
                Phi_dqh = init_dict["Phi_dqh"]
            if "I_dqh" in list(init_dict.keys()):
                I_dqh = init_dict["I_dqh"]
            if "Tmag_ref" in list(init_dict.keys()):
                Tmag_ref = init_dict["Tmag_ref"]
            if "E0" in list(init_dict.keys()):
                E0 = init_dict["E0"]
            if "E_dqh" in list(init_dict.keys()):
                E_dqh = init_dict["E_dqh"]
            if "orders_dqh" in list(init_dict.keys()):
                orders_dqh = init_dict["orders_dqh"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "T1_ref" in list(init_dict.keys()):
                T1_ref = init_dict["T1_ref"]
        # Set the properties (value check and convertion are done in setter)
        self.Phi_dqh = Phi_dqh
        self.I_dqh = I_dqh
        self.Tmag_ref = Tmag_ref
        self.E0 = E0
        self.E_dqh = E_dqh
        self.orders_dqh = orders_dqh
        # Call ELUT init
        super(ELUT_PMSM, self).__init__(R1=R1, L1=L1, T1_ref=T1_ref)
        # The class is frozen (in ELUT init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ELUT_PMSM_str = ""
        # Get the properties inherited from ELUT
        ELUT_PMSM_str += super(ELUT_PMSM, self).__str__()
        ELUT_PMSM_str += (
            "Phi_dqh = "
            + linesep
            + str(self.Phi_dqh).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_PMSM_str += (
            "I_dqh = "
            + linesep
            + str(self.I_dqh).replace(linesep, linesep + "\t")
            + linesep
        )
        ELUT_PMSM_str += "Tmag_ref = " + str(self.Tmag_ref) + linesep
        ELUT_PMSM_str += "E0 = " + str(self.E0) + linesep
        ELUT_PMSM_str += (
            "E_dqh = "
            + linesep
            + str(self.E_dqh).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_PMSM_str += (
            "orders_dqh = "
            + linesep
            + str(self.orders_dqh).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ELUT_PMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ELUT
        if not super(ELUT_PMSM, self).__eq__(other):
            return False
        if not array_equal(other.Phi_dqh, self.Phi_dqh):
            return False
        if other.I_dqh != self.I_dqh:
            return False
        if other.Tmag_ref != self.Tmag_ref:
            return False
        if other.E0 != self.E0:
            return False
        if not array_equal(other.E_dqh, self.E_dqh):
            return False
        if not array_equal(other.orders_dqh, self.orders_dqh):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ELUT
        diff_list.extend(super(ELUT_PMSM, self).compare(other, name=name))
        if not array_equal(other.Phi_dqh, self.Phi_dqh):
            diff_list.append(name + ".Phi_dqh")
        if other._I_dqh != self._I_dqh:
            diff_list.append(name + ".I_dqh")
        if other._Tmag_ref != self._Tmag_ref:
            diff_list.append(name + ".Tmag_ref")
        if other._E0 != self._E0:
            diff_list.append(name + ".E0")
        if not array_equal(other.E_dqh, self.E_dqh):
            diff_list.append(name + ".E_dqh")
        if not array_equal(other.orders_dqh, self.orders_dqh):
            diff_list.append(name + ".orders_dqh")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ELUT
        S += super(ELUT_PMSM, self).__sizeof__()
        S += getsizeof(self.Phi_dqh)
        if self.I_dqh is not None:
            for value in self.I_dqh:
                S += getsizeof(value)
        S += getsizeof(self.Tmag_ref)
        S += getsizeof(self.E0)
        S += getsizeof(self.E_dqh)
        S += getsizeof(self.orders_dqh)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from ELUT
        ELUT_PMSM_dict = super(ELUT_PMSM, self).as_dict(**kwargs)
        if self.Phi_dqh is None:
            ELUT_PMSM_dict["Phi_dqh"] = None
        else:
            ELUT_PMSM_dict["Phi_dqh"] = self.Phi_dqh.tolist()
        ELUT_PMSM_dict["I_dqh"] = self.I_dqh.copy() if self.I_dqh is not None else None
        ELUT_PMSM_dict["Tmag_ref"] = self.Tmag_ref
        ELUT_PMSM_dict["E0"] = self.E0
        if self.E_dqh is None:
            ELUT_PMSM_dict["E_dqh"] = None
        else:
            ELUT_PMSM_dict["E_dqh"] = self.E_dqh.tolist()
        if self.orders_dqh is None:
            ELUT_PMSM_dict["orders_dqh"] = None
        else:
            ELUT_PMSM_dict["orders_dqh"] = self.orders_dqh.tolist()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ELUT_PMSM_dict["__class__"] = "ELUT_PMSM"
        return ELUT_PMSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Phi_dqh = None
        self.I_dqh = None
        self.Tmag_ref = None
        self.E0 = None
        self.E_dqh = None
        self.orders_dqh = None
        # Set to None the properties inherited from ELUT
        super(ELUT_PMSM, self)._set_None()

    def _get_Phi_dqh(self):
        """getter of Phi_dqh"""
        return self._Phi_dqh

    def _set_Phi_dqh(self, value):
        """setter of Phi_dqh"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Phi_dqh", value, "ndarray")
        self._Phi_dqh = value

    Phi_dqh = property(
        fget=_get_Phi_dqh,
        fset=_set_Phi_dqh,
        doc=u"""Stator winding flux llinkage fundamental calculated from user-input inductance tables

        :Type: ndarray
        """,
    )

    def _get_I_dqh(self):
        """getter of I_dqh"""
        return self._I_dqh

    def _set_I_dqh(self, value):
        """setter of I_dqh"""
        if type(value) is int and value == -1:
            value = list()
        check_var("I_dqh", value, "list")
        self._I_dqh = value

    I_dqh = property(
        fget=_get_I_dqh,
        fset=_set_I_dqh,
        doc=u"""Id Iq Ih table corresponding to flux linkage data given in Phi_dqh

        :Type: list
        """,
    )

    def _get_Tmag_ref(self):
        """getter of Tmag_ref"""
        return self._Tmag_ref

    def _set_Tmag_ref(self, value):
        """setter of Tmag_ref"""
        check_var("Tmag_ref", value, "float")
        self._Tmag_ref = value

    Tmag_ref = property(
        fget=_get_Tmag_ref,
        fset=_set_Tmag_ref,
        doc=u"""Magnet average temperature at which Phi_dqh is given

        :Type: float
        """,
    )

    def _get_E0(self):
        """getter of E0"""
        return self._E0

    def _set_E0(self, value):
        """setter of E0"""
        check_var("E0", value, "float")
        self._E0 = value

    E0 = property(
        fget=_get_E0,
        fset=_set_E0,
        doc=u"""RMS fundamental back electromotive force (bemf) along Q-axis

        :Type: float
        """,
    )

    def _get_E_dqh(self):
        """getter of E_dqh"""
        return self._E_dqh

    def _set_E_dqh(self, value):
        """setter of E_dqh"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("E_dqh", value, "ndarray")
        self._E_dqh = value

    E_dqh = property(
        fget=_get_E_dqh,
        fset=_set_E_dqh,
        doc=u"""Back emf harmonics along DQH axis

        :Type: ndarray
        """,
    )

    def _get_orders_dqh(self):
        """getter of orders_dqh"""
        return self._orders_dqh

    def _set_orders_dqh(self, value):
        """setter of orders_dqh"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("orders_dqh", value, "ndarray")
        self._orders_dqh = value

    orders_dqh = property(
        fget=_get_orders_dqh,
        fset=_set_orders_dqh,
        doc=u"""Back harmonic orders (multiple of fundamental electrical frequency) corresponding to Edqh spectrum

        :Type: ndarray
        """,
    )
