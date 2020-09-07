# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotMag
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .LamSlot import LamSlot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotMag.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotMag.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlotMag.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamSlotMag.comp_radius_mec import comp_radius_mec
except ImportError as error:
    comp_radius_mec = error

try:
    from ..Methods.Machine.LamSlotMag.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlotMag.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamSlotMag.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlotMag.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSlotMag.comp_sym import comp_sym
except ImportError as error:
    comp_sym = error


from ._check import InitUnKnowClassError
from .Slot import Slot
from .Material import Material
from .Hole import Hole
from .Notch import Notch


class LamSlotMag(LamSlot):
    """Lamination with Slot for Magnets"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotMag.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMag.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMag method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlotMag.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_masses: " + str(comp_masses)
                )
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamSlotMag.comp_radius_mec
    if isinstance(comp_radius_mec, ImportError):
        comp_radius_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_radius_mec: "
                    + str(comp_radius_mec)
                )
            )
        )
    else:
        comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlotMag.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotMag.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamSlotMag.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMag method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlotMag.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMag method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSlotMag.comp_sym
    if isinstance(comp_sym, ImportError):
        comp_sym = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMag method comp_sym: " + str(comp_sym))
            )
        )
    else:
        comp_sym = comp_sym
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
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
        axial_vent=list(),
        notch=list(),
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if slot == -1:
            slot = Slot()
        if mat_type == -1:
            mat_type = Material()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            slot = obj.slot
            L1 = obj.L1
            mat_type = obj.mat_type
            Nrvd = obj.Nrvd
            Wrvd = obj.Wrvd
            Kf1 = obj.Kf1
            is_internal = obj.is_internal
            Rint = obj.Rint
            Rext = obj.Rext
            is_stator = obj.is_stator
            axial_vent = obj.axial_vent
            notch = obj.notch
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
        # Initialisation by argument
        # Call LamSlot init
        super(LamSlotMag, self).__init__(
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
        # The class is frozen (in LamSlot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamSlotMag_str = ""
        # Get the properties inherited from LamSlot
        LamSlotMag_str += super(LamSlotMag, self).__str__()
        return LamSlotMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlot
        if not super(LamSlotMag, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from LamSlot
        LamSlotMag_dict = super(LamSlotMag, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSlotMag_dict["__class__"] = "LamSlotMag"
        return LamSlotMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from LamSlot
        super(LamSlotMag, self)._set_None()
