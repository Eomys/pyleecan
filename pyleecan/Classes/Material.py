# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/Material.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/Material
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
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError
from .MatElectrical import MatElectrical
from .MatMagnetics import MatMagnetics
from .MatStructural import MatStructural
from .MatHT import MatHT
from .MatEconomical import MatEconomical


class Material(FrozenClass):

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="Material",
        is_isotropic=False,
        elec=-1,
        mag=-1,
        struct=-1,
        HT=-1,
        eco=-1,
        desc="Material description",
        path="",
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
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.is_isotropic = is_isotropic
        self.elec = elec
        self.mag = mag
        self.struct = struct
        self.HT = HT
        self.eco = eco
        self.desc = desc
        self.path = path

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Material_str = ""
        if self.parent is None:
            Material_str += "parent = None " + linesep
        else:
            Material_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Material_str += 'name = "' + str(self.name) + '"' + linesep
        Material_str += "is_isotropic = " + str(self.is_isotropic) + linesep
        if self.elec is not None:
            tmp = self.elec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Material_str += "elec = " + tmp
        else:
            Material_str += "elec = None" + linesep + linesep
        if self.mag is not None:
            tmp = self.mag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Material_str += "mag = " + tmp
        else:
            Material_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            tmp = self.struct.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Material_str += "struct = " + tmp
        else:
            Material_str += "struct = None" + linesep + linesep
        if self.HT is not None:
            tmp = self.HT.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Material_str += "HT = " + tmp
        else:
            Material_str += "HT = None" + linesep + linesep
        if self.eco is not None:
            tmp = self.eco.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Material_str += "eco = " + tmp
        else:
            Material_str += "eco = None" + linesep + linesep
        Material_str += 'desc = "' + str(self.desc) + '"' + linesep
        Material_str += 'path = "' + str(self.path) + '"' + linesep
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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name != self._name:
            diff_list.append(name + ".name")
        if other._is_isotropic != self._is_isotropic:
            diff_list.append(name + ".is_isotropic")
        if (other.elec is None and self.elec is not None) or (
            other.elec is not None and self.elec is None
        ):
            diff_list.append(name + ".elec None mismatch")
        elif self.elec is not None:
            diff_list.extend(self.elec.compare(other.elec, name=name + ".elec"))
        if (other.mag is None and self.mag is not None) or (
            other.mag is not None and self.mag is None
        ):
            diff_list.append(name + ".mag None mismatch")
        elif self.mag is not None:
            diff_list.extend(self.mag.compare(other.mag, name=name + ".mag"))
        if (other.struct is None and self.struct is not None) or (
            other.struct is not None and self.struct is None
        ):
            diff_list.append(name + ".struct None mismatch")
        elif self.struct is not None:
            diff_list.extend(self.struct.compare(other.struct, name=name + ".struct"))
        if (other.HT is None and self.HT is not None) or (
            other.HT is not None and self.HT is None
        ):
            diff_list.append(name + ".HT None mismatch")
        elif self.HT is not None:
            diff_list.extend(self.HT.compare(other.HT, name=name + ".HT"))
        if (other.eco is None and self.eco is not None) or (
            other.eco is not None and self.eco is None
        ):
            diff_list.append(name + ".eco None mismatch")
        elif self.eco is not None:
            diff_list.extend(self.eco.compare(other.eco, name=name + ".eco"))
        if other._desc != self._desc:
            diff_list.append(name + ".desc")
        if other._path != self._path:
            diff_list.append(name + ".path")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.is_isotropic)
        S += getsizeof(self.elec)
        S += getsizeof(self.mag)
        S += getsizeof(self.struct)
        S += getsizeof(self.HT)
        S += getsizeof(self.eco)
        S += getsizeof(self.desc)
        S += getsizeof(self.path)
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

        Material_dict = dict()
        Material_dict["name"] = self.name
        Material_dict["is_isotropic"] = self.is_isotropic
        if self.elec is None:
            Material_dict["elec"] = None
        else:
            Material_dict["elec"] = self.elec.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.mag is None:
            Material_dict["mag"] = None
        else:
            Material_dict["mag"] = self.mag.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.struct is None:
            Material_dict["struct"] = None
        else:
            Material_dict["struct"] = self.struct.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.HT is None:
            Material_dict["HT"] = None
        else:
            Material_dict["HT"] = self.HT.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.eco is None:
            Material_dict["eco"] = None
        else:
            Material_dict["eco"] = self.eco.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Material_dict["desc"] = self.desc
        Material_dict["path"] = self.path
        # The class name is added to the dict for deserialisation purpose
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

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""name of the material

        :Type: str
        """,
    )

    def _get_is_isotropic(self):
        """getter of is_isotropic"""
        return self._is_isotropic

    def _set_is_isotropic(self, value):
        """setter of is_isotropic"""
        check_var("is_isotropic", value, "bool")
        self._is_isotropic = value

    is_isotropic = property(
        fget=_get_is_isotropic,
        fset=_set_is_isotropic,
        doc=u"""If True, uniformity in all orientations

        :Type: bool
        """,
    )

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "elec")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MatElectrical()
        check_var("elec", value, "MatElectrical")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    elec = property(
        fget=_get_elec,
        fset=_set_elec,
        doc=u"""Electrical properties of the material

        :Type: MatElectrical
        """,
    )

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "mag")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MatMagnetics()
        check_var("mag", value, "MatMagnetics")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    mag = property(
        fget=_get_mag,
        fset=_set_mag,
        doc=u"""Magnetic properties of the material

        :Type: MatMagnetics
        """,
    )

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "struct"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MatStructural()
        check_var("struct", value, "MatStructural")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    struct = property(
        fget=_get_struct,
        fset=_set_struct,
        doc=u"""Structural properties of the material

        :Type: MatStructural
        """,
    )

    def _get_HT(self):
        """getter of HT"""
        return self._HT

    def _set_HT(self, value):
        """setter of HT"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "HT")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MatHT()
        check_var("HT", value, "MatHT")
        self._HT = value

        if self._HT is not None:
            self._HT.parent = self

    HT = property(
        fget=_get_HT,
        fset=_set_HT,
        doc=u"""Heat Transfer properties of the material

        :Type: MatHT
        """,
    )

    def _get_eco(self):
        """getter of eco"""
        return self._eco

    def _set_eco(self, value):
        """setter of eco"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "eco")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MatEconomical()
        check_var("eco", value, "MatEconomical")
        self._eco = value

        if self._eco is not None:
            self._eco.parent = self

    eco = property(
        fget=_get_eco,
        fset=_set_eco,
        doc=u"""Economical properties of the material

        :Type: MatEconomical
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""material description

        :Type: str
        """,
    )

    def _get_path(self):
        """getter of path"""
        return self._path

    def _set_path(self, value):
        """setter of path"""
        check_var("path", value, "str")
        self._path = value

    path = property(
        fget=_get_path,
        fset=_set_path,
        doc=u"""Path to the material file

        :Type: str
        """,
    )
