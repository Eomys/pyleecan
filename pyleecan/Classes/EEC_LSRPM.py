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
    from ..Methods.Simulation.EEC_LSRPM.solve_EEC import solve_EEC
except ImportError as error:
    solve_EEC = error

try:
    from ..Methods.Simulation.EEC_LSRPM.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error

try:
    from ..Methods.Simulation.EEC_LSRPM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError
from .FluxLink import FluxLink


class EEC_LSRPM(EEC):
    """Electric module: Electrical Equivalent Circuit for Squirrel Cage Induction Machine"""

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
    # cf Methods.Simulation.EEC_LSRPM.solve_EEC
    if isinstance(solve_EEC, ImportError):
        solve_EEC = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_LSRPM method solve_EEC: " + str(solve_EEC))
            )
        )
    else:
        solve_EEC = solve_EEC
    # cf Methods.Simulation.EEC_LSRPM.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_LSRPM method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
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
        parameters=-1,
        N0=1500,
        felec=100,
        fluxlink=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
        # Set the properties (value check and convertion are done in setter)
        self.parameters = parameters
        self.N0 = N0
        self.felec = felec
        self.fluxlink = fluxlink
        # Call EEC init
        super(EEC_LSRPM, self).__init__()
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_LSRPM_str = ""
        # Get the properties inherited from EEC
        EEC_LSRPM_str += super(EEC_LSRPM, self).__str__()
        EEC_LSRPM_str += "parameters = " + str(self.parameters) + linesep
        EEC_LSRPM_str += "N0 = " + str(self.N0) + linesep
        EEC_LSRPM_str += "felec = " + str(self.felec) + linesep
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_LSRPM_str += "fluxlink = " + tmp
        else:
            EEC_LSRPM_str += "fluxlink = None" + linesep + linesep
        return EEC_LSRPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_LSRPM, self).__eq__(other):
            return False
        if other.parameters != self.parameters:
            return False
        if other.N0 != self.N0:
            return False
        if other.felec != self.felec:
            return False
        if other.fluxlink != self.fluxlink:
            return False
        return True

    def compare(self, other, name="self"):
        """Compare two objects and return list of differences"""

        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EEC
        diff_list.extend(super(EEC_LSRPM, self).compare(other, name=name))
        if other._parameters != self._parameters:
            diff_list.append(name + ".parameters")
        if other._N0 != self._N0:
            diff_list.append(name + ".N0")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if (other.fluxlink is None and self.fluxlink is not None) or (
            other.fluxlink is not None and self.fluxlink is None
        ):
            diff_list.append(name + ".fluxlink None mismatch")
        elif self.fluxlink is not None:
            diff_list.extend(
                self.fluxlink.compare(other.fluxlink, name=name + ".fluxlink")
            )
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_LSRPM, self).__sizeof__()
        if self.parameters is not None:
            for key, value in self.parameters.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.N0)
        S += getsizeof(self.felec)
        S += getsizeof(self.fluxlink)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from EEC
        EEC_LSRPM_dict = super(EEC_LSRPM, self).as_dict(**kwargs)
        EEC_LSRPM_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        EEC_LSRPM_dict["N0"] = self.N0
        EEC_LSRPM_dict["felec"] = self.felec
        if self.fluxlink is None:
            EEC_LSRPM_dict["fluxlink"] = None
        else:
            EEC_LSRPM_dict["fluxlink"] = self.fluxlink.as_dict(**kwargs)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_LSRPM_dict["__class__"] = "EEC_LSRPM"
        return EEC_LSRPM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.parameters = None
        self.N0 = None
        self.felec = None
        if self.fluxlink is not None:
            self.fluxlink._set_None()
        # Set to None the properties inherited from EEC
        super(EEC_LSRPM, self)._set_None()

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

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "int")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""frequency

        :Type: int
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
