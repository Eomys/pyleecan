# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/WindingSC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/WindingSC
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Winding import Winding

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.WindingSC.comp_connection_mat import comp_connection_mat
except ImportError as error:
    comp_connection_mat = error

try:
    from ..Methods.Machine.WindingSC.get_dim_wind import get_dim_wind
except ImportError as error:
    get_dim_wind = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Conductor import Conductor
from .EndWinding import EndWinding


class WindingSC(Winding):
    """short-circuit winding (e.g. squirrel cage type)"""

    VERSION = 1
    NAME = "short-circuit"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.WindingSC.comp_connection_mat
    if isinstance(comp_connection_mat, ImportError):
        comp_connection_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingSC method comp_connection_mat: "
                    + str(comp_connection_mat)
                )
            )
        )
    else:
        comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.WindingSC.get_dim_wind
    if isinstance(get_dim_wind, ImportError):
        get_dim_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingSC method get_dim_wind: " + str(get_dim_wind)
                )
            )
        )
    else:
        get_dim_wind = get_dim_wind
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        coil_pitch=1,
        wind_mat=None,
        Nlayer=1,
        per_a=None,
        is_aper_a=None,
        end_winding=-1,
        is_reverse_layer=False,
        is_change_layer=False,
        is_permute_B_C=False,
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
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcp" in list(init_dict.keys()):
                Npcp = init_dict["Npcp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "wind_mat" in list(init_dict.keys()):
                wind_mat = init_dict["wind_mat"]
            if "Nlayer" in list(init_dict.keys()):
                Nlayer = init_dict["Nlayer"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "is_aper_a" in list(init_dict.keys()):
                is_aper_a = init_dict["is_aper_a"]
            if "end_winding" in list(init_dict.keys()):
                end_winding = init_dict["end_winding"]
            if "is_reverse_layer" in list(init_dict.keys()):
                is_reverse_layer = init_dict["is_reverse_layer"]
            if "is_change_layer" in list(init_dict.keys()):
                is_change_layer = init_dict["is_change_layer"]
            if "is_permute_B_C" in list(init_dict.keys()):
                is_permute_B_C = init_dict["is_permute_B_C"]
        # Set the properties (value check and convertion are done in setter)
        # Call Winding init
        super(WindingSC, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcp=Npcp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
            coil_pitch=coil_pitch,
            wind_mat=wind_mat,
            Nlayer=Nlayer,
            per_a=per_a,
            is_aper_a=is_aper_a,
            end_winding=end_winding,
            is_reverse_layer=is_reverse_layer,
            is_change_layer=is_change_layer,
            is_permute_B_C=is_permute_B_C,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        WindingSC_str = ""
        # Get the properties inherited from Winding
        WindingSC_str += super(WindingSC, self).__str__()
        return WindingSC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingSC, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Winding
        diff_list.extend(super(WindingSC, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Winding
        S += super(WindingSC, self).__sizeof__()
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

        # Get the properties inherited from Winding
        WindingSC_dict = super(WindingSC, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        WindingSC_dict["__class__"] = "WindingSC"
        return WindingSC_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Winding
        super(WindingSC, self)._set_None()
