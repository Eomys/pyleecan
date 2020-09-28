# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlot
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Lamination import Lamination

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlot.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlot.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlot.comp_radius_mec import comp_radius_mec
except ImportError as error:
    comp_radius_mec = error

try:
    from ..Methods.Machine.LamSlot.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlot.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamSlot.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlot.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.LamSlot.get_Zs import get_Zs
except ImportError as error:
    get_Zs = error

try:
    from ..Methods.Machine.LamSlot.get_bore_desc import get_bore_desc
except ImportError as error:
    get_bore_desc = error

try:
    from ..Methods.Machine.LamSlot.comp_radius_mid_yoke import comp_radius_mid_yoke
except ImportError as error:
    comp_radius_mid_yoke = error

try:
    from ..Methods.Machine.LamSlot.comp_sym import comp_sym
except ImportError as error:
    comp_sym = error


from ._check import InitUnKnowClassError
from .Slot import Slot
from .Material import Material
from .Hole import Hole
from .Notch import Notch


class LamSlot(Lamination):
    """Lamination with empty Slot"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlot.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlot.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlot method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlot.comp_radius_mec
    if isinstance(comp_radius_mec, ImportError):
        comp_radius_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method comp_radius_mec: " + str(comp_radius_mec)
                )
            )
        )
    else:
        comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlot.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlot.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlot.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlot method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlot.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method comp_height_yoke: "
                    + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamSlot.get_Zs
    if isinstance(get_Zs, ImportError):
        get_Zs = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlot method get_Zs: " + str(get_Zs))
            )
        )
    else:
        get_Zs = get_Zs
    # cf Methods.Machine.LamSlot.get_bore_desc
    if isinstance(get_bore_desc, ImportError):
        get_bore_desc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method get_bore_desc: " + str(get_bore_desc)
                )
            )
        )
    else:
        get_bore_desc = get_bore_desc
    # cf Methods.Machine.LamSlot.comp_radius_mid_yoke
    if isinstance(comp_radius_mid_yoke, ImportError):
        comp_radius_mid_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlot method comp_radius_mid_yoke: "
                    + str(comp_radius_mid_yoke)
                )
            )
        )
    else:
        comp_radius_mid_yoke = comp_radius_mid_yoke
    # cf Methods.Machine.LamSlot.comp_sym
    if isinstance(comp_sym, ImportError):
        comp_sym = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlot method comp_sym: " + str(comp_sym))
            )
        )
    else:
        comp_sym = comp_sym
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        axial_vent=-1,
        notch=-1,
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
        # Set the properties (value check and convertion are done in setter)
        self.slot = slot
        # Call Lamination init
        super(LamSlot, self).__init__(
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
        # The class is frozen (in Lamination init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSlot_str = ""
        # Get the properties inherited from Lamination
        LamSlot_str += super(LamSlot, self).__str__()
        if self.slot is not None:
            tmp = self.slot.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSlot_str += "slot = " + tmp
        else:
            LamSlot_str += "slot = None" + linesep + linesep
        return LamSlot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Lamination
        if not super(LamSlot, self).__eq__(other):
            return False
        if other.slot != self.slot:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Lamination
        LamSlot_dict = super(LamSlot, self).as_dict()
        if self.slot is None:
            LamSlot_dict["slot"] = None
        else:
            LamSlot_dict["slot"] = self.slot.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSlot_dict["__class__"] = "LamSlot"
        return LamSlot_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.slot is not None:
            self.slot._set_None()
        # Set to None the properties inherited from Lamination
        super(LamSlot, self)._set_None()

    def _get_slot(self):
        """getter of slot"""
        return self._slot

    def _set_slot(self, value):
        """setter of slot"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "slot")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Slot()
        check_var("slot", value, "Slot")
        self._slot = value

        if self._slot is not None:
            self._slot.parent = self

    slot = property(
        fget=_get_slot,
        fset=_set_slot,
        doc=u"""lamination Slot

        :Type: Slot
        """,
    )
