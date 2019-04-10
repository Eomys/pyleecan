# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotMag import SlotMag

from pyleecan.Methods.Slot.SlotMPolar.build_geometry import build_geometry
from pyleecan.Methods.Slot.SlotMPolar.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotMPolar.comp_angle_opening_magnet import comp_angle_opening_magnet
from pyleecan.Methods.Slot.SlotMPolar.comp_height import comp_height
from pyleecan.Methods.Slot.SlotMPolar.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotMPolar.get_point_bottom import get_point_bottom

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.MagnetPolar import MagnetPolar
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType14 import MagnetType14



class SlotMPolar(SlotMag):
    """Polar bottomed SlotMag"""

    VERSION = 1
    IS_SYMMETRICAL = 1
    IS_INSET = 1

    # cf Methods.Slot.SlotMPolar.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.SlotMPolar.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotMPolar.comp_angle_opening_magnet
    comp_angle_opening_magnet = comp_angle_opening_magnet
    # cf Methods.Slot.SlotMPolar.comp_height
    comp_height = comp_height
    # cf Methods.Slot.SlotMPolar.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.SlotMPolar.get_point_bottom
    get_point_bottom = get_point_bottom
    # save method is available in all object
    save = save

    def __init__(self, W0=0.314, H0=0, magnet=list(), W3=0, Zs=36, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["W0", "H0", "magnet", "W3", "Zs"])
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
        # Initialisation by argument
        self.W0 = W0
        self.H0 = H0
        # magnet can be None or a list of MagnetPolar object
        self.magnet = list()
        if type(magnet) is list:
            for obj in magnet:
                if obj is None:  # Default value
                    self.magnet.append(MagnetPolar())
                elif isinstance(obj, dict):
                    # Call the correct constructor according to the dict
                    load_dict = {"MagnetType11": MagnetType11, "MagnetType14": MagnetType14, "MagnetPolar": MagnetPolar}
                    obj_class = obj.get('__class__')
                    if obj_class is None:
                        self.magnet.append(MagnetPolar(init_dict=obj))
                    elif obj_class in list(load_dict.keys()):
                        self.magnet.append(load_dict[obj_class](init_dict=obj))
                    else:  # Avoid generation error or wrong modification in json
                        raise InitUnKnowClassError("Unknow class name in init_dict for magnet")
                else:
                    self.magnet.append(obj)
        elif magnet is None:
            self.magnet = list()
        else:
            self.magnet = magnet
        # Call SlotMag init
        super(SlotMPolar, self).__init__(W3=W3, Zs=Zs)
        # The class is frozen (in SlotMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotMPolar_str = ""
        # Get the properties inherited from SlotMag
        SlotMPolar_str += super(SlotMPolar, self).__str__() + linesep
        SlotMPolar_str += "W0 = " + str(self.W0) + linesep
        SlotMPolar_str += "H0 = " + str(self.H0) + linesep
        if len(self.magnet) == 0:
            SlotMPolar_str += "magnet = []"
        for ii in range(len(self.magnet)):
            SlotMPolar_str += "magnet["+str(ii)+"] = "+str(self.magnet[ii].as_dict())+"\n"
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
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotMag
        SlotMPolar_dict = super(SlotMPolar, self).as_dict()
        SlotMPolar_dict["W0"] = self.W0
        SlotMPolar_dict["H0"] = self.H0
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

    # Slot isthmus width.
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0,
                  doc=u"""Slot isthmus width.""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Slot isthmus height
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0,
                  doc=u"""Slot isthmus height""")

    def _get_magnet(self):
        """getter of magnet"""
        for obj in self._magnet:
            if obj is not None:
                obj.parent = self
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        check_var("magnet", value, "[MagnetPolar]")
        self._magnet = value

        for obj in self._magnet:
            if obj is not None:
                obj.parent = self
    # List of magnet
    # Type : [MagnetPolar]
    magnet = property(fget=_get_magnet, fset=_set_magnet,
                      doc=u"""List of magnet""")
