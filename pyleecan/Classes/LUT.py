# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LUT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LUT
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LUT.get_phase_dir import get_phase_dir
except ImportError as error:
    get_phase_dir = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class LUT(FrozenClass):
    """Abstract class for Look Up Table (LUT)"""

    VERSION = 1

    # cf Methods.Simulation.LUT.get_phase_dir
    if isinstance(get_phase_dir, ImportError):
        get_phase_dir = property(
            fget=lambda x: raise_(
                ImportError("Can't use LUT method get_phase_dir: " + str(get_phase_dir))
            )
        )
    else:
        get_phase_dir = get_phase_dir
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        R1=None,
        L1=None,
        T1_ref=20,
        OP_matrix=None,
        phase_dir=None,
        B=None,
        Phi_wind_stator=None,
        Tem=None,
        axes_dict=None,
        is_interp_along_curve=None,
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
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "T1_ref" in list(init_dict.keys()):
                T1_ref = init_dict["T1_ref"]
            if "OP_matrix" in list(init_dict.keys()):
                OP_matrix = init_dict["OP_matrix"]
            if "phase_dir" in list(init_dict.keys()):
                phase_dir = init_dict["phase_dir"]
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "Phi_wind_stator" in list(init_dict.keys()):
                Phi_wind_stator = init_dict["Phi_wind_stator"]
            if "Tem" in list(init_dict.keys()):
                Tem = init_dict["Tem"]
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "is_interp_along_curve" in list(init_dict.keys()):
                is_interp_along_curve = init_dict["is_interp_along_curve"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.R1 = R1
        self.L1 = L1
        self.T1_ref = T1_ref
        self.OP_matrix = OP_matrix
        self.phase_dir = phase_dir
        self.B = B
        self.Phi_wind_stator = Phi_wind_stator
        self.Tem = Tem
        self.axes_dict = axes_dict
        self.is_interp_along_curve = is_interp_along_curve

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LUT_str = ""
        if self.parent is None:
            LUT_str += "parent = None " + linesep
        else:
            LUT_str += "parent = " + str(type(self.parent)) + " object" + linesep
        LUT_str += "R1 = " + str(self.R1) + linesep
        LUT_str += "L1 = " + str(self.L1) + linesep
        LUT_str += "T1_ref = " + str(self.T1_ref) + linesep
        LUT_str += (
            "OP_matrix = "
            + linesep
            + str(self.OP_matrix).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        LUT_str += "phase_dir = " + str(self.phase_dir) + linesep
        LUT_str += "B = " + str(self.B) + linesep + linesep
        LUT_str += "Phi_wind_stator = " + str(self.Phi_wind_stator) + linesep + linesep
        LUT_str += "Tem = " + str(self.Tem) + linesep + linesep
        LUT_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        LUT_str += (
            "is_interp_along_curve = " + str(self.is_interp_along_curve) + linesep
        )
        return LUT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.R1 != self.R1:
            return False
        if other.L1 != self.L1:
            return False
        if other.T1_ref != self.T1_ref:
            return False
        if not array_equal(other.OP_matrix, self.OP_matrix):
            return False
        if other.phase_dir != self.phase_dir:
            return False
        if other.B != self.B:
            return False
        if other.Phi_wind_stator != self.Phi_wind_stator:
            return False
        if other.Tem != self.Tem:
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.is_interp_along_curve != self.is_interp_along_curve:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._R1 != self._R1:
            diff_list.append(name + ".R1")
        if other._L1 != self._L1:
            diff_list.append(name + ".L1")
        if other._T1_ref != self._T1_ref:
            diff_list.append(name + ".T1_ref")
        if not array_equal(other.OP_matrix, self.OP_matrix):
            diff_list.append(name + ".OP_matrix")
        if other._phase_dir != self._phase_dir:
            diff_list.append(name + ".phase_dir")
        if (other.B is None and self.B is not None) or (
            other.B is not None and self.B is None
        ):
            diff_list.append(name + ".B None mismatch")
        elif self.B is None:
            pass
        elif len(other.B) != len(self.B):
            diff_list.append("len(" + name + ".B)")
        else:
            for ii in range(len(other.B)):
                diff_list.extend(
                    self.B[ii].compare(other.B[ii], name=name + ".B[" + str(ii) + "]")
                )
        if (other.Phi_wind_stator is None and self.Phi_wind_stator is not None) or (
            other.Phi_wind_stator is not None and self.Phi_wind_stator is None
        ):
            diff_list.append(name + ".Phi_wind_stator None mismatch")
        elif self.Phi_wind_stator is None:
            pass
        elif len(other.Phi_wind_stator) != len(self.Phi_wind_stator):
            diff_list.append("len(" + name + ".Phi_wind_stator)")
        else:
            for ii in range(len(other.Phi_wind_stator)):
                diff_list.extend(
                    self.Phi_wind_stator[ii].compare(
                        other.Phi_wind_stator[ii],
                        name=name + ".Phi_wind_stator[" + str(ii) + "]",
                    )
                )
        if (other.Tem is None and self.Tem is not None) or (
            other.Tem is not None and self.Tem is None
        ):
            diff_list.append(name + ".Tem None mismatch")
        elif self.Tem is None:
            pass
        elif len(other.Tem) != len(self.Tem):
            diff_list.append("len(" + name + ".Tem)")
        else:
            for ii in range(len(other.Tem)):
                diff_list.extend(
                    self.Tem[ii].compare(
                        other.Tem[ii], name=name + ".Tem[" + str(ii) + "]"
                    )
                )
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key], name=name + ".axes_dict"
                    )
                )
        if other._is_interp_along_curve != self._is_interp_along_curve:
            diff_list.append(name + ".is_interp_along_curve")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.R1)
        S += getsizeof(self.L1)
        S += getsizeof(self.T1_ref)
        S += getsizeof(self.OP_matrix)
        S += getsizeof(self.phase_dir)
        if self.B is not None:
            for value in self.B:
                S += getsizeof(value)
        if self.Phi_wind_stator is not None:
            for value in self.Phi_wind_stator:
                S += getsizeof(value)
        if self.Tem is not None:
            for value in self.Tem:
                S += getsizeof(value)
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_interp_along_curve)
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

        LUT_dict = dict()
        LUT_dict["R1"] = self.R1
        LUT_dict["L1"] = self.L1
        LUT_dict["T1_ref"] = self.T1_ref
        if self.OP_matrix is None:
            LUT_dict["OP_matrix"] = None
        else:
            if type_handle_ndarray == 0:
                LUT_dict["OP_matrix"] = self.OP_matrix.tolist()
            elif type_handle_ndarray == 1:
                LUT_dict["OP_matrix"] = self.OP_matrix.copy()
            elif type_handle_ndarray == 2:
                LUT_dict["OP_matrix"] = self.OP_matrix
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        LUT_dict["phase_dir"] = self.phase_dir
        if self.B is None:
            LUT_dict["B"] = None
        else:
            LUT_dict["B"] = list()
            for obj in self.B:
                if obj is not None:
                    LUT_dict["B"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LUT_dict["B"].append(None)
        if self.Phi_wind_stator is None:
            LUT_dict["Phi_wind_stator"] = None
        else:
            LUT_dict["Phi_wind_stator"] = list()
            for obj in self.Phi_wind_stator:
                if obj is not None:
                    LUT_dict["Phi_wind_stator"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LUT_dict["Phi_wind_stator"].append(None)
        if self.Tem is None:
            LUT_dict["Tem"] = None
        else:
            LUT_dict["Tem"] = list()
            for obj in self.Tem:
                if obj is not None:
                    LUT_dict["Tem"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LUT_dict["Tem"].append(None)
        if self.axes_dict is None:
            LUT_dict["axes_dict"] = None
        else:
            LUT_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    LUT_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    LUT_dict["axes_dict"][key] = None
        LUT_dict["is_interp_along_curve"] = self.is_interp_along_curve
        # The class name is added to the dict for deserialisation purpose
        LUT_dict["__class__"] = "LUT"
        return LUT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.R1 = None
        self.L1 = None
        self.T1_ref = None
        self.OP_matrix = None
        self.phase_dir = None
        self.B = None
        self.Phi_wind_stator = None
        self.Tem = None
        self.axes_dict = None
        self.is_interp_along_curve = None

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float")
        self._R1 = value

    R1 = property(
        fget=_get_R1,
        fset=_set_R1,
        doc=u"""DC phase winding resistance at T1_ref per phase 

        :Type: float
        """,
    )

    def _get_L1(self):
        """getter of L1"""
        return self._L1

    def _set_L1(self, value):
        """setter of L1"""
        check_var("L1", value, "float")
        self._L1 = value

    L1 = property(
        fget=_get_L1,
        fset=_set_L1,
        doc=u"""Phase winding leakage inductance 

        :Type: float
        """,
    )

    def _get_T1_ref(self):
        """getter of T1_ref"""
        return self._T1_ref

    def _set_T1_ref(self, value):
        """setter of T1_ref"""
        check_var("T1_ref", value, "float")
        self._T1_ref = value

    T1_ref = property(
        fget=_get_T1_ref,
        fset=_set_T1_ref,
        doc=u"""Stator winding average temperature associated to R1, L1 parameters

        :Type: float
        """,
    )

    def _get_OP_matrix(self):
        """getter of OP_matrix"""
        return self._OP_matrix

    def _set_OP_matrix(self, value):
        """setter of OP_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("OP_matrix", value, "ndarray")
        self._OP_matrix = value

    OP_matrix = property(
        fget=_get_OP_matrix,
        fset=_set_OP_matrix,
        doc=u"""Array of operating point values of size (N,5) with N the number of operating points (Speed, Id, Iq, Torque, Power). OP values are set to nan if they are not given.

        :Type: ndarray
        """,
    )

    def _get_phase_dir(self):
        """getter of phase_dir"""
        return self._phase_dir

    def _set_phase_dir(self, value):
        """setter of phase_dir"""
        check_var("phase_dir", value, "int", Vmin=-1, Vmax=1)
        self._phase_dir = value

    phase_dir = property(
        fget=_get_phase_dir,
        fset=_set_phase_dir,
        doc=u"""Rotation direction of the stator phases (phase_dir*(n-1)*pi/qs, default value given by PHASE_DIR_REF)

        :Type: int
        :min: -1
        :max: 1
        """,
    )

    def _get_B(self):
        """getter of B"""
        if self._B is not None:
            for obj in self._B:
                if obj is not None:
                    obj.parent = self
        return self._B

    def _set_B(self, value):
        """setter of B"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "B"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("B", value, "[VectorField]")
        self._B = value

    B = property(
        fget=_get_B,
        fset=_set_B,
        doc=u"""Airgap flux density look-up table: list of VectorField objects whose (Id,Iq) is given by Idq list

        :Type: [SciDataTool.Classes.VectorField.VectorField]
        """,
    )

    def _get_Phi_wind_stator(self):
        """getter of Phi_wind_stator"""
        if self._Phi_wind_stator is not None:
            for obj in self._Phi_wind_stator:
                if obj is not None:
                    obj.parent = self
        return self._Phi_wind_stator

    def _set_Phi_wind_stator(self, value):
        """setter of Phi_wind_stator"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "Phi_wind_stator"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("Phi_wind_stator", value, "[DataND]")
        self._Phi_wind_stator = value

    Phi_wind_stator = property(
        fget=_get_Phi_wind_stator,
        fset=_set_Phi_wind_stator,
        doc=u"""Stator winding flux look-up table: list of DataTime objects whose (Id,Iq) is given by Idq list

        :Type: [SciDataTool.Classes.DataND.DataND]
        """,
    )

    def _get_Tem(self):
        """getter of Tem"""
        if self._Tem is not None:
            for obj in self._Tem:
                if obj is not None:
                    obj.parent = self
        return self._Tem

    def _set_Tem(self, value):
        """setter of Tem"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "Tem"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("Tem", value, "[DataND]")
        self._Tem = value

    Tem = property(
        fget=_get_Tem,
        fset=_set_Tem,
        doc=u"""Instaneous torque look-up table: list of DataTime objects whose (Id,Iq) is given by Idq list

        :Type: [SciDataTool.Classes.DataND.DataND]
        """,
    )

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc=u"""Dict containing axes data used for Magnetics

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_is_interp_along_curve(self):
        """getter of is_interp_along_curve"""
        return self._is_interp_along_curve

    def _set_is_interp_along_curve(self, value):
        """setter of is_interp_along_curve"""
        check_var("is_interp_along_curve", value, "bool")
        self._is_interp_along_curve = value

    is_interp_along_curve = property(
        fget=_get_is_interp_along_curve,
        fset=_set_is_interp_along_curve,
        doc=u"""True if interpolation can be performed along curve

        :Type: bool
        """,
    )
