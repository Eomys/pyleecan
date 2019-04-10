# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.HoleMag import HoleMag

from pyleecan.Methods.Slot.HoleM52.build_geometry import build_geometry
from pyleecan.Methods.Slot.HoleM52.check import check
from pyleecan.Methods.Slot.HoleM52.comp_alpha import comp_alpha
from pyleecan.Methods.Slot.HoleM52.comp_mass_magnets import comp_mass_magnets
from pyleecan.Methods.Slot.HoleM52.comp_radius import comp_radius
from pyleecan.Methods.Slot.HoleM52.comp_surface import comp_surface
from pyleecan.Methods.Slot.HoleM52.comp_surface_magnets import comp_surface_magnets
from pyleecan.Methods.Slot.HoleM52.comp_volume_magnets import comp_volume_magnets
from pyleecan.Methods.Slot.HoleM52.comp_W1 import comp_W1
from pyleecan.Methods.Slot.HoleM52.remove_magnet import remove_magnet

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.MagnetFlat import MagnetFlat
from pyleecan.Classes.MagnetPolar import MagnetPolar
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.Material import Material



class HoleM52(HoleMag):
    """V shape slot for buried magnet"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # cf Methods.Slot.HoleM52.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.HoleM52.check
    check = check
    # cf Methods.Slot.HoleM52.comp_alpha
    comp_alpha = comp_alpha
    # cf Methods.Slot.HoleM52.comp_mass_magnets
    comp_mass_magnets = comp_mass_magnets
    # cf Methods.Slot.HoleM52.comp_radius
    comp_radius = comp_radius
    # cf Methods.Slot.HoleM52.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.HoleM52.comp_surface_magnets
    comp_surface_magnets = comp_surface_magnets
    # cf Methods.Slot.HoleM52.comp_volume_magnets
    comp_volume_magnets = comp_volume_magnets
    # cf Methods.Slot.HoleM52.comp_W1
    comp_W1 = comp_W1
    # cf Methods.Slot.HoleM52.remove_magnet
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
            # Call the correct constructor according to the dict
            load_dict = {"MagnetFlat": MagnetFlat, "MagnetPolar": MagnetPolar, "MagnetType10": MagnetType10, "MagnetType11": MagnetType11, "MagnetType12": MagnetType12, "MagnetType13": MagnetType13, "MagnetType14": MagnetType14, "Magnet": Magnet}
            obj_class = magnet_0.get('__class__')
            if obj_class is None:
                self.magnet_0 = Magnet(init_dict=magnet_0)
            elif obj_class in list(load_dict.keys()):
                self.magnet_0 = load_dict[obj_class](init_dict=magnet_0)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for magnet_0")
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
        HoleM52_str += "magnet_0 = " + str(self.magnet_0.as_dict())
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
    H0 = property(fget=_get_H0, fset=_set_H0,
                  doc=u"""Slot depth""")

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Magnet width
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0,
                  doc=u"""Magnet width""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Magnet height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1,
                  doc=u"""Magnet height""")

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Tooth width
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3,
                  doc=u"""Tooth width""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Additional depth for the magnet
    # Type : float, min = 0
    H2 = property(fget=_get_H2, fset=_set_H2,
                  doc=u"""Additional depth for the magnet""")

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
    magnet_0 = property(fget=_get_magnet_0, fset=_set_magnet_0,
                        doc=u"""Magnet of the hole""")
