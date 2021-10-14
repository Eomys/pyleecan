# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Force.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Force
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Force.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Force.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Simulation.Force.comp_AGSF_transfer import comp_AGSF_transfer
except ImportError as error:
    comp_AGSF_transfer = error


from ._check import InitUnKnowClassError


class Force(FrozenClass):
    """Forces module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Force.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Force method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Force.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Force method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Simulation.Force.comp_AGSF_transfer
    if isinstance(comp_AGSF_transfer, ImportError):
        comp_AGSF_transfer = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Force method comp_AGSF_transfer: "
                    + str(comp_AGSF_transfer)
                )
            )
        )
    else:
        comp_AGSF_transfer = comp_AGSF_transfer
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_periodicity_t=None,
        is_periodicity_a=None,
        is_agsf_transfer=False,
        max_wavenumber_transfer=None,
        Rsbo_enforced_transfer=None,
        logger_name="Pyleecan.Force",
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
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_agsf_transfer" in list(init_dict.keys()):
                is_agsf_transfer = init_dict["is_agsf_transfer"]
            if "max_wavenumber_transfer" in list(init_dict.keys()):
                max_wavenumber_transfer = init_dict["max_wavenumber_transfer"]
            if "Rsbo_enforced_transfer" in list(init_dict.keys()):
                Rsbo_enforced_transfer = init_dict["Rsbo_enforced_transfer"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a
        self.is_agsf_transfer = is_agsf_transfer
        self.max_wavenumber_transfer = max_wavenumber_transfer
        self.Rsbo_enforced_transfer = Rsbo_enforced_transfer
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Force_str = ""
        if self.parent is None:
            Force_str += "parent = None " + linesep
        else:
            Force_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Force_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        Force_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        Force_str += "is_agsf_transfer = " + str(self.is_agsf_transfer) + linesep
        Force_str += (
            "max_wavenumber_transfer = " + str(self.max_wavenumber_transfer) + linesep
        )
        Force_str += (
            "Rsbo_enforced_transfer = " + str(self.Rsbo_enforced_transfer) + linesep
        )
        Force_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return Force_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.is_agsf_transfer != self.is_agsf_transfer:
            return False
        if other.max_wavenumber_transfer != self.max_wavenumber_transfer:
            return False
        if other.Rsbo_enforced_transfer != self.Rsbo_enforced_transfer:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._is_periodicity_t != self._is_periodicity_t:
            diff_list.append(name + ".is_periodicity_t")
        if other._is_periodicity_a != self._is_periodicity_a:
            diff_list.append(name + ".is_periodicity_a")
        if other._is_agsf_transfer != self._is_agsf_transfer:
            diff_list.append(name + ".is_agsf_transfer")
        if other._max_wavenumber_transfer != self._max_wavenumber_transfer:
            diff_list.append(name + ".max_wavenumber_transfer")
        if other._Rsbo_enforced_transfer != self._Rsbo_enforced_transfer:
            diff_list.append(name + ".Rsbo_enforced_transfer")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.is_periodicity_t)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.is_agsf_transfer)
        S += getsizeof(self.max_wavenumber_transfer)
        S += getsizeof(self.Rsbo_enforced_transfer)
        S += getsizeof(self.logger_name)
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

        Force_dict = dict()
        Force_dict["is_periodicity_t"] = self.is_periodicity_t
        Force_dict["is_periodicity_a"] = self.is_periodicity_a
        Force_dict["is_agsf_transfer"] = self.is_agsf_transfer
        Force_dict["max_wavenumber_transfer"] = self.max_wavenumber_transfer
        Force_dict["Rsbo_enforced_transfer"] = self.Rsbo_enforced_transfer
        Force_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_periodicity_t = None
        self.is_periodicity_a = None
        self.is_agsf_transfer = None
        self.max_wavenumber_transfer = None
        self.Rsbo_enforced_transfer = None
        self.logger_name = None

    def _get_is_periodicity_t(self):
        """getter of is_periodicity_t"""
        return self._is_periodicity_t

    def _set_is_periodicity_t(self, value):
        """setter of is_periodicity_t"""
        check_var("is_periodicity_t", value, "bool")
        self._is_periodicity_t = value

    is_periodicity_t = property(
        fget=_get_is_periodicity_t,
        fset=_set_is_periodicity_t,
        doc=u"""True to compute only on one time periodicity (use periodicities defined in output.force.Time). If None, automatically calculated based on Magnetics periodicities.

        :Type: bool
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
        doc=u"""True to compute only on one angle periodicity (use periodicities defined in output.force.Angle). If None, automatically calculated based on Magnetics periodicities.

        :Type: bool
        """,
    )

    def _get_is_agsf_transfer(self):
        """getter of is_agsf_transfer"""
        return self._is_agsf_transfer

    def _set_is_agsf_transfer(self, value):
        """setter of is_agsf_transfer"""
        check_var("is_agsf_transfer", value, "bool")
        self._is_agsf_transfer = value

    is_agsf_transfer = property(
        fget=_get_is_agsf_transfer,
        fset=_set_is_agsf_transfer,
        doc=u"""True to compute the AGSF transfer from air-gap to stator bore radius.

        :Type: bool
        """,
    )

    def _get_max_wavenumber_transfer(self):
        """getter of max_wavenumber_transfer"""
        return self._max_wavenumber_transfer

    def _set_max_wavenumber_transfer(self, value):
        """setter of max_wavenumber_transfer"""
        check_var("max_wavenumber_transfer", value, "int")
        self._max_wavenumber_transfer = value

    max_wavenumber_transfer = property(
        fget=_get_max_wavenumber_transfer,
        fset=_set_max_wavenumber_transfer,
        doc=u"""Maximum value to apply agsf transfer (to be used with FEA to avoid numerical noise amplification)

        :Type: int
        """,
    )

    def _get_Rsbo_enforced_transfer(self):
        """getter of Rsbo_enforced_transfer"""
        return self._Rsbo_enforced_transfer

    def _set_Rsbo_enforced_transfer(self, value):
        """setter of Rsbo_enforced_transfer"""
        check_var("Rsbo_enforced_transfer", value, "float")
        self._Rsbo_enforced_transfer = value

    Rsbo_enforced_transfer = property(
        fget=_get_Rsbo_enforced_transfer,
        fset=_set_Rsbo_enforced_transfer,
        doc=u"""To enforce the value of the radius for AGSF transfer

        :Type: float
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )
