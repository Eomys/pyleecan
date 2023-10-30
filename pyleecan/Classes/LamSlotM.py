# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .LamSlot import LamSlot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotM.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSlotM.get_dim_active import get_dim_active
except ImportError as error:
    get_dim_active = error

try:
    from ..Methods.Machine.LamSlotM.get_magnet_number import get_magnet_number
except ImportError as error:
    get_magnet_number = error

try:
    from ..Methods.Machine.LamSlotM.plot import plot
except ImportError as error:
    plot = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class LamSlotM(LamSlot):
    """Lamination with Slot for Magnets"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotM.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotM method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSlotM.get_dim_active
    if isinstance(get_dim_active, ImportError):
        get_dim_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotM method get_dim_active: " + str(get_dim_active)
                )
            )
        )
    else:
        get_dim_active = get_dim_active
    # cf Methods.Machine.LamSlotM.get_magnet_number
    if isinstance(get_magnet_number, ImportError):
        get_magnet_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotM method get_magnet_number: "
                    + str(get_magnet_number)
                )
            )
        )
    else:
        get_magnet_number = get_magnet_number
    # cf Methods.Machine.LamSlotM.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotM method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mur_lin_matrix=None,
        Brm20_matrix=None,
        slot=-1,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=-1,
        notch=-1,
        skew=None,
        bore=None,
        yoke=None,
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
            if "mur_lin_matrix" in list(init_dict.keys()):
                mur_lin_matrix = init_dict["mur_lin_matrix"]
            if "Brm20_matrix" in list(init_dict.keys()):
                Brm20_matrix = init_dict["Brm20_matrix"]
            if "slot" in list(init_dict.keys()):
                slot = init_dict["slot"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
            if "skew" in list(init_dict.keys()):
                skew = init_dict["skew"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
            if "yoke" in list(init_dict.keys()):
                yoke = init_dict["yoke"]
        # Set the properties (value check and convertion are done in setter)
        self.mur_lin_matrix = mur_lin_matrix
        self.Brm20_matrix = Brm20_matrix
        # Call LamSlot init
        super(LamSlotM, self).__init__(
            slot=slot,
            L1=L1,
            mat_type=mat_type,
            Nrvd=Nrvd,
            Wrvd=Wrvd,
            Kf1=Kf1,
            is_internal=is_internal,
            Rint=Rint,
            Rext=Rext,
            is_stator=is_stator,
            axial_vent=axial_vent,
            notch=notch,
            skew=skew,
            bore=bore,
            yoke=yoke,
        )
        # The class is frozen (in LamSlot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSlotM_str = ""
        # Get the properties inherited from LamSlot
        LamSlotM_str += super(LamSlotM, self).__str__()
        LamSlotM_str += (
            "mur_lin_matrix = "
            + linesep
            + str(self.mur_lin_matrix).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        LamSlotM_str += (
            "Brm20_matrix = "
            + linesep
            + str(self.Brm20_matrix).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return LamSlotM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlot
        if not super(LamSlotM, self).__eq__(other):
            return False
        if not array_equal(other.mur_lin_matrix, self.mur_lin_matrix):
            return False
        if not array_equal(other.Brm20_matrix, self.Brm20_matrix):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LamSlot
        diff_list.extend(
            super(LamSlotM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if not array_equal(other.mur_lin_matrix, self.mur_lin_matrix):
            diff_list.append(name + ".mur_lin_matrix")
        if not array_equal(other.Brm20_matrix, self.Brm20_matrix):
            diff_list.append(name + ".Brm20_matrix")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlot
        S += super(LamSlotM, self).__sizeof__()
        S += getsizeof(self.mur_lin_matrix)
        S += getsizeof(self.Brm20_matrix)
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

        # Get the properties inherited from LamSlot
        LamSlotM_dict = super(LamSlotM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.mur_lin_matrix is None:
            LamSlotM_dict["mur_lin_matrix"] = None
        else:
            if type_handle_ndarray == 0:
                LamSlotM_dict["mur_lin_matrix"] = self.mur_lin_matrix.tolist()
            elif type_handle_ndarray == 1:
                LamSlotM_dict["mur_lin_matrix"] = self.mur_lin_matrix.copy()
            elif type_handle_ndarray == 2:
                LamSlotM_dict["mur_lin_matrix"] = self.mur_lin_matrix
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.Brm20_matrix is None:
            LamSlotM_dict["Brm20_matrix"] = None
        else:
            if type_handle_ndarray == 0:
                LamSlotM_dict["Brm20_matrix"] = self.Brm20_matrix.tolist()
            elif type_handle_ndarray == 1:
                LamSlotM_dict["Brm20_matrix"] = self.Brm20_matrix.copy()
            elif type_handle_ndarray == 2:
                LamSlotM_dict["Brm20_matrix"] = self.Brm20_matrix
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSlotM_dict["__class__"] = "LamSlotM"
        return LamSlotM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.mur_lin_matrix is None:
            mur_lin_matrix_val = None
        else:
            mur_lin_matrix_val = self.mur_lin_matrix.copy()
        if self.Brm20_matrix is None:
            Brm20_matrix_val = None
        else:
            Brm20_matrix_val = self.Brm20_matrix.copy()
        if self.slot is None:
            slot_val = None
        else:
            slot_val = self.slot.copy()
        L1_val = self.L1
        if self.mat_type is None:
            mat_type_val = None
        else:
            mat_type_val = self.mat_type.copy()
        Nrvd_val = self.Nrvd
        Wrvd_val = self.Wrvd
        Kf1_val = self.Kf1
        is_internal_val = self.is_internal
        Rint_val = self.Rint
        Rext_val = self.Rext
        is_stator_val = self.is_stator
        if self.axial_vent is None:
            axial_vent_val = None
        else:
            axial_vent_val = list()
            for obj in self.axial_vent:
                axial_vent_val.append(obj.copy())
        if self.notch is None:
            notch_val = None
        else:
            notch_val = list()
            for obj in self.notch:
                notch_val.append(obj.copy())
        if self.skew is None:
            skew_val = None
        else:
            skew_val = self.skew.copy()
        if self.bore is None:
            bore_val = None
        else:
            bore_val = self.bore.copy()
        if self.yoke is None:
            yoke_val = None
        else:
            yoke_val = self.yoke.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            mur_lin_matrix=mur_lin_matrix_val,
            Brm20_matrix=Brm20_matrix_val,
            slot=slot_val,
            L1=L1_val,
            mat_type=mat_type_val,
            Nrvd=Nrvd_val,
            Wrvd=Wrvd_val,
            Kf1=Kf1_val,
            is_internal=is_internal_val,
            Rint=Rint_val,
            Rext=Rext_val,
            is_stator=is_stator_val,
            axial_vent=axial_vent_val,
            notch=notch_val,
            skew=skew_val,
            bore=bore_val,
            yoke=yoke_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mur_lin_matrix = None
        self.Brm20_matrix = None
        # Set to None the properties inherited from LamSlot
        super(LamSlotM, self)._set_None()

    def _get_mur_lin_matrix(self):
        """getter of mur_lin_matrix"""
        return self._mur_lin_matrix

    def _set_mur_lin_matrix(self, value):
        """setter of mur_lin_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("mur_lin_matrix", value, "ndarray")
        self._mur_lin_matrix = value

    mur_lin_matrix = property(
        fget=_get_mur_lin_matrix,
        fset=_set_mur_lin_matrix,
        doc=u"""Matrix to enforce a different relative magnetic permeability for each magnet layer (shape: [Nrad, Ntan, Zs])

        :Type: ndarray
        """,
    )

    def _get_Brm20_matrix(self):
        """getter of Brm20_matrix"""
        return self._Brm20_matrix

    def _set_Brm20_matrix(self, value):
        """setter of Brm20_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Brm20_matrix", value, "ndarray")
        self._Brm20_matrix = value

    Brm20_matrix = property(
        fget=_get_Brm20_matrix,
        fset=_set_Brm20_matrix,
        doc=u"""Matrix to enforce a different magnet remanence induction at 20degC for each magnet layer (shape: [Nrad, Ntan, Zs])

        :Type: ndarray
        """,
    )
