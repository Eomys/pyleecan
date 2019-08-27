# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Winding import Winding

from pyleecan.Methods.Machine.WindingUD.comp_connection_mat import comp_connection_mat
from pyleecan.Methods.Machine.WindingUD.get_dim_wind import get_dim_wind

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Conductor import Conductor
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22


class WindingUD(Winding):
    """User defined winding"""

    VERSION = 1

    # cf Methods.Machine.WindingUD.comp_connection_mat
    comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.WindingUD.get_dim_wind
    get_dim_wind = get_dim_wind
    # save method is available in all object
    save = save

    def __init__(
        self,
        user_wind_mat=None,
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
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if conductor == -1:
            conductor = Conductor()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "user_wind_mat",
                    "is_reverse_wind",
                    "Nslot_shift_wind",
                    "qs",
                    "Ntcoil",
                    "Npcpp",
                    "type_connection",
                    "p",
                    "Lewout",
                    "conductor",
                ],
            )
            # Overwrite default value with init_dict content
            if "user_wind_mat" in list(init_dict.keys()):
                user_wind_mat = init_dict["user_wind_mat"]
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
        # user_wind_mat can be None, a ndarray or a list
        set_array(self, "user_wind_mat", user_wind_mat)
        # Call Winding init
        super(WindingUD, self).__init__(
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

        WindingUD_str = ""
        # Get the properties inherited from Winding
        WindingUD_str += super(WindingUD, self).__str__() + linesep
        WindingUD_str += "user_wind_mat = " + linesep + str(self.user_wind_mat)
        return WindingUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingUD, self).__eq__(other):
            return False
        if not array_equal(other.user_wind_mat, self.user_wind_mat):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Winding
        WindingUD_dict = super(WindingUD, self).as_dict()
        if self.user_wind_mat is None:
            WindingUD_dict["user_wind_mat"] = None
        else:
            WindingUD_dict["user_wind_mat"] = self.user_wind_mat.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        WindingUD_dict["__class__"] = "WindingUD"
        return WindingUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.user_wind_mat = None
        # Set to None the properties inherited from Winding
        super(WindingUD, self)._set_None()

    def _get_user_wind_mat(self):
        """getter of user_wind_mat"""
        return self._user_wind_mat

    def _set_user_wind_mat(self, value):
        """setter of user_wind_mat"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("user_wind_mat", value, "ndarray")
        self._user_wind_mat = value

    # user defined Winding matrix
    # Type : ndarray
    user_wind_mat = property(
        fget=_get_user_wind_mat,
        fset=_set_user_wind_mat,
        doc=u"""user defined Winding matrix""",
    )
