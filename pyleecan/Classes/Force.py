# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Force.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Force
"""

from os import linesep
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
        is_periodicity_t=False,
        is_periodicity_a=False,
        is_agsf_transfer=False,
        max_wavenumber_transfer=None,
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
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_agsf_transfer" in list(init_dict.keys()):
                is_agsf_transfer = init_dict["is_agsf_transfer"]
            if "max_wavenumber_transfer" in list(init_dict.keys()):
                max_wavenumber_transfer = init_dict["max_wavenumber_transfer"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a
        self.is_agsf_transfer = is_agsf_transfer
        self.max_wavenumber_transfer = max_wavenumber_transfer

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
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Force_dict = dict()
        Force_dict["is_periodicity_t"] = self.is_periodicity_t
        Force_dict["is_periodicity_a"] = self.is_periodicity_a
        Force_dict["is_agsf_transfer"] = self.is_agsf_transfer
        Force_dict["max_wavenumber_transfer"] = self.max_wavenumber_transfer
        # The class name is added to the dict for deserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_periodicity_t = None
        self.is_periodicity_a = None
        self.is_agsf_transfer = None
        self.max_wavenumber_transfer = None

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
        doc=u"""True to compute only on one time periodicity (use periodicities defined in output.force.Time)

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
        doc=u"""True to compute only on one angle periodicity (use periodicities defined in output.force.Angle)

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
