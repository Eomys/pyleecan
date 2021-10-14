# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType12.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType12
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
from .Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.CondType12.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.CondType12.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType12.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.CondType12.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.CondType12.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Machine.CondType12.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.CondType12.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error


from ._check import InitUnKnowClassError
from .Material import Material


class CondType12(Conductor):
    """parallel stranded conductor consisting of at least a single round wire"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType12.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType12 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.CondType12.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType12.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType12.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType12.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12 method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType12.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType12 method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.CondType12.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12 method plot_schematics: "
                    + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Wwire=0.015,
        Wins_cond=0.015,
        Nwppc=1,
        Wins_wire=0,
        Kwoh=0.5,
        cond_mat=-1,
        ins_mat=-1,
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
            if "Wwire" in list(init_dict.keys()):
                Wwire = init_dict["Wwire"]
            if "Wins_cond" in list(init_dict.keys()):
                Wins_cond = init_dict["Wins_cond"]
            if "Nwppc" in list(init_dict.keys()):
                Nwppc = init_dict["Nwppc"]
            if "Wins_wire" in list(init_dict.keys()):
                Wins_wire = init_dict["Wins_wire"]
            if "Kwoh" in list(init_dict.keys()):
                Kwoh = init_dict["Kwoh"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Wwire = Wwire
        self.Wins_cond = Wins_cond
        self.Nwppc = Nwppc
        self.Wins_wire = Wins_wire
        self.Kwoh = Kwoh
        # Call Conductor init
        super(CondType12, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType12_str = ""
        # Get the properties inherited from Conductor
        CondType12_str += super(CondType12, self).__str__()
        CondType12_str += "Wwire = " + str(self.Wwire) + linesep
        CondType12_str += "Wins_cond = " + str(self.Wins_cond) + linesep
        CondType12_str += "Nwppc = " + str(self.Nwppc) + linesep
        CondType12_str += "Wins_wire = " + str(self.Wins_wire) + linesep
        CondType12_str += "Kwoh = " + str(self.Kwoh) + linesep
        return CondType12_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType12, self).__eq__(other):
            return False
        if other.Wwire != self.Wwire:
            return False
        if other.Wins_cond != self.Wins_cond:
            return False
        if other.Nwppc != self.Nwppc:
            return False
        if other.Wins_wire != self.Wins_wire:
            return False
        if other.Kwoh != self.Kwoh:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Conductor
        diff_list.extend(super(CondType12, self).compare(other, name=name))
        if other._Wwire != self._Wwire:
            diff_list.append(name + ".Wwire")
        if other._Wins_cond != self._Wins_cond:
            diff_list.append(name + ".Wins_cond")
        if other._Nwppc != self._Nwppc:
            diff_list.append(name + ".Nwppc")
        if other._Wins_wire != self._Wins_wire:
            diff_list.append(name + ".Wins_wire")
        if other._Kwoh != self._Kwoh:
            diff_list.append(name + ".Kwoh")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType12, self).__sizeof__()
        S += getsizeof(self.Wwire)
        S += getsizeof(self.Wins_cond)
        S += getsizeof(self.Nwppc)
        S += getsizeof(self.Wins_wire)
        S += getsizeof(self.Kwoh)
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

        # Get the properties inherited from Conductor
        CondType12_dict = super(CondType12, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType12_dict["Wwire"] = self.Wwire
        CondType12_dict["Wins_cond"] = self.Wins_cond
        CondType12_dict["Nwppc"] = self.Nwppc
        CondType12_dict["Wins_wire"] = self.Wins_wire
        CondType12_dict["Kwoh"] = self.Kwoh
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType12_dict["__class__"] = "CondType12"
        return CondType12_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wwire = None
        self.Wins_cond = None
        self.Nwppc = None
        self.Wins_wire = None
        self.Kwoh = None
        # Set to None the properties inherited from Conductor
        super(CondType12, self)._set_None()

    def _get_Wwire(self):
        """getter of Wwire"""
        return self._Wwire

    def _set_Wwire(self, value):
        """setter of Wwire"""
        check_var("Wwire", value, "float", Vmin=0)
        self._Wwire = value

    Wwire = property(
        fget=_get_Wwire,
        fset=_set_Wwire,
        doc=u"""cf schematics, single wire diameter without insulation [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Wins_cond(self):
        """getter of Wins_cond"""
        return self._Wins_cond

    def _set_Wins_cond(self, value):
        """setter of Wins_cond"""
        check_var("Wins_cond", value, "float", Vmin=0)
        self._Wins_cond = value

    Wins_cond = property(
        fget=_get_Wins_cond,
        fset=_set_Wins_cond,
        doc=u"""(advanced) cf schematics, winding coil insulation diameter [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Nwppc(self):
        """getter of Nwppc"""
        return self._Nwppc

    def _set_Nwppc(self, value):
        """setter of Nwppc"""
        check_var("Nwppc", value, "int", Vmin=1)
        self._Nwppc = value

    Nwppc = property(
        fget=_get_Nwppc,
        fset=_set_Nwppc,
        doc=u"""cf schematics, winding number of random wires (strands) in parallel per coil

        :Type: int
        :min: 1
        """,
    )

    def _get_Wins_wire(self):
        """getter of Wins_wire"""
        return self._Wins_wire

    def _set_Wins_wire(self, value):
        """setter of Wins_wire"""
        check_var("Wins_wire", value, "float", Vmin=0)
        self._Wins_wire = value

    Wins_wire = property(
        fget=_get_Wins_wire,
        fset=_set_Wins_wire,
        doc=u"""(advanced) cf schematics, winding strand insulation thickness [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Kwoh(self):
        """getter of Kwoh"""
        return self._Kwoh

    def _set_Kwoh(self, value):
        """setter of Kwoh"""
        check_var("Kwoh", value, "float", Vmin=0)
        self._Kwoh = value

    Kwoh = property(
        fget=_get_Kwoh,
        fset=_set_Kwoh,
        doc=u"""winding overhang factor which describes the fact that random round wire end-windings can be more or less compressed (0.5 for small motors, 0.8 for large motors) - can be used to tune the average turn length (relevant if type_cond==1)

        :Type: float
        :min: 0
        """,
    )
