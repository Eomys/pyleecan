# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_LSRPM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_LSRPM
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
    from ..Methods.Simulation.EEC_LSRPM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_LSRPM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC_LSRPM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError
from .FluxLink import FluxLink
from .OP import OP


class EEC_LSRPM(EEC):
    """Electrical Equivalent Circuit for LSRPM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_LSRPM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_LSRPM method comp_parameters: "
                    + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_LSRPM.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_LSRPM method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.EEC_LSRPM.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_LSRPM method comp_joule_losses: "
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
        fluxlink=None,
        N0=1500,
        type_skin_effect=1,
        OP=None,
        Tsta=20,
        Trot=20,
        Xkr_skinS=1,
        Xke_skinS=1,
        Xkr_skinR=1,
        Xke_skinR=1,
        R1=None,
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
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
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
        # Set the properties (value check and convertion are done in setter)
        self.fluxlink = fluxlink
        self.N0 = N0
        # Call EEC init
        super(EEC_LSRPM, self).__init__(
            type_skin_effect=type_skin_effect,
            OP=OP,
            Tsta=Tsta,
            Trot=Trot,
            Xkr_skinS=Xkr_skinS,
            Xke_skinS=Xke_skinS,
            Xkr_skinR=Xkr_skinR,
            Xke_skinR=Xke_skinR,
            R1=R1,
        )
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_LSRPM_str = ""
        # Get the properties inherited from EEC
        EEC_LSRPM_str += super(EEC_LSRPM, self).__str__()
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_LSRPM_str += "fluxlink = " + tmp
        else:
            EEC_LSRPM_str += "fluxlink = None" + linesep + linesep
        EEC_LSRPM_str += "N0 = " + str(self.N0) + linesep
        return EEC_LSRPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_LSRPM, self).__eq__(other):
            return False
        if other.fluxlink != self.fluxlink:
            return False
        if other.N0 != self.N0:
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
        diff_list.extend(super(EEC_LSRPM, self).compare(other, name=name))
        if (other.fluxlink is None and self.fluxlink is not None) or (
            other.fluxlink is not None and self.fluxlink is None
        ):
            diff_list.append(name + ".fluxlink None mismatch")
        elif self.fluxlink is not None:
            diff_list.extend(
                self.fluxlink.compare(other.fluxlink, name=name + ".fluxlink")
            )
        if other._N0 != self._N0:
            diff_list.append(name + ".N0")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_LSRPM, self).__sizeof__()
        S += getsizeof(self.fluxlink)
        S += getsizeof(self.N0)
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
        EEC_LSRPM_dict = super(EEC_LSRPM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.fluxlink is None:
            EEC_LSRPM_dict["fluxlink"] = None
        else:
            EEC_LSRPM_dict["fluxlink"] = self.fluxlink.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        EEC_LSRPM_dict["N0"] = self.N0
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_LSRPM_dict["__class__"] = "EEC_LSRPM"
        return EEC_LSRPM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.fluxlink is not None:
            self.fluxlink._set_None()
        self.N0 = None
        # Set to None the properties inherited from EEC
        super(EEC_LSRPM, self)._set_None()

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

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "int")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotation speed

        :Type: int
        """,
    )
