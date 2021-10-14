# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_SCIM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_SCIM
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
    from ..Methods.Simulation.EEC_SCIM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_SCIM.solve_EEC import solve_EEC
except ImportError as error:
    solve_EEC = error

try:
    from ..Methods.Simulation.EEC_SCIM.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError


class EEC_SCIM(EEC):
    """Electric module: Electrical Equivalent Circuit for Squirrel Cage Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
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
    # cf Methods.Simulation.EEC_SCIM.solve_EEC
    if isinstance(solve_EEC, ImportError):
        solve_EEC = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method solve_EEC: " + str(solve_EEC))
            )
        )
    else:
        solve_EEC = solve_EEC
    # cf Methods.Simulation.EEC_SCIM.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
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
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        I=1,
        parameters=-1,
        is_periodicity_a=True,
        nb_worker=None,
        N0=None,
        felec=None,
        Nt_tot=32,
        Nrev=1,
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
            if "I" in list(init_dict.keys()):
                I = init_dict["I"]
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "nb_worker" in list(init_dict.keys()):
                nb_worker = init_dict["nb_worker"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
        # Set the properties (value check and convertion are done in setter)
        self.I = I
        self.parameters = parameters
        self.is_periodicity_a = is_periodicity_a
        self.nb_worker = nb_worker
        self.N0 = N0
        self.felec = felec
        self.Nt_tot = Nt_tot
        self.Nrev = Nrev
        # Call EEC init
        super(EEC_SCIM, self).__init__()
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_SCIM_str = ""
        # Get the properties inherited from EEC
        EEC_SCIM_str += super(EEC_SCIM, self).__str__()
        EEC_SCIM_str += "I = " + str(self.I) + linesep
        EEC_SCIM_str += "parameters = " + str(self.parameters) + linesep
        EEC_SCIM_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        EEC_SCIM_str += "nb_worker = " + str(self.nb_worker) + linesep
        EEC_SCIM_str += "N0 = " + str(self.N0) + linesep
        EEC_SCIM_str += "felec = " + str(self.felec) + linesep
        EEC_SCIM_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        EEC_SCIM_str += "Nrev = " + str(self.Nrev) + linesep
        return EEC_SCIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_SCIM, self).__eq__(other):
            return False
        if other.I != self.I:
            return False
        if other.parameters != self.parameters:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.nb_worker != self.nb_worker:
            return False
        if other.N0 != self.N0:
            return False
        if other.felec != self.felec:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Nrev != self.Nrev:
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
        if other._I != self._I:
            diff_list.append(name + ".I")
        if other._parameters != self._parameters:
            diff_list.append(name + ".parameters")
        if other._is_periodicity_a != self._is_periodicity_a:
            diff_list.append(name + ".is_periodicity_a")
        if other._nb_worker != self._nb_worker:
            diff_list.append(name + ".nb_worker")
        if other._N0 != self._N0:
            diff_list.append(name + ".N0")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if other._Nt_tot != self._Nt_tot:
            diff_list.append(name + ".Nt_tot")
        if other._Nrev != self._Nrev:
            diff_list.append(name + ".Nrev")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_SCIM, self).__sizeof__()
        S += getsizeof(self.I)
        if self.parameters is not None:
            for key, value in self.parameters.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.nb_worker)
        S += getsizeof(self.N0)
        S += getsizeof(self.felec)
        S += getsizeof(self.Nt_tot)
        S += getsizeof(self.Nrev)
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
        EEC_SCIM_dict["I"] = self.I
        EEC_SCIM_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        EEC_SCIM_dict["is_periodicity_a"] = self.is_periodicity_a
        EEC_SCIM_dict["nb_worker"] = self.nb_worker
        EEC_SCIM_dict["N0"] = self.N0
        EEC_SCIM_dict["felec"] = self.felec
        EEC_SCIM_dict["Nt_tot"] = self.Nt_tot
        EEC_SCIM_dict["Nrev"] = self.Nrev
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_SCIM_dict["__class__"] = "EEC_SCIM"
        return EEC_SCIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.I = None
        self.parameters = None
        self.is_periodicity_a = None
        self.nb_worker = None
        self.N0 = None
        self.felec = None
        self.Nt_tot = None
        self.Nrev = None
        # Set to None the properties inherited from EEC
        super(EEC_SCIM, self)._set_None()

    def _get_I(self):
        """getter of I"""
        return self._I

    def _set_I(self, value):
        """setter of I"""
        check_var("I", value, "float")
        self._I = value

    I = property(
        fget=_get_I,
        fset=_set_I,
        doc=u"""RMS current for parameter estimation

        :Type: float
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
        doc=u"""True to compute only on one angle periodicity (use periodicities defined in output.mag.Angle)

        :Type: bool
        """,
    )

    def _get_nb_worker(self):
        """getter of nb_worker"""
        return self._nb_worker

    def _set_nb_worker(self, value):
        """setter of nb_worker"""
        check_var("nb_worker", value, "int")
        self._nb_worker = value

    nb_worker = property(
        fget=_get_nb_worker,
        fset=_set_nb_worker,
        doc=u"""To run FEMM in parallel (the parallelization is on the time loop)

        :Type: int
        """,
    )

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "float")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: float
        """,
    )

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "float")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""electrical frequency

        :Type: float
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int", Vmin=1)
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Time discretization

        :Type: int
        :min: 1
        """,
    )

    def _get_Nrev(self):
        """getter of Nrev"""
        return self._Nrev

    def _set_Nrev(self, value):
        """setter of Nrev"""
        check_var("Nrev", value, "float", Vmin=0)
        self._Nrev = value

    Nrev = property(
        fget=_get_Nrev,
        fset=_set_Nrev,
        doc=u"""Number of rotor revolution (to compute the final time)

        :Type: float
        :min: 0
        """,
    )
