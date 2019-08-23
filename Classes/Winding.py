# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Machine.Winding.comp_Ncspc import comp_Ncspc
from pyleecan.Methods.Machine.Winding.comp_Ntspc import comp_Ntspc
from pyleecan.Methods.Machine.Winding.comp_phasor_angle import comp_phasor_angle
from pyleecan.Methods.Machine.Winding.comp_resistance_norm import comp_resistance_norm
from pyleecan.Methods.Machine.Winding.comp_winding_factor import comp_winding_factor

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Conductor import Conductor
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22


class Winding(FrozenClass):
    """Winding abstract class"""

    VERSION = 1

    # cf Methods.Machine.Winding.comp_Ncspc
    comp_Ncspc = comp_Ncspc
    # cf Methods.Machine.Winding.comp_Ntspc
    comp_Ntspc = comp_Ntspc
    # cf Methods.Machine.Winding.comp_phasor_angle
    comp_phasor_angle = comp_phasor_angle
    # cf Methods.Machine.Winding.comp_resistance_norm
    comp_resistance_norm = comp_resistance_norm
    # cf Methods.Machine.Winding.comp_winding_factor
    comp_winding_factor = comp_winding_factor
    # save method is available in all object
    save = save

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
        self.parent = None
        self.is_reverse_wind = is_reverse_wind
        self.Nslot_shift_wind = Nslot_shift_wind
        self.qs = qs
        self.Ntcoil = Ntcoil
        self.Npcpp = Npcpp
        self.type_connection = type_connection
        self.p = p
        self.Lewout = Lewout
        # conductor can be None, a Conductor object or a dict
        if isinstance(conductor, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "CondType11": CondType11,
                "CondType12": CondType12,
                "CondType21": CondType21,
                "CondType22": CondType22,
                "Conductor": Conductor,
            }
            obj_class = conductor.get("__class__")
            if obj_class is None:
                self.conductor = Conductor(init_dict=conductor)
            elif obj_class in list(load_dict.keys()):
                self.conductor = load_dict[obj_class](init_dict=conductor)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError(
                    "Unknow class name in init_dict for conductor"
                )
        else:
            self.conductor = conductor

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Winding_str = ""
        if self.parent is None:
            Winding_str += "parent = None " + linesep
        else:
            Winding_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Winding_str += "is_reverse_wind = " + str(self.is_reverse_wind) + linesep
        Winding_str += "Nslot_shift_wind = " + str(self.Nslot_shift_wind) + linesep
        Winding_str += "qs = " + str(self.qs) + linesep
        Winding_str += "Ntcoil = " + str(self.Ntcoil) + linesep
        Winding_str += "Npcpp = " + str(self.Npcpp) + linesep
        Winding_str += "type_connection = " + str(self.type_connection) + linesep
        Winding_str += "p = " + str(self.p) + linesep
        Winding_str += "Lewout = " + str(self.Lewout) + linesep
        Winding_str += "conductor = " + str(self.conductor.as_dict())
        return Winding_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_reverse_wind != self.is_reverse_wind:
            return False
        if other.Nslot_shift_wind != self.Nslot_shift_wind:
            return False
        if other.qs != self.qs:
            return False
        if other.Ntcoil != self.Ntcoil:
            return False
        if other.Npcpp != self.Npcpp:
            return False
        if other.type_connection != self.type_connection:
            return False
        if other.p != self.p:
            return False
        if other.Lewout != self.Lewout:
            return False
        if other.conductor != self.conductor:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Winding_dict = dict()
        Winding_dict["is_reverse_wind"] = self.is_reverse_wind
        Winding_dict["Nslot_shift_wind"] = self.Nslot_shift_wind
        Winding_dict["qs"] = self.qs
        Winding_dict["Ntcoil"] = self.Ntcoil
        Winding_dict["Npcpp"] = self.Npcpp
        Winding_dict["type_connection"] = self.type_connection
        Winding_dict["p"] = self.p
        Winding_dict["Lewout"] = self.Lewout
        if self.conductor is None:
            Winding_dict["conductor"] = None
        else:
            Winding_dict["conductor"] = self.conductor.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Winding_dict["__class__"] = "Winding"
        return Winding_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_reverse_wind = None
        self.Nslot_shift_wind = None
        self.qs = None
        self.Ntcoil = None
        self.Npcpp = None
        self.type_connection = None
        self.p = None
        self.Lewout = None
        if self.conductor is not None:
            self.conductor._set_None()

    def _get_is_reverse_wind(self):
        """getter of is_reverse_wind"""
        return self._is_reverse_wind

    def _set_is_reverse_wind(self, value):
        """setter of is_reverse_wind"""
        check_var("is_reverse_wind", value, "bool")
        self._is_reverse_wind = value

    # 1 to reverse the default winding algorithm along the airgap (c,b,a instead of a,b,c along the trigonometric direction)
    # Type : bool
    is_reverse_wind = property(
        fget=_get_is_reverse_wind,
        fset=_set_is_reverse_wind,
        doc=u"""1 to reverse the default winding algorithm along the airgap (c,b,a instead of a,b,c along the trigonometric direction)""",
    )

    def _get_Nslot_shift_wind(self):
        """getter of Nslot_shift_wind"""
        return self._Nslot_shift_wind

    def _set_Nslot_shift_wind(self, value):
        """setter of Nslot_shift_wind"""
        check_var("Nslot_shift_wind", value, "int")
        self._Nslot_shift_wind = value

    # 0 not to change the stator winding connection matrix built by MANATEE number of slots to shift the coils obtained with MANATEE winding algorithm (a,b,c becomes b,c,a with Nslot_shift_wind1=1)
    # Type : int
    Nslot_shift_wind = property(
        fget=_get_Nslot_shift_wind,
        fset=_set_Nslot_shift_wind,
        doc=u"""0 not to change the stator winding connection matrix built by MANATEE number of slots to shift the coils obtained with MANATEE winding algorithm (a,b,c becomes b,c,a with Nslot_shift_wind1=1)""",
    )

    def _get_qs(self):
        """getter of qs"""
        return self._qs

    def _set_qs(self, value):
        """setter of qs"""
        check_var("qs", value, "int", Vmin=1, Vmax=100)
        self._qs = value

    # number of phases
    # Type : int, min = 1, max = 100
    qs = property(fget=_get_qs, fset=_set_qs, doc=u"""number of phases """)

    def _get_Ntcoil(self):
        """getter of Ntcoil"""
        return self._Ntcoil

    def _set_Ntcoil(self, value):
        """setter of Ntcoil"""
        check_var("Ntcoil", value, "int", Vmin=1, Vmax=1000)
        self._Ntcoil = value

    # number of turns per coil
    # Type : int, min = 1, max = 1000
    Ntcoil = property(
        fget=_get_Ntcoil, fset=_set_Ntcoil, doc=u"""number of turns per coil"""
    )

    def _get_Npcpp(self):
        """getter of Npcpp"""
        return self._Npcpp

    def _set_Npcpp(self, value):
        """setter of Npcpp"""
        check_var("Npcpp", value, "int", Vmin=1, Vmax=1000)
        self._Npcpp = value

    # number of parallel circuits per phase (maximum 2p)
    # Type : int, min = 1, max = 1000
    Npcpp = property(
        fget=_get_Npcpp,
        fset=_set_Npcpp,
        doc=u"""number of parallel circuits per phase (maximum 2p)""",
    )

    def _get_type_connection(self):
        """getter of type_connection"""
        return self._type_connection

    def _set_type_connection(self, value):
        """setter of type_connection"""
        check_var("type_connection", value, "int", Vmin=0, Vmax=1)
        self._type_connection = value

    # Winding connection : 0 star (Y), 1 triangle (delta)
    # Type : int, min = 0, max = 1
    type_connection = property(
        fget=_get_type_connection,
        fset=_set_type_connection,
        doc=u"""Winding connection : 0 star (Y), 1 triangle (delta)""",
    )

    def _get_p(self):
        """getter of p"""
        return self._p

    def _set_p(self, value):
        """setter of p"""
        check_var("p", value, "int", Vmin=1, Vmax=100)
        self._p = value

    # pole pairs number
    # Type : int, min = 1, max = 100
    p = property(fget=_get_p, fset=_set_p, doc=u"""pole pairs number""")

    def _get_Lewout(self):
        """getter of Lewout"""
        return self._Lewout

    def _set_Lewout(self, value):
        """setter of Lewout"""
        check_var("Lewout", value, "float", Vmin=0, Vmax=100)
        self._Lewout = value

    # straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length
    # Type : float, min = 0, max = 100
    Lewout = property(
        fget=_get_Lewout,
        fset=_set_Lewout,
        doc=u"""straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length """,
    )

    def _get_conductor(self):
        """getter of conductor"""
        return self._conductor

    def _set_conductor(self, value):
        """setter of conductor"""
        check_var("conductor", value, "Conductor")
        self._conductor = value

        if self._conductor is not None:
            self._conductor.parent = self

    # Winding's conductor
    # Type : Conductor
    conductor = property(
        fget=_get_conductor, fset=_set_conductor, doc=u"""Winding's conductor"""
    )
