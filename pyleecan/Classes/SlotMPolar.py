# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotMPolar.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotMPolar
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .SlotMag import SlotMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotMPolar.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotMPolar.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotMPolar.comp_angle_opening_magnet import (
        comp_angle_opening_magnet,
    )
except ImportError as error:
    comp_angle_opening_magnet = error

try:
    from ..Methods.Slot.SlotMPolar.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotMPolar.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotMPolar.get_point_bottom import get_point_bottom
except ImportError as error:
    get_point_bottom = error


from ._check import InitUnKnowClassError
from .MagnetPolar import MagnetPolar


class SlotMPolar(SlotMag):
    """Polar bottomed SlotMag"""

    VERSION = 1
    IS_SYMMETRICAL = 1
    IS_INSET = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotMPolar.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotMPolar.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotMPolar.comp_angle_opening_magnet
    if isinstance(comp_angle_opening_magnet, ImportError):
        comp_angle_opening_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method comp_angle_opening_magnet: "
                    + str(comp_angle_opening_magnet)
                )
            )
        )
    else:
        comp_angle_opening_magnet = comp_angle_opening_magnet
    # cf Methods.Slot.SlotMPolar.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotMPolar.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotMPolar.get_point_bottom
    if isinstance(get_point_bottom, ImportError):
        get_point_bottom = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotMPolar method get_point_bottom: "
                    + str(get_point_bottom)
                )
            )
        )
    else:
        get_point_bottom = get_point_bottom
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, W0=0.314, H0=0, magnet=-1, W3=0, Zs=36, init_dict=None, init_str=None
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
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "magnet" in list(init_dict.keys()):
                magnet = init_dict["magnet"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.H0 = H0
        self.magnet = magnet
        # Call SlotMag init
        super(SlotMPolar, self).__init__(W3=W3, Zs=Zs)
        # The class is frozen (in SlotMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotMPolar_str = ""
        # Get the properties inherited from SlotMag
        SlotMPolar_str += super(SlotMPolar, self).__str__()
        SlotMPolar_str += "W0 = " + str(self.W0) + linesep
        SlotMPolar_str += "H0 = " + str(self.H0) + linesep
        if len(self.magnet) == 0:
            SlotMPolar_str += "magnet = []" + linesep
        for ii in range(len(self.magnet)):
            tmp = self.magnet[ii].__str__().replace(linesep, linesep + "\t") + linesep
            SlotMPolar_str += "magnet[" + str(ii) + "] =" + tmp + linesep + linesep
        return SlotMPolar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotMag
        if not super(SlotMPolar, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.magnet != self.magnet:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotMag
        SlotMPolar_dict = super(SlotMPolar, self).as_dict()
        SlotMPolar_dict["W0"] = self.W0
        SlotMPolar_dict["H0"] = self.H0
        if self.magnet is None:
            SlotMPolar_dict["magnet"] = None
        else:
            SlotMPolar_dict["magnet"] = list()
            for obj in self.magnet:
                SlotMPolar_dict["magnet"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotMPolar_dict["__class__"] = "SlotMPolar"
        return SlotMPolar_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        for obj in self.magnet:
            obj._set_None()
        # Set to None the properties inherited from SlotMag
        super(SlotMPolar, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Slot isthmus width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc=u"""Slot isthmus height

        :Type: float
        :min: 0
        """,
    )

    def _get_magnet(self):
        """getter of magnet"""
        if self._magnet is not None:
            for obj in self._magnet:
                if obj is not None:
                    obj.parent = self
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "magnet"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("magnet", value, "[MagnetPolar]")
        self._magnet = value

    magnet = property(
        fget=_get_magnet,
        fset=_set_magnet,
        doc=u"""List of magnet

        :Type: [MagnetPolar]
        """,
    )
