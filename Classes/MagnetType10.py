# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.MagnetFlat import MagnetFlat

from pyleecan.Methods.Machine.MagnetType10.build_geometry import build_geometry
from pyleecan.Methods.Machine.MagnetType10.comp_height import comp_height
from pyleecan.Methods.Machine.MagnetType10.comp_surface import comp_surface

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class MagnetType10(MagnetFlat):
    """single magnet with rectangular shape"""

    VERSION = 1
    IS_FLAT_BOT = 1
    IS_FLAT_TOP = 1

    # cf Methods.Machine.MagnetType10.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.MagnetType10.comp_height
    comp_height = comp_height
    # cf Methods.Machine.MagnetType10.comp_surface
    comp_surface = comp_surface

    def __init__(
        self,
        Wmag=0.002,
        Hmag=0.001,
        mat_type=-1,
        type_magnetization=0,
        Lmag=0.95,
        init_dict=None,
    ):
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
            check_init_dict(
                init_dict, ["Wmag", "Hmag", "mat_type", "type_magnetization", "Lmag"]
            )
            # Overwrite default value with init_dict content
            if "Wmag" in list(init_dict.keys()):
                Wmag = init_dict["Wmag"]
            if "Hmag" in list(init_dict.keys()):
                Hmag = init_dict["Hmag"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
            if "Lmag" in list(init_dict.keys()):
                Lmag = init_dict["Lmag"]
        # Initialisation by argument
        self.Wmag = Wmag
        self.Hmag = Hmag
        # Call MagnetFlat init
        super(MagnetType10, self).__init__(
            mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag
        )
        # The class is frozen (in MagnetFlat init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagnetType10_str = ""
        # Get the properties inherited from MagnetFlat
        MagnetType10_str += super(MagnetType10, self).__str__() + linesep
        MagnetType10_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType10_str += "Hmag = " + str(self.Hmag)
        return MagnetType10_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MagnetFlat
        if not super(MagnetType10, self).__eq__(other):
            return False
        if other.Wmag != self.Wmag:
            return False
        if other.Hmag != self.Hmag:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MagnetFlat
        MagnetType10_dict = super(MagnetType10, self).as_dict()
        MagnetType10_dict["Wmag"] = self.Wmag
        MagnetType10_dict["Hmag"] = self.Hmag
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MagnetType10_dict["__class__"] = "MagnetType10"
        return MagnetType10_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wmag = None
        self.Hmag = None
        # Set to None the properties inherited from MagnetFlat
        super(MagnetType10, self)._set_None()

    def _get_Wmag(self):
        """getter of Wmag"""
        return self._Wmag

    def _set_Wmag(self, value):
        """setter of Wmag"""
        check_var("Wmag", value, "float", Vmin=0)
        self._Wmag = value

    # magnet bottom width [m]
    # Type : float, min = 0
    Wmag = property(fget=_get_Wmag, fset=_set_Wmag, doc=u"""magnet bottom width [m]""")

    def _get_Hmag(self):
        """getter of Hmag"""
        return self._Hmag

    def _set_Hmag(self, value):
        """setter of Hmag"""
        check_var("Hmag", value, "float", Vmin=0)
        self._Hmag = value

    # magnet radial height [m]
    # Type : float, min = 0
    Hmag = property(fget=_get_Hmag, fset=_set_Hmag, doc=u"""magnet radial height [m]""")
