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
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotWind.comp_angle_wind_eq import comp_angle_wind_eq
except ImportError as error:
    comp_angle_wind_eq = error

try:
    from ..Methods.Slot.SlotWind.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from ..Methods.Slot.SlotWind.comp_radius_mid_wind import comp_radius_mid_wind
except ImportError as error:
    comp_radius_mid_wind = error

try:
    from ..Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error

try:
    from ..Methods.Slot.SlotWind.plot_wind import plot_wind
except ImportError as error:
    plot_wind = error


from ._check import InitUnKnowClassError


class SlotWind(Slot):
    """Slot for winding (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotWind.comp_angle_wind_eq
    if isinstance(comp_angle_wind_eq, ImportError):
        comp_angle_wind_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_angle_wind_eq: "
                    + str(comp_angle_wind_eq)
                )
            )
        )
    else:
        comp_angle_wind_eq = comp_angle_wind_eq
    # cf Methods.Slot.SlotWind.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotWind.comp_radius_mid_wind
    if isinstance(comp_radius_mid_wind, ImportError):
        comp_radius_mid_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_radius_mid_wind: "
                    + str(comp_radius_mid_wind)
                )
            )
        )
    else:
        comp_radius_mid_wind = comp_radius_mid_wind
    # cf Methods.Slot.SlotWind.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotWind method comp_surface_wind: "
                    + str(comp_surface_wind)
                )
            )
        )
    else:
        comp_surface_wind = comp_surface_wind
    # cf Methods.Slot.SlotWind.plot_wind
    if isinstance(plot_wind, ImportError):
        plot_wind = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotWind method plot_wind: " + str(plot_wind))
            )
        )
    else:
        plot_wind = plot_wind
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

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
        """Convert this objet in a readeable string (for print)"""

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
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Slot
        SlotWind_dict = super(SlotWind, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotWind_dict["__class__"] = "SlotWind"
        return SlotWind_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Slot
        super(SlotWind, self)._set_None()
