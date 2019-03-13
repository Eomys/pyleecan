# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.BHCurve import BHCurve

from pyleecan.Methods.Material.BHCurveParam.comp_B import comp_B

from pyleecan.Classes.check import InitUnKnowClassError


class BHCurveParam(BHCurve):
    """Analyticaly defined B(H) curve"""

    VERSION = 1

    # cf Methods.Material.BHCurveParam.comp_B
    comp_B = comp_B
    # save method is available in all object
    save = save

    def __init__(self, Bmax=1.5, mur_0=8585, mur_1=21.79, a=0.255, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Bmax", "mur_0", "mur_1", "a"])
            # Overwrite default value with init_dict content
            if "Bmax" in list(init_dict.keys()):
                Bmax = init_dict["Bmax"]
            if "mur_0" in list(init_dict.keys()):
                mur_0 = init_dict["mur_0"]
            if "mur_1" in list(init_dict.keys()):
                mur_1 = init_dict["mur_1"]
            if "a" in list(init_dict.keys()):
                a = init_dict["a"]
        # Initialisation by argument
        self.Bmax = Bmax
        self.mur_0 = mur_0
        self.mur_1 = mur_1
        self.a = a
        # Call BHCurve init
        super(BHCurveParam, self).__init__()
        # The class is frozen (in BHCurve init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        BHCurveParam_str = ""
        # Get the properties inherited from BHCurve
        BHCurveParam_str += super(BHCurveParam, self).__str__() + linesep
        BHCurveParam_str += "Bmax = " + str(self.Bmax) + linesep
        BHCurveParam_str += "mur_0 = " + str(self.mur_0) + linesep
        BHCurveParam_str += "mur_1 = " + str(self.mur_1) + linesep
        BHCurveParam_str += "a = " + str(self.a)
        return BHCurveParam_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from BHCurve
        if not super(BHCurveParam, self).__eq__(other):
            return False
        if other.Bmax != self.Bmax:
            return False
        if other.mur_0 != self.mur_0:
            return False
        if other.mur_1 != self.mur_1:
            return False
        if other.a != self.a:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from BHCurve
        BHCurveParam_dict = super(BHCurveParam, self).as_dict()
        BHCurveParam_dict["Bmax"] = self.Bmax
        BHCurveParam_dict["mur_0"] = self.mur_0
        BHCurveParam_dict["mur_1"] = self.mur_1
        BHCurveParam_dict["a"] = self.a
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        BHCurveParam_dict["__class__"] = "BHCurveParam"
        return BHCurveParam_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Bmax = None
        self.mur_0 = None
        self.mur_1 = None
        self.a = None
        # Set to None the properties inherited from BHCurve
        super(BHCurveParam, self)._set_None()

    def _get_Bmax(self):
        """getter of Bmax"""
        return self._Bmax

    def _set_Bmax(self, value):
        """setter of Bmax"""
        check_var("Bmax", value, "float", Vmin=0)
        self._Bmax = value

    # Max flux density
    # Type : float, min = 0
    Bmax = property(fget=_get_Bmax, fset=_set_Bmax, doc=u"""Max flux density""")

    def _get_mur_0(self):
        """getter of mur_0"""
        return self._mur_0

    def _set_mur_0(self, value):
        """setter of mur_0"""
        check_var("mur_0", value, "float", Vmin=0)
        self._mur_0 = value

    # relative permeability close to H = 0
    # Type : float, min = 0
    mur_0 = property(
        fget=_get_mur_0,
        fset=_set_mur_0,
        doc=u"""relative permeability close to H = 0""",
    )

    def _get_mur_1(self):
        """getter of mur_1"""
        return self._mur_1

    def _set_mur_1(self, value):
        """setter of mur_1"""
        check_var("mur_1", value, "float", Vmin=0)
        self._mur_1 = value

    # relative permeability when H tends to infinity
    # Type : float, min = 0
    mur_1 = property(
        fget=_get_mur_1,
        fset=_set_mur_1,
        doc=u"""relative permeability when H tends to infinity""",
    )

    def _get_a(self):
        """getter of a"""
        return self._a

    def _set_a(self, value):
        """setter of a"""
        check_var("a", value, "float", Vmin=0, Vmax=1)
        self._a = value

    # shape parameter of the B(H) curve elbow
    # Type : float, min = 0, max = 1
    a = property(
        fget=_get_a, fset=_set_a, doc=u"""shape parameter of the B(H) curve elbow"""
    )
