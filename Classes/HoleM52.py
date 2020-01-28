# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/HoleM52.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.HoleMag import HoleMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.HoleM52.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Slot.HoleM52.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_alpha import comp_alpha
except ImportError as error:
    comp_alpha = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_mass_magnets import comp_mass_magnets
except ImportError as error:
    comp_mass_magnets = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_surface_magnets import comp_surface_magnets
except ImportError as error:
    comp_surface_magnets = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_volume_magnets import comp_volume_magnets
except ImportError as error:
    comp_volume_magnets = error

try:
    from pyleecan.Methods.Slot.HoleM52.comp_W1 import comp_W1
except ImportError as error:
    comp_W1 = error

try:
    from pyleecan.Methods.Slot.HoleM52.get_height_magnet import get_height_magnet
except ImportError as error:
    get_height_magnet = error

try:
    from pyleecan.Methods.Slot.HoleM52.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Material import Material


class HoleM52(HoleMag):
    """V shape slot for buried magnet"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleM52.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleM52.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM52 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.HoleM52.comp_alpha
    if isinstance(comp_alpha, ImportError):
        comp_alpha = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM52 method comp_alpha: " + str(comp_alpha))
            )
        )
    else:
        comp_alpha = comp_alpha
    # cf Methods.Slot.HoleM52.comp_mass_magnets
    if isinstance(comp_mass_magnets, ImportError):
        comp_mass_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method comp_mass_magnets: "
                    + str(comp_mass_magnets)
                )
            )
        )
    else:
        comp_mass_magnets = comp_mass_magnets
    # cf Methods.Slot.HoleM52.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM52 method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.HoleM52.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.HoleM52.comp_surface_magnets
    if isinstance(comp_surface_magnets, ImportError):
        comp_surface_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method comp_surface_magnets: "
                    + str(comp_surface_magnets)
                )
            )
        )
    else:
        comp_surface_magnets = comp_surface_magnets
    # cf Methods.Slot.HoleM52.comp_volume_magnets
    if isinstance(comp_volume_magnets, ImportError):
        comp_volume_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method comp_volume_magnets: "
                    + str(comp_volume_magnets)
                )
            )
        )
    else:
        comp_volume_magnets = comp_volume_magnets
    # cf Methods.Slot.HoleM52.comp_W1
    if isinstance(comp_W1, ImportError):
        comp_W1 = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM52 method comp_W1: " + str(comp_W1))
            )
        )
    else:
        comp_W1 = comp_W1
    # cf Methods.Slot.HoleM52.get_height_magnet
    if isinstance(get_height_magnet, ImportError):
        get_height_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method get_height_magnet: "
                    + str(get_height_magnet)
                )
            )
        )
    else:
        get_height_magnet = get_height_magnet
    # cf Methods.Slot.HoleM52.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM52 method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # save method is available in all object
    save = save

    def __init__(self, H0=0.003, W0=0.003, H1=0, W3=0.013, H2=0.02, magnet_0=-1, Zh=36, mat_void=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if magnet_0 == -1:
            magnet_0 = Magnet()
        if mat_void == -1:
            mat_void = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["H0", "W0", "H1", "W3", "H2", "magnet_0", "Zh", "mat_void"])
            # Overwrite default value with init_dict content
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "magnet_0" in list(init_dict.keys()):
                magnet_0 = init_dict["magnet_0"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.H0 = H0
        self.W0 = W0
        self.H1 = H1
        self.W3 = W3
        self.H2 = H2
        # magnet_0 can be None, a Magnet object or a dict
        if isinstance(magnet_0, dict):
            # Check that the type is correct (including daughter)
            class_name = magnet_0.get('__class__')
            if class_name not in ['Magnet', 'MagnetFlat', 'MagnetPolar', 'MagnetType10', 'MagnetType11', 'MagnetType12', 'MagnetType13', 'MagnetType14']:
                raise InitUnKnowClassError("Unknow class name "+class_name+" in init_dict for magnet_0")
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])
            class_obj = getattr(module,class_name)
            self.magnet_0 = class_obj(init_dict=magnet_0)
        else:
            self.magnet_0 = magnet_0
        # Call HoleMag init
        super(HoleM52, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleM52_str = ""
        # Get the properties inherited from HoleMag
        HoleM52_str += super(HoleM52, self).__str__() + linesep
        HoleM52_str += "H0 = " + str(self.H0) + linesep
        HoleM52_str += "W0 = " + str(self.W0) + linesep
        HoleM52_str += "H1 = " + str(self.H1) + linesep
        HoleM52_str += "W3 = " + str(self.W3) + linesep
        HoleM52_str += "H2 = " + str(self.H2) + linesep
        if self.magnet_0 is not None:
            HoleM52_str += "magnet_0 = " + str(self.magnet_0.as_dict()) + linesep + linesep
        else:
            HoleM52_str += "magnet_0 = None"
        return HoleM52_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleM52, self).__eq__(other):
            return False
        if other.H0 != self.H0:
            return False
        if other.W0 != self.W0:
            return False
        if other.H1 != self.H1:
            return False
        if other.W3 != self.W3:
            return False
        if other.H2 != self.H2:
            return False
        if other.magnet_0 != self.magnet_0:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from HoleMag
        HoleM52_dict = super(HoleM52, self).as_dict()
        HoleM52_dict["H0"] = self.H0
        HoleM52_dict["W0"] = self.W0
        HoleM52_dict["H1"] = self.H1
        HoleM52_dict["W3"] = self.W3
        HoleM52_dict["H2"] = self.H2
        if self.magnet_0 is None:
            HoleM52_dict["magnet_0"] = None
        else:
            HoleM52_dict["magnet_0"] = self.magnet_0.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleM52_dict["__class__"] = "HoleM52"
        return HoleM52_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H0 = None
        self.W0 = None
        self.H1 = None
        self.W3 = None
        self.H2 = None
        if self.magnet_0 is not None:
            self.magnet_0._set_None()
        # Set to None the properties inherited from HoleMag
        super(HoleM52, self)._set_None()

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Slot depth
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Slot depth""")

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Magnet width
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0, doc=u"""Magnet width""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Magnet height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Magnet height""")

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Tooth width
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Tooth width""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Additional depth for the magnet
    # Type : float, min = 0
    H2 = property(
        fget=_get_H2, fset=_set_H2, doc=u"""Additional depth for the magnet"""
    )

    def _get_magnet_0(self):
        """getter of magnet_0"""
        return self._magnet_0

    def _set_magnet_0(self, value):
        """setter of magnet_0"""
        check_var("magnet_0", value, "Magnet")
        self._magnet_0 = value

        if self._magnet_0 is not None:
            self._magnet_0.parent = self
    # Magnet of the hole
    # Type : Magnet
    magnet_0 = property(
        fget=_get_magnet_0, fset=_set_magnet_0, doc=u"""Magnet of the hole"""
    )
