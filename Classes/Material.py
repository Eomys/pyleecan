# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.MatElectrical import MatElectrical
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.MatStructural import MatStructural
from pyleecan.Classes.MatHT import MatHT
from pyleecan.Classes.MatEconomical import MatEconomical


class Material(FrozenClass):

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        name="M400-50A",
        is_isotropic=False,
        elec=-1,
        mag=-1,
        struct=-1,
        HT=-1,
        eco=-1,
        desc="Lamination M400-50A",
        path="",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if elec == -1:
            elec = MatElectrical()
        if mag == -1:
            mag = MatMagnetics()
        if struct == -1:
            struct = MatStructural()
        if HT == -1:
            HT = MatHT()
        if eco == -1:
            eco = MatEconomical()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "name",
                    "is_isotropic",
                    "elec",
                    "mag",
                    "struct",
                    "HT",
                    "eco",
                    "desc",
                    "path",
                ],
            )
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "is_isotropic" in list(init_dict.keys()):
                is_isotropic = init_dict["is_isotropic"]
            if "elec" in list(init_dict.keys()):
                elec = init_dict["elec"]
            if "mag" in list(init_dict.keys()):
                mag = init_dict["mag"]
            if "struct" in list(init_dict.keys()):
                struct = init_dict["struct"]
            if "HT" in list(init_dict.keys()):
                HT = init_dict["HT"]
            if "eco" in list(init_dict.keys()):
                eco = init_dict["eco"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "path" in list(init_dict.keys()):
                path = init_dict["path"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.is_isotropic = is_isotropic
        # elec can be None, a MatElectrical object or a dict
        if isinstance(elec, dict):
            self.elec = MatElectrical(init_dict=elec)
        else:
            self.elec = elec
        # mag can be None, a MatMagnetics object or a dict
        if isinstance(mag, dict):
            # Check that the type is correct (including daughter)
            class_name = mag.get("__class__")
            if class_name not in ["MatMagnetics", "MatLamination", "MatMagnet"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for mag"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.mag = class_obj(init_dict=mag)
        else:
            self.mag = mag
        # struct can be None, a MatStructural object or a dict
        if isinstance(struct, dict):
            self.struct = MatStructural(init_dict=struct)
        else:
            self.struct = struct
        # HT can be None, a MatHT object or a dict
        if isinstance(HT, dict):
            self.HT = MatHT(init_dict=HT)
        else:
            self.HT = HT
        # eco can be None, a MatEconomical object or a dict
        if isinstance(eco, dict):
            self.eco = MatEconomical(init_dict=eco)
        else:
            self.eco = eco
        self.desc = desc
        self.path = path

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
        if self.elec is not None:
            Material_str += "elec = " + str(self.elec.as_dict()) + linesep + linesep
        else:
            Material_str += "elec = None" + linesep + linesep
        if self.mag is not None:
            Material_str += "mag = " + str(self.mag.as_dict()) + linesep + linesep
        else:
            Material_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            Material_str += "struct = " + str(self.struct.as_dict()) + linesep + linesep
        else:
            Material_str += "struct = None" + linesep + linesep
        if self.HT is not None:
            Material_str += "HT = " + str(self.HT.as_dict()) + linesep + linesep
        else:
            Material_str += "HT = None" + linesep + linesep
        if self.eco is not None:
            Material_str += "eco = " + str(self.eco.as_dict()) + linesep + linesep
        else:
            Material_str += "eco = None" + linesep + linesep
        Material_str += 'desc = "' + str(self.desc) + '"' + linesep
        Material_str += 'path = "' + str(self.path) + '"'
        return Material_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.is_isotropic != self.is_isotropic:
            return False
        if other.elec != self.elec:
            return False
        if other.mag != self.mag:
            return False
        if other.struct != self.struct:
            return False
        if other.HT != self.HT:
            return False
        if other.eco != self.eco:
            return False
        if other.desc != self.desc:
            return False
        if other.path != self.path:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Material_dict = dict()
        Material_dict["name"] = self.name
        Material_dict["is_isotropic"] = self.is_isotropic
        if self.elec is None:
            Material_dict["elec"] = None
        else:
            Material_dict["elec"] = self.elec.as_dict()
        if self.mag is None:
            Material_dict["mag"] = None
        else:
            Material_dict["mag"] = self.mag.as_dict()
        if self.struct is None:
            Material_dict["struct"] = None
        else:
            Material_dict["struct"] = self.struct.as_dict()
        if self.HT is None:
            Material_dict["HT"] = None
        else:
            Material_dict["HT"] = self.HT.as_dict()
        if self.eco is None:
            Material_dict["eco"] = None
        else:
            Material_dict["eco"] = self.eco.as_dict()
        Material_dict["desc"] = self.desc
        Material_dict["path"] = self.path
        # The class name is added to the dict fordeserialisation purpose
        Material_dict["__class__"] = "Material"
        return Material_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.is_isotropic = None
        if self.elec is not None:
            self.elec._set_None()
        if self.mag is not None:
            self.mag._set_None()
        if self.struct is not None:
            self.struct._set_None()
        if self.HT is not None:
            self.HT._set_None()
        if self.eco is not None:
            self.eco._set_None()
        self.desc = None
        self.path = None

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

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        check_var("elec", value, "MatElectrical")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    # Electrical properties of the material
    # Type : MatElectrical
    elec = property(
        fget=_get_elec, fset=_set_elec, doc=u"""Electrical properties of the material"""
    )

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        check_var("mag", value, "MatMagnetics")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    # Magnetic properties of the material
    # Type : MatMagnetics
    mag = property(
        fget=_get_mag, fset=_set_mag, doc=u"""Magnetic properties of the material"""
    )

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        check_var("struct", value, "MatStructural")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    # Structural properties of the material
    # Type : MatStructural
    struct = property(
        fget=_get_struct,
        fset=_set_struct,
        doc=u"""Structural properties of the material""",
    )

    def _get_HT(self):
        """getter of HT"""
        return self._HT

    def _set_HT(self, value):
        """setter of HT"""
        check_var("HT", value, "MatHT")
        self._HT = value

        if self._HT is not None:
            self._HT.parent = self

    # Heat Transfer properties of the material
    # Type : MatHT
    HT = property(
        fget=_get_HT, fset=_set_HT, doc=u"""Heat Transfer properties of the material"""
    )

    def _get_eco(self):
        """getter of eco"""
        return self._eco

    def _set_eco(self, value):
        """setter of eco"""
        check_var("eco", value, "MatEconomical")
        self._eco = value

        if self._eco is not None:
            self._eco.parent = self

    # Economical properties of the material
    # Type : MatEconomical
    eco = property(
        fget=_get_eco, fset=_set_eco, doc=u"""Economical properties of the material"""
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

    def _get_path(self):
        """getter of path"""
        return self._path

    def _set_path(self, value):
        """setter of path"""
        check_var("path", value, "str")
        self._path = value

    # Path to the material file
    # Type : str
    path = property(
        fget=_get_path, fset=_set_path, doc=u"""Path to the material file"""
    )
