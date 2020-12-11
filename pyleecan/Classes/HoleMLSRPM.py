# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleMLSRPM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleMLSRPM
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
    from ..Methods.Slot.HoleMLSRPM.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.HoleMLSRPM.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.HoleMLSRPM.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error

try:
    from ..Methods.Slot.HoleMLSRPM.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error


from ._check import InitUnKnowClassError
from .Magnet import Magnet
from .Material import Material


class HoleMLSRPM(HoleMag):
    """V shape slot for buried magnet"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleMLSRPM.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMLSRPM method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleMLSRPM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleMLSRPM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.HoleMLSRPM.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMLSRPM method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # cf Methods.Slot.HoleMLSRPM.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMLSRPM method has_magnet: " + str(has_magnet)
                )
            )
        )
    else:
        has_magnet = has_magnet
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        H1=0.0023734787,
        W0=0.00388,
        W1=0.219911482,
        W2=0.0007,
        R1=0.0003,
        R2=0.019327,
        R3=0.0165,
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
            H1 = obj.H1
            W0 = obj.W0
            W1 = obj.W1
            W2 = obj.W2
            R1 = obj.R1
            R2 = obj.R2
            R3 = obj.R3
            magnet_0 = obj.magnet_0
            Zh = obj.Zh
            mat_void = obj.mat_void
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "R2" in list(init_dict.keys()):
                R2 = init_dict["R2"]
            if "R3" in list(init_dict.keys()):
                R3 = init_dict["R3"]
            if "magnet_0" in list(init_dict.keys()):
                magnet_0 = init_dict["magnet_0"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.H1 = H1
        self.W0 = W0
        self.W1 = W1
        self.W2 = W2
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
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
        super(HoleMLSRPM, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleMLSRPM_str = ""
        # Get the properties inherited from HoleMag
        HoleMLSRPM_str += super(HoleMLSRPM, self).__str__()
        HoleMLSRPM_str += "H1 = " + str(self.H1) + linesep
        HoleMLSRPM_str += "W0 = " + str(self.W0) + linesep
        HoleMLSRPM_str += "W1 = " + str(self.W1) + linesep
        HoleMLSRPM_str += "W2 = " + str(self.W2) + linesep
        HoleMLSRPM_str += "R1 = " + str(self.R1) + linesep
        HoleMLSRPM_str += "R2 = " + str(self.R2) + linesep
        HoleMLSRPM_str += "R3 = " + str(self.R3) + linesep
        if self.magnet_0 is not None:
            tmp = self.magnet_0.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleMLSRPM_str += "magnet_0 = " + tmp
        else:
            HoleMLSRPM_str += "magnet_0 = None" + linesep + linesep
        return HoleMLSRPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleMLSRPM, self).__eq__(other):
            return False
        if other.H1 != self.H1:
            return False
        if other.W0 != self.W0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.R1 != self.R1:
            return False
        if other.R2 != self.R2:
            return False
        if other.R3 != self.R3:
            return False
        if other.magnet_0 != self.magnet_0:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from HoleMag
        HoleMLSRPM_dict = super(HoleMLSRPM, self).as_dict()
        HoleMLSRPM_dict["H1"] = self.H1
        HoleMLSRPM_dict["W0"] = self.W0
        HoleMLSRPM_dict["W1"] = self.W1
        HoleMLSRPM_dict["W2"] = self.W2
        HoleMLSRPM_dict["R1"] = self.R1
        HoleMLSRPM_dict["R2"] = self.R2
        HoleMLSRPM_dict["R3"] = self.R3
        if self.magnet_0 is None:
            HoleMLSRPM_dict["magnet_0"] = None
        else:
            HoleMLSRPM_dict["magnet_0"] = self.magnet_0.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleMLSRPM_dict["__class__"] = "HoleMLSRPM"
        return HoleMLSRPM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H1 = None
        self.W0 = None
        self.W1 = None
        self.W2 = None
        self.R1 = None
        self.R2 = None
        self.R3 = None
        if self.magnet_0 is not None:
            self.magnet_0._set_None()
        # Set to None the properties inherited from HoleMag
        super(HoleMLSRPM, self)._set_None()

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
        doc=u"""Magnet depth

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
        doc=u"""Magnet top width

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
        doc=u"""Magnet width angular 1 

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
        doc=u"""Small distance

        :Type: float
        :min: 0
        """,
    )

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    R1 = property(
        fget=_get_R1,
        fset=_set_R1,
        doc=u"""Rounding radius

        :Type: float
        :min: 0
        """,
    )

    def _get_R2(self):
        """getter of R2"""
        return self._R2

    def _set_R2(self, value):
        """setter of R2"""
        check_var("R2", value, "float")
        self._R2 = value

    R2 = property(
        fget=_get_R2,
        fset=_set_R2,
        doc=u"""Radius 2

        :Type: float
        """,
    )

    def _get_R3(self):
        """getter of R3"""
        return self._R3

    def _set_R3(self, value):
        """setter of R3"""
        check_var("R3", value, "float")
        self._R3 = value

    R3 = property(
        fget=_get_R3,
        fset=_set_R3,
        doc=u"""Radius 3

        :Type: float
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
        doc=u"""Magnet of the hole

        :Type: Magnet
        """,
    )
