# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleM61.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleM61
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
from .HoleMag import HoleMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleM61._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.HoleM61.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.HoleM61.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error

try:
    from ..Methods.Slot.HoleM61.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error

try:
    from ..Methods.Slot.HoleM61.comp_surface_magnet_id import comp_surface_magnet_id
except ImportError as error:
    comp_surface_magnet_id = error

try:
    from ..Methods.Slot.HoleM61.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.HoleM61.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.HoleM61.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.HoleM61.comp_magnetization_dict import comp_magnetization_dict
except ImportError as error:
    comp_magnetization_dict = error


from numpy import isnan
from ._check import InitUnKnowClassError


class HoleM61(HoleMag):
    """Hole M61"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleM61._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.HoleM61.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleM61.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method plot_schematics: " + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # cf Methods.Slot.HoleM61.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # cf Methods.Slot.HoleM61.comp_surface_magnet_id
    if isinstance(comp_surface_magnet_id, ImportError):
        comp_surface_magnet_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method comp_surface_magnet_id: "
                    + str(comp_surface_magnet_id)
                )
            )
        )
    else:
        comp_surface_magnet_id = comp_surface_magnet_id
    # cf Methods.Slot.HoleM61.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM61 method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.HoleM61.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM61 method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.HoleM61.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleM61 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.HoleM61.comp_magnetization_dict
    if isinstance(comp_magnetization_dict, ImportError):
        comp_magnetization_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleM61 method comp_magnetization_dict: "
                    + str(comp_magnetization_dict)
                )
            )
        )
    else:
        comp_magnetization_dict = comp_magnetization_dict
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=None,
        W1=None,
        W2=None,
        W3=None,
        H0=None,
        H1=None,
        H2=None,
        magnet_0=-1,
        magnet_1=-1,
        magnet_2=-1,
        magnet_3=-1,
        Zh=36,
        mat_void=-1,
        magnetization_dict_offset=None,
        Alpha0=0,
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
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "magnet_0" in list(init_dict.keys()):
                magnet_0 = init_dict["magnet_0"]
            if "magnet_1" in list(init_dict.keys()):
                magnet_1 = init_dict["magnet_1"]
            if "magnet_2" in list(init_dict.keys()):
                magnet_2 = init_dict["magnet_2"]
            if "magnet_3" in list(init_dict.keys()):
                magnet_3 = init_dict["magnet_3"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
            if "magnetization_dict_offset" in list(init_dict.keys()):
                magnetization_dict_offset = init_dict["magnetization_dict_offset"]
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.H0 = H0
        self.H1 = H1
        self.H2 = H2
        self.magnet_0 = magnet_0
        self.magnet_1 = magnet_1
        self.magnet_2 = magnet_2
        self.magnet_3 = magnet_3
        # Call HoleMag init
        super(HoleM61, self).__init__(
            Zh=Zh,
            mat_void=mat_void,
            magnetization_dict_offset=magnetization_dict_offset,
            Alpha0=Alpha0,
        )
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        HoleM61_str = ""
        # Get the properties inherited from HoleMag
        HoleM61_str += super(HoleM61, self).__str__()
        HoleM61_str += "W0 = " + str(self.W0) + linesep
        HoleM61_str += "W1 = " + str(self.W1) + linesep
        HoleM61_str += "W2 = " + str(self.W2) + linesep
        HoleM61_str += "W3 = " + str(self.W3) + linesep
        HoleM61_str += "H0 = " + str(self.H0) + linesep
        HoleM61_str += "H1 = " + str(self.H1) + linesep
        HoleM61_str += "H2 = " + str(self.H2) + linesep
        if self.magnet_0 is not None:
            tmp = self.magnet_0.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleM61_str += "magnet_0 = " + tmp
        else:
            HoleM61_str += "magnet_0 = None" + linesep + linesep
        if self.magnet_1 is not None:
            tmp = self.magnet_1.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleM61_str += "magnet_1 = " + tmp
        else:
            HoleM61_str += "magnet_1 = None" + linesep + linesep
        if self.magnet_2 is not None:
            tmp = self.magnet_2.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleM61_str += "magnet_2 = " + tmp
        else:
            HoleM61_str += "magnet_2 = None" + linesep + linesep
        if self.magnet_3 is not None:
            tmp = self.magnet_3.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            HoleM61_str += "magnet_3 = " + tmp
        else:
            HoleM61_str += "magnet_3 = None" + linesep + linesep
        return HoleM61_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleM61, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.W3 != self.W3:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.H2 != self.H2:
            return False
        if other.magnet_0 != self.magnet_0:
            return False
        if other.magnet_1 != self.magnet_1:
            return False
        if other.magnet_2 != self.magnet_2:
            return False
        if other.magnet_3 != self.magnet_3:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from HoleMag
        diff_list.extend(
            super(HoleM61, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._W0 is not None
            and self._W0 is not None
            and isnan(other._W0)
            and isnan(self._W0)
        ):
            pass
        elif other._W0 != self._W0:
            if is_add_value:
                val_str = " (self=" + str(self._W0) + ", other=" + str(other._W0) + ")"
                diff_list.append(name + ".W0" + val_str)
            else:
                diff_list.append(name + ".W0")
        if (
            other._W1 is not None
            and self._W1 is not None
            and isnan(other._W1)
            and isnan(self._W1)
        ):
            pass
        elif other._W1 != self._W1:
            if is_add_value:
                val_str = " (self=" + str(self._W1) + ", other=" + str(other._W1) + ")"
                diff_list.append(name + ".W1" + val_str)
            else:
                diff_list.append(name + ".W1")
        if (
            other._W2 is not None
            and self._W2 is not None
            and isnan(other._W2)
            and isnan(self._W2)
        ):
            pass
        elif other._W2 != self._W2:
            if is_add_value:
                val_str = " (self=" + str(self._W2) + ", other=" + str(other._W2) + ")"
                diff_list.append(name + ".W2" + val_str)
            else:
                diff_list.append(name + ".W2")
        if (
            other._W3 is not None
            and self._W3 is not None
            and isnan(other._W3)
            and isnan(self._W3)
        ):
            pass
        elif other._W3 != self._W3:
            if is_add_value:
                val_str = " (self=" + str(self._W3) + ", other=" + str(other._W3) + ")"
                diff_list.append(name + ".W3" + val_str)
            else:
                diff_list.append(name + ".W3")
        if (
            other._H0 is not None
            and self._H0 is not None
            and isnan(other._H0)
            and isnan(self._H0)
        ):
            pass
        elif other._H0 != self._H0:
            if is_add_value:
                val_str = " (self=" + str(self._H0) + ", other=" + str(other._H0) + ")"
                diff_list.append(name + ".H0" + val_str)
            else:
                diff_list.append(name + ".H0")
        if (
            other._H1 is not None
            and self._H1 is not None
            and isnan(other._H1)
            and isnan(self._H1)
        ):
            pass
        elif other._H1 != self._H1:
            if is_add_value:
                val_str = " (self=" + str(self._H1) + ", other=" + str(other._H1) + ")"
                diff_list.append(name + ".H1" + val_str)
            else:
                diff_list.append(name + ".H1")
        if (
            other._H2 is not None
            and self._H2 is not None
            and isnan(other._H2)
            and isnan(self._H2)
        ):
            pass
        elif other._H2 != self._H2:
            if is_add_value:
                val_str = " (self=" + str(self._H2) + ", other=" + str(other._H2) + ")"
                diff_list.append(name + ".H2" + val_str)
            else:
                diff_list.append(name + ".H2")
        if (other.magnet_0 is None and self.magnet_0 is not None) or (
            other.magnet_0 is not None and self.magnet_0 is None
        ):
            diff_list.append(name + ".magnet_0 None mismatch")
        elif self.magnet_0 is not None:
            diff_list.extend(
                self.magnet_0.compare(
                    other.magnet_0,
                    name=name + ".magnet_0",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.magnet_1 is None and self.magnet_1 is not None) or (
            other.magnet_1 is not None and self.magnet_1 is None
        ):
            diff_list.append(name + ".magnet_1 None mismatch")
        elif self.magnet_1 is not None:
            diff_list.extend(
                self.magnet_1.compare(
                    other.magnet_1,
                    name=name + ".magnet_1",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.magnet_2 is None and self.magnet_2 is not None) or (
            other.magnet_2 is not None and self.magnet_2 is None
        ):
            diff_list.append(name + ".magnet_2 None mismatch")
        elif self.magnet_2 is not None:
            diff_list.extend(
                self.magnet_2.compare(
                    other.magnet_2,
                    name=name + ".magnet_2",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.magnet_3 is None and self.magnet_3 is not None) or (
            other.magnet_3 is not None and self.magnet_3 is None
        ):
            diff_list.append(name + ".magnet_3 None mismatch")
        elif self.magnet_3 is not None:
            diff_list.extend(
                self.magnet_3.compare(
                    other.magnet_3,
                    name=name + ".magnet_3",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from HoleMag
        S += super(HoleM61, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.W1)
        S += getsizeof(self.W2)
        S += getsizeof(self.W3)
        S += getsizeof(self.H0)
        S += getsizeof(self.H1)
        S += getsizeof(self.H2)
        S += getsizeof(self.magnet_0)
        S += getsizeof(self.magnet_1)
        S += getsizeof(self.magnet_2)
        S += getsizeof(self.magnet_3)
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

        # Get the properties inherited from HoleMag
        HoleM61_dict = super(HoleM61, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        HoleM61_dict["W0"] = self.W0
        HoleM61_dict["W1"] = self.W1
        HoleM61_dict["W2"] = self.W2
        HoleM61_dict["W3"] = self.W3
        HoleM61_dict["H0"] = self.H0
        HoleM61_dict["H1"] = self.H1
        HoleM61_dict["H2"] = self.H2
        if self.magnet_0 is None:
            HoleM61_dict["magnet_0"] = None
        else:
            HoleM61_dict["magnet_0"] = self.magnet_0.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.magnet_1 is None:
            HoleM61_dict["magnet_1"] = None
        else:
            HoleM61_dict["magnet_1"] = self.magnet_1.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.magnet_2 is None:
            HoleM61_dict["magnet_2"] = None
        else:
            HoleM61_dict["magnet_2"] = self.magnet_2.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.magnet_3 is None:
            HoleM61_dict["magnet_3"] = None
        else:
            HoleM61_dict["magnet_3"] = self.magnet_3.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        HoleM61_dict["__class__"] = "HoleM61"
        return HoleM61_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        W0_val = self.W0
        W1_val = self.W1
        W2_val = self.W2
        W3_val = self.W3
        H0_val = self.H0
        H1_val = self.H1
        H2_val = self.H2
        if self.magnet_0 is None:
            magnet_0_val = None
        else:
            magnet_0_val = self.magnet_0.copy()
        if self.magnet_1 is None:
            magnet_1_val = None
        else:
            magnet_1_val = self.magnet_1.copy()
        if self.magnet_2 is None:
            magnet_2_val = None
        else:
            magnet_2_val = self.magnet_2.copy()
        if self.magnet_3 is None:
            magnet_3_val = None
        else:
            magnet_3_val = self.magnet_3.copy()
        Zh_val = self.Zh
        if self.mat_void is None:
            mat_void_val = None
        else:
            mat_void_val = self.mat_void.copy()
        if self.magnetization_dict_offset is None:
            magnetization_dict_offset_val = None
        else:
            magnetization_dict_offset_val = self.magnetization_dict_offset.copy()
        Alpha0_val = self.Alpha0
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            W0=W0_val,
            W1=W1_val,
            W2=W2_val,
            W3=W3_val,
            H0=H0_val,
            H1=H1_val,
            H2=H2_val,
            magnet_0=magnet_0_val,
            magnet_1=magnet_1_val,
            magnet_2=magnet_2_val,
            magnet_3=magnet_3_val,
            Zh=Zh_val,
            mat_void=mat_void_val,
            magnetization_dict_offset=magnetization_dict_offset_val,
            Alpha0=Alpha0_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.W1 = None
        self.W2 = None
        self.W3 = None
        self.H0 = None
        self.H1 = None
        self.H2 = None
        if self.magnet_0 is not None:
            self.magnet_0._set_None()
        if self.magnet_1 is not None:
            self.magnet_1._set_None()
        if self.magnet_2 is not None:
            self.magnet_2._set_None()
        if self.magnet_3 is not None:
            self.magnet_3._set_None()
        # Set to None the properties inherited from HoleMag
        super(HoleM61, self)._set_None()

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
        doc=u"""Distance beetween two Hole

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
        doc=u"""Magnet width

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
        doc=u"""Tooth width

        :Type: float
        :min: 0
        """,
    )

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
        doc=u"""Distance from the lamination bore

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
        doc=u"""Magnet height

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
        doc=u"""Distance beetween the lamination bore and top of the slot

        :Type: float
        :min: 0
        """,
    )

    def _get_magnet_0(self):
        """getter of magnet_0"""
        return self._magnet_0

    def _set_magnet_0(self, value):
        """setter of magnet_0"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_0"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_0")
            value = Magnet()
        check_var("magnet_0", value, "Magnet")
        self._magnet_0 = value

        if self._magnet_0 is not None:
            self._magnet_0.parent = self

    magnet_0 = property(
        fget=_get_magnet_0,
        fset=_set_magnet_0,
        doc=u"""First Magnet

        :Type: Magnet
        """,
    )

    def _get_magnet_1(self):
        """getter of magnet_1"""
        return self._magnet_1

    def _set_magnet_1(self, value):
        """setter of magnet_1"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_1"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_1")
            value = Magnet()
        check_var("magnet_1", value, "Magnet")
        self._magnet_1 = value

        if self._magnet_1 is not None:
            self._magnet_1.parent = self

    magnet_1 = property(
        fget=_get_magnet_1,
        fset=_set_magnet_1,
        doc=u"""Second Magnet

        :Type: Magnet
        """,
    )

    def _get_magnet_2(self):
        """getter of magnet_2"""
        return self._magnet_2

    def _set_magnet_2(self, value):
        """setter of magnet_2"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_2"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_2")
            value = Magnet()
        check_var("magnet_2", value, "Magnet")
        self._magnet_2 = value

        if self._magnet_2 is not None:
            self._magnet_2.parent = self

    magnet_2 = property(
        fget=_get_magnet_2,
        fset=_set_magnet_2,
        doc=u"""Third Magnet

        :Type: Magnet
        """,
    )

    def _get_magnet_3(self):
        """getter of magnet_3"""
        return self._magnet_3

    def _set_magnet_3(self, value):
        """setter of magnet_3"""
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
                "pyleecan.Classes", value.get("__class__"), "magnet_3"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class("pyleecan.Classes", "Magnet", "magnet_3")
            value = Magnet()
        check_var("magnet_3", value, "Magnet")
        self._magnet_3 = value

        if self._magnet_3 is not None:
            self._magnet_3.parent = self

    magnet_3 = property(
        fget=_get_magnet_3,
        fset=_set_magnet_3,
        doc=u"""Fourth Magnet

        :Type: Magnet
        """,
    )
