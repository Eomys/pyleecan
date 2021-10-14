# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Machine.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Machine
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.Machine.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.Machine.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.Machine.comp_angle_offset_initial import (
        comp_angle_offset_initial,
    )
except ImportError as error:
    comp_angle_offset_initial = error

try:
    from ..Methods.Machine.Machine.comp_desc_dict import comp_desc_dict
except ImportError as error:
    comp_desc_dict = error

try:
    from ..Methods.Machine.Machine.comp_length_airgap_active import (
        comp_length_airgap_active,
    )
except ImportError as error:
    comp_length_airgap_active = error

try:
    from ..Methods.Machine.Machine.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.Machine.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from ..Methods.Machine.Machine.comp_Rgap_mec import comp_Rgap_mec
except ImportError as error:
    comp_Rgap_mec = error

try:
    from ..Methods.Machine.Machine.comp_periodicity import comp_periodicity
except ImportError as error:
    comp_periodicity = error

try:
    from ..Methods.Machine.Machine.comp_width_airgap_mag import comp_width_airgap_mag
except ImportError as error:
    comp_width_airgap_mag = error

try:
    from ..Methods.Machine.Machine.comp_width_airgap_mec import comp_width_airgap_mec
except ImportError as error:
    comp_width_airgap_mec = error

try:
    from ..Methods.Machine.Machine.get_material_dict import get_material_dict
except ImportError as error:
    get_material_dict = error

try:
    from ..Methods.Machine.Machine.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error

try:
    from ..Methods.Machine.Machine.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.Machine.plot_anim_rotor import plot_anim_rotor
except ImportError as error:
    plot_anim_rotor = error

try:
    from ..Methods.Machine.Machine.get_lam_list import get_lam_list
except ImportError as error:
    get_lam_list = error

try:
    from ..Methods.Machine.Machine.get_lam_list_label import get_lam_list_label
except ImportError as error:
    get_lam_list_label = error

try:
    from ..Methods.Machine.Machine.get_lam_by_label import get_lam_by_label
except ImportError as error:
    get_lam_by_label = error

try:
    from ..Methods.Machine.Machine.get_lam_index import get_lam_index
except ImportError as error:
    get_lam_index = error

try:
    from ..Methods.Machine.Machine.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.Machine.set_pole_pair_number import set_pole_pair_number
except ImportError as error:
    set_pole_pair_number = error


from ._check import InitUnKnowClassError
from .Frame import Frame
from .Shaft import Shaft


