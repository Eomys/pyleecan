# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/WindingCW.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/WindingCW
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
from .Winding import Winding

from ._check import InitUnKnowClassError
from .Conductor import Conductor
from .EndWinding import EndWinding


class WindingCW(Winding):
    """Abstract non-overlapping 'concentrated' tooth winding"""

    VERSION = 1

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
        Npcpp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        end_winding=-1,
        init_dict=None,
        init_str=None,
    ):
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
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcpp" in list(init_dict.keys()):
                Npcpp = init_dict["Npcpp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
            if "end_winding" in list(init_dict.keys()):
                end_winding = init_dict["end_winding"]
        # Set the properties (value check and convertion are done in setter)
        # Call Winding init
        super(WindingCW, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcpp=Npcpp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
            end_winding=end_winding,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        WindingCW_str = ""
        # Get the properties inherited from Winding
        WindingCW_str += super(WindingCW, self).__str__()
        return WindingCW_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingCW, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self"):
        """Compare two objects and return list of differences"""

        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Winding
        diff_list.extend(super(WindingCW, self).compare(other, name=name))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Winding
        S += super(WindingCW, self).__sizeof__()
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Winding
        WindingCW_dict = super(WindingCW, self).as_dict()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        WindingCW_dict["__class__"] = "WindingCW"
        return WindingCW_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Winding
        super(WindingCW, self)._set_None()
