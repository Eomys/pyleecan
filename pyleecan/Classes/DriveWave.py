# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/DriveWave.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/DriveWave
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
from .Drive import Drive

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.DriveWave.get_wave import get_wave
except ImportError as error:
    get_wave = error


from ._check import InitUnKnowClassError
from .Import import Import


class DriveWave(Drive):
    """Drive to generate a wave according to an Import object"""

    VERSION = 1

    # cf Methods.Simulation.DriveWave.get_wave
    if isinstance(get_wave, ImportError):
        get_wave = property(
            fget=lambda x: raise_(
                ImportError("Can't use DriveWave method get_wave: " + str(get_wave))
            )
        )
    else:
        get_wave = get_wave
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        wave=-1,
        Umax=800,
        Imax=800,
        is_current=False,
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
            if "wave" in list(init_dict.keys()):
                wave = init_dict["wave"]
            if "Umax" in list(init_dict.keys()):
                Umax = init_dict["Umax"]
            if "Imax" in list(init_dict.keys()):
                Imax = init_dict["Imax"]
            if "is_current" in list(init_dict.keys()):
                is_current = init_dict["is_current"]
        # Set the properties (value check and convertion are done in setter)
        self.wave = wave
        # Call Drive init
        super(DriveWave, self).__init__(Umax=Umax, Imax=Imax, is_current=is_current)
        # The class is frozen (in Drive init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        DriveWave_str = ""
        # Get the properties inherited from Drive
        DriveWave_str += super(DriveWave, self).__str__()
        if self.wave is not None:
            tmp = self.wave.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            DriveWave_str += "wave = " + tmp
        else:
            DriveWave_str += "wave = None" + linesep + linesep
        return DriveWave_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Drive
        if not super(DriveWave, self).__eq__(other):
            return False
        if other.wave != self.wave:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Drive
        diff_list.extend(super(DriveWave, self).compare(other, name=name))
        if (other.wave is None and self.wave is not None) or (
            other.wave is not None and self.wave is None
        ):
            diff_list.append(name + ".wave None mismatch")
        elif self.wave is not None:
            diff_list.extend(self.wave.compare(other.wave, name=name + ".wave"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Drive
        S += super(DriveWave, self).__sizeof__()
        S += getsizeof(self.wave)
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

        # Get the properties inherited from Drive
        DriveWave_dict = super(DriveWave, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.wave is None:
            DriveWave_dict["wave"] = None
        else:
            DriveWave_dict["wave"] = self.wave.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        DriveWave_dict["__class__"] = "DriveWave"
        return DriveWave_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.wave is not None:
            self.wave._set_None()
        # Set to None the properties inherited from Drive
        super(DriveWave, self)._set_None()

    def _get_wave(self):
        """getter of wave"""
        return self._wave

    def _set_wave(self, value):
        """setter of wave"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "wave")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Import()
        check_var("wave", value, "Import")
        self._wave = value

        if self._wave is not None:
            self._wave.parent = self

    wave = property(
        fget=_get_wave,
        fset=_set_wave,
        doc=u"""Wave generator

        :Type: Import
        """,
    )
