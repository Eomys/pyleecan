# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.Conductor.check import check
except ImportError as error:
    check = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class Conductor(FrozenClass):
    """abstact class for conductors"""

    VERSION = 1

    # cf Methods.Machine.Conductor.check
    if isinstance(check, ImportError):
        check = property(fget=lambda x: raise_(ImportError("Can't use Conductor method check: " + str(check))))
    else:
        check = check
    # save method is available in all object
    save = save

    def __init__(self, cond_mat=-1, ins_mat=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if cond_mat == -1:
            cond_mat = Material()
        if ins_mat == -1:
            ins_mat = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["cond_mat", "ins_mat"])
            # Overwrite default value with init_dict content
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Initialisation by argument
        self.parent = None
        # cond_mat can be None, a Material object or a dict
        if isinstance(cond_mat, dict):
            self.cond_mat = Material(init_dict=cond_mat)
        else:
            self.cond_mat = cond_mat
        # ins_mat can be None, a Material object or a dict
        if isinstance(ins_mat, dict):
            self.ins_mat = Material(init_dict=ins_mat)
        else:
            self.ins_mat = ins_mat

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Conductor_str = ""
        if self.parent is None:
            Conductor_str += "parent = None " + linesep
        else:
            Conductor_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Conductor_str += "cond_mat = " + str(self.cond_mat.as_dict()) + linesep + linesep
        Conductor_str += "ins_mat = " + str(self.ins_mat.as_dict())
        return Conductor_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.cond_mat != self.cond_mat:
            return False
        if other.ins_mat != self.ins_mat:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Conductor_dict = dict()
        if self.cond_mat is None:
            Conductor_dict["cond_mat"] = None
        else:
            Conductor_dict["cond_mat"] = self.cond_mat.as_dict()
        if self.ins_mat is None:
            Conductor_dict["ins_mat"] = None
        else:
            Conductor_dict["ins_mat"] = self.ins_mat.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Conductor_dict["__class__"] = "Conductor"
        return Conductor_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.cond_mat is not None:
            self.cond_mat._set_None()
        if self.ins_mat is not None:
            self.ins_mat._set_None()

    def _get_cond_mat(self):
        """getter of cond_mat"""
        return self._cond_mat

    def _set_cond_mat(self, value):
        """setter of cond_mat"""
        check_var("cond_mat", value, "Material")
        self._cond_mat = value

        if self._cond_mat is not None:
            self._cond_mat.parent = self
    # Material of the conductor
    # Type : Material
    cond_mat = property(fget=_get_cond_mat, fset=_set_cond_mat,
                        doc=u"""Material of the conductor""")

    def _get_ins_mat(self):
        """getter of ins_mat"""
        return self._ins_mat

    def _set_ins_mat(self, value):
        """setter of ins_mat"""
        check_var("ins_mat", value, "Material")
        self._ins_mat = value

        if self._ins_mat is not None:
            self._ins_mat.parent = self
    # Material of the insulation
    # Type : Material
    ins_mat = property(fget=_get_ins_mat, fset=_set_ins_mat,
                       doc=u"""Material of the insulation""")
