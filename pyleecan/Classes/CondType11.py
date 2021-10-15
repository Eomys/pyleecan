# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType11.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType11
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
    from ..Methods.Machine.CondType11.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType11.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.CondType11.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.CondType11.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Machine.CondType11.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.CondType11.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error


from ._check import InitUnKnowClassError
from .Material import Material


class CondType11(Conductor):
    """parallel stranded conductor consisting of at least a single rectangular wire"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType11.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType11 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType11.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType11 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType11.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType11 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType11.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType11 method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType11.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType11 method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.CondType11.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType11 method plot_schematics: "
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
        Hwire=0.01,
        Wwire=0.01,
        Nwppc_rad=1,
        Nwppc_tan=1,
        Wins_wire=0,
        Wins_coil=0,
        type_winding_shape=0,
        alpha_ew=58,
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
            if "Hwire" in list(init_dict.keys()):
                Hwire = init_dict["Hwire"]
            if "Wwire" in list(init_dict.keys()):
                Wwire = init_dict["Wwire"]
            if "Nwppc_rad" in list(init_dict.keys()):
                Nwppc_rad = init_dict["Nwppc_rad"]
            if "Nwppc_tan" in list(init_dict.keys()):
                Nwppc_tan = init_dict["Nwppc_tan"]
            if "Wins_wire" in list(init_dict.keys()):
                Wins_wire = init_dict["Wins_wire"]
            if "Wins_coil" in list(init_dict.keys()):
                Wins_coil = init_dict["Wins_coil"]
            if "type_winding_shape" in list(init_dict.keys()):
                type_winding_shape = init_dict["type_winding_shape"]
            if "alpha_ew" in list(init_dict.keys()):
                alpha_ew = init_dict["alpha_ew"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Hwire = Hwire
        self.Wwire = Wwire
        self.Nwppc_rad = Nwppc_rad
        self.Nwppc_tan = Nwppc_tan
        self.Wins_wire = Wins_wire
        self.Wins_coil = Wins_coil
        self.type_winding_shape = type_winding_shape
        self.alpha_ew = alpha_ew
        # Call Conductor init
        super(CondType11, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType11_str = ""
        # Get the properties inherited from Conductor
        CondType11_str += super(CondType11, self).__str__()
        CondType11_str += "Hwire = " + str(self.Hwire) + linesep
        CondType11_str += "Wwire = " + str(self.Wwire) + linesep
        CondType11_str += "Nwppc_rad = " + str(self.Nwppc_rad) + linesep
        CondType11_str += "Nwppc_tan = " + str(self.Nwppc_tan) + linesep
        CondType11_str += "Wins_wire = " + str(self.Wins_wire) + linesep
        CondType11_str += "Wins_coil = " + str(self.Wins_coil) + linesep
        CondType11_str += (
            "type_winding_shape = " + str(self.type_winding_shape) + linesep
        )
        CondType11_str += "alpha_ew = " + str(self.alpha_ew) + linesep
        return CondType11_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType11, self).__eq__(other):
            return False
        if other.Hwire != self.Hwire:
            return False
        if other.Wwire != self.Wwire:
            return False
        if other.Nwppc_rad != self.Nwppc_rad:
            return False
        if other.Nwppc_tan != self.Nwppc_tan:
            return False
        if other.Wins_wire != self.Wins_wire:
            return False
        if other.Wins_coil != self.Wins_coil:
            return False
        if other.type_winding_shape != self.type_winding_shape:
            return False
        if other.alpha_ew != self.alpha_ew:
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
        diff_list.extend(super(CondType11, self).compare(other, name=name))
        if other._Hwire != self._Hwire:
            diff_list.append(name + ".Hwire")
        if other._Wwire != self._Wwire:
            diff_list.append(name + ".Wwire")
        if other._Nwppc_rad != self._Nwppc_rad:
            diff_list.append(name + ".Nwppc_rad")
        if other._Nwppc_tan != self._Nwppc_tan:
            diff_list.append(name + ".Nwppc_tan")
        if other._Wins_wire != self._Wins_wire:
            diff_list.append(name + ".Wins_wire")
        if other._Wins_coil != self._Wins_coil:
            diff_list.append(name + ".Wins_coil")
        if other._type_winding_shape != self._type_winding_shape:
            diff_list.append(name + ".type_winding_shape")
        if other._alpha_ew != self._alpha_ew:
            diff_list.append(name + ".alpha_ew")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType11, self).__sizeof__()
        S += getsizeof(self.Hwire)
        S += getsizeof(self.Wwire)
        S += getsizeof(self.Nwppc_rad)
        S += getsizeof(self.Nwppc_tan)
        S += getsizeof(self.Wins_wire)
        S += getsizeof(self.Wins_coil)
        S += getsizeof(self.type_winding_shape)
        S += getsizeof(self.alpha_ew)
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
        CondType11_dict = super(CondType11, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType11_dict["Hwire"] = self.Hwire
        CondType11_dict["Wwire"] = self.Wwire
        CondType11_dict["Nwppc_rad"] = self.Nwppc_rad
        CondType11_dict["Nwppc_tan"] = self.Nwppc_tan
        CondType11_dict["Wins_wire"] = self.Wins_wire
        CondType11_dict["Wins_coil"] = self.Wins_coil
        CondType11_dict["type_winding_shape"] = self.type_winding_shape
        CondType11_dict["alpha_ew"] = self.alpha_ew
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType11_dict["__class__"] = "CondType11"
        return CondType11_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hwire = None
        self.Wwire = None
        self.Nwppc_rad = None
        self.Nwppc_tan = None
        self.Wins_wire = None
        self.Wins_coil = None
        self.type_winding_shape = None
        self.alpha_ew = None
        # Set to None the properties inherited from Conductor
        super(CondType11, self)._set_None()

    def _get_Hwire(self):
        """getter of Hwire"""
        return self._Hwire

    def _set_Hwire(self, value):
        """setter of Hwire"""
        check_var("Hwire", value, "float", Vmin=0)
        self._Hwire = value

    Hwire = property(
        fget=_get_Hwire,
        fset=_set_Hwire,
        doc=u"""cf schematics, single wire height without insulation [m]

        :Type: float
        :min: 0
        """,
    )

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
        doc=u"""cf schematics, single wire width without insulation [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Nwppc_rad(self):
        """getter of Nwppc_rad"""
        return self._Nwppc_rad

    def _set_Nwppc_rad(self, value):
        """setter of Nwppc_rad"""
        check_var("Nwppc_rad", value, "int", Vmin=1)
        self._Nwppc_rad = value

    Nwppc_rad = property(
        fget=_get_Nwppc_rad,
        fset=_set_Nwppc_rad,
        doc=u"""cf schematics, stator winding number of preformed wires (strands) in parallel per coil along radial (vertical) direction

        :Type: int
        :min: 1
        """,
    )

    def _get_Nwppc_tan(self):
        """getter of Nwppc_tan"""
        return self._Nwppc_tan

    def _set_Nwppc_tan(self, value):
        """setter of Nwppc_tan"""
        check_var("Nwppc_tan", value, "int", Vmin=1)
        self._Nwppc_tan = value

    Nwppc_tan = property(
        fget=_get_Nwppc_tan,
        fset=_set_Nwppc_tan,
        doc=u"""cf schematics, stator winding number of preformed wires (strands) in parallel per coil along tangential (horizontal) direction

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

    def _get_Wins_coil(self):
        """getter of Wins_coil"""
        return self._Wins_coil

    def _set_Wins_coil(self, value):
        """setter of Wins_coil"""
        check_var("Wins_coil", value, "float", Vmin=0)
        self._Wins_coil = value

    Wins_coil = property(
        fget=_get_Wins_coil,
        fset=_set_Wins_coil,
        doc=u"""(advanced) cf schematics, winding coil insulation  thickness [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_type_winding_shape(self):
        """getter of type_winding_shape"""
        return self._type_winding_shape

    def _set_type_winding_shape(self, value):
        """setter of type_winding_shape"""
        check_var("type_winding_shape", value, "int", Vmin=0, Vmax=1)
        self._type_winding_shape = value

    type_winding_shape = property(
        fget=_get_type_winding_shape,
        fset=_set_type_winding_shape,
        doc=u"""type of winding shape for end winding length calculation\n0 for hairpin windings\n1 for normal windings

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_alpha_ew(self):
        """getter of alpha_ew"""
        return self._alpha_ew

    def _set_alpha_ew(self, value):
        """setter of alpha_ew"""
        check_var("alpha_ew", value, "float", Vmin=0, Vmax=180)
        self._alpha_ew = value

    alpha_ew = property(
        fget=_get_alpha_ew,
        fset=_set_alpha_ew,
        doc=u"""angle of winding overhang hairpin coils [deg]

        :Type: float
        :min: 0
        :max: 180
        """,
    )
