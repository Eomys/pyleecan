# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/Machine.csv
WARNING! All changes made in this file will be lost!
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
    from ..Methods.Machine.Machine.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.Machine.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.Machine.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.Machine.comp_width_airgap_mag import comp_width_airgap_mag
except ImportError as error:
    comp_width_airgap_mag = error

try:
    from ..Methods.Machine.Machine.comp_width_airgap_mec import comp_width_airgap_mec
except ImportError as error:
    comp_width_airgap_mec = error

try:
    from ..Methods.Machine.Machine.get_lamination import get_lamination
except ImportError as error:
    get_lamination = error

try:
    from ..Methods.Machine.Machine.comp_Rgap_mec import comp_Rgap_mec
except ImportError as error:
    comp_Rgap_mec = error

try:
    from ..Methods.Machine.Machine.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.Machine.comp_output_geo import comp_output_geo
except ImportError as error:
    comp_output_geo = error

try:
    from ..Methods.Machine.Machine.comp_length_airgap_active import (
        comp_length_airgap_active,
    )
except ImportError as error:
    comp_length_airgap_active = error

try:
    from ..Methods.Machine.Machine.get_polar_eq import get_polar_eq
except ImportError as error:
    get_polar_eq = error

try:
    from ..Methods.Machine.Machine.plot_anim_rotor import plot_anim_rotor
except ImportError as error:
    plot_anim_rotor = error

try:
    from ..Methods.Machine.Machine.get_material_list import get_material_list
except ImportError as error:
    get_material_list = error

try:
    from ..Methods.Machine.Machine.comp_sym import comp_sym
except ImportError as error:
    comp_sym = error

try:
    from ..Methods.Machine.Machine.comp_desc_dict import comp_desc_dict
except ImportError as error:
    comp_desc_dict = error


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
    # cf Methods.Machine.Machine.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method comp_masses: " + str(comp_masses))
            )
        )
    else:
        comp_masses = comp_masses
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
    # cf Methods.Machine.Machine.get_lamination
    if isinstance(get_lamination, ImportError):
        get_lamination = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_lamination: " + str(get_lamination)
                )
            )
        )
    else:
        get_lamination = get_lamination
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
    # cf Methods.Machine.Machine.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method plot: " + str(plot))
            )
        )
    else:
        plot = plot
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
    # cf Methods.Machine.Machine.get_material_list
    if isinstance(get_material_list, ImportError):
        get_material_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine method get_material_list: "
                    + str(get_material_list)
                )
            )
        )
    else:
        get_material_list = get_material_list
    # cf Methods.Machine.Machine.comp_sym
    if isinstance(comp_sym, ImportError):
        comp_sym = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine method comp_sym: " + str(comp_sym))
            )
        )
    else:
        comp_sym = comp_sym
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
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            frame = obj.frame
            shaft = obj.shaft
            name = obj.name
            desc = obj.desc
            type_machine = obj.type_machine
            logger_name = obj.logger_name
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
        # Initialisation by argument
        self.parent = None
        # frame can be None, a Frame object or a dict
        if isinstance(frame, dict):
            self.frame = Frame(init_dict=frame)
        elif isinstance(frame, str):
            from ..Functions.load import load

            self.frame = load(frame)
        else:
            self.frame = frame
        # shaft can be None, a Shaft object or a dict
        if isinstance(shaft, dict):
            self.shaft = Shaft(init_dict=shaft)
        elif isinstance(shaft, str):
            from ..Functions.load import load

            self.shaft = load(shaft)
        else:
            self.shaft = shaft
        self.name = name
        self.desc = desc
        self.type_machine = type_machine
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Machine_dict = dict()
        if self.frame is None:
            Machine_dict["frame"] = None
        else:
            Machine_dict["frame"] = self.frame.as_dict()
        if self.shaft is None:
            Machine_dict["shaft"] = None
        else:
            Machine_dict["shaft"] = self.shaft.as_dict()
        Machine_dict["name"] = self.name
        Machine_dict["desc"] = self.desc
        Machine_dict["type_machine"] = self.type_machine
        Machine_dict["logger_name"] = self.logger_name
        # The class name is added to the dict fordeserialisation purpose
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
        check_var("frame", value, "Frame")
        self._frame = value

        if self._frame is not None:
            self._frame.parent = self

    # Machine's Frame
    # Type : Frame
    frame = property(fget=_get_frame, fset=_set_frame, doc=u"""Machine's Frame""")

    def _get_shaft(self):
        """getter of shaft"""
        return self._shaft

    def _set_shaft(self, value):
        """setter of shaft"""
        check_var("shaft", value, "Shaft")
        self._shaft = value

        if self._shaft is not None:
            self._shaft.parent = self

    # Machine's Shaft
    # Type : Shaft
    shaft = property(fget=_get_shaft, fset=_set_shaft, doc=u"""Machine's Shaft""")

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the machine
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the machine""")

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    # Machine description
    # Type : str
    desc = property(fget=_get_desc, fset=_set_desc, doc=u"""Machine description""")

    def _get_type_machine(self):
        """getter of type_machine"""
        return self._type_machine

    def _set_type_machine(self, value):
        """setter of type_machine"""
        check_var("type_machine", value, "int")
        self._type_machine = value

    # Integer to store the machine type (for the GUI, should be replaced by a test of the object type)
    # Type : int
    type_machine = property(
        fget=_get_type_machine,
        fset=_set_type_machine,
        doc=u"""Integer to store the machine type (for the GUI, should be replaced by a test of the object type)""",
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    # Name of the logger to use
    # Type : str
    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use""",
    )
