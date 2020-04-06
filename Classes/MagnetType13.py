# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MagnetType13.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MagnetFlat import MagnetFlat

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MagnetType13.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.MagnetType13.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Machine.MagnetType13.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class MagnetType13(MagnetFlat):
    """single magnet with rectangular base and curved-top shape"""

    VERSION = 1
    IS_FLAT_BOT = 1
    IS_FLAT_TOP = 0

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MagnetType13.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType13 method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.MagnetType13.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType13 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.MagnetType13.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType13 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
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
            assert(type(init_dict) is dict)
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
        # Call MagnetFlat init
        super(MagnetType13, self).__init__(mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag)
        # The class is frozen (in MagnetFlat init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagnetType13_str = ""
        # Get the properties inherited from MagnetFlat
        MagnetType13_str += super(MagnetType13, self).__str__()
        MagnetType13_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType13_str += "Hmag = " + str(self.Hmag) + linesep
        MagnetType13_str += "Rtop = " + str(self.Rtop) + linesep
        return MagnetType13_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MagnetFlat
        if not super(MagnetType13, self).__eq__(other):
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

        # Get the properties inherited from MagnetFlat
        MagnetType13_dict = super(MagnetType13, self).as_dict()
        MagnetType13_dict["Wmag"] = self.Wmag
        MagnetType13_dict["Hmag"] = self.Hmag
        MagnetType13_dict["Rtop"] = self.Rtop
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MagnetType13_dict["__class__"] = "MagnetType13"
        return MagnetType13_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wmag = None
        self.Hmag = None
        self.Rtop = None
        # Set to None the properties inherited from MagnetFlat
        super(MagnetType13, self)._set_None()

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self,'logger_name'):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger('Pyleecan')

    def _get_Wmag(self):
        """getter of Wmag"""
        return self._Wmag

    def _set_Wmag(self, value):
        """setter of Wmag"""
        check_var("Wmag", value, "float", Vmin=0)
        self._Wmag = value

    # magnet bottom width [m]
    # Type : float, min = 0
    Wmag = property(
        fget=_get_Wmag, fset=_set_Wmag, doc=u"""magnet bottom width [m]"""
    )

    def _get_Hmag(self):
        """getter of Hmag"""
        return self._Hmag

    def _set_Hmag(self, value):
        """setter of Hmag"""
        check_var("Hmag", value, "float", Vmin=0)
        self._Hmag = value

    # magnet radial height [m]
    # Type : float, min = 0
    Hmag = property(
        fget=_get_Hmag, fset=_set_Hmag, doc=u"""magnet radial height [m]"""
    )

    def _get_Rtop(self):
        """getter of Rtop"""
        return self._Rtop

    def _set_Rtop(self, value):
        """setter of Rtop"""
        check_var("Rtop", value, "float", Vmin=0)
        self._Rtop = value

    # radius of the circular top shape [m]
    # Type : float, min = 0
    Rtop = property(
        fget=_get_Rtop, fset=_set_Rtop, doc=u"""radius of the circular top shape [m]"""
    )
