# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/WindingSC.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
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


from ._check import InitUnKnowClassError
from .Conductor import Conductor


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
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcpp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
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

        if conductor == -1:
            conductor = Conductor()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            is_reverse_wind = obj.is_reverse_wind
            Nslot_shift_wind = obj.Nslot_shift_wind
            qs = obj.qs
            Ntcoil = obj.Ntcoil
            Npcpp = obj.Npcpp
            type_connection = obj.type_connection
            p = obj.p
            Lewout = obj.Lewout
            conductor = obj.conductor
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
        # Initialisation by argument
        # Call Winding init
        super(WindingSC, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcpp=Npcpp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Winding
        WindingSC_dict = super(WindingSC, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        WindingSC_dict["__class__"] = "WindingSC"
        return WindingSC_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Winding
        super(WindingSC, self)._set_None()