class Machine(FrozenClass):
    """Abstract class for machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Machine.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.Machine.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.Machine.comp_angle_offset_initial
    if isinstance(comp_angle_offset_initial, ImportError):
        comp_angle_offset_initial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_angle_offset_initial: "
                    + str(comp_angle_offset_initial)
                )
            )
        )
    else:
        comp_angle_offset_initial = comp_angle_offset_initial
    # cf Methods.Machine.Machine.comp_desc_dict
    if isinstance(comp_desc_dict, ImportError):
        comp_desc_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_desc_dict: " + str(comp_desc_dict)
                )
            )
        )
    else:
        comp_desc_dict = comp_desc_dict
    # cf Methods.Machine.Machine.comp_length_airgap_active
    if isinstance(comp_length_airgap_active, ImportError):
        comp_length_airgap_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_length_airgap_active: "
                    + str(comp_length_airgap_active)
                )
            )
        )
    else:
        comp_length_airgap_active = comp_length_airgap_active
    # cf Methods.Machine.Machine.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method comp_masses: " + str(comp_masses))
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.Machine.comp_output_geo
    if isinstance(comp_output_geo, ImportError):
        comp_output_geo = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_output_geo: " + str(comp_output_geo)
                )
            )
        )
    else:
        comp_output_geo = comp_output_geo
    # cf Methods.Machine.Machine.comp_Rgap_mec
    if isinstance(comp_Rgap_mec, ImportError):
        comp_Rgap_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_Rgap_mec: " + str(comp_Rgap_mec)
                )
            )
        )
    else:
        comp_Rgap_mec = comp_Rgap_mec
    # cf Methods.Machine.Machine.comp_periodicity
    if isinstance(comp_periodicity, ImportError):
        comp_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_periodicity: "
                    + str(comp_periodicity)
                )
            )
        )
    else:
        comp_periodicity = comp_periodicity
    # cf Methods.Machine.Machine.comp_width_airgap_mag
    if isinstance(comp_width_airgap_mag, ImportError):
        comp_width_airgap_mag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_width_airgap_mag: "
                    + str(comp_width_airgap_mag)
                )
            )
        )
    else:
        comp_width_airgap_mag = comp_width_airgap_mag
    # cf Methods.Machine.Machine.comp_width_airgap_mec
    if isinstance(comp_width_airgap_mec, ImportError):
        comp_width_airgap_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method comp_width_airgap_mec: "
                    + str(comp_width_airgap_mec)
                )
            )
        )
    else:
        comp_width_airgap_mec = comp_width_airgap_mec
    # cf Methods.Machine.Machine.get_material_dict
    if isinstance(get_material_dict, ImportError):
        get_material_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_material_dict: "
                    + str(get_material_dict)
                )
            )
        )
    else:
        get_material_dict = get_material_dict
    # cf Methods.Machine.Machine.get_polar_eq
    if isinstance(get_polar_eq, ImportError):
        get_polar_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_polar_eq: " + str(get_polar_eq)
                )
            )
        )
    else:
        get_polar_eq = get_polar_eq
    # cf Methods.Machine.Machine.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.Machine.plot_anim_rotor
    if isinstance(plot_anim_rotor, ImportError):
        plot_anim_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method plot_anim_rotor: " + str(plot_anim_rotor)
                )
            )
        )
    else:
        plot_anim_rotor = plot_anim_rotor
    # cf Methods.Machine.Machine.get_lam_list
    if isinstance(get_lam_list, ImportError):
        get_lam_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lam_list: " + str(get_lam_list)
                )
            )
        )
    else:
        get_lam_list = get_lam_list
    # cf Methods.Machine.Machine.get_lam_list_label
    if isinstance(get_lam_list_label, ImportError):
        get_lam_list_label = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lam_list_label: "
                    + str(get_lam_list_label)
                )
            )
        )
    else:
        get_lam_list_label = get_lam_list_label
    # cf Methods.Machine.Machine.get_lam_by_label
    if isinstance(get_lam_by_label, ImportError):
        get_lam_by_label = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lam_by_label: "
                    + str(get_lam_by_label)
                )
            )
        )
    else:
        get_lam_by_label = get_lam_by_label
    # cf Methods.Machine.Machine.get_lam_index
    if isinstance(get_lam_index, ImportError):
        get_lam_index = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lam_index: " + str(get_lam_index)
                )
            )
        )
    else:
        get_lam_index = get_lam_index
    # cf Methods.Machine.Machine.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.Machine.set_pole_pair_number
    if isinstance(set_pole_pair_number, ImportError):
        set_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method set_pole_pair_number: "
                    + str(set_pole_pair_number)
                )
            )
        )
    else:
        set_pole_pair_number = set_pole_pair_number
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
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
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.frame = frame
        self.shaft = shaft
        self.name = name
        self.desc = desc
        self.type_machine = type_machine
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Machine_str = ""
        if self.parent is None:
            Machine_str += "parent = None " + linesep
        else:
            Machine_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.frame is not None:
            tmp = self.frame.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Machine_str += "frame = " + tmp
        else:
            Machine_str += "frame = None" + linesep + linesep
        if self.shaft is not None:
            tmp = self.shaft.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Machine_str += "shaft = " + tmp
        else:
            Machine_str += "shaft = None" + linesep + linesep
        Machine_str += 'name = "' + str(self.name) + '"' + linesep
        Machine_str += 'desc = "' + str(self.desc) + '"' + linesep
        Machine_str += "type_machine = " + str(self.type_machine) + linesep
        Machine_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return Machine_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.frame != self.frame:
            return False
        if other.shaft != self.shaft:
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        if other.type_machine != self.type_machine:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.frame is None and self.frame is not None) or (
            other.frame is not None and self.frame is None
        ):
            diff_list.append(name + ".frame None mismatch")
        elif self.frame is not None:
            diff_list.extend(self.frame.compare(other.frame, name=name + ".frame"))
        if (other.shaft is None and self.shaft is not None) or (
            other.shaft is not None and self.shaft is None
        ):
            diff_list.append(name + ".shaft None mismatch")
        elif self.shaft is not None:
            diff_list.extend(self.shaft.compare(other.shaft, name=name + ".shaft"))
        if other._name != self._name:
            diff_list.append(name + ".name")
        if other._desc != self._desc:
            diff_list.append(name + ".desc")
        if other._type_machine != self._type_machine:
            diff_list.append(name + ".type_machine")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.frame)
        S += getsizeof(self.shaft)
        S += getsizeof(self.name)
        S += getsizeof(self.desc)
        S += getsizeof(self.type_machine)
        S += getsizeof(self.logger_name)
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

        Machine_dict = dict()
        if self.frame is None:
            Machine_dict["frame"] = None
        else:
            Machine_dict["frame"] = self.frame.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.shaft is None:
            Machine_dict["shaft"] = None
        else:
            Machine_dict["shaft"] = self.shaft.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Machine_dict["name"] = self.name
        Machine_dict["desc"] = self.desc
        Machine_dict["type_machine"] = self.type_machine
        Machine_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        Machine_dict["__class__"] = "Machine"
        return Machine_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.frame is not None:
            self.frame._set_None()
        if self.shaft is not None:
            self.shaft._set_None()
        self.name = None
        self.desc = None
        self.type_machine = None
        self.logger_name = None

    def _get_frame(self):
        """getter of frame"""
        return self._frame

    def _set_frame(self, value):
        """setter of frame"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "frame"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Frame()
        check_var("frame", value, "Frame")
        self._frame = value

        if self._frame is not None:
            self._frame.parent = self

    frame = property(
        fget=_get_frame,
        fset=_set_frame,
        doc=u"""Machine's Frame

        :Type: Frame
        """,
    )

    def _get_shaft(self):
        """getter of shaft"""
        return self._shaft

    def _set_shaft(self, value):
        """setter of shaft"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "shaft"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Shaft()
        check_var("shaft", value, "Shaft")
        self._shaft = value

        if self._shaft is not None:
            self._shaft.parent = self

    shaft = property(
        fget=_get_shaft,
        fset=_set_shaft,
        doc=u"""Machine's Shaft

        :Type: Shaft
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the machine

        :Type: str
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""Machine description

        :Type: str
        """,
    )

    def _get_type_machine(self):
        """getter of type_machine"""
        return self._type_machine

    def _set_type_machine(self, value):
        """setter of type_machine"""
        check_var("type_machine", value, "int")
        self._type_machine = value

    type_machine = property(
        fget=_get_type_machine,
        fset=_set_type_machine,
        doc=u"""Integer to store the machine type (for the GUI, should be replaced by a test of the object type)

        :Type: int
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )
