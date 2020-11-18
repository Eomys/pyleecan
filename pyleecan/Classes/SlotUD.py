# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotUD
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotUD.set_from_point_list import set_from_point_list
except ImportError as error:
    set_from_point_list = error

try:
    from ..Methods.Slot.SlotUD.get_surface_wind import get_surface_wind
except ImportError as error:
    get_surface_wind = error

try:
    from ..Methods.Slot.SlotUD.check import check
except ImportError as error:
    check = error


from ._check import InitUnKnowClassError
from .Line import Line


class SlotUD(SlotWind):
    """"User defined" Slot from a line list. """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotUD.set_from_point_list
    if isinstance(set_from_point_list, ImportError):
        set_from_point_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method set_from_point_list: "
                    + str(set_from_point_list)
                )
            )
        )
    else:
        set_from_point_list = set_from_point_list
    # cf Methods.Slot.SlotUD.get_surface_wind
    if isinstance(get_surface_wind, ImportError):
        get_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method get_surface_wind: " + str(get_surface_wind)
                )
            )
        )
    else:
        get_surface_wind = get_surface_wind
    # cf Methods.Slot.SlotUD.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotUD method check: " + str(check))
            )
        )
    else:
        check = check
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, line_list=-1, wind_begin_index=None, wind_end_index=None, type_line_wind=0, Zs=36, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "line_list" in list(init_dict.keys()):
                line_list = init_dict["line_list"]
            if "wind_begin_index" in list(init_dict.keys()):
                wind_begin_index = init_dict["wind_begin_index"]
            if "wind_end_index" in list(init_dict.keys()):
                wind_end_index = init_dict["wind_end_index"]
            if "type_line_wind" in list(init_dict.keys()):
                type_line_wind = init_dict["type_line_wind"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.line_list = line_list
        self.wind_begin_index = wind_begin_index
        self.wind_end_index = wind_end_index
        self.type_line_wind = type_line_wind
        # Call SlotWind init
        super(SlotUD, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotUD_str = ""
        # Get the properties inherited from SlotWind
        SlotUD_str += super(SlotUD, self).__str__()
        if len(self.line_list) == 0:
            SlotUD_str += "line_list = []" + linesep
        for ii in range(len(self.line_list)):
            tmp = self.line_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            SlotUD_str += "line_list["+str(ii)+"] ="+ tmp + linesep + linesep
        SlotUD_str += "wind_begin_index = " + str(self.wind_begin_index) + linesep
        SlotUD_str += "wind_end_index = " + str(self.wind_end_index) + linesep
        SlotUD_str += "type_line_wind = " + str(self.type_line_wind) + linesep
        return SlotUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotUD, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
            return False
        if other.wind_begin_index != self.wind_begin_index:
            return False
        if other.wind_end_index != self.wind_end_index:
            return False
        if other.type_line_wind != self.type_line_wind:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotUD_dict = super(SlotUD, self).as_dict()
        if self.line_list is None:
            SlotUD_dict["line_list"] = None
        else:
            SlotUD_dict["line_list"] = list()
            for obj in self.line_list:
                SlotUD_dict["line_list"].append(obj.as_dict())
        SlotUD_dict["wind_begin_index"] = self.wind_begin_index
        SlotUD_dict["wind_end_index"] = self.wind_end_index
        SlotUD_dict["type_line_wind"] = self.type_line_wind
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotUD_dict["__class__"] = "SlotUD"
        return SlotUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.line_list:
            obj._set_None()
        self.wind_begin_index = None
        self.wind_end_index = None
        self.type_line_wind = None
        # Set to None the properties inherited from SlotWind
        super(SlotUD, self)._set_None()

    def _get_line_list(self):
        """getter of line_list"""
        if self._line_list is not None:
            for obj in self._line_list:
                if obj is not None:
                    obj.parent = self
        return self._line_list

    def _set_line_list(self, value):
        """setter of line_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class('pyleecan.Classes', obj.get('__class__'), 'line_list')
                    value[ii] = class_obj(init_dict=obj)
        if value == -1:
            value = list()
        check_var("line_list", value, "[Line]")
        self._line_list = value

    line_list = property(
        fget=_get_line_list,
        fset=_set_line_list,
        doc=u"""list of line to draw the edges of the slot

        :Type: [Line]
        """,
    )

    def _get_wind_begin_index(self):
        """getter of wind_begin_index"""
        return self._wind_begin_index

    def _set_wind_begin_index(self, value):
        """setter of wind_begin_index"""
        check_var("wind_begin_index", value, "int")
        self._wind_begin_index = value

    wind_begin_index = property(
        fget=_get_wind_begin_index,
        fset=_set_wind_begin_index,
        doc=u"""Index of the first line to include in the winding

        :Type: int
        """,
    )

    def _get_wind_end_index(self):
        """getter of wind_end_index"""
        return self._wind_end_index

    def _set_wind_end_index(self, value):
        """setter of wind_end_index"""
        check_var("wind_end_index", value, "int")
        self._wind_end_index = value

    wind_end_index = property(
        fget=_get_wind_end_index,
        fset=_set_wind_end_index,
        doc=u"""Index of the last line to include in the winding

        :Type: int
        """,
    )

    def _get_type_line_wind(self):
        """getter of type_line_wind"""
        return self._type_line_wind

    def _set_type_line_wind(self, value):
        """setter of type_line_wind"""
        check_var("type_line_wind", value, "int", Vmin=0, Vmax=1)
        self._type_line_wind = value

    type_line_wind = property(
        fget=_get_type_line_wind,
        fset=_set_type_line_wind,
        doc=u"""0 to close winding with Segment, 1 for Arc1

        :Type: int
        :min: 0
        :max: 1
        """,
    )
