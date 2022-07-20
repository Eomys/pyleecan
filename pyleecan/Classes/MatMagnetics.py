# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatMagnetics.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatMagnetics
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
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

try:
    from ..Methods.Material.MatMagnetics.get_Hc import get_Hc
except ImportError as error:
    get_Hc = error

try:
    from ..Methods.Material.MatMagnetics.get_Brm import get_Brm
except ImportError as error:
    get_Brm = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


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
    # cf Methods.Material.MatMagnetics.get_Hc
    if isinstance(get_Hc, ImportError):
        get_Hc = property(
            fget=lambda x: raise_(
                ImportError("Can't use MatMagnetics method get_Hc: " + str(get_Hc))
            )
        )
    else:
        get_Hc = get_Hc
    # cf Methods.Material.MatMagnetics.get_Brm
    if isinstance(get_Brm, ImportError):
        get_Brm = property(
            fget=lambda x: raise_(
                ImportError("Can't use MatMagnetics method get_Brm: " + str(get_Brm))
            )
        )
    else:
        get_Brm = get_Brm
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mur_lin=1,
        Brm20=0,
        alpha_Br=0,
        Wlam=0,
        BH_curve=-1,
        LossData=-1,
        ModelBH=-1,
        is_BH_extrapolate=False,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "mur_lin" in list(init_dict.keys()):
                mur_lin = init_dict["mur_lin"]
            if "Brm20" in list(init_dict.keys()):
                Brm20 = init_dict["Brm20"]
            if "alpha_Br" in list(init_dict.keys()):
                alpha_Br = init_dict["alpha_Br"]
            if "Wlam" in list(init_dict.keys()):
                Wlam = init_dict["Wlam"]
            if "BH_curve" in list(init_dict.keys()):
                BH_curve = init_dict["BH_curve"]
            if "LossData" in list(init_dict.keys()):
                LossData = init_dict["LossData"]
            if "ModelBH" in list(init_dict.keys()):
                ModelBH = init_dict["ModelBH"]
            if "is_BH_extrapolate" in list(init_dict.keys()):
                is_BH_extrapolate = init_dict["is_BH_extrapolate"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.mur_lin = mur_lin
        self.Brm20 = Brm20
        self.alpha_Br = alpha_Br
        self.Wlam = Wlam
        self.BH_curve = BH_curve
        self.LossData = LossData
        self.ModelBH = ModelBH
        self.is_BH_extrapolate = is_BH_extrapolate

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MatMagnetics_str = ""
        if self.parent is None:
            MatMagnetics_str += "parent = None " + linesep
        else:
            MatMagnetics_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MatMagnetics_str += "mur_lin = " + str(self.mur_lin) + linesep
        MatMagnetics_str += "Brm20 = " + str(self.Brm20) + linesep
        MatMagnetics_str += "alpha_Br = " + str(self.alpha_Br) + linesep
        MatMagnetics_str += "Wlam = " + str(self.Wlam) + linesep
        if self.BH_curve is not None:
            tmp = self.BH_curve.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MatMagnetics_str += "BH_curve = " + tmp
        else:
            MatMagnetics_str += "BH_curve = None" + linesep + linesep
        if self.LossData is not None:
            tmp = self.LossData.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MatMagnetics_str += "LossData = " + tmp
        else:
            MatMagnetics_str += "LossData = None" + linesep + linesep
        if self.ModelBH is not None:
            tmp = self.ModelBH.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MatMagnetics_str += "ModelBH = " + tmp
        else:
            MatMagnetics_str += "ModelBH = None" + linesep + linesep
        MatMagnetics_str += (
            "is_BH_extrapolate = " + str(self.is_BH_extrapolate) + linesep
        )
        return MatMagnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mur_lin != self.mur_lin:
            return False
        if other.Brm20 != self.Brm20:
            return False
        if other.alpha_Br != self.alpha_Br:
            return False
        if other.Wlam != self.Wlam:
            return False
        if other.BH_curve != self.BH_curve:
            return False
        if other.LossData != self.LossData:
            return False
        if other.ModelBH != self.ModelBH:
            return False
        if other.is_BH_extrapolate != self.is_BH_extrapolate:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (
            other._mur_lin is not None
            and self._mur_lin is not None
            and isnan(other._mur_lin)
            and isnan(self._mur_lin)
        ):
            pass
        elif other._mur_lin != self._mur_lin:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._mur_lin)
                    + ", other="
                    + str(other._mur_lin)
                    + ")"
                )
                diff_list.append(name + ".mur_lin" + val_str)
            else:
                diff_list.append(name + ".mur_lin")
        if (
            other._Brm20 is not None
            and self._Brm20 is not None
            and isnan(other._Brm20)
            and isnan(self._Brm20)
        ):
            pass
        elif other._Brm20 != self._Brm20:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Brm20) + ", other=" + str(other._Brm20) + ")"
                )
                diff_list.append(name + ".Brm20" + val_str)
            else:
                diff_list.append(name + ".Brm20")
        if (
            other._alpha_Br is not None
            and self._alpha_Br is not None
            and isnan(other._alpha_Br)
            and isnan(self._alpha_Br)
        ):
            pass
        elif other._alpha_Br != self._alpha_Br:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._alpha_Br)
                    + ", other="
                    + str(other._alpha_Br)
                    + ")"
                )
                diff_list.append(name + ".alpha_Br" + val_str)
            else:
                diff_list.append(name + ".alpha_Br")
        if (
            other._Wlam is not None
            and self._Wlam is not None
            and isnan(other._Wlam)
            and isnan(self._Wlam)
        ):
            pass
        elif other._Wlam != self._Wlam:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Wlam) + ", other=" + str(other._Wlam) + ")"
                )
                diff_list.append(name + ".Wlam" + val_str)
            else:
                diff_list.append(name + ".Wlam")
        if (other.BH_curve is None and self.BH_curve is not None) or (
            other.BH_curve is not None and self.BH_curve is None
        ):
            diff_list.append(name + ".BH_curve None mismatch")
        elif self.BH_curve is not None:
            diff_list.extend(
                self.BH_curve.compare(
                    other.BH_curve,
                    name=name + ".BH_curve",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.LossData is None and self.LossData is not None) or (
            other.LossData is not None and self.LossData is None
        ):
            diff_list.append(name + ".LossData None mismatch")
        elif self.LossData is not None:
            diff_list.extend(
                self.LossData.compare(
                    other.LossData,
                    name=name + ".LossData",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.ModelBH is None and self.ModelBH is not None) or (
            other.ModelBH is not None and self.ModelBH is None
        ):
            diff_list.append(name + ".ModelBH None mismatch")
        elif self.ModelBH is not None:
            diff_list.extend(
                self.ModelBH.compare(
                    other.ModelBH,
                    name=name + ".ModelBH",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._is_BH_extrapolate != self._is_BH_extrapolate:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_BH_extrapolate)
                    + ", other="
                    + str(other._is_BH_extrapolate)
                    + ")"
                )
                diff_list.append(name + ".is_BH_extrapolate" + val_str)
            else:
                diff_list.append(name + ".is_BH_extrapolate")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.mur_lin)
        S += getsizeof(self.Brm20)
        S += getsizeof(self.alpha_Br)
        S += getsizeof(self.Wlam)
        S += getsizeof(self.BH_curve)
        S += getsizeof(self.LossData)
        S += getsizeof(self.ModelBH)
        S += getsizeof(self.is_BH_extrapolate)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        MatMagnetics_dict = dict()
        MatMagnetics_dict["mur_lin"] = self.mur_lin
        MatMagnetics_dict["Brm20"] = self.Brm20
        MatMagnetics_dict["alpha_Br"] = self.alpha_Br
        MatMagnetics_dict["Wlam"] = self.Wlam
        if self.BH_curve is None:
            MatMagnetics_dict["BH_curve"] = None
        else:
            MatMagnetics_dict["BH_curve"] = self.BH_curve.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.LossData is None:
            MatMagnetics_dict["LossData"] = None
        else:
            MatMagnetics_dict["LossData"] = self.LossData.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.ModelBH is None:
            MatMagnetics_dict["ModelBH"] = None
        else:
            MatMagnetics_dict["ModelBH"] = self.ModelBH.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        MatMagnetics_dict["is_BH_extrapolate"] = self.is_BH_extrapolate
        # The class name is added to the dict for deserialisation purpose
        MatMagnetics_dict["__class__"] = "MatMagnetics"
        return MatMagnetics_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        mur_lin_val = self.mur_lin
        Brm20_val = self.Brm20
        alpha_Br_val = self.alpha_Br
        Wlam_val = self.Wlam
        if self.BH_curve is None:
            BH_curve_val = None
        else:
            BH_curve_val = self.BH_curve.copy()
        if self.LossData is None:
            LossData_val = None
        else:
            LossData_val = self.LossData.copy()
        if self.ModelBH is None:
            ModelBH_val = None
        else:
            ModelBH_val = self.ModelBH.copy()
        is_BH_extrapolate_val = self.is_BH_extrapolate
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            mur_lin=mur_lin_val,
            Brm20=Brm20_val,
            alpha_Br=alpha_Br_val,
            Wlam=Wlam_val,
            BH_curve=BH_curve_val,
            LossData=LossData_val,
            ModelBH=ModelBH_val,
            is_BH_extrapolate=is_BH_extrapolate_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mur_lin = None
        self.Brm20 = None
        self.alpha_Br = None
        self.Wlam = None
        if self.BH_curve is not None:
            self.BH_curve._set_None()
        if self.LossData is not None:
            self.LossData._set_None()
        if self.ModelBH is not None:
            self.ModelBH._set_None()
        self.is_BH_extrapolate = None

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
        doc=u"""magnet remanence induction at 20degC (calculated from mur_lin and Hc if not provided)

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
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "BH_curve")
        ImportMatrixVal = import_class(
            "pyleecan.Classes", "ImportMatrixVal", "BH_curve"
        )
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "BH_curve"
            )
            value = class_obj(init_dict=value)
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

    def _get_LossData(self):
        """getter of LossData"""
        return self._LossData

    def _set_LossData(self, value):
        """setter of LossData"""
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "LossData")
        ImportMatrixVal = import_class(
            "pyleecan.Classes", "ImportMatrixVal", "LossData"
        )
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "LossData"
            )
            value = class_obj(init_dict=value)
        check_var("LossData", value, "ImportMatrix")
        self._LossData = value

        if self._LossData is not None:
            self._LossData.parent = self

    LossData = property(
        fget=_get_LossData,
        fset=_set_LossData,
        doc=u"""specific loss data value triplets, i.e. B, f, P

        :Type: ImportMatrix
        """,
    )

    def _get_ModelBH(self):
        """getter of ModelBH"""
        return self._ModelBH

    def _set_ModelBH(self, value):
        """setter of ModelBH"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "ModelBH"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            ModelBH = import_class("pyleecan.Classes", "ModelBH", "ModelBH")
            value = ModelBH()
        check_var("ModelBH", value, "ModelBH")
        self._ModelBH = value

        if self._ModelBH is not None:
            self._ModelBH.parent = self

    ModelBH = property(
        fget=_get_ModelBH,
        fset=_set_ModelBH,
        doc=u"""a model of BH curve with an analytical expression

        :Type: ModelBH
        """,
    )

    def _get_is_BH_extrapolate(self):
        """getter of is_BH_extrapolate"""
        return self._is_BH_extrapolate

    def _set_is_BH_extrapolate(self, value):
        """setter of is_BH_extrapolate"""
        check_var("is_BH_extrapolate", value, "bool")
        self._is_BH_extrapolate = value

    is_BH_extrapolate = property(
        fget=_get_is_BH_extrapolate,
        fset=_set_is_BH_extrapolate,
        doc=u"""1 to use ModelBH to fit input data and extrapolate BH curve

        :Type: bool
        """,
    )
