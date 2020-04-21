# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/LamSquirrelCage.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .LamSlotWind import LamSlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSquirrelCage.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSquirrelCage.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSquirrelCage.comp_length_ring import comp_length_ring
except ImportError as error:
    comp_length_ring = error

try:
    from ..Methods.Machine.LamSquirrelCage.plot import plot
except ImportError as error:
    plot = error


from ._check import InitUnKnowClassError
from .Material import Material
from .Winding import Winding
from .Slot import Slot
from .Hole import Hole
from .Notch import Notch


class LamSquirrelCage(LamSlotWind):
    """squirrel cages lamination"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSquirrelCage.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSquirrelCage.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCage method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSquirrelCage.comp_length_ring
    if isinstance(comp_length_ring, ImportError):
        comp_length_ring = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSquirrelCage method comp_length_ring: "
                    + str(comp_length_ring)
                )
            )
        )
    else:
        comp_length_ring = comp_length_ring
    # cf Methods.Machine.LamSquirrelCage.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSquirrelCage method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Hscr=0.03,
        Lscr=0.015,
        ring_mat=-1,
        Ksfill=None,
        winding=-1,
        slot=-1,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=list(),
        notch=list(),
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if ring_mat == -1:
            ring_mat = Material()
        if winding == -1:
            winding = Winding()
        if slot == -1:
            slot = Slot()
        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Hscr" in list(init_dict.keys()):
                Hscr = init_dict["Hscr"]
            if "Lscr" in list(init_dict.keys()):
                Lscr = init_dict["Lscr"]
            if "ring_mat" in list(init_dict.keys()):
                ring_mat = init_dict["ring_mat"]
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "slot" in list(init_dict.keys()):
                slot = init_dict["slot"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
        # Initialisation by argument
        self.Hscr = Hscr
        self.Lscr = Lscr
        # ring_mat can be None, a Material object or a dict
        if isinstance(ring_mat, dict):
            self.ring_mat = Material(init_dict=ring_mat)
        else:
            self.ring_mat = ring_mat
        # Call LamSlotWind init
        super(LamSquirrelCage, self).__init__(
            Ksfill=Ksfill,
            winding=winding,
            slot=slot,
            L1=L1,
            mat_type=mat_type,
            Nrvd=Nrvd,
            Wrvd=Wrvd,
            Kf1=Kf1,
            is_internal=is_internal,
            Rint=Rint,
            Rext=Rext,
            is_stator=is_stator,
            axial_vent=axial_vent,
            notch=notch,
        )
        # The class is frozen (in LamSlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamSquirrelCage_str = ""
        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_str += super(LamSquirrelCage, self).__str__()
        LamSquirrelCage_str += "Hscr = " + str(self.Hscr) + linesep
        LamSquirrelCage_str += "Lscr = " + str(self.Lscr) + linesep
        if self.ring_mat is not None:
            tmp = self.ring_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSquirrelCage_str += "ring_mat = " + tmp
        else:
            LamSquirrelCage_str += "ring_mat = None" + linesep + linesep
        return LamSquirrelCage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotWind
        if not super(LamSquirrelCage, self).__eq__(other):
            return False
        if other.Hscr != self.Hscr:
            return False
        if other.Lscr != self.Lscr:
            return False
        if other.ring_mat != self.ring_mat:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from LamSlotWind
        LamSquirrelCage_dict = super(LamSquirrelCage, self).as_dict()
        LamSquirrelCage_dict["Hscr"] = self.Hscr
        LamSquirrelCage_dict["Lscr"] = self.Lscr
        if self.ring_mat is None:
            LamSquirrelCage_dict["ring_mat"] = None
        else:
            LamSquirrelCage_dict["ring_mat"] = self.ring_mat.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSquirrelCage_dict["__class__"] = "LamSquirrelCage"
        return LamSquirrelCage_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hscr = None
        self.Lscr = None
        if self.ring_mat is not None:
            self.ring_mat._set_None()
        # Set to None the properties inherited from LamSlotWind
        super(LamSquirrelCage, self)._set_None()

    def _get_Hscr(self):
        """getter of Hscr"""
        return self._Hscr

    def _set_Hscr(self, value):
        """setter of Hscr"""
        check_var("Hscr", value, "float", Vmin=0)
        self._Hscr = value

    # short circuit ring section radial height [m]
    # Type : float, min = 0
    Hscr = property(
        fget=_get_Hscr,
        fset=_set_Hscr,
        doc=u"""short circuit ring section radial height [m]""",
    )

    def _get_Lscr(self):
        """getter of Lscr"""
        return self._Lscr

    def _set_Lscr(self, value):
        """setter of Lscr"""
        check_var("Lscr", value, "float", Vmin=0)
        self._Lscr = value

    # short circuit ring section axial length
    # Type : float, min = 0
    Lscr = property(
        fget=_get_Lscr,
        fset=_set_Lscr,
        doc=u"""short circuit ring section axial length""",
    )

    def _get_ring_mat(self):
        """getter of ring_mat"""
        return self._ring_mat

    def _set_ring_mat(self, value):
        """setter of ring_mat"""
        check_var("ring_mat", value, "Material")
        self._ring_mat = value

        if self._ring_mat is not None:
            self._ring_mat.parent = self

    # Material of the Rotor short circuit ring
    # Type : Material
    ring_mat = property(
        fget=_get_ring_mat,
        fset=_set_ring_mat,
        doc=u"""Material of the Rotor short circuit ring""",
    )
