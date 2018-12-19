# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.MatMagnetics import MatMagnetics

from pyleecan.Classes.check import InitUnKnowClassError


class MatMagnet(MatMagnetics):

    VERSION = 1

    def __init__(self, Hc=1, alpha_Br=0, Brm20=1, mur_lin=1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Hc", "alpha_Br", "Brm20", "mur_lin"])
            # Overwrite default value with init_dict content
            if "Hc" in list(init_dict.keys()):
                Hc = init_dict["Hc"]
            if "alpha_Br" in list(init_dict.keys()):
                alpha_Br = init_dict["alpha_Br"]
            if "Brm20" in list(init_dict.keys()):
                Brm20 = init_dict["Brm20"]
            if "mur_lin" in list(init_dict.keys()):
                mur_lin = init_dict["mur_lin"]
        # Initialisation by argument
        self.Hc = Hc
        self.alpha_Br = alpha_Br
        self.Brm20 = Brm20
        # Call MatMagnetics init
        super(MatMagnet, self).__init__(mur_lin=mur_lin)
        # The class is frozen (in MatMagnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatMagnet_str = ""
        # Get the properties inherited from MatMagnetics
        MatMagnet_str += super(MatMagnet, self).__str__() + linesep
        MatMagnet_str += "Hc = " + str(self.Hc) + linesep
        MatMagnet_str += "alpha_Br = " + str(self.alpha_Br) + linesep
        MatMagnet_str += "Brm20 = " + str(self.Brm20)
        return MatMagnet_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MatMagnetics
        if not super(MatMagnet, self).__eq__(other):
            return False
        if other.Hc != self.Hc:
            return False
        if other.alpha_Br != self.alpha_Br:
            return False
        if other.Brm20 != self.Brm20:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MatMagnetics
        MatMagnet_dict = super(MatMagnet, self).as_dict()
        MatMagnet_dict["Hc"] = self.Hc
        MatMagnet_dict["alpha_Br"] = self.alpha_Br
        MatMagnet_dict["Brm20"] = self.Brm20
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MatMagnet_dict["__class__"] = "MatMagnet"
        return MatMagnet_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hc = None
        self.alpha_Br = None
        self.Brm20 = None
        # Set to None the properties inherited from MatMagnetics
        super(MatMagnet, self)._set_None()

    def _get_Hc(self):
        """getter of Hc"""
        return self._Hc

    def _set_Hc(self, value):
        """setter of Hc"""
        check_var("Hc", value, "float", Vmin=0)
        self._Hc = value

    # Coercitivity field
    # Type : float, min = 0
    Hc = property(fget=_get_Hc, fset=_set_Hc, doc=u"""Coercitivity field""")

    def _get_alpha_Br(self):
        """getter of alpha_Br"""
        return self._alpha_Br

    def _set_alpha_Br(self, value):
        """setter of alpha_Br"""
        check_var("alpha_Br", value, "float")
        self._alpha_Br = value

    # temperature coefficient for remanent flux density /°C compared to 20°C
    # Type : float
    alpha_Br = property(
        fget=_get_alpha_Br,
        fset=_set_alpha_Br,
        doc=u"""temperature coefficient for remanent flux density /°C compared to 20°C""",
    )

    def _get_Brm20(self):
        """getter of Brm20"""
        return self._Brm20

    def _set_Brm20(self, value):
        """setter of Brm20"""
        check_var("Brm20", value, "float")
        self._Brm20 = value

    # magnet remanence induction at 20°C
    # Type : float
    Brm20 = property(
        fget=_get_Brm20, fset=_set_Brm20, doc=u"""magnet remanence induction at 20°C"""
    )
