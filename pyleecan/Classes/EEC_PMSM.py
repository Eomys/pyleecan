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
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_PMSM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_PMSM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC_PMSM.solve_PWM import solve_PWM
except ImportError as error:
    solve_PWM = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_torque_sync_rel import comp_torque_sync_rel
except ImportError as error:
    comp_torque_sync_rel = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_BEMF_harmonics import comp_BEMF_harmonics
except ImportError as error:
    comp_BEMF_harmonics = error


from ._check import InitUnKnowClassError
from .IndMag import IndMag
from .FluxLink import FluxLink
from .LUT import LUT
from .Drive import Drive


class EEC_PMSM(EEC):
    """Electrical Equivalent Circuit of Permanent Magnet Synchronous Machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
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
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        indmag=None,
        fluxlink=None,
        parameters=None,
        LUT_enforced=None,
        drive=None,
        type_skin_effect=1,
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
            if "indmag" in list(init_dict.keys()):
                indmag = init_dict["indmag"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "LUT_enforced" in list(init_dict.keys()):
                LUT_enforced = init_dict["LUT_enforced"]
            if "drive" in list(init_dict.keys()):
                drive = init_dict["drive"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
        # Set the properties (value check and convertion are done in setter)
        self.indmag = indmag
        self.fluxlink = fluxlink
        # Call EEC init
        super(EEC_PMSM, self).__init__(
            parameters=parameters,
            LUT_enforced=LUT_enforced,
            drive=drive,
            type_skin_effect=type_skin_effect,
        )
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_PMSM_str = ""
        # Get the properties inherited from EEC
        EEC_PMSM_str += super(EEC_PMSM, self).__str__()
        if self.indmag is not None:
            tmp = self.indmag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "indmag = " + tmp
        else:
            EEC_PMSM_str += "indmag = None" + linesep + linesep
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "fluxlink = " + tmp
        else:
            EEC_PMSM_str += "fluxlink = None" + linesep + linesep
        return EEC_PMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_PMSM, self).__eq__(other):
            return False
        if other.indmag != self.indmag:
            return False
        if other.fluxlink != self.fluxlink:
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
        diff_list.extend(super(EEC_PMSM, self).compare(other, name=name))
        if (other.indmag is None and self.indmag is not None) or (
            other.indmag is not None and self.indmag is None
        ):
            diff_list.append(name + ".indmag None mismatch")
        elif self.indmag is not None:
            diff_list.extend(self.indmag.compare(other.indmag, name=name + ".indmag"))
        if (other.fluxlink is None and self.fluxlink is not None) or (
            other.fluxlink is not None and self.fluxlink is None
        ):
            diff_list.append(name + ".fluxlink None mismatch")
        elif self.fluxlink is not None:
            diff_list.extend(
                self.fluxlink.compare(other.fluxlink, name=name + ".fluxlink")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_PMSM, self).__sizeof__()
        S += getsizeof(self.indmag)
        S += getsizeof(self.fluxlink)
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
        if self.indmag is None:
            EEC_PMSM_dict["indmag"] = None
        else:
            EEC_PMSM_dict["indmag"] = self.indmag.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.fluxlink is None:
            EEC_PMSM_dict["fluxlink"] = None
        else:
            EEC_PMSM_dict["fluxlink"] = self.fluxlink.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_PMSM_dict["__class__"] = "EEC_PMSM"
        return EEC_PMSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.indmag is not None:
            self.indmag._set_None()
        if self.fluxlink is not None:
            self.fluxlink._set_None()
        # Set to None the properties inherited from EEC
        super(EEC_PMSM, self)._set_None()

    def _get_indmag(self):
        """getter of indmag"""
        return self._indmag

    def _set_indmag(self, value):
        """setter of indmag"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "indmag"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = IndMag()
        check_var("indmag", value, "IndMag")
        self._indmag = value

        if self._indmag is not None:
            self._indmag.parent = self

    indmag = property(
        fget=_get_indmag,
        fset=_set_indmag,
        doc=u"""Magnetic inductance

        :Type: IndMag
        """,
    )

    def _get_fluxlink(self):
        """getter of fluxlink"""
        return self._fluxlink

    def _set_fluxlink(self, value):
        """setter of fluxlink"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "fluxlink"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = FluxLink()
        check_var("fluxlink", value, "FluxLink")
        self._fluxlink = value

        if self._fluxlink is not None:
            self._fluxlink.parent = self

    fluxlink = property(
        fget=_get_fluxlink,
        fset=_set_fluxlink,
        doc=u"""Flux Linkage

        :Type: FluxLink
        """,
    )
