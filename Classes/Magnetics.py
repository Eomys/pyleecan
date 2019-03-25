# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Simulation.Magnetics.run import run
from pyleecan.Methods.Simulation.Magnetics.comp_time_angle import comp_time_angle

from pyleecan.Classes.check import InitUnKnowClassError


class Magnetics(FrozenClass):
    """Magnetic module abstract object"""

    VERSION = 1

    # cf Methods.Simulation.Magnetics.run
    run = run
    # cf Methods.Simulation.Magnetics.comp_time_angle
    comp_time_angle = comp_time_angle
    # save method is available in all object
    save = save

    def __init__(
        self,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_vent=False,
        is_mmfs=True,
        is_mmfr=True,
        is_stator_linear_BH=0,
        is_rotor_linear_BH=0,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "is_remove_slotS",
                    "is_remove_slotR",
                    "is_remove_vent",
                    "is_mmfs",
                    "is_mmfr",
                    "is_stator_linear_BH",
                    "is_rotor_linear_BH",
                ],
            )
            # Overwrite default value with init_dict content
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_vent" in list(init_dict.keys()):
                is_remove_vent = init_dict["is_remove_vent"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "is_stator_linear_BH" in list(init_dict.keys()):
                is_stator_linear_BH = init_dict["is_stator_linear_BH"]
            if "is_rotor_linear_BH" in list(init_dict.keys()):
                is_rotor_linear_BH = init_dict["is_rotor_linear_BH"]
        # Initialisation by argument
        self.parent = None
        self.is_remove_slotS = is_remove_slotS
        self.is_remove_slotR = is_remove_slotR
        self.is_remove_vent = is_remove_vent
        self.is_mmfs = is_mmfs
        self.is_mmfr = is_mmfr
        self.is_stator_linear_BH = is_stator_linear_BH
        self.is_rotor_linear_BH = is_rotor_linear_BH

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Magnetics_str = ""
        if self.parent is None:
            Magnetics_str += "parent = None " + linesep
        else:
            Magnetics_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Magnetics_str += "is_remove_slotS = " + str(self.is_remove_slotS) + linesep
        Magnetics_str += "is_remove_slotR = " + str(self.is_remove_slotR) + linesep
        Magnetics_str += "is_remove_vent = " + str(self.is_remove_vent) + linesep
        Magnetics_str += "is_mmfs = " + str(self.is_mmfs) + linesep
        Magnetics_str += "is_mmfr = " + str(self.is_mmfr) + linesep
        Magnetics_str += (
            "is_stator_linear_BH = " + str(self.is_stator_linear_BH) + linesep
        )
        Magnetics_str += "is_rotor_linear_BH = " + str(self.is_rotor_linear_BH)
        return Magnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_remove_slotS != self.is_remove_slotS:
            return False
        if other.is_remove_slotR != self.is_remove_slotR:
            return False
        if other.is_remove_vent != self.is_remove_vent:
            return False
        if other.is_mmfs != self.is_mmfs:
            return False
        if other.is_mmfr != self.is_mmfr:
            return False
        if other.is_stator_linear_BH != self.is_stator_linear_BH:
            return False
        if other.is_rotor_linear_BH != self.is_rotor_linear_BH:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Magnetics_dict = dict()
        Magnetics_dict["is_remove_slotS"] = self.is_remove_slotS
        Magnetics_dict["is_remove_slotR"] = self.is_remove_slotR
        Magnetics_dict["is_remove_vent"] = self.is_remove_vent
        Magnetics_dict["is_mmfs"] = self.is_mmfs
        Magnetics_dict["is_mmfr"] = self.is_mmfr
        Magnetics_dict["is_stator_linear_BH"] = self.is_stator_linear_BH
        Magnetics_dict["is_rotor_linear_BH"] = self.is_rotor_linear_BH
        # The class name is added to the dict fordeserialisation purpose
        Magnetics_dict["__class__"] = "Magnetics"
        return Magnetics_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_remove_slotS = None
        self.is_remove_slotR = None
        self.is_remove_vent = None
        self.is_mmfs = None
        self.is_mmfr = None
        self.is_stator_linear_BH = None
        self.is_rotor_linear_BH = None

    def _get_is_remove_slotS(self):
        """getter of is_remove_slotS"""
        return self._is_remove_slotS

    def _set_is_remove_slotS(self, value):
        """setter of is_remove_slotS"""
        check_var("is_remove_slotS", value, "bool")
        self._is_remove_slotS = value

    # 1 to artificially remove stator slotting effects in permeance mmf calculations
    # Type : bool
    is_remove_slotS = property(
        fget=_get_is_remove_slotS,
        fset=_set_is_remove_slotS,
        doc=u"""1 to artificially remove stator slotting effects in permeance mmf calculations""",
    )

    def _get_is_remove_slotR(self):
        """getter of is_remove_slotR"""
        return self._is_remove_slotR

    def _set_is_remove_slotR(self, value):
        """setter of is_remove_slotR"""
        check_var("is_remove_slotR", value, "bool")
        self._is_remove_slotR = value

    # 1 to artificially remove rotor slotting effects in permeance mmf calculations
    # Type : bool
    is_remove_slotR = property(
        fget=_get_is_remove_slotR,
        fset=_set_is_remove_slotR,
        doc=u"""1 to artificially remove rotor slotting effects in permeance mmf calculations""",
    )

    def _get_is_remove_vent(self):
        """getter of is_remove_vent"""
        return self._is_remove_vent

    def _set_is_remove_vent(self, value):
        """setter of is_remove_vent"""
        check_var("is_remove_vent", value, "bool")
        self._is_remove_vent = value

    # 1 to artificially remove the ventilations duct
    # Type : bool
    is_remove_vent = property(
        fget=_get_is_remove_vent,
        fset=_set_is_remove_vent,
        doc=u"""1 to artificially remove the ventilations duct""",
    )

    def _get_is_mmfs(self):
        """getter of is_mmfs"""
        return self._is_mmfs

    def _set_is_mmfs(self, value):
        """setter of is_mmfs"""
        check_var("is_mmfs", value, "bool")
        self._is_mmfs = value

    # 1 to compute the stator magnetomotive force / stator armature magnetic field
    # Type : bool
    is_mmfs = property(
        fget=_get_is_mmfs,
        fset=_set_is_mmfs,
        doc=u"""1 to compute the stator magnetomotive force / stator armature magnetic field""",
    )

    def _get_is_mmfr(self):
        """getter of is_mmfr"""
        return self._is_mmfr

    def _set_is_mmfr(self, value):
        """setter of is_mmfr"""
        check_var("is_mmfr", value, "bool")
        self._is_mmfr = value

    # 1 to compute the rotor magnetomotive force / rotor magnetic field
    # Type : bool
    is_mmfr = property(
        fget=_get_is_mmfr,
        fset=_set_is_mmfr,
        doc=u"""1 to compute the rotor magnetomotive force / rotor magnetic field""",
    )

    def _get_is_stator_linear_BH(self):
        """getter of is_stator_linear_BH"""
        return self._is_stator_linear_BH

    def _set_is_stator_linear_BH(self, value):
        """setter of is_stator_linear_BH"""
        check_var("is_stator_linear_BH", value, "int", Vmin=0, Vmax=2)
        self._is_stator_linear_BH = value

    # 0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)
    # Type : int, min = 0, max = 2
    is_stator_linear_BH = property(
        fget=_get_is_stator_linear_BH,
        fset=_set_is_stator_linear_BH,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)""",
    )

    def _get_is_rotor_linear_BH(self):
        """getter of is_rotor_linear_BH"""
        return self._is_rotor_linear_BH

    def _set_is_rotor_linear_BH(self, value):
        """setter of is_rotor_linear_BH"""
        check_var("is_rotor_linear_BH", value, "int", Vmin=0, Vmax=2)
        self._is_rotor_linear_BH = value

    # 0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)
    # Type : int, min = 0, max = 2
    is_rotor_linear_BH = property(
        fget=_get_is_rotor_linear_BH,
        fset=_set_is_rotor_linear_BH,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)""",
    )
