# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Material/MatHT.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from pyleecan.Classes._check import InitUnKnowClassError


class MatHT(FrozenClass):
    """Material Heat Transfer properties"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, lambda_x=1, lambda_y=1, lambda_z=1, Cp=1, alpha=0.00393, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert(type(init_dict) is dict)
            # Overwrite default value with init_dict content
            if "lambda_x" in list(init_dict.keys()):
                lambda_x = init_dict["lambda_x"]
            if "lambda_y" in list(init_dict.keys()):
                lambda_y = init_dict["lambda_y"]
            if "lambda_z" in list(init_dict.keys()):
                lambda_z = init_dict["lambda_z"]
            if "Cp" in list(init_dict.keys()):
                Cp = init_dict["Cp"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Initialisation by argument
        self.parent = None
        self.lambda_x = lambda_x
        self.lambda_y = lambda_y
        self.lambda_z = lambda_z
        self.Cp = Cp
        self.alpha = alpha

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatHT_str = ""
        if self.parent is None:
            MatHT_str += "parent = None " + linesep
        else:
            MatHT_str += "parent = " + str(type(self.parent)) + " object" + linesep
        MatHT_str += "lambda_x = " + str(self.lambda_x) + linesep
        MatHT_str += "lambda_y = " + str(self.lambda_y) + linesep
        MatHT_str += "lambda_z = " + str(self.lambda_z) + linesep
        MatHT_str += "Cp = " + str(self.Cp) + linesep
        MatHT_str += "alpha = " + str(self.alpha) + linesep
        return MatHT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.lambda_x != self.lambda_x:
            return False
        if other.lambda_y != self.lambda_y:
            return False
        if other.lambda_z != self.lambda_z:
            return False
        if other.Cp != self.Cp:
            return False
        if other.alpha != self.alpha:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatHT_dict = dict()
        MatHT_dict["lambda_x"] = self.lambda_x
        MatHT_dict["lambda_y"] = self.lambda_y
        MatHT_dict["lambda_z"] = self.lambda_z
        MatHT_dict["Cp"] = self.Cp
        MatHT_dict["alpha"] = self.alpha
        # The class name is added to the dict fordeserialisation purpose
        MatHT_dict["__class__"] = "MatHT"
        return MatHT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.lambda_x = None
        self.lambda_y = None
        self.lambda_z = None
        self.Cp = None
        self.alpha = None

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self,'logger_name'):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger('Pyleecan')

    def _get_lambda_x(self):
        """getter of lambda_x"""
        return self._lambda_x

    def _set_lambda_x(self, value):
        """setter of lambda_x"""
        check_var("lambda_x", value, "float", Vmin=0)
        self._lambda_x = value

    # thermal conductivity (XY is lamination plane, Z is rotation axis)
    # Type : float, min = 0
    lambda_x = property(
        fget=_get_lambda_x,
        fset=_set_lambda_x,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)""",
    )

    def _get_lambda_y(self):
        """getter of lambda_y"""
        return self._lambda_y

    def _set_lambda_y(self, value):
        """setter of lambda_y"""
        check_var("lambda_y", value, "float", Vmin=0)
        self._lambda_y = value

    # thermal conductivity (XY is lamination plane, Z is rotation axis)
    # Type : float, min = 0
    lambda_y = property(
        fget=_get_lambda_y,
        fset=_set_lambda_y,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)""",
    )

    def _get_lambda_z(self):
        """getter of lambda_z"""
        return self._lambda_z

    def _set_lambda_z(self, value):
        """setter of lambda_z"""
        check_var("lambda_z", value, "float", Vmin=0)
        self._lambda_z = value

    # thermal conductivity (XY is lamination plane, Z is rotation axis)
    # Type : float, min = 0
    lambda_z = property(
        fget=_get_lambda_z,
        fset=_set_lambda_z,
        doc=u"""thermal conductivity (XY is lamination plane, Z is rotation axis)""",
    )

    def _get_Cp(self):
        """getter of Cp"""
        return self._Cp

    def _set_Cp(self, value):
        """setter of Cp"""
        check_var("Cp", value, "float", Vmin=0)
        self._Cp = value

    # specific heat capacity
    # Type : float, min = 0
    Cp = property(
        fget=_get_Cp, fset=_set_Cp, doc=u"""specific heat capacity"""
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float", Vmin=0)
        self._alpha = value

    # thermal expansion coefficient
    # Type : float, min = 0
    alpha = property(
        fget=_get_alpha, fset=_set_alpha, doc=u"""thermal expansion coefficient"""
    )
