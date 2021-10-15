# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/FrameBar.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/FrameBar
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
from .Frame import Frame

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.FrameBar.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.FrameBar.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.FrameBar.comp_height_gap import comp_height_gap
except ImportError as error:
    comp_height_gap = error

try:
    from ..Methods.Machine.FrameBar.build_geometry_bar import build_geometry_bar
except ImportError as error:
    build_geometry_bar = error

try:
    from ..Methods.Machine.FrameBar.comp_surface_bar import comp_surface_bar
except ImportError as error:
    comp_surface_bar = error

try:
    from ..Methods.Machine.FrameBar.comp_surface_gap import comp_surface_gap
except ImportError as error:
    comp_surface_gap = error


from ._check import InitUnKnowClassError
from .Material import Material


class FrameBar(Frame):
    """machine frame with polar structural bars between frame and outer lamination"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.FrameBar.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.FrameBar.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.FrameBar.comp_height_gap
    if isinstance(comp_height_gap, ImportError):
        comp_height_gap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method comp_height_gap: " + str(comp_height_gap)
                )
            )
        )
    else:
        comp_height_gap = comp_height_gap
    # cf Methods.Machine.FrameBar.build_geometry_bar
    if isinstance(build_geometry_bar, ImportError):
        build_geometry_bar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method build_geometry_bar: "
                    + str(build_geometry_bar)
                )
            )
        )
    else:
        build_geometry_bar = build_geometry_bar
    # cf Methods.Machine.FrameBar.comp_surface_bar
    if isinstance(comp_surface_bar, ImportError):
        comp_surface_bar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method comp_surface_bar: "
                    + str(comp_surface_bar)
                )
            )
        )
    else:
        comp_surface_bar = comp_surface_bar
    # cf Methods.Machine.FrameBar.comp_surface_gap
    if isinstance(comp_surface_gap, ImportError):
        comp_surface_gap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FrameBar method comp_surface_gap: "
                    + str(comp_surface_gap)
                )
            )
        )
    else:
        comp_surface_gap = comp_surface_gap
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Nbar=8,
        wbar=0.01,
        Lfra=0.35,
        Rint=0.2,
        Rext=0.2,
        mat_type=-1,
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
            if "Nbar" in list(init_dict.keys()):
                Nbar = init_dict["Nbar"]
            if "wbar" in list(init_dict.keys()):
                wbar = init_dict["wbar"]
            if "Lfra" in list(init_dict.keys()):
                Lfra = init_dict["Lfra"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
        # Set the properties (value check and convertion are done in setter)
        self.Nbar = Nbar
        self.wbar = wbar
        # Call Frame init
        super(FrameBar, self).__init__(
            Lfra=Lfra, Rint=Rint, Rext=Rext, mat_type=mat_type
        )
        # The class is frozen (in Frame init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        FrameBar_str = ""
        # Get the properties inherited from Frame
        FrameBar_str += super(FrameBar, self).__str__()
        FrameBar_str += "Nbar = " + str(self.Nbar) + linesep
        FrameBar_str += "wbar = " + str(self.wbar) + linesep
        return FrameBar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Frame
        if not super(FrameBar, self).__eq__(other):
            return False
        if other.Nbar != self.Nbar:
            return False
        if other.wbar != self.wbar:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Frame
        diff_list.extend(super(FrameBar, self).compare(other, name=name))
        if other._Nbar != self._Nbar:
            diff_list.append(name + ".Nbar")
        if other._wbar != self._wbar:
            diff_list.append(name + ".wbar")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Frame
        S += super(FrameBar, self).__sizeof__()
        S += getsizeof(self.Nbar)
        S += getsizeof(self.wbar)
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

        # Get the properties inherited from Frame
        FrameBar_dict = super(FrameBar, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        FrameBar_dict["Nbar"] = self.Nbar
        FrameBar_dict["wbar"] = self.wbar
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        FrameBar_dict["__class__"] = "FrameBar"
        return FrameBar_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Nbar = None
        self.wbar = None
        # Set to None the properties inherited from Frame
        super(FrameBar, self)._set_None()

    def _get_Nbar(self):
        """getter of Nbar"""
        return self._Nbar

    def _set_Nbar(self, value):
        """setter of Nbar"""
        check_var("Nbar", value, "int", Vmin=1)
        self._Nbar = value

    Nbar = property(
        fget=_get_Nbar,
        fset=_set_Nbar,
        doc=u"""Number of bars

        :Type: int
        :min: 1
        """,
    )

    def _get_wbar(self):
        """getter of wbar"""
        return self._wbar

    def _set_wbar(self, value):
        """setter of wbar"""
        check_var("wbar", value, "float", Vmin=0)
        self._wbar = value

    wbar = property(
        fget=_get_wbar,
        fset=_set_wbar,
        doc=u"""Width of bars

        :Type: float
        :min: 0
        """,
    )
