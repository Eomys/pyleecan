# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ELUT_SCIM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ELUT_SCIM
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
    from ..Methods.Simulation.ELUT_SCIM.get_parameters import get_parameters
except ImportError as error:
    get_parameters = error

try:
    from ..Methods.Simulation.ELUT_SCIM.get_Lm import get_Lm
except ImportError as error:
    get_Lm = error

try:
    from ..Methods.Simulation.ELUT_SCIM.comp_Lm_from_Phim import comp_Lm_from_Phim
except ImportError as error:
    comp_Lm_from_Phim = error

try:
    from ..Methods.Simulation.ELUT_SCIM.import_from_data import import_from_data
except ImportError as error:
    import_from_data = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ELUT_SCIM(ELUT):
    """ELUT class for SCIM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ELUT_SCIM.get_parameters
    if isinstance(get_parameters, ImportError):
        get_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_SCIM method get_parameters: " + str(get_parameters)
                )
            )
        )
    else:
        get_parameters = get_parameters
    # cf Methods.Simulation.ELUT_SCIM.get_Lm
    if isinstance(get_Lm, ImportError):
        get_Lm = property(
            fget=lambda x: raise_(
                ImportError("Can't use ELUT_SCIM method get_Lm: " + str(get_Lm))
            )
        )
    else:
        get_Lm = get_Lm
    # cf Methods.Simulation.ELUT_SCIM.comp_Lm_from_Phim
    if isinstance(comp_Lm_from_Phim, ImportError):
        comp_Lm_from_Phim = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_SCIM method comp_Lm_from_Phim: "
                    + str(comp_Lm_from_Phim)
                )
            )
        )
    else:
        comp_Lm_from_Phim = comp_Lm_from_Phim
    # cf Methods.Simulation.ELUT_SCIM.import_from_data
    if isinstance(import_from_data, ImportError):
        import_from_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT_SCIM method import_from_data: "
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
        Phi_m=None,
        Trot_ref=20,
        K_RSE_rot=None,
        K_ISE_rot=None,
        Rs=None,
        Ls=None,
        Tsta_ref=20,
        K_RSE_sta=None,
        K_ISE_sta=None,
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
            if "Phi_m" in list(init_dict.keys()):
                Phi_m = init_dict["Phi_m"]
            if "Trot_ref" in list(init_dict.keys()):
                Trot_ref = init_dict["Trot_ref"]
            if "K_RSE_rot" in list(init_dict.keys()):
                K_RSE_rot = init_dict["K_RSE_rot"]
            if "K_ISE_rot" in list(init_dict.keys()):
                K_ISE_rot = init_dict["K_ISE_rot"]
            if "Rs" in list(init_dict.keys()):
                Rs = init_dict["Rs"]
            if "Ls" in list(init_dict.keys()):
                Ls = init_dict["Ls"]
            if "Tsta_ref" in list(init_dict.keys()):
                Tsta_ref = init_dict["Tsta_ref"]
            if "K_RSE_sta" in list(init_dict.keys()):
                K_RSE_sta = init_dict["K_RSE_sta"]
            if "K_ISE_sta" in list(init_dict.keys()):
                K_ISE_sta = init_dict["K_ISE_sta"]
        # Set the properties (value check and convertion are done in setter)
        self.Phi_m = Phi_m
        self.Trot_ref = Trot_ref
        self.K_RSE_rot = K_RSE_rot
        self.K_ISE_rot = K_ISE_rot
        # Call ELUT init
        super(ELUT_SCIM, self).__init__(
            Rs=Rs, Ls=Ls, Tsta_ref=Tsta_ref, K_RSE_sta=K_RSE_sta, K_ISE_sta=K_ISE_sta
        )
        # The class is frozen (in ELUT init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ELUT_SCIM_str = ""
        # Get the properties inherited from ELUT
        ELUT_SCIM_str += super(ELUT_SCIM, self).__str__()
        ELUT_SCIM_str += (
            "Phi_m = "
            + linesep
            + str(self.Phi_m).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_SCIM_str += "Trot_ref = " + str(self.Trot_ref) + linesep
        ELUT_SCIM_str += (
            "K_RSE_rot = "
            + linesep
            + str(self.K_RSE_rot).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_SCIM_str += (
            "K_ISE_rot = "
            + linesep
            + str(self.K_ISE_rot).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ELUT_SCIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ELUT
        if not super(ELUT_SCIM, self).__eq__(other):
            return False
        if not array_equal(other.Phi_m, self.Phi_m):
            return False
        if other.Trot_ref != self.Trot_ref:
            return False
        if not array_equal(other.K_RSE_rot, self.K_RSE_rot):
            return False
        if not array_equal(other.K_ISE_rot, self.K_ISE_rot):
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
        diff_list.extend(super(ELUT_SCIM, self).compare(other, name=name))
        if not array_equal(other.Phi_m, self.Phi_m):
            diff_list.append(name + ".Phi_m")
        if other._Trot_ref != self._Trot_ref:
            diff_list.append(name + ".Trot_ref")
        if not array_equal(other.K_RSE_rot, self.K_RSE_rot):
            diff_list.append(name + ".K_RSE_rot")
        if not array_equal(other.K_ISE_rot, self.K_ISE_rot):
            diff_list.append(name + ".K_ISE_rot")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ELUT
        S += super(ELUT_SCIM, self).__sizeof__()
        S += getsizeof(self.Phi_m)
        S += getsizeof(self.Trot_ref)
        S += getsizeof(self.K_RSE_rot)
        S += getsizeof(self.K_ISE_rot)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from ELUT
        ELUT_SCIM_dict = super(ELUT_SCIM, self).as_dict(**kwargs)
        if self.Phi_m is None:
            ELUT_SCIM_dict["Phi_m"] = None
        else:
            ELUT_SCIM_dict["Phi_m"] = self.Phi_m.tolist()
        ELUT_SCIM_dict["Trot_ref"] = self.Trot_ref
        if self.K_RSE_rot is None:
            ELUT_SCIM_dict["K_RSE_rot"] = None
        else:
            ELUT_SCIM_dict["K_RSE_rot"] = self.K_RSE_rot.tolist()
        if self.K_ISE_rot is None:
            ELUT_SCIM_dict["K_ISE_rot"] = None
        else:
            ELUT_SCIM_dict["K_ISE_rot"] = self.K_ISE_rot.tolist()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ELUT_SCIM_dict["__class__"] = "ELUT_SCIM"
        return ELUT_SCIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Phi_m = None
        self.Trot_ref = None
        self.K_RSE_rot = None
        self.K_ISE_rot = None
        # Set to None the properties inherited from ELUT
        super(ELUT_SCIM, self)._set_None()

    def _get_Phi_m(self):
        """getter of Phi_m"""
        return self._Phi_m

    def _set_Phi_m(self, value):
        """setter of Phi_m"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Phi_m", value, "ndarray")
        self._Phi_m = value

    Phi_m = property(
        fget=_get_Phi_m,
        fset=_set_Phi_m,
        doc=u"""Stator winding flux look-up table: list of DataTime objects whose (Id,Iq) is given by Idq list

        :Type: ndarray
        """,
    )

    def _get_Trot_ref(self):
        """getter of Trot_ref"""
        return self._Trot_ref

    def _set_Trot_ref(self, value):
        """setter of Trot_ref"""
        check_var("Trot_ref", value, "float")
        self._Trot_ref = value

    Trot_ref = property(
        fget=_get_Trot_ref,
        fset=_set_Trot_ref,
        doc=u"""Rotor bar average temperature at which Phi_m is given

        :Type: float
        """,
    )

    def _get_K_RSE_rot(self):
        """getter of K_RSE_rot"""
        return self._K_RSE_rot

    def _set_K_RSE_rot(self, value):
        """setter of K_RSE_rot"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("K_RSE_rot", value, "ndarray")
        self._K_RSE_rot = value

    K_RSE_rot = property(
        fget=_get_K_RSE_rot,
        fset=_set_K_RSE_rot,
        doc=u"""Rotor winding Resistance Skin Effect factor function of frequency

        :Type: ndarray
        """,
    )

    def _get_K_ISE_rot(self):
        """getter of K_ISE_rot"""
        return self._K_ISE_rot

    def _set_K_ISE_rot(self, value):
        """setter of K_ISE_rot"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("K_ISE_rot", value, "ndarray")
        self._K_ISE_rot = value

    K_ISE_rot = property(
        fget=_get_K_ISE_rot,
        fset=_set_K_ISE_rot,
        doc=u"""Rotor winding Inductance Skin Effect factor function of frequency

        :Type: ndarray
        """,
    )
