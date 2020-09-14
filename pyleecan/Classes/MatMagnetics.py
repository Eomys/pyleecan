# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatMagnetics.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatMagnetics
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Material.MatMagnetics.get_BH import get_BH
except ImportError as error:
    get_BH = error

try:
    from ..Methods.Material.MatMagnetics.plot_BH import plot_BH
except ImportError as error:
    plot_BH = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix


class MatMagnetics(FrozenClass):
    """magnetic material properties"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Material.MatMagnetics.get_BH
    if isinstance(get_BH, ImportError):
        get_BH = property(
            fget=lambda x: raise_(
                ImportError("Can't use MatMagnetics method get_BH: " + str(get_BH))
            )
        )
    else:
        get_BH = get_BH
    # cf Methods.Material.MatMagnetics.plot_BH
    if isinstance(plot_BH, ImportError):
        plot_BH = property(
            fget=lambda x: raise_(
                ImportError("Can't use MatMagnetics method plot_BH: " + str(plot_BH))
            )
        )
    else:
        plot_BH = plot_BH
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, mur_lin=1, Hc=0, Brm20=0, alpha_Br=0, Wlam=0, BH_curve=-1, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if BH_curve == -1:
            BH_curve = ImportMatrix()
        if init_str is not None :  # Initialisation by str
            from ..Functions.load import load
            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            mur_lin = obj.mur_lin
            Hc = obj.Hc
            Brm20 = obj.Brm20
            alpha_Br = obj.alpha_Br
            Wlam = obj.Wlam
            BH_curve = obj.BH_curve
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "mur_lin" in list(init_dict.keys()):
                mur_lin = init_dict["mur_lin"]
            if "Hc" in list(init_dict.keys()):
                Hc = init_dict["Hc"]
            if "Brm20" in list(init_dict.keys()):
                Brm20 = init_dict["Brm20"]
            if "alpha_Br" in list(init_dict.keys()):
                alpha_Br = init_dict["alpha_Br"]
            if "Wlam" in list(init_dict.keys()):
                Wlam = init_dict["Wlam"]
            if "BH_curve" in list(init_dict.keys()):
                BH_curve = init_dict["BH_curve"]
        # Initialisation by argument
        self.parent = None
        self.mur_lin = mur_lin
        self.Hc = Hc
        self.Brm20 = Brm20
        self.alpha_Br = alpha_Br
        self.Wlam = Wlam
        # BH_curve can be None, a ImportMatrix object or a dict
        if isinstance(BH_curve, dict):
            # Check that the type is correct (including daughter)
            class_name = BH_curve.get("__class__")
            if class_name not in ['ImportMatrix', 'ImportGenMatrixSin', 'ImportGenToothSaw', 'ImportGenVectLin', 'ImportGenVectSin', 'ImportMatlab', 'ImportMatrixVal', 'ImportMatrixXls']:
                raise InitUnKnowClassError(
                    "Unknow class name "
                    + class_name
                    + " in init_dict for BH_curve"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])
            class_obj = getattr(module,class_name)
            self.BH_curve = class_obj(init_dict=BH_curve)
        elif isinstance(BH_curve, str):
            from ..Functions.load import load
            BH_curve = load(BH_curve)
            # Check that the type is correct (including daughter)
            class_name = BH_curve.__class__.__name__
            if class_name not in ['ImportMatrix', 'ImportGenMatrixSin', 'ImportGenToothSaw', 'ImportGenVectLin', 'ImportGenVectSin', 'ImportMatlab', 'ImportMatrixVal', 'ImportMatrixXls']:
                raise InitUnKnowClassError(
                    "Unknow class name "
                    + class_name
                    + " in init_dict for BH_curve"
                )
            self.BH_curve=BH_curve
        else:
            self.BH_curve = BH_curve

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatMagnetics_str = ""
        if self.parent is None:
            MatMagnetics_str += "parent = None " + linesep
        else:
            MatMagnetics_str += "parent = " + str(type(self.parent)) + " object" + linesep
        MatMagnetics_str += "mur_lin = " + str(self.mur_lin) + linesep
        MatMagnetics_str += "Hc = " + str(self.Hc) + linesep
        MatMagnetics_str += "Brm20 = " + str(self.Brm20) + linesep
        MatMagnetics_str += "alpha_Br = " + str(self.alpha_Br) + linesep
        MatMagnetics_str += "Wlam = " + str(self.Wlam) + linesep
        if self.BH_curve is not None:
            tmp = self.BH_curve.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MatMagnetics_str += "BH_curve = "+ tmp
        else:
            MatMagnetics_str += "BH_curve = None" + linesep + linesep
        return MatMagnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mur_lin != self.mur_lin:
            return False
        if other.Hc != self.Hc:
            return False
        if other.Brm20 != self.Brm20:
            return False
        if other.alpha_Br != self.alpha_Br:
            return False
        if other.Wlam != self.Wlam:
            return False
        if other.BH_curve != self.BH_curve:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatMagnetics_dict = dict()
        MatMagnetics_dict["mur_lin"] = self.mur_lin
        MatMagnetics_dict["Hc"] = self.Hc
        MatMagnetics_dict["Brm20"] = self.Brm20
        MatMagnetics_dict["alpha_Br"] = self.alpha_Br
        MatMagnetics_dict["Wlam"] = self.Wlam
        if self.BH_curve is None:
            MatMagnetics_dict["BH_curve"] = None
        else:
            MatMagnetics_dict["BH_curve"] = self.BH_curve.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        MatMagnetics_dict["__class__"] = "MatMagnetics"
        return MatMagnetics_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mur_lin = None
        self.Hc = None
        self.Brm20 = None
        self.alpha_Br = None
        self.Wlam = None
        if self.BH_curve is not None:
            self.BH_curve._set_None()

    def _get_mur_lin(self):
        """getter of mur_lin"""
        return self._mur_lin

    def _set_mur_lin(self, value):
        """setter of mur_lin"""
        check_var("mur_lin", value, "float", Vmin=0)
        self._mur_lin = value

    mur_lin = property(
        fget=_get_mur_lin,
        fset=_set_mur_lin,
        doc=u"""Relative magnetic permeability

        :Type: float
        :min: 0
        """,
    )

    def _get_Hc(self):
        """getter of Hc"""
        return self._Hc

    def _set_Hc(self, value):
        """setter of Hc"""
        check_var("Hc", value, "float", Vmin=0)
        self._Hc = value

    Hc = property(
        fget=_get_Hc,
        fset=_set_Hc,
        doc=u"""Coercitivity field

        :Type: float
        :min: 0
        """,
    )

    def _get_Brm20(self):
        """getter of Brm20"""
        return self._Brm20

    def _set_Brm20(self, value):
        """setter of Brm20"""
        check_var("Brm20", value, "float")
        self._Brm20 = value

    Brm20 = property(
        fget=_get_Brm20,
        fset=_set_Brm20,
        doc=u"""magnet remanence induction at 20degC

        :Type: float
        """,
    )

    def _get_alpha_Br(self):
        """getter of alpha_Br"""
        return self._alpha_Br

    def _set_alpha_Br(self, value):
        """setter of alpha_Br"""
        check_var("alpha_Br", value, "float")
        self._alpha_Br = value

    alpha_Br = property(
        fget=_get_alpha_Br,
        fset=_set_alpha_Br,
        doc=u"""temperature coefficient for remanent flux density /degC compared to 20degC

        :Type: float
        """,
    )

    def _get_Wlam(self):
        """getter of Wlam"""
        return self._Wlam

    def _set_Wlam(self, value):
        """setter of Wlam"""
        check_var("Wlam", value, "float", Vmin=0)
        self._Wlam = value

    Wlam = property(
        fget=_get_Wlam,
        fset=_set_Wlam,
        doc=u"""lamination sheet width without insulation [m] (0 == not laminated)

        :Type: float
        :min: 0
        """,
    )

    def _get_BH_curve(self):
        """getter of BH_curve"""
        return self._BH_curve

    def _set_BH_curve(self, value):
        """setter of BH_curve"""
        if isinstance(value,ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value,list):
            value = ImportMatrixVal(value=array(value))
        check_var("BH_curve", value, "ImportMatrix")
        self._BH_curve = value

        if self._BH_curve is not None:
            self._BH_curve.parent = self
    BH_curve = property(
        fget=_get_BH_curve,
        fset=_set_BH_curve,
        doc=u"""nonlinear B(H) curve (two columns matrix, H and B(H))

        :Type: ImportMatrix
        """,
    )
