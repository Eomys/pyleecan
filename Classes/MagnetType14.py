# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.MagnetPolar import MagnetPolar

from pyleecan.Methods.Machine.MagnetType14.build_geometry import build_geometry
from pyleecan.Methods.Machine.MagnetType14.comp_height import comp_height

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class MagnetType14(MagnetPolar):
    """single magnet with polar base and curved-top shape """

    VERSION = 1
    IS_FLAT_BOT = 0
    IS_FLAT_TOP = 0

    # cf Methods.Machine.MagnetType14.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.MagnetType14.comp_height
    comp_height = comp_height
    # save method is available in all object
    save = save

    def __init__(self, Wmag=0.002, Hmag=0.001, Rtop=0.05, mat_type=-1, type_magnetization=0, Lmag=0.95, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Wmag", "Hmag", "Rtop", "mat_type", "type_magnetization", "Lmag"])
            # Overwrite default value with init_dict content
            if "Wmag" in list(init_dict.keys()):
                Wmag = init_dict["Wmag"]
            if "Hmag" in list(init_dict.keys()):
                Hmag = init_dict["Hmag"]
            if "Rtop" in list(init_dict.keys()):
                Rtop = init_dict["Rtop"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
            if "Lmag" in list(init_dict.keys()):
                Lmag = init_dict["Lmag"]
        # Initialisation by argument
        self.Wmag = Wmag
        self.Hmag = Hmag
        self.Rtop = Rtop
        # Call MagnetPolar init
        super(MagnetType14, self).__init__(mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag)
        # The class is frozen (in MagnetPolar init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagnetType14_str = ""
        # Get the properties inherited from MagnetPolar
        MagnetType14_str += super(MagnetType14, self).__str__() + linesep
        MagnetType14_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType14_str += "Hmag = " + str(self.Hmag) + linesep
        MagnetType14_str += "Rtop = " + str(self.Rtop)
        return MagnetType14_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MagnetPolar
        if not super(MagnetType14, self).__eq__(other):
            return False
        if other.Wmag != self.Wmag:
            return False
        if other.Hmag != self.Hmag:
            return False
        if other.Rtop != self.Rtop:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MagnetPolar
        MagnetType14_dict = super(MagnetType14, self).as_dict()
        MagnetType14_dict["Wmag"] = self.Wmag
        MagnetType14_dict["Hmag"] = self.Hmag
        MagnetType14_dict["Rtop"] = self.Rtop
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MagnetType14_dict["__class__"] = "MagnetType14"
        return MagnetType14_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wmag = None
        self.Hmag = None
        self.Rtop = None
        # Set to None the properties inherited from MagnetPolar
        super(MagnetType14, self)._set_None()

    def _get_Wmag(self):
        """getter of Wmag"""
        return self._Wmag

    def _set_Wmag(self, value):
        """setter of Wmag"""
        check_var("Wmag", value, "float", Vmin=0)
        self._Wmag = value

    # magnet bottom width [rad]
    # Type : float, min = 0
    Wmag = property(fget=_get_Wmag, fset=_set_Wmag,
                    doc=u"""magnet bottom width [rad]""")

    def _get_Hmag(self):
        """getter of Hmag"""
        return self._Hmag

    def _set_Hmag(self, value):
        """setter of Hmag"""
        check_var("Hmag", value, "float", Vmin=0)
        self._Hmag = value

    # magnet radial height [m]
    # Type : float, min = 0
    Hmag = property(fget=_get_Hmag, fset=_set_Hmag,
                    doc=u"""magnet radial height [m]""")

    def _get_Rtop(self):
        """getter of Rtop"""
        return self._Rtop

    def _set_Rtop(self, value):
        """setter of Rtop"""
        check_var("Rtop", value, "float", Vmin=0)
        self._Rtop = value

    # radius of the circular top shape [m]
    # Type : float, min = 0
    Rtop = property(fget=_get_Rtop, fset=_set_Rtop,
                    doc=u"""radius of the circular top shape [m]""")
