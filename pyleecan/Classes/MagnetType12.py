# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MagnetType12.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MagnetType12
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .MagnetFlat import MagnetFlat

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MagnetType12.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.MagnetType12.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.MagnetType12.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error


from ._check import InitUnKnowClassError
from .Material import Material


class MagnetType12(MagnetFlat):
    """single magnet with rectangular base and polar top"""

    VERSION = 1
    IS_FLAT_BOT = 1
    IS_FLAT_TOP = 0

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MagnetType12.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType12 method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.MagnetType12.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType12 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.MagnetType12.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagnetType12 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Wmag=0.002,
        Hmag=0.001,
        mat_type=-1,
        type_magnetization=0,
        Lmag=0.95,
        init_dict=None,
        init_str=None,
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
        # Set the properties (value check and convertion are done in setter)
        self.Wmag = Wmag
        self.Hmag = Hmag
        # Call MagnetFlat init
        super(MagnetType12, self).__init__(
            mat_type=mat_type, type_magnetization=type_magnetization, Lmag=Lmag
        )
        # The class is frozen (in MagnetFlat init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MagnetType12_str = ""
        # Get the properties inherited from MagnetFlat
        MagnetType12_str += super(MagnetType12, self).__str__()
        MagnetType12_str += "Wmag = " + str(self.Wmag) + linesep
        MagnetType12_str += "Hmag = " + str(self.Hmag) + linesep
        return MagnetType12_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MagnetFlat
        if not super(MagnetType12, self).__eq__(other):
            return False
        if other.Wmag != self.Wmag:
            return False
        if other.Hmag != self.Hmag:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from MagnetFlat
        S += super(MagnetType12, self).__sizeof__()
        S += getsizeof(self.Wmag)
        S += getsizeof(self.Hmag)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from MagnetFlat
        MagnetType12_dict = super(MagnetType12, self).as_dict()
        MagnetType12_dict["Wmag"] = self.Wmag
        MagnetType12_dict["Hmag"] = self.Hmag
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MagnetType12_dict["__class__"] = "MagnetType12"
        return MagnetType12_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wmag = None
        self.Hmag = None
        # Set to None the properties inherited from MagnetFlat
        super(MagnetType12, self)._set_None()

    def _get_Wmag(self):
        """getter of Wmag"""
        return self._Wmag

    def _set_Wmag(self, value):
        """setter of Wmag"""
        check_var("Wmag", value, "float", Vmin=0)
        self._Wmag = value

    Wmag = property(
        fget=_get_Wmag,
        fset=_set_Wmag,
        doc=u"""magnet bottom width [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Hmag(self):
        """getter of Hmag"""
        return self._Hmag

    def _set_Hmag(self, value):
        """setter of Hmag"""
        check_var("Hmag", value, "float", Vmin=0)
        self._Hmag = value

    Hmag = property(
        fget=_get_Hmag,
        fset=_set_Hmag,
        doc=u"""magnet radial height [m]

        :Type: float
        :min: 0
        """,
    )
