# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MagnetType11.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MagnetPolar import MagnetPolar

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MagnetType11._comp_point_coordinate import (
        _comp_point_coordinate,
    )
except ImportError as error:
    _comp_point_coordinate = error

try:
    from pyleecan.Methods.Machine.MagnetType11.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.MagnetType11.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Machine.MagnetType11.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class MagnetType11(MagnetPolar):
    """single magnet with polar shape"""

    VERSION = 1
    IS_FLAT_BOT = 0
    IS_FLAT_TOP = 0

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MagnetType11._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType11 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Machine.MagnetType11.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType11 method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.MagnetType11.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType11 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.MagnetType11.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType11 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # save method is available in all object
    save = save

    def __init__(
        self,
        Wmag=2.00e-03,
        Hmag=1.00e-03,
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
        # Call MagnetPolar init
        super(MagnetType11, self).__init__(
            mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag
        )
        # The class is frozen (in MagnetPolar init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagnetType11_str = ""
        # Get the properties inherited from MagnetPolar
        MagnetType11_str += super(MagnetType11, self).__str__()
        MagnetType11_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType11_str += "Hmag = " + str(self.Hmag) + linesep
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
    Wmag = property(
        fget=_get_Wmag, fset=_set_Wmag, doc=u"""magnet bottom width [rad]"""
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
    Hmag = property(fget=_get_Hmag, fset=_set_Hmag, doc=u"""magnet radial height [m]""")
