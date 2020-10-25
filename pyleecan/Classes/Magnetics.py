# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Magnetics.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Magnetics
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
    from ..Methods.Simulation.Magnetics.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Magnetics.comp_time_angle import comp_time_angle
except ImportError as error:
    comp_time_angle = error

try:
    from ..Methods.Simulation.Magnetics.comp_emf import comp_emf
except ImportError as error:
    comp_emf = error


from ._check import InitUnKnowClassError


class Magnetics(FrozenClass):
    """Magnetic module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Magnetics.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Magnetics method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Magnetics.comp_time_angle
    if isinstance(comp_time_angle, ImportError):
        comp_time_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Magnetics method comp_time_angle: "
                    + str(comp_time_angle)
                )
            )
        )
    else:
        comp_time_angle = comp_time_angle
    # cf Methods.Simulation.Magnetics.comp_emf
    if isinstance(comp_emf, ImportError):
        comp_emf = property(
            fget=lambda x: raise_(
                ImportError("Can't use Magnetics method comp_emf: " + str(comp_emf))
            )
        )
    else:
        comp_emf = comp_emf
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_vent=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
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
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_vent" in list(init_dict.keys()):
                is_remove_vent = init_dict["is_remove_vent"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_remove_slotS = is_remove_slotS
        self.is_remove_slotR = is_remove_slotR
        self.is_remove_vent = is_remove_vent
        self.is_mmfs = is_mmfs
        self.is_mmfr = is_mmfr
        self.type_BH_stator = type_BH_stator
        self.type_BH_rotor = type_BH_rotor
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Magnetics_str = ""
        if self.parent is None:
            Magnetics_str += "parent = None " + linesep
        else:
            Magnetics_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Magnetics_str += "is_remove_slotS = " + str(self.is_remove_slotS) + linesep
        Magnetics_str += "is_remove_slotR = " + str(self.is_remove_slotR) + linesep
        Magnetics_str += "is_remove_vent = " + str(self.is_remove_vent) + linesep
        Magnetics_str += "is_mmfs = " + str(self.is_mmfs) + linesep
        Magnetics_str += "is_mmfr = " + str(self.is_mmfr) + linesep
        Magnetics_str += "type_BH_stator = " + str(self.type_BH_stator) + linesep
        Magnetics_str += "type_BH_rotor = " + str(self.type_BH_rotor) + linesep
        Magnetics_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        Magnetics_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        return Magnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_remove_slotS != self.is_remove_slotS:
            return False
        if other.is_remove_slotR != self.is_remove_slotR:
            return False
        if other.is_remove_vent != self.is_remove_vent:
            return False
        if other.is_mmfs != self.is_mmfs:
            return False
        if other.is_mmfr != self.is_mmfr:
            return False
        if other.type_BH_stator != self.type_BH_stator:
            return False
        if other.type_BH_rotor != self.type_BH_rotor:
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Magnetics_dict = dict()
        Magnetics_dict["is_remove_slotS"] = self.is_remove_slotS
        Magnetics_dict["is_remove_slotR"] = self.is_remove_slotR
        Magnetics_dict["is_remove_vent"] = self.is_remove_vent
        Magnetics_dict["is_mmfs"] = self.is_mmfs
        Magnetics_dict["is_mmfr"] = self.is_mmfr
        Magnetics_dict["type_BH_stator"] = self.type_BH_stator
        Magnetics_dict["type_BH_rotor"] = self.type_BH_rotor
        Magnetics_dict["is_periodicity_t"] = self.is_periodicity_t
        Magnetics_dict["is_periodicity_a"] = self.is_periodicity_a
        # The class name is added to the dict for deserialisation purpose
        Magnetics_dict["__class__"] = "Magnetics"
        return Magnetics_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_remove_slotS = None
        self.is_remove_slotR = None
        self.is_remove_vent = None
        self.is_mmfs = None
        self.is_mmfr = None
        self.type_BH_stator = None
        self.type_BH_rotor = None
        self.is_periodicity_t = None
        self.is_periodicity_a = None

    def _get_is_remove_slotS(self):
        """getter of is_remove_slotS"""
        return self._is_remove_slotS

    def _set_is_remove_slotS(self, value):
        """setter of is_remove_slotS"""
        check_var("is_remove_slotS", value, "bool")
        self._is_remove_slotS = value

    is_remove_slotS = property(
        fget=_get_is_remove_slotS,
        fset=_set_is_remove_slotS,
        doc=u"""1 to artificially remove stator slotting effects in permeance mmf calculations

        :Type: bool
        """,
    )

    def _get_is_remove_slotR(self):
        """getter of is_remove_slotR"""
        return self._is_remove_slotR

    def _set_is_remove_slotR(self, value):
        """setter of is_remove_slotR"""
        check_var("is_remove_slotR", value, "bool")
        self._is_remove_slotR = value

    is_remove_slotR = property(
        fget=_get_is_remove_slotR,
        fset=_set_is_remove_slotR,
        doc=u"""1 to artificially remove rotor slotting effects in permeance mmf calculations

        :Type: bool
        """,
    )

    def _get_is_remove_vent(self):
        """getter of is_remove_vent"""
        return self._is_remove_vent

    def _set_is_remove_vent(self, value):
        """setter of is_remove_vent"""
        check_var("is_remove_vent", value, "bool")
        self._is_remove_vent = value

    is_remove_vent = property(
        fget=_get_is_remove_vent,
        fset=_set_is_remove_vent,
        doc=u"""1 to artificially remove the ventilations duct

        :Type: bool
        """,
    )

    def _get_is_mmfs(self):
        """getter of is_mmfs"""
        return self._is_mmfs

    def _set_is_mmfs(self, value):
        """setter of is_mmfs"""
        check_var("is_mmfs", value, "bool")
        self._is_mmfs = value

    is_mmfs = property(
        fget=_get_is_mmfs,
        fset=_set_is_mmfs,
        doc=u"""1 to compute the stator magnetomotive force / stator armature magnetic field

        :Type: bool
        """,
    )

    def _get_is_mmfr(self):
        """getter of is_mmfr"""
        return self._is_mmfr

    def _set_is_mmfr(self, value):
        """setter of is_mmfr"""
        check_var("is_mmfr", value, "bool")
        self._is_mmfr = value

    is_mmfr = property(
        fget=_get_is_mmfr,
        fset=_set_is_mmfr,
        doc=u"""1 to compute the rotor magnetomotive force / rotor magnetic field

        :Type: bool
        """,
    )

    def _get_type_BH_stator(self):
        """getter of type_BH_stator"""
        return self._type_BH_stator

    def _set_type_BH_stator(self, value):
        """setter of type_BH_stator"""
        check_var("type_BH_stator", value, "int", Vmin=0, Vmax=2)
        self._type_BH_stator = value

    type_BH_stator = property(
        fget=_get_type_BH_stator,
        fset=_set_type_BH_stator,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)

        :Type: int
        :min: 0
        :max: 2
        """,
    )

    def _get_type_BH_rotor(self):
        """getter of type_BH_rotor"""
        return self._type_BH_rotor

    def _set_type_BH_rotor(self, value):
        """setter of type_BH_rotor"""
        check_var("type_BH_rotor", value, "int", Vmin=0, Vmax=2)
        self._type_BH_rotor = value

    type_BH_rotor = property(
        fget=_get_type_BH_rotor,
        fset=_set_type_BH_rotor,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)

        :Type: int
        :min: 0
        :max: 2
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
        doc=u"""True to compute only on one time periodicity (use periodicities defined in output.mag.Time)

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
        doc=u"""True to compute only on one angle periodicity (use periodicities defined in output.mag.Angle)

        :Type: bool
        """,
    )
