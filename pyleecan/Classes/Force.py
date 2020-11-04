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
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_comp_nodal_force=False,
        is_periodicity_t=False,
        is_periodicity_a=False,
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
            if "is_comp_nodal_force" in list(init_dict.keys()):
                is_comp_nodal_force = init_dict["is_comp_nodal_force"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_comp_nodal_force = is_comp_nodal_force
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Force_str = ""
        if self.parent is None:
            Force_str += "parent = None " + linesep
        else:
            Force_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Force_str += "is_comp_nodal_force = " + str(self.is_comp_nodal_force) + linesep
        Force_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        Force_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        return Force_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_comp_nodal_force != self.is_comp_nodal_force:
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Force_dict = dict()
        Force_dict["is_comp_nodal_force"] = self.is_comp_nodal_force
        Force_dict["is_periodicity_t"] = self.is_periodicity_t
        Force_dict["is_periodicity_a"] = self.is_periodicity_a
        # The class name is added to the dict for deserialisation purpose
        Force_dict["__class__"] = "Force"
        return Force_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_comp_nodal_force = None
        self.is_periodicity_t = None
        self.is_periodicity_a = None

    def _get_is_comp_nodal_force(self):
        """getter of is_comp_nodal_force"""
        return self._is_comp_nodal_force

    def _set_is_comp_nodal_force(self, value):
        """setter of is_comp_nodal_force"""
        check_var("is_comp_nodal_force", value, "bool")
        self._is_comp_nodal_force = value

    is_comp_nodal_force = property(
        fget=_get_is_comp_nodal_force,
        fset=_set_is_comp_nodal_force,
        doc=u"""1 to compute lumped tooth forces

        :Type: bool
        """,
    )

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
