# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotWind.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotWind
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotWind.comp_angle_active_eq import comp_angle_active_eq
except ImportError as error:
    comp_angle_active_eq = error

try:
    from ..Methods.Slot.SlotWind.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotWind.comp_radius_mid_active import comp_radius_mid_active
except ImportError as error:
    comp_radius_mid_active = error

try:
    from ..Methods.Slot.SlotWind.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Slot.SlotWind.plot_active import plot_active
except ImportError as error:
    plot_active = error

try:
    from ..Methods.Slot.SlotWind.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error


from ._check import InitUnKnowClassError


class SlotWind(Slot):
    """Slot for winding (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotWind.comp_angle_active_eq
    if isinstance(comp_angle_active_eq, ImportError):
        comp_angle_active_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_angle_active_eq: "
                    + str(comp_angle_active_eq)
                )
            )
        )
    else:
        comp_angle_active_eq = comp_angle_active_eq
    # cf Methods.Slot.SlotWind.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotWind.comp_radius_mid_active
    if isinstance(comp_radius_mid_active, ImportError):
        comp_radius_mid_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_radius_mid_active: "
                    + str(comp_radius_mid_active)
                )
            )
        )
    else:
        comp_radius_mid_active = comp_radius_mid_active
    # cf Methods.Slot.SlotWind.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Slot.SlotWind.plot_active
    if isinstance(plot_active, ImportError):
        plot_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method plot_active: " + str(plot_active)
                )
            )
        )
    else:
        plot_active = plot_active
    # cf Methods.Slot.SlotWind.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Zs=36, init_dict=None, init_str=None):
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
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        # Call Slot init
        super(SlotWind, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotWind_str = ""
        # Get the properties inherited from Slot
        SlotWind_str += super(SlotWind, self).__str__()
        return SlotWind_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotWind, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Slot
        SlotWind_dict = super(SlotWind, self).as_dict()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotWind_dict["__class__"] = "SlotWind"
        return SlotWind_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Slot
        super(SlotWind, self)._set_None()
