# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.MatElectrical import MatElectrical
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.MatLamination import MatLamination
from pyleecan.Classes.MatMagnet import MatMagnet
from pyleecan.Classes.MatMechanics import MatMechanics
from pyleecan.Classes.MatThermics import MatThermics
from pyleecan.Classes.MatEconomical import MatEconomical


class Material(FrozenClass):

    VERSION = 1

    def __init__(
        self,
        name="M400-50A",
        is_isotropic=False,
        electrical=-1,
        magnetics=-1,
        mechanics=-1,
        thermics=-1,
        economical=-1,
        desc="Lamination M400-50A",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if electrical == -1:
            electrical = MatElectrical()
        if magnetics == -1:
            magnetics = MatMagnetics()
        if mechanics == -1:
            mechanics = MatMechanics()
        if thermics == -1:
            thermics = MatThermics()
        if economical == -1:
            economical = MatEconomical()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "name",
                    "is_isotropic",
                    "electrical",
                    "magnetics",
                    "mechanics",
                    "thermics",
                    "economical",
                    "desc",
                ],
            )
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "is_isotropic" in list(init_dict.keys()):
                is_isotropic = init_dict["is_isotropic"]
            if "electrical" in list(init_dict.keys()):
                electrical = init_dict["electrical"]
            if "magnetics" in list(init_dict.keys()):
                magnetics = init_dict["magnetics"]
            if "mechanics" in list(init_dict.keys()):
                mechanics = init_dict["mechanics"]
            if "thermics" in list(init_dict.keys()):
                thermics = init_dict["thermics"]
            if "economical" in list(init_dict.keys()):
                economical = init_dict["economical"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.is_isotropic = is_isotropic
        # electrical can be None, a MatElectrical object or a dict
        if isinstance(electrical, dict):
            self.electrical = MatElectrical(init_dict=electrical)
        else:
            self.electrical = electrical
        # magnetics can be None, a MatMagnetics object or a dict
        if isinstance(magnetics, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "MatLamination": MatLamination,
                "MatMagnet": MatMagnet,
                "MatMagnetics": MatMagnetics,
            }
            obj_class = magnetics.get("__class__")
            if obj_class is None:
                self.magnetics = MatMagnetics(init_dict=magnetics)
            elif obj_class in list(load_dict.keys()):
                self.magnetics = load_dict[obj_class](init_dict=magnetics)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError(
                    "Unknow class name in init_dict for magnetics"
                )
        else:
            self.magnetics = magnetics
        # mechanics can be None, a MatMechanics object or a dict
        if isinstance(mechanics, dict):
            self.mechanics = MatMechanics(init_dict=mechanics)
        else:
            self.mechanics = mechanics
        # thermics can be None, a MatThermics object or a dict
        if isinstance(thermics, dict):
            self.thermics = MatThermics(init_dict=thermics)
        else:
            self.thermics = thermics
        # economical can be None, a MatEconomical object or a dict
        if isinstance(economical, dict):
            self.economical = MatEconomical(init_dict=economical)
        else:
            self.economical = economical
        self.desc = desc

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Material_str = ""
        if self.parent is None:
            Material_str += "parent = None " + linesep
        else:
            Material_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Material_str += 'name = "' + str(self.name) + '"' + linesep
        Material_str += "is_isotropic = " + str(self.is_isotropic) + linesep
        Material_str += (
            "electrical = " + str(self.electrical.as_dict()) + linesep + linesep
        )
        Material_str += (
            "magnetics = " + str(self.magnetics.as_dict()) + linesep + linesep
        )
        Material_str += (
            "mechanics = " + str(self.mechanics.as_dict()) + linesep + linesep
        )
        Material_str += "thermics = " + str(self.thermics.as_dict()) + linesep + linesep
        Material_str += (
            "economical = " + str(self.economical.as_dict()) + linesep + linesep
        )
        Material_str += 'desc = "' + str(self.desc) + '"'
        return Material_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.is_isotropic != self.is_isotropic:
            return False
        if other.electrical != self.electrical:
            return False
        if other.magnetics != self.magnetics:
            return False
        if other.mechanics != self.mechanics:
            return False
        if other.thermics != self.thermics:
            return False
        if other.economical != self.economical:
            return False
        if other.desc != self.desc:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Material_dict = dict()
        Material_dict["name"] = self.name
        Material_dict["is_isotropic"] = self.is_isotropic
        if self.electrical is None:
            Material_dict["electrical"] = None
        else:
            Material_dict["electrical"] = self.electrical.as_dict()
        if self.magnetics is None:
            Material_dict["magnetics"] = None
        else:
            Material_dict["magnetics"] = self.magnetics.as_dict()
        if self.mechanics is None:
            Material_dict["mechanics"] = None
        else:
            Material_dict["mechanics"] = self.mechanics.as_dict()
        if self.thermics is None:
            Material_dict["thermics"] = None
        else:
            Material_dict["thermics"] = self.thermics.as_dict()
        if self.economical is None:
            Material_dict["economical"] = None
        else:
            Material_dict["economical"] = self.economical.as_dict()
        Material_dict["desc"] = self.desc
        # The class name is added to the dict fordeserialisation purpose
        Material_dict["__class__"] = "Material"
        return Material_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.is_isotropic = None
        if self.electrical is not None:
            self.electrical._set_None()
        if self.magnetics is not None:
            self.magnetics._set_None()
        if self.mechanics is not None:
            self.mechanics._set_None()
        if self.thermics is not None:
            self.thermics._set_None()
        if self.economical is not None:
            self.economical._set_None()
        self.desc = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # name of the material
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""name of the material""")

    def _get_is_isotropic(self):
        """getter of is_isotropic"""
        return self._is_isotropic

    def _set_is_isotropic(self, value):
        """setter of is_isotropic"""
        check_var("is_isotropic", value, "bool")
        self._is_isotropic = value

    # If True, uniformity in all orientations
    # Type : bool
    is_isotropic = property(
        fget=_get_is_isotropic,
        fset=_set_is_isotropic,
        doc=u"""If True, uniformity in all orientations""",
    )

    def _get_electrical(self):
        """getter of electrical"""
        return self._electrical

    def _set_electrical(self, value):
        """setter of electrical"""
        check_var("electrical", value, "MatElectrical")
        self._electrical = value

        if self._electrical is not None:
            self._electrical.parent = self

    # Electrical properties of the material
    # Type : MatElectrical
    electrical = property(
        fget=_get_electrical,
        fset=_set_electrical,
        doc=u"""Electrical properties of the material""",
    )

    def _get_magnetics(self):
        """getter of magnetics"""
        return self._magnetics

    def _set_magnetics(self, value):
        """setter of magnetics"""
        check_var("magnetics", value, "MatMagnetics")
        self._magnetics = value

        if self._magnetics is not None:
            self._magnetics.parent = self

    # Magnetic properties of the material
    # Type : MatMagnetics
    magnetics = property(
        fget=_get_magnetics,
        fset=_set_magnetics,
        doc=u"""Magnetic properties of the material""",
    )

    def _get_mechanics(self):
        """getter of mechanics"""
        return self._mechanics

    def _set_mechanics(self, value):
        """setter of mechanics"""
        check_var("mechanics", value, "MatMechanics")
        self._mechanics = value

        if self._mechanics is not None:
            self._mechanics.parent = self

    # Mechanics properties of the material
    # Type : MatMechanics
    mechanics = property(
        fget=_get_mechanics,
        fset=_set_mechanics,
        doc=u"""Mechanics properties of the material""",
    )

    def _get_thermics(self):
        """getter of thermics"""
        return self._thermics

    def _set_thermics(self, value):
        """setter of thermics"""
        check_var("thermics", value, "MatThermics")
        self._thermics = value

        if self._thermics is not None:
            self._thermics.parent = self

    # Thermics properties of the material
    # Type : MatThermics
    thermics = property(
        fget=_get_thermics,
        fset=_set_thermics,
        doc=u"""Thermics properties of the material""",
    )

    def _get_economical(self):
        """getter of economical"""
        return self._economical

    def _set_economical(self, value):
        """setter of economical"""
        check_var("economical", value, "MatEconomical")
        self._economical = value

        if self._economical is not None:
            self._economical.parent = self

    # Economical properties of the material
    # Type : MatEconomical
    economical = property(
        fget=_get_economical,
        fset=_set_economical,
        doc=u"""Economical properties of the material""",
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    # material description
    # Type : str
    desc = property(fget=_get_desc, fset=_set_desc, doc=u"""material description""")
