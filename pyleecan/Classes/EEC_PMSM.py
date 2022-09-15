# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_PMSM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_PMSM
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
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_PMSM.clear_parameters import clear_parameters
except ImportError as error:
    clear_parameters = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_BEMF_harmonics import comp_BEMF_harmonics
except ImportError as error:
    comp_BEMF_harmonics = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_Ld import comp_Ld
except ImportError as error:
    comp_Ld = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_Lq import comp_Lq
except ImportError as error:
    comp_Lq = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_Phidq import comp_Phidq
except ImportError as error:
    comp_Phidq = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_Phidq_mag import comp_Phidq_mag
except ImportError as error:
    comp_Phidq_mag = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_torque_sync_rel import comp_torque_sync_rel
except ImportError as error:
    comp_torque_sync_rel = error

try:
    from ..Methods.Simulation.EEC_PMSM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC_PMSM.solve_PWM import solve_PWM
except ImportError as error:
    solve_PWM = error

try:
    from ..Methods.Simulation.EEC_PMSM.update_from_ref import update_from_ref
except ImportError as error:
    update_from_ref = error


from numpy import isnan
from ._check import InitUnKnowClassError


class EEC_PMSM(EEC):
    """Electrical Equivalent Circuit of Permanent Magnet Synchronous Machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_PMSM.clear_parameters
    if isinstance(clear_parameters, ImportError):
        clear_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method clear_parameters: "
                    + str(clear_parameters)
                )
            )
        )
    else:
        clear_parameters = clear_parameters
    # cf Methods.Simulation.EEC_PMSM.comp_BEMF_harmonics
    if isinstance(comp_BEMF_harmonics, ImportError):
        comp_BEMF_harmonics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_BEMF_harmonics: "
                    + str(comp_BEMF_harmonics)
                )
            )
        )
    else:
        comp_BEMF_harmonics = comp_BEMF_harmonics
    # cf Methods.Simulation.EEC_PMSM.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_joule_losses: "
                    + str(comp_joule_losses)
                )
            )
        )
    else:
        comp_joule_losses = comp_joule_losses
    # cf Methods.Simulation.EEC_PMSM.comp_Ld
    if isinstance(comp_Ld, ImportError):
        comp_Ld = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method comp_Ld: " + str(comp_Ld))
            )
        )
    else:
        comp_Ld = comp_Ld
    # cf Methods.Simulation.EEC_PMSM.comp_Lq
    if isinstance(comp_Lq, ImportError):
        comp_Lq = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method comp_Lq: " + str(comp_Lq))
            )
        )
    else:
        comp_Lq = comp_Lq
    # cf Methods.Simulation.EEC_PMSM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_parameters: " + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_PMSM.comp_Phidq
    if isinstance(comp_Phidq, ImportError):
        comp_Phidq = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method comp_Phidq: " + str(comp_Phidq))
            )
        )
    else:
        comp_Phidq = comp_Phidq
    # cf Methods.Simulation.EEC_PMSM.comp_Phidq_mag
    if isinstance(comp_Phidq_mag, ImportError):
        comp_Phidq_mag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_Phidq_mag: " + str(comp_Phidq_mag)
                )
            )
        )
    else:
        comp_Phidq_mag = comp_Phidq_mag
    # cf Methods.Simulation.EEC_PMSM.comp_torque_sync_rel
    if isinstance(comp_torque_sync_rel, ImportError):
        comp_torque_sync_rel = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_torque_sync_rel: "
                    + str(comp_torque_sync_rel)
                )
            )
        )
    else:
        comp_torque_sync_rel = comp_torque_sync_rel
    # cf Methods.Simulation.EEC_PMSM.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.EEC_PMSM.solve_PWM
    if isinstance(solve_PWM, ImportError):
        solve_PWM = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method solve_PWM: " + str(solve_PWM))
            )
        )
    else:
        solve_PWM = solve_PWM
    # cf Methods.Simulation.EEC_PMSM.update_from_ref
    if isinstance(update_from_ref, ImportError):
        update_from_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method update_from_ref: " + str(update_from_ref)
                )
            )
        )
    else:
        update_from_ref = update_from_ref
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Ld=None,
        Lq=None,
        Phid=None,
        Phiq=None,
        Phid_mag=None,
        Phiq_mag=None,
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
            if "Ld" in list(init_dict.keys()):
                Ld = init_dict["Ld"]
            if "Lq" in list(init_dict.keys()):
                Lq = init_dict["Lq"]
            if "Phid" in list(init_dict.keys()):
                Phid = init_dict["Phid"]
            if "Phiq" in list(init_dict.keys()):
                Phiq = init_dict["Phiq"]
            if "Phid_mag" in list(init_dict.keys()):
                Phid_mag = init_dict["Phid_mag"]
            if "Phiq_mag" in list(init_dict.keys()):
                Phiq_mag = init_dict["Phiq_mag"]
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
        self.Ld = Ld
        self.Lq = Lq
        self.Phid = Phid
        self.Phiq = Phiq
        self.Phid_mag = Phid_mag
        self.Phiq_mag = Phiq_mag
        # Call EEC init
        super(EEC_PMSM, self).__init__(
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

        EEC_PMSM_str = ""
        # Get the properties inherited from EEC
        EEC_PMSM_str += super(EEC_PMSM, self).__str__()
        EEC_PMSM_str += "Ld = " + str(self.Ld) + linesep
        EEC_PMSM_str += "Lq = " + str(self.Lq) + linesep
        EEC_PMSM_str += "Phid = " + str(self.Phid) + linesep
        EEC_PMSM_str += "Phiq = " + str(self.Phiq) + linesep
        EEC_PMSM_str += "Phid_mag = " + str(self.Phid_mag) + linesep
        EEC_PMSM_str += "Phiq_mag = " + str(self.Phiq_mag) + linesep
        return EEC_PMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_PMSM, self).__eq__(other):
            return False
        if other.Ld != self.Ld:
            return False
        if other.Lq != self.Lq:
            return False
        if other.Phid != self.Phid:
            return False
        if other.Phiq != self.Phiq:
            return False
        if other.Phid_mag != self.Phid_mag:
            return False
        if other.Phiq_mag != self.Phiq_mag:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EEC
        diff_list.extend(
            super(EEC_PMSM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Ld is not None
            and self._Ld is not None
            and isnan(other._Ld)
            and isnan(self._Ld)
        ):
            pass
        elif other._Ld != self._Ld:
            if is_add_value:
                val_str = " (self=" + str(self._Ld) + ", other=" + str(other._Ld) + ")"
                diff_list.append(name + ".Ld" + val_str)
            else:
                diff_list.append(name + ".Ld")
        if (
            other._Lq is not None
            and self._Lq is not None
            and isnan(other._Lq)
            and isnan(self._Lq)
        ):
            pass
        elif other._Lq != self._Lq:
            if is_add_value:
                val_str = " (self=" + str(self._Lq) + ", other=" + str(other._Lq) + ")"
                diff_list.append(name + ".Lq" + val_str)
            else:
                diff_list.append(name + ".Lq")
        if (
            other._Phid is not None
            and self._Phid is not None
            and isnan(other._Phid)
            and isnan(self._Phid)
        ):
            pass
        elif other._Phid != self._Phid:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Phid) + ", other=" + str(other._Phid) + ")"
                )
                diff_list.append(name + ".Phid" + val_str)
            else:
                diff_list.append(name + ".Phid")
        if (
            other._Phiq is not None
            and self._Phiq is not None
            and isnan(other._Phiq)
            and isnan(self._Phiq)
        ):
            pass
        elif other._Phiq != self._Phiq:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Phiq) + ", other=" + str(other._Phiq) + ")"
                )
                diff_list.append(name + ".Phiq" + val_str)
            else:
                diff_list.append(name + ".Phiq")
        if (
            other._Phid_mag is not None
            and self._Phid_mag is not None
            and isnan(other._Phid_mag)
            and isnan(self._Phid_mag)
        ):
            pass
        elif other._Phid_mag != self._Phid_mag:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Phid_mag)
                    + ", other="
                    + str(other._Phid_mag)
                    + ")"
                )
                diff_list.append(name + ".Phid_mag" + val_str)
            else:
                diff_list.append(name + ".Phid_mag")
        if (
            other._Phiq_mag is not None
            and self._Phiq_mag is not None
            and isnan(other._Phiq_mag)
            and isnan(self._Phiq_mag)
        ):
            pass
        elif other._Phiq_mag != self._Phiq_mag:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Phiq_mag)
                    + ", other="
                    + str(other._Phiq_mag)
                    + ")"
                )
                diff_list.append(name + ".Phiq_mag" + val_str)
            else:
                diff_list.append(name + ".Phiq_mag")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_PMSM, self).__sizeof__()
        S += getsizeof(self.Ld)
        S += getsizeof(self.Lq)
        S += getsizeof(self.Phid)
        S += getsizeof(self.Phiq)
        S += getsizeof(self.Phid_mag)
        S += getsizeof(self.Phiq_mag)
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
        EEC_PMSM_dict = super(EEC_PMSM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        EEC_PMSM_dict["Ld"] = self.Ld
        EEC_PMSM_dict["Lq"] = self.Lq
        EEC_PMSM_dict["Phid"] = self.Phid
        EEC_PMSM_dict["Phiq"] = self.Phiq
        EEC_PMSM_dict["Phid_mag"] = self.Phid_mag
        EEC_PMSM_dict["Phiq_mag"] = self.Phiq_mag
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_PMSM_dict["__class__"] = "EEC_PMSM"
        return EEC_PMSM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Ld_val = self.Ld
        Lq_val = self.Lq
        Phid_val = self.Phid
        Phiq_val = self.Phiq
        Phid_mag_val = self.Phid_mag
        Phiq_mag_val = self.Phiq_mag
        type_skin_effect_val = self.type_skin_effect
        if self.OP is None:
            OP_val = None
        else:
            OP_val = self.OP.copy()
        Tsta_val = self.Tsta
        Trot_val = self.Trot
        Xkr_skinS_val = self.Xkr_skinS
        Xke_skinS_val = self.Xke_skinS
        Xkr_skinR_val = self.Xkr_skinR
        Xke_skinR_val = self.Xke_skinR
        R1_val = self.R1
        if self.fluxlink is None:
            fluxlink_val = None
        else:
            fluxlink_val = self.fluxlink.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Ld=Ld_val,
            Lq=Lq_val,
            Phid=Phid_val,
            Phiq=Phiq_val,
            Phid_mag=Phid_mag_val,
            Phiq_mag=Phiq_mag_val,
            type_skin_effect=type_skin_effect_val,
            OP=OP_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            Xkr_skinS=Xkr_skinS_val,
            Xke_skinS=Xke_skinS_val,
            Xkr_skinR=Xkr_skinR_val,
            Xke_skinR=Xke_skinR_val,
            R1=R1_val,
            fluxlink=fluxlink_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Ld = None
        self.Lq = None
        self.Phid = None
        self.Phiq = None
        self.Phid_mag = None
        self.Phiq_mag = None
        # Set to None the properties inherited from EEC
        super(EEC_PMSM, self)._set_None()

    def _get_Ld(self):
        """getter of Ld"""
        return self._Ld

    def _set_Ld(self, value):
        """setter of Ld"""
        check_var("Ld", value, "float")
        self._Ld = value

    Ld = property(
        fget=_get_Ld,
        fset=_set_Ld,
        doc=u"""Stator winding inductance along d-axis

        :Type: float
        """,
    )

    def _get_Lq(self):
        """getter of Lq"""
        return self._Lq

    def _set_Lq(self, value):
        """setter of Lq"""
        check_var("Lq", value, "float")
        self._Lq = value

    Lq = property(
        fget=_get_Lq,
        fset=_set_Lq,
        doc=u"""Stator winding inductance along q-axis

        :Type: float
        """,
    )

    def _get_Phid(self):
        """getter of Phid"""
        return self._Phid

    def _set_Phid(self, value):
        """setter of Phid"""
        check_var("Phid", value, "float")
        self._Phid = value

    Phid = property(
        fget=_get_Phid,
        fset=_set_Phid,
        doc=u"""Stator winding flux along d-axis

        :Type: float
        """,
    )

    def _get_Phiq(self):
        """getter of Phiq"""
        return self._Phiq

    def _set_Phiq(self, value):
        """setter of Phiq"""
        check_var("Phiq", value, "float")
        self._Phiq = value

    Phiq = property(
        fget=_get_Phiq,
        fset=_set_Phiq,
        doc=u"""Stator winding flux along q-axis

        :Type: float
        """,
    )

    def _get_Phid_mag(self):
        """getter of Phid_mag"""
        return self._Phid_mag

    def _set_Phid_mag(self, value):
        """setter of Phid_mag"""
        check_var("Phid_mag", value, "float")
        self._Phid_mag = value

    Phid_mag = property(
        fget=_get_Phid_mag,
        fset=_set_Phid_mag,
        doc=u"""Stator winding flux along d-axis in open-circuit (rotor flux linkage)

        :Type: float
        """,
    )

    def _get_Phiq_mag(self):
        """getter of Phiq_mag"""
        return self._Phiq_mag

    def _set_Phiq_mag(self, value):
        """setter of Phiq_mag"""
        check_var("Phiq_mag", value, "float")
        self._Phiq_mag = value

    Phiq_mag = property(
        fget=_get_Phiq_mag,
        fset=_set_Phiq_mag,
        doc=u"""Stator winding flux along q-axis in open-circuit (rotor flux linkage)

        :Type: float
        """,
    )
