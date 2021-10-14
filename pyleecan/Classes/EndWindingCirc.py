# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/EndWindingCirc.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/EndWindingCirc
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
from .EndWinding import EndWinding

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.EndWindingCirc.comp_length_endwinding import (
        comp_length_endwinding,
    )
except ImportError as error:
    comp_length_endwinding = error


from ._check import InitUnKnowClassError


class EndWindingCirc(EndWinding):
    """Class of the machine's end winding assuming a circular shape"""

    VERSION = 1

    # cf Methods.Machine.EndWindingCirc.comp_length_endwinding
    if isinstance(comp_length_endwinding, ImportError):
        comp_length_endwinding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EndWindingCirc method comp_length_endwinding: "
                    + str(comp_length_endwinding)
                )
            )
        )
    else:
        comp_length_endwinding = comp_length_endwinding
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, coil_pitch=None, init_dict=None, init_str=None):
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
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
        # Set the properties (value check and convertion are done in setter)
        self.coil_pitch = coil_pitch
        # Call EndWinding init
        super(EndWindingCirc, self).__init__()
        # The class is frozen (in EndWinding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EndWindingCirc_str = ""
        # Get the properties inherited from EndWinding
        EndWindingCirc_str += super(EndWindingCirc, self).__str__()
        EndWindingCirc_str += "coil_pitch = " + str(self.coil_pitch) + linesep
        return EndWindingCirc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EndWinding
        if not super(EndWindingCirc, self).__eq__(other):
            return False
        if other.coil_pitch != self.coil_pitch:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EndWinding
        diff_list.extend(super(EndWindingCirc, self).compare(other, name=name))
        if other._coil_pitch != self._coil_pitch:
            diff_list.append(name + ".coil_pitch")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EndWinding
        S += super(EndWindingCirc, self).__sizeof__()
        S += getsizeof(self.coil_pitch)
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

        # Get the properties inherited from EndWinding
        EndWindingCirc_dict = super(EndWindingCirc, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        EndWindingCirc_dict["coil_pitch"] = self.coil_pitch
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EndWindingCirc_dict["__class__"] = "EndWindingCirc"
        return EndWindingCirc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coil_pitch = None
        # Set to None the properties inherited from EndWinding
        super(EndWindingCirc, self)._set_None()

    def _get_coil_pitch(self):
        """getter of coil_pitch"""
        return self._coil_pitch

    def _set_coil_pitch(self, value):
        """setter of coil_pitch"""
        check_var("coil_pitch", value, "float")
        self._coil_pitch = value

    coil_pitch = property(
        fget=_get_coil_pitch,
        fset=_set_coil_pitch,
        doc=u"""effective coil pitch (override) for length calculation

        :Type: float
        """,
    )
