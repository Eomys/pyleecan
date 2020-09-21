# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleM58.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleM58
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .HoleMag import HoleMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleM58.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.HoleM58.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.HoleM58.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.HoleM58.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error

try:
    from ..Methods.Slot.HoleM58.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.HoleM58.comp_surface_magnet_id import comp_surface_magnet_id
except ImportError as error:
    comp_surface_magnet_id = error


from ._check import InitUnKnowClassError
from .Magnet import Magnet
from .Material import Material


class HoleM58(HoleMag):
    """One magnet with circular notches"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleM58.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM58 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleM58.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM58 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.HoleM58.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM58 method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.HoleM58.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM58 method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # cf Methods.Slot.HoleM58.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM58 method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.HoleM58.comp_surface_magnet_id
    if isinstance(comp_surface_magnet_id, ImportError):
        comp_surface_magnet_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM58 method comp_surface_magnet_id: "
                    + str(comp_surface_magnet_id)
                )
            )
        )
    else:
        comp_surface_magnet_id = comp_surface_magnet_id
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        H0=0.003,
        W0=0.003,
        H1=0,
        W1=0.013,
        H2=0.02,
        W2=0.01,
        W3=0.01,
        R0=0.01,
        magnet_0=-1,
        Zh=36,
        mat_void=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if magnet_0 == -1:
            magnet_0 = Magnet()
        if mat_void == -1:
            mat_void = Material()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            H0 = obj.H0
            W0 = obj.W0
            H1 = obj.H1
            W1 = obj.W1
            H2 = obj.H2
            W2 = obj.W2
            W3 = obj.W3
            R0 = obj.R0
            magnet_0 = obj.magnet_0
            Zh = obj.Zh
            mat_void = obj.mat_void
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "R0" in list(init_dict.keys()):
                R0 = init_dict["R0"]
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
        self.W1 = W1
        self.H2 = H2
        self.W2 = W2
        self.W3 = W3
        self.R0 = R0
        # magnet_0 can be None, a Magnet object or a dict
        if isinstance(magnet_0, dict):
            # Check that the type is correct (including daughter)
            class_name = magnet_0.get("__class__")
            if class_name not in [
                "Magnet",
                "MagnetFlat",
                "MagnetPolar",
                "MagnetType10",
                "MagnetType11",
                "MagnetType12",
                "MagnetType13",
                "MagnetType14",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for magnet_0"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.magnet_0 = class_obj(init_dict=magnet_0)
        elif isinstance(magnet_0, str):
            from ..Functions.load import load

            magnet_0 = load(magnet_0)
            # Check that the type is correct (including daughter)
            class_name = magnet_0.__class__.__name__
            if class_name not in [
                "Magnet",
                "MagnetFlat",
                "MagnetPolar",
                "MagnetType10",
                "MagnetType11",
                "MagnetType12",
                "MagnetType13",
                "MagnetType14",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for magnet_0"
                )
            self.magnet_0 = magnet_0
        else:
            self.magnet_0 = magnet_0
        # Call HoleMag init
        super(HoleM58, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleM58_str = ""
        # Get the properties inherited from HoleMag
        HoleM58_str += super(HoleM58, self).__str__()
        HoleM58_str += "H0 = " + str(self.H0) + linesep
        HoleM58_str += "W0 = " + str(self.W0) + linesep
        HoleM58_str += "H1 = " + str(self.H1) + linesep
        HoleM58_str += "W1 = " + str(self.W1) + linesep
        HoleM58_str += "H2 = " + str(self.H2) + linesep
        HoleM58_str += "W2 = " + str(self.W2) + linesep
        HoleM58_str += "W3 = " + str(self.W3) + linesep
        HoleM58_str += "R0 = " + str(self.R0) + linesep
        if self.magnet_0 is not None:
            tmp = self.magnet_0.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleM58_str += "magnet_0 = " + tmp
        else:
            HoleM58_str += "magnet_0 = None" + linesep + linesep
        return HoleM58_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleM58, self).__eq__(other):
            return False
        if other.H0 != self.H0:
            return False
        if other.W0 != self.W0:
            return False
        if other.H1 != self.H1:
            return False
        if other.W1 != self.W1:
            return False
        if other.H2 != self.H2:
            return False
        if other.W2 != self.W2:
            return False
        if other.W3 != self.W3:
            return False
        if other.R0 != self.R0:
            return False
        if other.magnet_0 != self.magnet_0:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from HoleMag
        HoleM58_dict = super(HoleM58, self).as_dict()
        HoleM58_dict["H0"] = self.H0
        HoleM58_dict["W0"] = self.W0
        HoleM58_dict["H1"] = self.H1
        HoleM58_dict["W1"] = self.W1
        HoleM58_dict["H2"] = self.H2
        HoleM58_dict["W2"] = self.W2
        HoleM58_dict["W3"] = self.W3
        HoleM58_dict["R0"] = self.R0
        if self.magnet_0 is None:
            HoleM58_dict["magnet_0"] = None
        else:
            HoleM58_dict["magnet_0"] = self.magnet_0.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleM58_dict["__class__"] = "HoleM58"
        return HoleM58_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H0 = None
        self.W0 = None
        self.H1 = None
        self.W1 = None
        self.H2 = None
        self.W2 = None
        self.W3 = None
        self.R0 = None
        if self.magnet_0 is not None:
            self.magnet_0._set_None()
        # Set to None the properties inherited from HoleMag
        super(HoleM58, self)._set_None()

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
        doc=u"""Slot depth

        :Type: float
        :min: 0
        """,
    )

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
        doc=u"""Slot width

        :Type: float
        :min: 0
        """,
    )

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    H1 = property(
        fget=_get_H1,
        fset=_set_H1,
        doc=u"""Distance from the lamination Bore

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc=u"""Magnet width

        :Type: float
        :min: 0
        """,
    )

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    H2 = property(
        fget=_get_H2,
        fset=_set_H2,
        doc=u"""Magnet Height

        :Type: float
        :min: 0
        """,
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    W2 = property(
        fget=_get_W2,
        fset=_set_W2,
        doc=u"""Distance Magnet to side of the notch

        :Type: float
        :min: 0
        """,
    )

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    W3 = property(
        fget=_get_W3,
        fset=_set_W3,
        doc=u"""Tooth angular opening width

        :Type: float
        :min: 0
        """,
    )

    def _get_R0(self):
        """getter of R0"""
        return self._R0

    def _set_R0(self, value):
        """setter of R0"""
        check_var("R0", value, "float", Vmin=0)
        self._R0 = value

    R0 = property(
        fget=_get_R0,
        fset=_set_R0,
        doc=u"""Notch radius

        :Type: float
        :min: 0
        """,
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

    magnet_0 = property(
        fget=_get_magnet_0,
        fset=_set_magnet_0,
        doc=u"""Magnet

        :Type: Magnet
        """,
    )
