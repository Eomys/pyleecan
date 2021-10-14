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
    from ..Methods.Simulation.EEC_PMSM.solve_EEC import solve_EEC
except ImportError as error:
    solve_EEC = error

try:
    from ..Methods.Simulation.EEC_PMSM.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error

try:
    from ..Methods.Simulation.EEC_PMSM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError
from .IndMag import IndMag
from .FluxLink import FluxLink
from .Drive import Drive


class EEC_PMSM(EEC):
    """Electric module: Electrical Equivalent Circuit"""

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
    # cf Methods.Simulation.EEC_PMSM.solve_EEC
    if isinstance(solve_EEC, ImportError):
        solve_EEC = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method solve_EEC: " + str(solve_EEC))
            )
        )
    else:
        solve_EEC = solve_EEC
    # cf Methods.Simulation.EEC_PMSM.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
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
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        indmag=None,
        fluxlink=None,
        parameters=-1,
        freq0=None,
        drive=None,
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
            if "freq0" in list(init_dict.keys()):
                freq0 = init_dict["freq0"]
            if "drive" in list(init_dict.keys()):
                drive = init_dict["drive"]
        # Set the properties (value check and convertion are done in setter)
        self.indmag = indmag
        self.fluxlink = fluxlink
        self.parameters = parameters
        self.freq0 = freq0
        self.drive = drive
        # Call EEC init
        super(EEC_PMSM, self).__init__()
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
        EEC_PMSM_str += "parameters = " + str(self.parameters) + linesep
        EEC_PMSM_str += "freq0 = " + str(self.freq0) + linesep
        if self.drive is not None:
            tmp = self.drive.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "drive = " + tmp
        else:
            EEC_PMSM_str += "drive = None" + linesep + linesep
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
        if other.parameters != self.parameters:
            return False
        if other.freq0 != self.freq0:
            return False
        if other.drive != self.drive:
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
        if other._parameters != self._parameters:
            diff_list.append(name + ".parameters")
        if other._freq0 != self._freq0:
            diff_list.append(name + ".freq0")
        if (other.drive is None and self.drive is not None) or (
            other.drive is not None and self.drive is None
        ):
            diff_list.append(name + ".drive None mismatch")
        elif self.drive is not None:
            diff_list.extend(self.drive.compare(other.drive, name=name + ".drive"))
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
        if self.parameters is not None:
            for key, value in self.parameters.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.freq0)
        S += getsizeof(self.drive)
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
        EEC_PMSM_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        EEC_PMSM_dict["freq0"] = self.freq0
        if self.drive is None:
            EEC_PMSM_dict["drive"] = None
        else:
            EEC_PMSM_dict["drive"] = self.drive.as_dict(
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
        self.parameters = None
        self.freq0 = None
        if self.drive is not None:
            self.drive._set_None()
        # Set to None the properties inherited from EEC
        super(EEC_PMSM, self)._set_None()

    def _get_indmag(self):
        """getter of indmag"""
        return self._indmag

    def _set_indmag(self, value):
        """setter of indmag"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
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
            value = load_init_dict(value)[1]
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

    def _get_parameters(self):
        """getter of parameters"""
        return self._parameters

    def _set_parameters(self, value):
        """setter of parameters"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("parameters", value, "dict")
        self._parameters = value

    parameters = property(
        fget=_get_parameters,
        fset=_set_parameters,
        doc=u"""Parameters of the EEC: computed if empty, or enforced

        :Type: dict
        """,
    )

    def _get_freq0(self):
        """getter of freq0"""
        return self._freq0

    def _set_freq0(self, value):
        """setter of freq0"""
        check_var("freq0", value, "float")
        self._freq0 = value

    freq0 = property(
        fget=_get_freq0,
        fset=_set_freq0,
        doc=u"""Frequency

        :Type: float
        """,
    )

    def _get_drive(self):
        """getter of drive"""
        return self._drive

    def _set_drive(self, value):
        """setter of drive"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "drive"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Drive()
        check_var("drive", value, "Drive")
        self._drive = value

        if self._drive is not None:
            self._drive.parent = self

    drive = property(
        fget=_get_drive,
        fset=_set_drive,
        doc=u"""Drive

        :Type: Drive
        """,
    )
