# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class MatMagnetics(FrozenClass):

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, mur_lin=1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["mur_lin"])
            # Overwrite default value with init_dict content
            if "mur_lin" in list(init_dict.keys()):
                mur_lin = init_dict["mur_lin"]
        # Initialisation by argument
        self.parent = None
        self.mur_lin = mur_lin

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatMagnetics_str = ""
        if self.parent is None:
            MatMagnetics_str += "parent = None " + linesep
        else:
            MatMagnetics_str += "parent = " + str(type(self.parent)) + " object" + linesep
        MatMagnetics_str += "mur_lin = " + str(self.mur_lin)
        return MatMagnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mur_lin != self.mur_lin:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatMagnetics_dict = dict()
        MatMagnetics_dict["mur_lin"] = self.mur_lin
        # The class name is added to the dict fordeserialisation purpose
        MatMagnetics_dict["__class__"] = "MatMagnetics"
        return MatMagnetics_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mur_lin = None

    def _get_mur_lin(self):
        """getter of mur_lin"""
        return self._mur_lin

    def _set_mur_lin(self, value):
        """setter of mur_lin"""
        check_var("mur_lin", value, "float", Vmin=0)
        self._mur_lin = value

    # Relative magnetic permeability
    # Type : float, min = 0
    mur_lin = property(fget=_get_mur_lin, fset=_set_mur_lin,
                       doc=u"""Relative magnetic permeability""")
