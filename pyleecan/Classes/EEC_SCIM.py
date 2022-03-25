# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_SCIM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_SCIM
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
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_SCIM._comp_flux_mean import _comp_flux_mean
except ImportError as error:
    _comp_flux_mean = error

try:
    from ..Methods.Simulation.EEC_SCIM._comp_Lm_FEA import _comp_Lm_FEA
except ImportError as error:
    _comp_Lm_FEA = error

try:
    from ..Methods.Simulation.EEC_SCIM.clear_parameters import clear_parameters
except ImportError as error:
    clear_parameters = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_K21 import comp_K21
except ImportError as error:
    comp_K21 = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_L1 import comp_L1
except ImportError as error:
    comp_L1 = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_L2 import comp_L2
except ImportError as error:
    comp_L2 = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_R2 import comp_R2
except ImportError as error:
    comp_R2 = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_skin_effect import comp_skin_effect
except ImportError as error:
    comp_skin_effect = error

try:
    from ..Methods.Simulation.EEC_SCIM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC_SCIM.solve_elementary import solve_elementary
except ImportError as error:
    solve_elementary = error

try:
    from ..Methods.Simulation.EEC_SCIM.update_from_ref import update_from_ref
except ImportError as error:
    update_from_ref = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class EEC_SCIM(EEC):
    """Electric module: Electrical Equivalent Circuit for Squirrel Cage Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_SCIM._comp_flux_mean
    if isinstance(_comp_flux_mean, ImportError):
        _comp_flux_mean = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method _comp_flux_mean: " + str(_comp_flux_mean)
                )
            )
        )
    else:
        _comp_flux_mean = _comp_flux_mean
    # cf Methods.Simulation.EEC_SCIM._comp_Lm_FEA
    if isinstance(_comp_Lm_FEA, ImportError):
        _comp_Lm_FEA = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method _comp_Lm_FEA: " + str(_comp_Lm_FEA)
                )
            )
        )
    else:
        _comp_Lm_FEA = _comp_Lm_FEA
    # cf Methods.Simulation.EEC_SCIM.clear_parameters
    if isinstance(clear_parameters, ImportError):
        clear_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method clear_parameters: "
                    + str(clear_parameters)
                )
            )
        )
    else:
        clear_parameters = clear_parameters
    # cf Methods.Simulation.EEC_SCIM.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method comp_joule_losses: "
                    + str(comp_joule_losses)
                )
            )
        )
    else:
        comp_joule_losses = comp_joule_losses
    # cf Methods.Simulation.EEC_SCIM.comp_K21
    if isinstance(comp_K21, ImportError):
        comp_K21 = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method comp_K21: " + str(comp_K21))
            )
        )
    else:
        comp_K21 = comp_K21
    # cf Methods.Simulation.EEC_SCIM.comp_L1
    if isinstance(comp_L1, ImportError):
        comp_L1 = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method comp_L1: " + str(comp_L1))
            )
        )
    else:
        comp_L1 = comp_L1
    # cf Methods.Simulation.EEC_SCIM.comp_L2
    if isinstance(comp_L2, ImportError):
        comp_L2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method comp_L2: " + str(comp_L2))
            )
        )
    else:
        comp_L2 = comp_L2
    # cf Methods.Simulation.EEC_SCIM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method comp_parameters: " + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_SCIM.comp_R2
    if isinstance(comp_R2, ImportError):
        comp_R2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method comp_R2: " + str(comp_R2))
            )
        )
    else:
        comp_R2 = comp_R2
    # cf Methods.Simulation.EEC_SCIM.comp_skin_effect
    if isinstance(comp_skin_effect, ImportError):
        comp_skin_effect = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method comp_skin_effect: "
                    + str(comp_skin_effect)
                )
            )
        )
    else:
        comp_skin_effect = comp_skin_effect
    # cf Methods.Simulation.EEC_SCIM.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.EEC_SCIM.solve_elementary
    if isinstance(solve_elementary, ImportError):
        solve_elementary = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method solve_elementary: "
                    + str(solve_elementary)
                )
            )
        )
    else:
        solve_elementary = solve_elementary
    # cf Methods.Simulation.EEC_SCIM.update_from_ref
    if isinstance(update_from_ref, ImportError):
        update_from_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method update_from_ref: " + str(update_from_ref)
                )
            )
        )
    else:
        update_from_ref = update_from_ref
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Rfe=None,
        L1=None,
        R2=None,
        L2=None,
        K21Z=None,
        K21I=None,
        Im_table=None,
        Lm_table=None,
        I1=None,
        I2=None,
        U1=None,
        U2=None,
        If=None,
        Lm=None,
        Im=None,
        type_skin_effect=1,
        OP=None,
        Tsta=20,
        Trot=20,
        Xkr_skinS=1,
        Xke_skinS=1,
        Xkr_skinR=1,
        Xke_skinR=1,
        R1=None,
        fluxlink=None,
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
            if "Rfe" in list(init_dict.keys()):
                Rfe = init_dict["Rfe"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "R2" in list(init_dict.keys()):
                R2 = init_dict["R2"]
            if "L2" in list(init_dict.keys()):
                L2 = init_dict["L2"]
            if "K21Z" in list(init_dict.keys()):
                K21Z = init_dict["K21Z"]
            if "K21I" in list(init_dict.keys()):
                K21I = init_dict["K21I"]
            if "Im_table" in list(init_dict.keys()):
                Im_table = init_dict["Im_table"]
            if "Lm_table" in list(init_dict.keys()):
                Lm_table = init_dict["Lm_table"]
            if "I1" in list(init_dict.keys()):
                I1 = init_dict["I1"]
            if "I2" in list(init_dict.keys()):
                I2 = init_dict["I2"]
            if "U1" in list(init_dict.keys()):
                U1 = init_dict["U1"]
            if "U2" in list(init_dict.keys()):
                U2 = init_dict["U2"]
            if "If" in list(init_dict.keys()):
                If = init_dict["If"]
            if "Lm" in list(init_dict.keys()):
                Lm = init_dict["Lm"]
            if "Im" in list(init_dict.keys()):
                Im = init_dict["Im"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "Xkr_skinS" in list(init_dict.keys()):
                Xkr_skinS = init_dict["Xkr_skinS"]
            if "Xke_skinS" in list(init_dict.keys()):
                Xke_skinS = init_dict["Xke_skinS"]
            if "Xkr_skinR" in list(init_dict.keys()):
                Xkr_skinR = init_dict["Xkr_skinR"]
            if "Xke_skinR" in list(init_dict.keys()):
                Xke_skinR = init_dict["Xke_skinR"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
        # Set the properties (value check and convertion are done in setter)
        self.Rfe = Rfe
        self.L1 = L1
        self.R2 = R2
        self.L2 = L2
        self.K21Z = K21Z
        self.K21I = K21I
        self.Im_table = Im_table
        self.Lm_table = Lm_table
        self.I1 = I1
        self.I2 = I2
        self.U1 = U1
        self.U2 = U2
        self.If = If
        self.Lm = Lm
        self.Im = Im
        # Call EEC init
        super(EEC_SCIM, self).__init__(
            type_skin_effect=type_skin_effect,
            OP=OP,
            Tsta=Tsta,
            Trot=Trot,
            Xkr_skinS=Xkr_skinS,
            Xke_skinS=Xke_skinS,
            Xkr_skinR=Xkr_skinR,
            Xke_skinR=Xke_skinR,
            R1=R1,
            fluxlink=fluxlink,
        )
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_SCIM_str = ""
        # Get the properties inherited from EEC
        EEC_SCIM_str += super(EEC_SCIM, self).__str__()
        EEC_SCIM_str += "Rfe = " + str(self.Rfe) + linesep
        EEC_SCIM_str += "L1 = " + str(self.L1) + linesep
        EEC_SCIM_str += "R2 = " + str(self.R2) + linesep
        EEC_SCIM_str += "L2 = " + str(self.L2) + linesep
        EEC_SCIM_str += "K21Z = " + str(self.K21Z) + linesep
        EEC_SCIM_str += "K21I = " + str(self.K21I) + linesep
        EEC_SCIM_str += (
            "Im_table = "
            + linesep
            + str(self.Im_table).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        EEC_SCIM_str += (
            "Lm_table = "
            + linesep
            + str(self.Lm_table).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        EEC_SCIM_str += "I1 = " + str(self.I1) + linesep
        EEC_SCIM_str += "I2 = " + str(self.I2) + linesep
        EEC_SCIM_str += "U1 = " + str(self.U1) + linesep
        EEC_SCIM_str += "U2 = " + str(self.U2) + linesep
        EEC_SCIM_str += "If = " + str(self.If) + linesep
        EEC_SCIM_str += "Lm = " + str(self.Lm) + linesep
        EEC_SCIM_str += "Im = " + str(self.Im) + linesep
        return EEC_SCIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_SCIM, self).__eq__(other):
            return False
        if other.Rfe != self.Rfe:
            return False
        if other.L1 != self.L1:
            return False
        if other.R2 != self.R2:
            return False
        if other.L2 != self.L2:
            return False
        if other.K21Z != self.K21Z:
            return False
        if other.K21I != self.K21I:
            return False
        if not array_equal(other.Im_table, self.Im_table):
            return False
        if not array_equal(other.Lm_table, self.Lm_table):
            return False
        if other.I1 != self.I1:
            return False
        if other.I2 != self.I2:
            return False
        if other.U1 != self.U1:
            return False
        if other.U2 != self.U2:
            return False
        if other.If != self.If:
            return False
        if other.Lm != self.Lm:
            return False
        if other.Im != self.Im:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EEC
        diff_list.extend(super(EEC_SCIM, self).compare(other, name=name))
        if other._Rfe != self._Rfe:
            diff_list.append(name + ".Rfe")
        if other._L1 != self._L1:
            diff_list.append(name + ".L1")
        if other._R2 != self._R2:
            diff_list.append(name + ".R2")
        if other._L2 != self._L2:
            diff_list.append(name + ".L2")
        if other._K21Z != self._K21Z:
            diff_list.append(name + ".K21Z")
        if other._K21I != self._K21I:
            diff_list.append(name + ".K21I")
        if not array_equal(other.Im_table, self.Im_table):
            diff_list.append(name + ".Im_table")
        if not array_equal(other.Lm_table, self.Lm_table):
            diff_list.append(name + ".Lm_table")
        if other._I1 != self._I1:
            diff_list.append(name + ".I1")
        if other._I2 != self._I2:
            diff_list.append(name + ".I2")
        if other._U1 != self._U1:
            diff_list.append(name + ".U1")
        if other._U2 != self._U2:
            diff_list.append(name + ".U2")
        if other._If != self._If:
            diff_list.append(name + ".If")
        if other._Lm != self._Lm:
            diff_list.append(name + ".Lm")
        if other._Im != self._Im:
            diff_list.append(name + ".Im")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_SCIM, self).__sizeof__()
        S += getsizeof(self.Rfe)
        S += getsizeof(self.L1)
        S += getsizeof(self.R2)
        S += getsizeof(self.L2)
        S += getsizeof(self.K21Z)
        S += getsizeof(self.K21I)
        S += getsizeof(self.Im_table)
        S += getsizeof(self.Lm_table)
        S += getsizeof(self.I1)
        S += getsizeof(self.I2)
        S += getsizeof(self.U1)
        S += getsizeof(self.U2)
        S += getsizeof(self.If)
        S += getsizeof(self.Lm)
        S += getsizeof(self.Im)
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

        # Get the properties inherited from EEC
        EEC_SCIM_dict = super(EEC_SCIM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        EEC_SCIM_dict["Rfe"] = self.Rfe
        EEC_SCIM_dict["L1"] = self.L1
        EEC_SCIM_dict["R2"] = self.R2
        EEC_SCIM_dict["L2"] = self.L2
        EEC_SCIM_dict["K21Z"] = self.K21Z
        EEC_SCIM_dict["K21I"] = self.K21I
        if self.Im_table is None:
            EEC_SCIM_dict["Im_table"] = None
        else:
            if type_handle_ndarray == 0:
                EEC_SCIM_dict["Im_table"] = self.Im_table.tolist()
            elif type_handle_ndarray == 1:
                EEC_SCIM_dict["Im_table"] = self.Im_table.copy()
            elif type_handle_ndarray == 2:
                EEC_SCIM_dict["Im_table"] = self.Im_table
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Lm_table is None:
            EEC_SCIM_dict["Lm_table"] = None
        else:
            if type_handle_ndarray == 0:
                EEC_SCIM_dict["Lm_table"] = self.Lm_table.tolist()
            elif type_handle_ndarray == 1:
                EEC_SCIM_dict["Lm_table"] = self.Lm_table.copy()
            elif type_handle_ndarray == 2:
                EEC_SCIM_dict["Lm_table"] = self.Lm_table
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.I1 is None:
            EEC_SCIM_dict["I1"] = None
        elif isinstance(self.I1, float):
            EEC_SCIM_dict["I1"] = self.I1
        else:
            EEC_SCIM_dict["I1"] = str(self.I1)
        if self.I2 is None:
            EEC_SCIM_dict["I2"] = None
        elif isinstance(self.I2, float):
            EEC_SCIM_dict["I2"] = self.I2
        else:
            EEC_SCIM_dict["I2"] = str(self.I2)
        if self.U1 is None:
            EEC_SCIM_dict["U1"] = None
        elif isinstance(self.U1, float):
            EEC_SCIM_dict["U1"] = self.U1
        else:
            EEC_SCIM_dict["U1"] = str(self.U1)
        if self.U2 is None:
            EEC_SCIM_dict["U2"] = None
        elif isinstance(self.U2, float):
            EEC_SCIM_dict["U2"] = self.U2
        else:
            EEC_SCIM_dict["U2"] = str(self.U2)
        if self.If is None:
            EEC_SCIM_dict["If"] = None
        elif isinstance(self.If, float):
            EEC_SCIM_dict["If"] = self.If
        else:
            EEC_SCIM_dict["If"] = str(self.If)
        EEC_SCIM_dict["Lm"] = self.Lm
        if self.Im is None:
            EEC_SCIM_dict["Im"] = None
        elif isinstance(self.Im, float):
            EEC_SCIM_dict["Im"] = self.Im
        else:
            EEC_SCIM_dict["Im"] = str(self.Im)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_SCIM_dict["__class__"] = "EEC_SCIM"
        return EEC_SCIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Rfe = None
        self.L1 = None
        self.R2 = None
        self.L2 = None
        self.K21Z = None
        self.K21I = None
        self.Im_table = None
        self.Lm_table = None
        self.I1 = None
        self.I2 = None
        self.U1 = None
        self.U2 = None
        self.If = None
        self.Lm = None
        self.Im = None
        # Set to None the properties inherited from EEC
        super(EEC_SCIM, self)._set_None()

    def _get_Rfe(self):
        """getter of Rfe"""
        return self._Rfe

    def _set_Rfe(self, value):
        """setter of Rfe"""
        check_var("Rfe", value, "float")
        self._Rfe = value

    Rfe = property(
        fget=_get_Rfe,
        fset=_set_Rfe,
        doc=u"""Iron loss resistance

        :Type: float
        """,
    )

    def _get_L1(self):
        """getter of L1"""
        return self._L1

    def _set_L1(self, value):
        """setter of L1"""
        check_var("L1", value, "float")
        self._L1 = value

    L1 = property(
        fget=_get_L1,
        fset=_set_L1,
        doc=u"""Stator phase inductance

        :Type: float
        """,
    )

    def _get_R2(self):
        """getter of R2"""
        return self._R2

    def _set_R2(self, value):
        """setter of R2"""
        check_var("R2", value, "float")
        self._R2 = value

    R2 = property(
        fget=_get_R2,
        fset=_set_R2,
        doc=u"""Rotor phase resistance

        :Type: float
        """,
    )

    def _get_L2(self):
        """getter of L2"""
        return self._L2

    def _set_L2(self, value):
        """setter of L2"""
        check_var("L2", value, "float")
        self._L2 = value

    L2 = property(
        fget=_get_L2,
        fset=_set_L2,
        doc=u"""Rotor phase inductance

        :Type: float
        """,
    )

    def _get_K21Z(self):
        """getter of K21Z"""
        return self._K21Z

    def _set_K21Z(self, value):
        """setter of K21Z"""
        check_var("K21Z", value, "float")
        self._K21Z = value

    K21Z = property(
        fget=_get_K21Z,
        fset=_set_K21Z,
        doc=u"""transformation ratio from secondary (2, rotor) to primary (1, stator) for impedance

        :Type: float
        """,
    )

    def _get_K21I(self):
        """getter of K21I"""
        return self._K21I

    def _set_K21I(self, value):
        """setter of K21I"""
        check_var("K21I", value, "float")
        self._K21I = value

    K21I = property(
        fget=_get_K21I,
        fset=_set_K21I,
        doc=u"""transformation ratio from secondary (2, rotor) to primary (1, stator) for current

        :Type: float
        """,
    )

    def _get_Im_table(self):
        """getter of Im_table"""
        return self._Im_table

    def _set_Im_table(self, value):
        """setter of Im_table"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Im_table", value, "ndarray")
        self._Im_table = value

    Im_table = property(
        fget=_get_Im_table,
        fset=_set_Im_table,
        doc=u"""Array of magnetizing current

        :Type: ndarray
        """,
    )

    def _get_Lm_table(self):
        """getter of Lm_table"""
        return self._Lm_table

    def _set_Lm_table(self, value):
        """setter of Lm_table"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Lm_table", value, "ndarray")
        self._Lm_table = value

    Lm_table = property(
        fget=_get_Lm_table,
        fset=_set_Lm_table,
        doc=u"""Array of magnetizing inductance function of Im_table

        :Type: ndarray
        """,
    )

    def _get_I1(self):
        """getter of I1"""
        return self._I1

    def _set_I1(self, value):
        """setter of I1"""
        if isinstance(value, str):
            value = complex(value)
        check_var("I1", value, "complex")
        self._I1 = value

    I1 = property(
        fget=_get_I1,
        fset=_set_I1,
        doc=u"""Stator phase current (after solve)

        :Type: complex
        """,
    )

    def _get_I2(self):
        """getter of I2"""
        return self._I2

    def _set_I2(self, value):
        """setter of I2"""
        if isinstance(value, str):
            value = complex(value)
        check_var("I2", value, "complex")
        self._I2 = value

    I2 = property(
        fget=_get_I2,
        fset=_set_I2,
        doc=u"""Rotor phase current (after solve)

        :Type: complex
        """,
    )

    def _get_U1(self):
        """getter of U1"""
        return self._U1

    def _set_U1(self, value):
        """setter of U1"""
        if isinstance(value, str):
            value = complex(value)
        check_var("U1", value, "complex")
        self._U1 = value

    U1 = property(
        fget=_get_U1,
        fset=_set_U1,
        doc=u"""Stator phase voltage (after solve)

        :Type: complex
        """,
    )

    def _get_U2(self):
        """getter of U2"""
        return self._U2

    def _set_U2(self, value):
        """setter of U2"""
        if isinstance(value, str):
            value = complex(value)
        check_var("U2", value, "complex")
        self._U2 = value

    U2 = property(
        fget=_get_U2,
        fset=_set_U2,
        doc=u"""Rotor phase voltage (after solve)

        :Type: complex
        """,
    )

    def _get_If(self):
        """getter of If"""
        return self._If

    def _set_If(self, value):
        """setter of If"""
        if isinstance(value, str):
            value = complex(value)
        check_var("If", value, "complex")
        self._If = value

    If = property(
        fget=_get_If,
        fset=_set_If,
        doc=u"""Iron loss current (after solve)

        :Type: complex
        """,
    )

    def _get_Lm(self):
        """getter of Lm"""
        return self._Lm

    def _set_Lm(self, value):
        """setter of Lm"""
        check_var("Lm", value, "float")
        self._Lm = value

    Lm = property(
        fget=_get_Lm,
        fset=_set_Lm,
        doc=u"""Magnetizing inductance (after solve)

        :Type: float
        """,
    )

    def _get_Im(self):
        """getter of Im"""
        return self._Im

    def _set_Im(self, value):
        """setter of Im"""
        if isinstance(value, str):
            value = complex(value)
        check_var("Im", value, "complex")
        self._Im = value

    Im = property(
        fget=_get_Im,
        fset=_set_Im,
        doc=u"""Magnetizing current (after solve)

        :Type: complex
        """,
    )
