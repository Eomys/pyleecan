# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LUTdq.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LUTdq
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
from .LUT import LUT

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LUTdq.get_Ldqh import get_Ldqh
except ImportError as error:
    get_Ldqh = error

try:
    from ..Methods.Simulation.LUTdq.get_Lmdqh import get_Lmdqh
except ImportError as error:
    get_Lmdqh = error

try:
    from ..Methods.Simulation.LUTdq.get_Phidqh_mean import get_Phidqh_mean
except ImportError as error:
    get_Phidqh_mean = error

try:
    from ..Methods.Simulation.LUTdq.get_Phidqh_mag import get_Phidqh_mag
except ImportError as error:
    get_Phidqh_mag = error

try:
    from ..Methods.Simulation.LUTdq.get_Phidqh_mag_mean import get_Phidqh_mag_mean
except ImportError as error:
    get_Phidqh_mag_mean = error

try:
    from ..Methods.Simulation.LUTdq.interp_Phi_dqh import interp_Phi_dqh
except ImportError as error:
    interp_Phi_dqh = error


from numpy import array, array_equal
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from scipy.interpolate.interpolate import RegularGridInterpolator
except ImportError:
    RegularGridInterpolator = ImportError
from ._check import InitUnKnowClassError


class LUTdq(LUT):
    """Look Up Table class for dq OP matrix"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.LUTdq.get_Ldqh
    if isinstance(get_Ldqh, ImportError):
        get_Ldqh = property(
            fget=lambda x: raise_(
                ImportError("Can't use LUTdq method get_Ldqh: " + str(get_Ldqh))
            )
        )
    else:
        get_Ldqh = get_Ldqh
    # cf Methods.Simulation.LUTdq.get_Lmdqh
    if isinstance(get_Lmdqh, ImportError):
        get_Lmdqh = property(
            fget=lambda x: raise_(
                ImportError("Can't use LUTdq method get_Lmdqh: " + str(get_Lmdqh))
            )
        )
    else:
        get_Lmdqh = get_Lmdqh
    # cf Methods.Simulation.LUTdq.get_Phidqh_mean
    if isinstance(get_Phidqh_mean, ImportError):
        get_Phidqh_mean = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LUTdq method get_Phidqh_mean: " + str(get_Phidqh_mean)
                )
            )
        )
    else:
        get_Phidqh_mean = get_Phidqh_mean
    # cf Methods.Simulation.LUTdq.get_Phidqh_mag
    if isinstance(get_Phidqh_mag, ImportError):
        get_Phidqh_mag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LUTdq method get_Phidqh_mag: " + str(get_Phidqh_mag)
                )
            )
        )
    else:
        get_Phidqh_mag = get_Phidqh_mag
    # cf Methods.Simulation.LUTdq.get_Phidqh_mag_mean
    if isinstance(get_Phidqh_mag_mean, ImportError):
        get_Phidqh_mag_mean = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LUTdq method get_Phidqh_mag_mean: "
                    + str(get_Phidqh_mag_mean)
                )
            )
        )
    else:
        get_Phidqh_mag_mean = get_Phidqh_mag_mean
    # cf Methods.Simulation.LUTdq.interp_Phi_dqh
    if isinstance(interp_Phi_dqh, ImportError):
        interp_Phi_dqh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LUTdq method interp_Phi_dqh: " + str(interp_Phi_dqh)
                )
            )
        )
    else:
        interp_Phi_dqh = interp_Phi_dqh
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Phi_dqh_mean=None,
        Tmag_ref=20,
        Phi_dqh_mag=None,
        Phi_wind=None,
        Phi_dqh_interp=None,
        R1=None,
        L1=None,
        T1_ref=20,
        OP_matrix=None,
        phase_dir=None,
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
            if "Phi_dqh_mean" in list(init_dict.keys()):
                Phi_dqh_mean = init_dict["Phi_dqh_mean"]
            if "Tmag_ref" in list(init_dict.keys()):
                Tmag_ref = init_dict["Tmag_ref"]
            if "Phi_dqh_mag" in list(init_dict.keys()):
                Phi_dqh_mag = init_dict["Phi_dqh_mag"]
            if "Phi_wind" in list(init_dict.keys()):
                Phi_wind = init_dict["Phi_wind"]
            if "Phi_dqh_interp" in list(init_dict.keys()):
                Phi_dqh_interp = init_dict["Phi_dqh_interp"]
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
        # Set the properties (value check and convertion are done in setter)
        self.Phi_dqh_mean = Phi_dqh_mean
        self.Tmag_ref = Tmag_ref
        self.Phi_dqh_mag = Phi_dqh_mag
        self.Phi_wind = Phi_wind
        self.Phi_dqh_interp = Phi_dqh_interp
        # Call LUT init
        super(LUTdq, self).__init__(
            R1=R1, L1=L1, T1_ref=T1_ref, OP_matrix=OP_matrix, phase_dir=phase_dir
        )
        # The class is frozen (in LUT init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LUTdq_str = ""
        # Get the properties inherited from LUT
        LUTdq_str += super(LUTdq, self).__str__()
        LUTdq_str += (
            "Phi_dqh_mean = "
            + linesep
            + str(self.Phi_dqh_mean).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        LUTdq_str += "Tmag_ref = " + str(self.Tmag_ref) + linesep
        LUTdq_str += "Phi_dqh_mag = " + str(self.Phi_dqh_mag) + linesep + linesep
        LUTdq_str += "Phi_wind = " + str(self.Phi_wind) + linesep + linesep
        LUTdq_str += "Phi_dqh_interp = " + str(self.Phi_dqh_interp) + linesep + linesep
        return LUTdq_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LUT
        if not super(LUTdq, self).__eq__(other):
            return False
        if not array_equal(other.Phi_dqh_mean, self.Phi_dqh_mean):
            return False
        if other.Tmag_ref != self.Tmag_ref:
            return False
        if other.Phi_dqh_mag != self.Phi_dqh_mag:
            return False
        if other.Phi_wind != self.Phi_wind:
            return False
        if other.Phi_dqh_interp != self.Phi_dqh_interp:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LUT
        diff_list.extend(super(LUTdq, self).compare(other, name=name))
        if not array_equal(other.Phi_dqh_mean, self.Phi_dqh_mean):
            diff_list.append(name + ".Phi_dqh_mean")
        if other._Tmag_ref != self._Tmag_ref:
            diff_list.append(name + ".Tmag_ref")
        if (other.Phi_dqh_mag is None and self.Phi_dqh_mag is not None) or (
            other.Phi_dqh_mag is not None and self.Phi_dqh_mag is None
        ):
            diff_list.append(name + ".Phi_dqh_mag None mismatch")
        elif self.Phi_dqh_mag is not None:
            diff_list.extend(
                self.Phi_dqh_mag.compare(other.Phi_dqh_mag, name=name + ".Phi_dqh_mag")
            )
        if (other.Phi_wind is None and self.Phi_wind is not None) or (
            other.Phi_wind is not None and self.Phi_wind is None
        ):
            diff_list.append(name + ".Phi_wind None mismatch")
        elif self.Phi_wind is None:
            pass
        elif len(other.Phi_wind) != len(self.Phi_wind):
            diff_list.append("len(" + name + ".Phi_wind)")
        else:
            for ii in range(len(other.Phi_wind)):
                diff_list.extend(
                    self.Phi_wind[ii].compare(
                        other.Phi_wind[ii], name=name + ".Phi_wind[" + str(ii) + "]"
                    )
                )
        if (other.Phi_dqh_interp is None and self.Phi_dqh_interp is not None) or (
            other.Phi_dqh_interp is not None and self.Phi_dqh_interp is None
        ):
            diff_list.append(name + ".Phi_dqh_interp None mismatch")
        elif (
            self.Phi_dqh_interp is not None
            and self.Phi_dqh_interp != other.Phi_dqh_interp
        ):
            diff_list.append(name + ".Phi_dqh_interp")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LUT
        S += super(LUTdq, self).__sizeof__()
        S += getsizeof(self.Phi_dqh_mean)
        S += getsizeof(self.Tmag_ref)
        S += getsizeof(self.Phi_dqh_mag)
        if self.Phi_wind is not None:
            for value in self.Phi_wind:
                S += getsizeof(value)
        S += getsizeof(self.Phi_dqh_interp)
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

        # Get the properties inherited from LUT
        LUTdq_dict = super(LUTdq, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.Phi_dqh_mean is None:
            LUTdq_dict["Phi_dqh_mean"] = None
        else:
            if type_handle_ndarray == 0:
                LUTdq_dict["Phi_dqh_mean"] = self.Phi_dqh_mean.tolist()
            elif type_handle_ndarray == 1:
                LUTdq_dict["Phi_dqh_mean"] = self.Phi_dqh_mean.copy()
            elif type_handle_ndarray == 2:
                LUTdq_dict["Phi_dqh_mean"] = self.Phi_dqh_mean
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        LUTdq_dict["Tmag_ref"] = self.Tmag_ref
        if self.Phi_dqh_mag is None:
            LUTdq_dict["Phi_dqh_mag"] = None
        else:
            LUTdq_dict["Phi_dqh_mag"] = self.Phi_dqh_mag.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Phi_wind is None:
            LUTdq_dict["Phi_wind"] = None
        else:
            LUTdq_dict["Phi_wind"] = list()
            for obj in self.Phi_wind:
                if obj is not None:
                    LUTdq_dict["Phi_wind"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    LUTdq_dict["Phi_wind"].append(None)
        if self.Phi_dqh_interp is None:
            LUTdq_dict["Phi_dqh_interp"] = None
        else:
            # Store serialized data (using cloudpickle) and str
            # to read it in json save files
            LUTdq_dict["Phi_dqh_interp"] = {
                "__class__": str(type(self._Phi_dqh_interp)),
                "__repr__": str(self._Phi_dqh_interp.__repr__()),
                "serialized": dumps(self._Phi_dqh_interp).decode("ISO-8859-2"),
            }
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LUTdq_dict["__class__"] = "LUTdq"
        return LUTdq_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Phi_dqh_mean = None
        self.Tmag_ref = None
        self.Phi_dqh_mag = None
        self.Phi_wind = None
        self.Phi_dqh_interp = None
        # Set to None the properties inherited from LUT
        super(LUTdq, self)._set_None()

    def _get_Phi_dqh_mean(self):
        """getter of Phi_dqh_mean"""
        return self._Phi_dqh_mean

    def _set_Phi_dqh_mean(self, value):
        """setter of Phi_dqh_mean"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Phi_dqh_mean", value, "ndarray")
        self._Phi_dqh_mean = value

    Phi_dqh_mean = property(
        fget=_get_Phi_dqh_mean,
        fset=_set_Phi_dqh_mean,
        doc=u"""RMS stator winding flux table in dqh frame (including magnets and currents given by I_dqh)

        :Type: ndarray
        """,
    )

    def _get_Tmag_ref(self):
        """getter of Tmag_ref"""
        return self._Tmag_ref

    def _set_Tmag_ref(self, value):
        """setter of Tmag_ref"""
        check_var("Tmag_ref", value, "float")
        self._Tmag_ref = value

    Tmag_ref = property(
        fget=_get_Tmag_ref,
        fset=_set_Tmag_ref,
        doc=u"""Magnet average temperature at which Phi_dqh is given

        :Type: float
        """,
    )

    def _get_Phi_dqh_mag(self):
        """getter of Phi_dqh_mag"""
        return self._Phi_dqh_mag

    def _set_Phi_dqh_mag(self, value):
        """setter of Phi_dqh_mag"""
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
                "SciDataTool.Classes", value.get("__class__"), "Phi_dqh_mag"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Phi_dqh_mag", value, "DataND")
        self._Phi_dqh_mag = value

    Phi_dqh_mag = property(
        fget=_get_Phi_dqh_mag,
        fset=_set_Phi_dqh_mag,
        doc=u"""RMS stator winding flux linkage spectrum in dqh frame including harmonics (only magnets)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Phi_wind(self):
        """getter of Phi_wind"""
        if self._Phi_wind is not None:
            for obj in self._Phi_wind:
                if obj is not None:
                    obj.parent = self
        return self._Phi_wind

    def _set_Phi_wind(self, value):
        """setter of Phi_wind"""
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
                        "SciDataTool.Classes", obj.get("__class__"), "Phi_wind"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("Phi_wind", value, "[DataND]")
        self._Phi_wind = value

    Phi_wind = property(
        fget=_get_Phi_wind,
        fset=_set_Phi_wind,
        doc=u"""Stator winding flux function of time and phases

        :Type: [SciDataTool.Classes.DataND.DataND]
        """,
    )

    def _get_Phi_dqh_interp(self):
        """getter of Phi_dqh_interp"""
        return self._Phi_dqh_interp

    def _set_Phi_dqh_interp(self, value):
        """setter of Phi_dqh_interp"""
        if value == -1:
            value = RegularGridInterpolator()
        check_var("Phi_dqh_interp", value, "RegularGridInterpolator")
        self._Phi_dqh_interp = value

    Phi_dqh_interp = property(
        fget=_get_Phi_dqh_interp,
        fset=_set_Phi_dqh_interp,
        doc=u"""Interpolant function of Phi_dqh

        :Type: scipy.interpolate.interpolate.RegularGridInterpolator
        """,
    )
