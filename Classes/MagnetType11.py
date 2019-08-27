# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.MagnetPolar import MagnetPolar

from pyleecan.Methods.Machine.MagnetType11._comp_point_coordinate import _comp_point_coordinate
from pyleecan.Methods.Machine.MagnetType11.build_geometry import build_geometry
from pyleecan.Methods.Machine.MagnetType11.comp_height import comp_height
from pyleecan.Methods.Machine.MagnetType11.comp_surface import comp_surface

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class MagnetType11(MagnetPolar):
    """single magnet with polar shape"""

    VERSION = 1
    IS_FLAT_BOT = 0
    IS_FLAT_TOP = 0

    # cf Methods.Machine.MagnetType11._comp_point_coordinate
    _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Machine.MagnetType11.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.MagnetType11.comp_height
    comp_height = comp_height
    # cf Methods.Machine.MagnetType11.comp_surface
    comp_surface = comp_surface
    # save method is available in all object
    save = save

    def __init__(self, Wmag=0.002, Hmag=0.001, mat_type=-1, type_magnetization=0, Lmag=0.95, init_dict=None):
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
            check_init_dict(init_dict, ["Wmag", "Hmag", "mat_type", "type_magnetization", "Lmag"])
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
        # Call MagnetPolar init
        super(MagnetType11, self).__init__(mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag)
        # The class is frozen (in MagnetPolar init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagnetType11_str = ""
        # Get the properties inherited from MagnetPolar
        MagnetType11_str += super(MagnetType11, self).__str__() + linesep
        MagnetType11_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType11_str += "Hmag = " + str(self.Hmag)
        return MagnetType11_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MagnetPolar
        if not super(MagnetType11, self).__eq__(other):
            return False
        if other.Wmag != self.Wmag:
            return False
        if other.Hmag != self.Hmag:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MagnetPolar
        MagnetType11_dict = super(MagnetType11, self).as_dict()
        MagnetType11_dict["Wmag"] = self.Wmag
        MagnetType11_dict["Hmag"] = self.Hmag
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MagnetType11_dict["__class__"] = "MagnetType11"
        return MagnetType11_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wmag = None
        self.Hmag = None
        # Set to None the properties inherited from MagnetPolar
        super(MagnetType11, self)._set_None()

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
